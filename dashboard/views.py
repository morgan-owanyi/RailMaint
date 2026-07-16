from django.shortcuts import render

from employees.models import Employee
from assets.models import Asset
from workorders.models import WorkOrder
from maintenance_logs.models import MaintenanceLog


def dashboard(request):

    context = {

        "employee_count": Employee.objects.count(),

        "asset_count": Asset.objects.count(),

        "open_workorders": WorkOrder.objects.filter(
            status="OPEN"
        ).count(),

        "completed_workorders": WorkOrder.objects.filter(
            status="COMPLETED"
        ).count(),

        "maintenance_logs": MaintenanceLog.objects.count(),

        "recent_workorders": WorkOrder.objects.order_by("-created_at")[:5],

        "recent_logs": MaintenanceLog.objects.order_by("-created_at")[:5],

    }

    return render(
        request,
        "dashboard/index.html",
        context
    )