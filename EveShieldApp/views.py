import json
import random

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from EveShieldApp import models
from EveShieldApp.forms import GBVReportForm, UserProfileForm, UserRegistrationForm


def home(request):
    """Home page view"""
    return render(request, "onboarding/home.html")


# Accounts
def signup(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect("eveshield:accounts:profile")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created for {user.username}! You can now log in.")
            return redirect("eveshield:accounts:login")
    else:
        form = UserRegistrationForm()

    return render(request, "users/signup.html", {"form": form})


def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect("eveshield:accounts:profile")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("eveshield:accounts:profile")
        messages.error(request, "Invalid username or password.")

    return render(request, "users/login.html")


@login_required
def profile(request):
    """User profile view"""
    profile_obj, _ = models.UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("eveshield:accounts:profile")
    else:
        form = UserProfileForm(instance=profile_obj)

    return render(
        request,
        "users/profile.html",
        {"profile": profile_obj, "form": form},
    )


# Reports
def submit_report(request):
    """Anonymous GBV report submission view"""
    if request.method == "POST":
        form = GBVReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                (
                    "Thank you for your report. Your submission has been received and will be reviewed. "
                    "Your identity remains anonymous."
                ),
            )
            return redirect("eveshield:reports:submit_report")
    else:
        form = GBVReportForm()

    return render(request, "tracking/submit_report.html", {"form": form})


@staff_member_required
def admin_dashboard(request):
    """Admin dashboard for managing GBV reports"""
    reports_qs = models.GBVReport.objects.all()

    # Filtering
    status_filter = request.GET.get("status", "")
    if status_filter:
        reports_qs = reports_qs.filter(status=status_filter)

    # Search
    search_query = request.GET.get("search", "")
    if search_query:
        reports_qs = reports_qs.filter(location__icontains=search_query) | reports_qs.filter(
            details__icontains=search_query
        )

    # Pagination
    paginator = Paginator(reports_qs, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Statistics
    total_reports = models.GBVReport.objects.count()
    pending_reports = models.GBVReport.objects.filter(status=models.ReportStatus.PENDING).count()
    reviewed_reports = models.GBVReport.objects.filter(status=models.ReportStatus.REVIEWED).count()

    context = {
        "page_obj": page_obj,
        "total_reports": total_reports,
        "pending_reports": pending_reports,
        "reviewed_reports": reviewed_reports,
        "status_filter": status_filter,
        "search_query": search_query,
    }

    return render(request, "tracking/admin_dashboard.html", context)


@staff_member_required
def report_detail(request, report_id):
    """View and update individual report details"""
    report = models.GBVReport.objects.get(id=report_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        admin_notes = request.POST.get("admin_notes", "")

        if new_status in [choice[0] for choice in models.ReportStatus.choices]:
            report.status = new_status
            report.admin_notes = admin_notes
            report.save()
            messages.success(request, "Report updated successfully!")
            return redirect("eveshield:reports:report_detail", report_id=report_id)

    return render(request, "tracking/report_detail.html", {"report": report})


# Lawyers
def lawyer_directory(request):
    """Display directory of lawyers"""
    lawyers_qs = models.Lawyer.objects.filter(is_active=True)

    county_filter = request.GET.get("county", "")
    if county_filter:
        lawyers_qs = lawyers_qs.filter(county__icontains=county_filter)

    search_query = request.GET.get("search", "")
    if search_query:
        lawyers_qs = lawyers_qs.filter(name__icontains=search_query) | lawyers_qs.filter(
            specialization__icontains=search_query
        )

    counties = (
        models.Lawyer.objects.filter(is_active=True)
        .values_list("county", flat=True)
        .distinct()
        .order_by("county")
    )

    paginator = Paginator(lawyers_qs, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "counties": counties,
        "county_filter": county_filter,
        "search_query": search_query,
    }

    return render(request, "resources/lawyers/directory.html", context)


# Mental health
def therapist_directory(request):
    """Display directory of mental health professionals"""
    therapists_qs = models.Therapist.objects.filter(is_active=True)

    county_filter = request.GET.get("county", "")
    if county_filter:
        therapists_qs = therapists_qs.filter(county__icontains=county_filter)

    search_query = request.GET.get("search", "")
    if search_query:
        therapists_qs = therapists_qs.filter(name__icontains=search_query) | therapists_qs.filter(
            specialty__icontains=search_query
        )

    counties = (
        models.Therapist.objects.filter(is_active=True)
        .values_list("county", flat=True)
        .distinct()
        .order_by("county")
    )

    paginator = Paginator(therapists_qs, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "counties": counties,
        "county_filter": county_filter,
        "search_query": search_query,
    }

    return render(request, "resources/mental_health/directory.html", context)


def mental_health_chatbot(request):
    """Mental health chatbot view"""
    chatbot_responses = {
        "greeting": [
            "Hello! I'm here to provide mental health support and information. How can I help you today?",
            "Hi there! I'm a mental health support assistant. What would you like to know?",
            "Welcome! I can help with self-care tips, grounding exercises, and guide you to professional help. What do you need?",
        ],
        "grounding": [
            "Here's a simple grounding exercise: Name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste. This helps bring you back to the present moment.",
            "Try deep breathing: Inhale for 4 counts, hold for 4 counts, exhale for 4 counts. Repeat 5 times.",
            "Grounding technique: Place your feet flat on the floor. Notice the sensation. Wiggle your toes. Feel your body in the chair. This helps anchor you in the present.",
        ],
        "self_care": [
            "Self-care is important: Get enough sleep, eat regular meals, stay hydrated, and take breaks when needed.",
            "Practice self-compassion. Be kind to yourself. You're doing the best you can.",
            "Set boundaries. It's okay to say no. Your wellbeing matters.",
            "Connect with supportive people. You don't have to go through this alone.",
        ],
        "professional_help": [
            "If you're experiencing severe distress, thoughts of self-harm, or feel unsafe, please contact a mental health professional immediately. You can find therapists in our directory.",
            "It's important to seek professional help if symptoms persist or interfere with daily life. Check our therapist directory for professionals in your area.",
            "Remember: Seeking help is a sign of strength, not weakness. Professional therapists can provide specialized support.",
        ],
        "crisis": [
            "If you're in immediate danger or having thoughts of self-harm, please contact emergency services (999) or a crisis hotline immediately.",
            "For immediate crisis support, call the National GBV Hotline or emergency services. Your safety is the priority.",
        ],
        "default": [
            "I understand you're going through a difficult time. Would you like information about grounding exercises, self-care tips, or finding a professional therapist?",
            "I'm here to help. You can ask me about self-care, grounding techniques, or how to find professional support.",
        ],
    }

    if request.method == "POST":
        user_message = request.POST.get("message", "").lower().strip()
        response = get_chatbot_response(user_message, chatbot_responses)

        return render(
            request,
            "triggering/mental_health_chatbot.html",
            {
                "response": response,
                "user_message": request.POST.get("message", ""),
                "chatbot_responses": json.dumps(chatbot_responses),
            },
        )

    return render(
        request,
        "triggering/mental_health_chatbot.html",
        {"chatbot_responses": json.dumps(chatbot_responses)},
    )


def get_chatbot_response(user_message, responses):
    """Rule-based response logic for mental health chatbot"""
    greeting_keywords = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    grounding_keywords = ["grounding", "anxious", "panic", "overwhelmed", "anxiety", "calm", "breathing"]
    self_care_keywords = ["self care", "self-care", "cope", "coping", "feel better", "help myself"]
    professional_keywords = ["therapist", "counselor", "professional", "therapy", "need help", "see someone"]
    crisis_keywords = ["suicide", "self harm", "hurt myself", "end it", "kill myself", "danger", "emergency"]

    user_lower = user_message.lower()

    if any(keyword in user_lower for keyword in crisis_keywords):
        return random.choice(responses["crisis"])

    if any(keyword in user_lower for keyword in greeting_keywords):
        return random.choice(responses["greeting"])

    if any(keyword in user_lower for keyword in grounding_keywords):
        return random.choice(responses["grounding"])

    if any(keyword in user_lower for keyword in self_care_keywords):
        return random.choice(responses["self_care"])

    if any(keyword in user_lower for keyword in professional_keywords):
        return random.choice(responses["professional_help"])

    return random.choice(responses["default"])


# Legal chatbot
def legal_chatbot(request):
    """Legal aid chatbot view - rule-based Q&A system"""
    legal_responses = {
        "p3_form": {
            "question": "how do i file a p3 form",
            "response": (
                "To file a P3 form (Police Form 3 - Medical Examination Report):\n"
                "1. Report to the nearest police station and file a report\n"
                "2. Request a P3 form from the police\n"
                "3. Take the P3 form to a government hospital or approved medical facility\n"
                "4. A qualified medical officer will examine you and fill out the form\n"
                "5. Return the completed P3 form to the police station\n"
                "6. Keep a copy for your records\n\n"
                "The P3 form is crucial evidence in GBV cases. It documents physical injuries and is admissible in court."
            ),
        },
        "legal_aid": {
            "question": "how do i get legal aid",
            "response": (
                "You can get legal aid through several ways:\n"
                "1. Contact a lawyer from our Legal Aid Directory\n"
                "2. Reach out to organizations like FIDA (Federation of Women Lawyers)\n"
                "3. Contact the Legal Aid Board if available in your area\n"
                "4. Some NGOs provide free legal services for GBV cases\n\n"
                "Many lawyers offer pro bono (free) services for GBV survivors. Check our directory for lawyers in your county."
            ),
        },
        "reporting": {
            "question": "how do i report gbv",
            "response": (
                "To report Gender-Based Violence:\n"
                "1. Go to the nearest police station\n"
                "2. File a report with the police\n"
                "3. Request a P3 form for medical examination\n"
                "4. You can also submit an anonymous report through EveShield\n"
                "5. Contact GBV hotlines for immediate support\n\n"
                "Remember: You have the right to report. The police are required to take your report seriously."
            ),
        },
        "rights": {
            "question": "what are my rights",
            "response": (
                "As a GBV survivor, you have the right to:\n"
                "- Report the incident to police\n"
                "- Receive medical attention\n"
                "- Access legal representation\n"
                "- Protection from further harm\n"
                "- Privacy and confidentiality\n"
                "- Support services (counseling, shelter if needed)\n"
                "- Fair treatment without discrimination\n\n"
                "No one has the right to harm you. The law protects you."
            ),
        },
        "protection_order": {
            "question": "protection order",
            "response": (
                "A Protection Order is a court order that protects you from an abuser:\n"
                "1. Apply at the nearest court (Magistrate's Court)\n"
                "2. You can apply in person or through a lawyer\n"
                "3. The court can issue temporary orders immediately\n"
                "4. The abuser will be served and must comply\n"
                "5. Violation of a protection order is a criminal offense\n\n"
                "A protection order can prohibit the abuser from contacting you, coming near you, or entering your home."
            ),
        },
        "evidence": {
            "question": "evidence",
            "response": (
                "Important evidence to collect:\n"
                "- Medical reports (P3 form)\n"
                "- Photos of injuries\n"
                "- Text messages, emails, or social media messages\n"
                "- Witness statements\n"
                "- Police reports\n"
                "- Any documents related to the incident\n\n"
                "Keep all evidence safe. Store it in a secure place. This evidence can be crucial in court."
            ),
        },
        "court_process": {
            "question": "court process",
            "response": (
                "The court process for GBV cases:\n"
                "1. Report to police and file charges\n"
                "2. Investigation by police\n"
                "3. Case forwarded to prosecution\n"
                "4. Court hearing dates set\n"
                "5. You may need to testify as a witness\n"
                "6. Court makes a decision\n\n"
                "The process can take time. A lawyer can guide you through each step. You have the right to legal representation."
            ),
        },
        "default": {
            "response": (
                "I'm here to help with legal questions about GBV. You can ask me about:\n"
                "- How to file a P3 form\n"
                "- Getting legal aid\n"
                "- Reporting GBV\n"
                "- Your rights as a survivor\n"
                "- Protection orders\n"
                "- Collecting evidence\n"
                "- The court process\n\n"
                "Or browse our Legal Aid Directory to find a lawyer in your area."
            )
        },
    }

    if request.method == "POST":
        user_message = request.POST.get("message", "").lower().strip()
        response = get_legal_response(user_message, legal_responses)

        return render(
            request,
            "triggering/legal_chatbot.html",
            {
                "response": response,
                "user_message": request.POST.get("message", ""),
                "legal_responses": json.dumps(legal_responses),
            },
        )

    return render(
        request,
        "triggering/legal_chatbot.html",
        {"legal_responses": json.dumps(legal_responses)},
    )


def get_legal_response(user_message, responses):
    """Rule-based response logic for legal chatbot"""
    user_lower = user_message.lower()

    for key, data in responses.items():
        if key == "default":
            continue
        if data["question"] in user_lower or any(word in user_lower for word in data["question"].split() if len(word) > 3):
            return data["response"]

    if "p3" in user_lower or "medical form" in user_lower or "medical report" in user_lower:
        return responses["p3_form"]["response"]

    if "legal aid" in user_lower or "lawyer" in user_lower or "attorney" in user_lower:
        return responses["legal_aid"]["response"]

    if "report" in user_lower and ("gbv" in user_lower or "violence" in user_lower):
        return responses["reporting"]["response"]

    if "right" in user_lower or "rights" in user_lower:
        return responses["rights"]["response"]

    if "protection" in user_lower and "order" in user_lower:
        return responses["protection_order"]["response"]

    if "evidence" in user_lower or "proof" in user_lower:
        return responses["evidence"]["response"]

    if "court" in user_lower or "trial" in user_lower or "hearing" in user_lower:
        return responses["court_process"]["response"]

    return responses["default"]["response"]


# Resources
def resource_list(request):
    """List all educational resources"""
    articles_qs = models.ResourceArticle.objects.filter(is_published=True)

    category_filter = request.GET.get("category", "")
    if category_filter:
        articles_qs = articles_qs.filter(category=category_filter)

    search_query = request.GET.get("search", "")
    if search_query:
        articles_qs = articles_qs.filter(title__icontains=search_query) | articles_qs.filter(
            content__icontains=search_query
        )

    paginator = Paginator(articles_qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = models.ResourceArticle._meta.get_field("category").choices

    context = {
        "page_obj": page_obj,
        "category_filter": category_filter,
        "search_query": search_query,
        "categories": categories,
    }

    return render(request, "resources/articles/list.html", context)


def resource_detail(request, slug):
    """View individual resource article"""
    article = get_object_or_404(models.ResourceArticle, slug=slug, is_published=True)

    related_articles = (
        models.ResourceArticle.objects.filter(category=article.category, is_published=True)
        .exclude(id=article.id)[:3]
    )

    return render(
        request,
        "resources/articles/detail.html",
        {"article": article, "related_articles": related_articles},
    )


def emergency_contacts(request):
    """Emergency contacts page"""
    contacts = {
        "national_gbv_hotline": {
            "name": "National GBV Hotline",
            "phone": "1195",
            "description": "24/7 helpline for gender-based violence support",
        },
        "police_emergency": {
            "name": "Police Emergency",
            "phone": "999",
            "description": "Emergency police services",
        },
        "child_helpline": {
            "name": "Child Helpline",
            "phone": "116",
            "description": "Support for children in distress",
        },
    }

    return render(request, "resources/articles/emergency_contacts.html", {"contacts": contacts})
