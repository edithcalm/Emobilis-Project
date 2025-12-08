from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from EveShieldApp import models


class UserRegistrationForm(UserCreationForm):
    """Custom user registration form"""

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone = forms.CharField(max_length=20, required=False)
    county = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            models.UserProfile.objects.create(
                user=user,
                phone=self.cleaned_data.get("phone", ""),
                county=self.cleaned_data.get("county", ""),
            )
        return user


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile"""

    class Meta:
        model = models.UserProfile
        fields = ("phone", "county")


class GBVReportForm(forms.ModelForm):
    """Form for anonymous GBV reporting"""

    type_of_violence = forms.ChoiceField(
        choices=models.ViolenceType.choices,
        widget=forms.Select(attrs={"class": "form-select"}),
        required=True,
    )
    location = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "e.g., Nairobi, Mombasa, Kisumu"}
        ),
        required=True,
        help_text="Please provide the county, town, or area where the incident occurred",
    )
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Please provide as much detail as possible about the incident...",
            }
        ),
        required=True,
        help_text="Describe what happened in detail",
    )
    incident_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        required=False,
        help_text="Date when the incident occurred (optional)",
    )
    file_upload = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control", "accept": "image/*,.pdf,.doc,.docx"}),
        required=False,
        help_text="Optional: Upload photos, documents, or other evidence (max 10MB)",
    )

    class Meta:
        model = models.GBVReport
        fields = ["type_of_violence", "location", "details", "incident_date", "file_upload"]

