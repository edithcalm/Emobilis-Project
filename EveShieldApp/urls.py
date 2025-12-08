from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from EveShieldApp import views

# Customize admin site branding
admin.site.site_header = "EveShield Administration"
admin.site.site_title = "EveShield Admin"
admin.site.index_title = "Welcome to EveShield Admin Panel"

app_name = "eveshield"

accounts_patterns = (
    [
        path("signup/", views.signup, name="signup"),
        path("login/", views.user_login, name="login"),
        path("logout/", auth_views.LogoutView.as_view(), name="logout"),
        path("profile/", views.profile, name="profile"),
    ],
    "accounts",
)

reports_patterns = (
    [
        path("submit/", views.submit_report, name="submit_report"),
        path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
        path("admin/report/<int:report_id>/", views.report_detail, name="report_detail"),
    ],
    "reports",
)

lawyer_patterns = (
    [
        path("", views.lawyer_directory, name="directory"),
    ],
    "lawyers",
)

mental_health_patterns = (
    [
        path("", views.therapist_directory, name="directory"),
        path("chatbot/", views.mental_health_chatbot, name="chatbot"),
    ],
    "mental_health",
)

chatbot_patterns = (
    [
        path("legal/", views.legal_chatbot, name="legal_chatbot"),
    ],
    "chatbot",
)

resource_patterns = (
    [
        path("", views.resource_list, name="list"),
        path("article/<slug:slug>/", views.resource_detail, name="detail"),
        path("emergency-contacts/", views.emergency_contacts, name="emergency_contacts"),
    ],
    "resources",
)

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/", include(accounts_patterns, namespace="accounts")),
    path("reports/", include(reports_patterns, namespace="reports")),
    path("lawyers/", include(lawyer_patterns, namespace="lawyers")),
    path("mental-health/", include(mental_health_patterns, namespace="mental_health")),
    path("chatbot/", include(chatbot_patterns, namespace="chatbot")),
    path("resources/", include(resource_patterns, namespace="resources")),
]
