from django.contrib import admin

from .models import Employee, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "employee_number",
        "full_name",
        "department",
        "designation",
        "status",
    )

    list_filter = (
        "department",
        "status",
    )

    search_fields = (
        "employee_number",
        "first_name",
        "last_name",
    )

    ordering = (
        "employee_number",
    )