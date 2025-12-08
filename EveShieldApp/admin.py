from django.contrib import admin

from EveShieldApp import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "county", "created_at")
    list_filter = ("county", "created_at")
    search_fields = ("user__username", "user__email", "phone", "county")


@admin.register(models.GBVReport)
class GBVReportAdmin(admin.ModelAdmin):
    list_display = ("id", "type_of_violence", "location", "status", "created_at")
    list_filter = ("status", "type_of_violence", "created_at")
    search_fields = ("location", "details", "admin_notes")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Report Information",
            {"fields": ("type_of_violence", "location", "details", "incident_date", "file_upload")},
        ),
        ("Status & Management", {"fields": ("status", "admin_notes", "created_at", "updated_at")}),
    )


@admin.register(models.Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ("name", "county", "phone", "email", "is_active", "created_at")
    list_filter = ("county", "is_active", "created_at")
    search_fields = ("name", "county", "specialization", "phone", "email")
    list_editable = ("is_active",)


@admin.register(models.Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ("name", "county", "specialty", "phone", "email", "is_active", "created_at")
    list_filter = ("county", "is_active", "created_at")
    search_fields = ("name", "county", "specialty", "phone", "email")
    list_editable = ("is_active",)


@admin.register(models.ResourceArticle)
class ResourceArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "created_at")
    list_filter = ("category", "is_published", "created_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_published",)
