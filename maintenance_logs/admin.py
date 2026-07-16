from django.contrib import admin
from .models import MaintenanceLog


@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):

    list_display = (
        "work_order",
        "technician",
        "maintenance_date",
        "hours_worked",
    )

    list_filter = (
        "maintenance_date",
    )

    search_fields = (
        "work_order__work_order_number",
        "technician__first_name",
        "technician__last_name",
    )