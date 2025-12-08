from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Extended user profile for additional information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"


class ViolenceType(models.TextChoices):
    """Types of gender-based violence"""

    PHYSICAL = "physical", "Physical Violence"
    SEXUAL = "sexual", "Sexual Violence"
    EMOTIONAL = "emotional", "Emotional/Psychological Violence"
    ECONOMIC = "economic", "Economic Violence"
    DIGITAL = "digital", "Digital/Online Violence"
    OTHER = "other", "Other"


class ReportStatus(models.TextChoices):
    """Status of GBV reports"""

    PENDING = "pending", "Pending"
    REVIEWED = "reviewed", "Reviewed"
    IN_PROGRESS = "in_progress", "In Progress"
    RESOLVED = "resolved", "Resolved"


class GBVReport(models.Model):
    """Anonymous GBV incident report model"""

    # Anonymous fields - no user association
    type_of_violence = models.CharField(
        max_length=20,
        choices=ViolenceType.choices,
        default=ViolenceType.OTHER,
    )
    location = models.CharField(max_length=255, help_text="County, town, or area")
    details = models.TextField(help_text="Detailed description of the incident")
    incident_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date when the incident occurred",
    )
    file_upload = models.FileField(
        upload_to="reports/%Y/%m/%d/",
        blank=True,
        null=True,
        help_text="Optional: Upload evidence (photos, documents, etc.)",
    )

    # Status tracking
    status = models.CharField(
        max_length=20,
        choices=ReportStatus.choices,
        default=ReportStatus.PENDING,
    )

    # Admin notes (only visible to admins)
    admin_notes = models.TextField(
        blank=True,
        null=True,
        help_text="Internal notes for admin use only",
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "GBV Report"
        verbose_name_plural = "GBV Reports"

    def __str__(self) -> str:
        return (
            f"Report #{self.id} - "
            f"{self.get_type_of_violence_display()} - {self.status}"
        )


class Lawyer(models.Model):
    """Legal aid directory - lawyers and firms assisting GBV victims"""

    name = models.CharField(max_length=255, help_text="Lawyer or firm name")
    phone = models.CharField(max_length=20, help_text="Phone number")
    whatsapp = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="WhatsApp number (optional)",
    )
    email = models.EmailField(blank=True, null=True, help_text="Email address")
    county = models.CharField(max_length=100, help_text="County where services are provided")
    specialization = models.CharField(
        max_length=255,
        help_text="Specialization areas (e.g., GBV cases, family law, criminal law)",
    )
    address = models.TextField(blank=True, null=True, help_text="Physical address (optional)")
    is_active = models.BooleanField(default=True, help_text="Is this lawyer currently available?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["county", "name"]
        verbose_name = "Lawyer"
        verbose_name_plural = "Lawyers"

    def __str__(self) -> str:
        return f"{self.name} - {self.county}"


class Therapist(models.Model):
    """Mental health support directory - therapists, psychologists, and trauma counselors"""

    name = models.CharField(max_length=255, help_text="Therapist or counselor name")
    specialty = models.CharField(
        max_length=255,
        help_text=(
            "Specialty areas (e.g., trauma counseling, PTSD, domestic violence, anxiety)"
        ),
    )
    phone = models.CharField(max_length=20, help_text="Phone number")
    email = models.EmailField(blank=True, null=True, help_text="Email address (optional)")
    county = models.CharField(max_length=100, help_text="County where services are provided")
    address = models.TextField(
        blank=True,
        null=True,
        help_text="Physical address or clinic name (optional)",
    )
    qualifications = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Professional qualifications (optional)",
    )
    is_active = models.BooleanField(default=True, help_text="Is this therapist currently available?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["county", "name"]
        verbose_name = "Therapist"
        verbose_name_plural = "Therapists"

    def __str__(self) -> str:
        return f"{self.name} - {self.county}"


class ResourceArticle(models.Model):
    """Educational resource articles about GBV"""

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of title")
    content = models.TextField(help_text="Full article content (HTML allowed)")
    category = models.CharField(
        max_length=100,
        choices=[
            ("rights", "Know Your Rights"),
            ("complaint", "How to File a Complaint"),
            ("emergency", "Emergency Steps"),
            ("support", "Support Services"),
            ("prevention", "Prevention"),
            ("other", "Other"),
        ],
        default="other",
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Resource Article"
        verbose_name_plural = "Resource Articles"

    def __str__(self) -> str:
        return self.title
