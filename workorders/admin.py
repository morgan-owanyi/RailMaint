from django.contrib import admin
from .models import WorkOrder


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):

    list_display = (
        "work_order_number",
        "asset",
        "assigned_employee",
        "priority",
        "status",
        "target_completion",
    )

    list_filter = (
        "priority",
        "status",
    )

    search_fields = (
        "work_order_number",
        "title",
    )
