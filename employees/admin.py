from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_number",
        "first_name",
        "last_name",
        "department",
        "position",
        "status",
    )

    search_fields = (
        "employee_number",
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "department",
        "status",
    )

    ordering = (
        "employee_number",
    )