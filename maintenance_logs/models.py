from django.db import models
from django.utils import timezone

from workorders.models import WorkOrder
from employees.models import Employee


class MaintenanceLog(models.Model):

    work_order = models.ForeignKey(
        WorkOrder,
        on_delete=models.CASCADE,
        related_name="maintenance_logs"
    )

    technician = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT
    )

    maintenance_date = models.DateField(
        default=timezone.now
    )

    hours_worked = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    work_performed = models.TextField()

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-maintenance_date"]

    def __str__(self):
        return f"{self.work_order.work_order_number} - {self.technician}"