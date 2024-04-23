from django.contrib import admin
from .models import Company, Profile, WorkExperience


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    ordering = ('title',)


class WorkExperienceInLine(admin.TabularInline):
    model = WorkExperience
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInLine]
    list_display = ('user', 'phone_number', 'role')
    list_filter = ('role',)

    search_fields = ('user', 'phone_number')
    ordering = ('user', 'phone_number')
