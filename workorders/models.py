from django.db import models
from employees.models import Employee
from assets.models import Asset
from django.utils import timezone


class WorkOrder(models.Model):

    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("ASSIGNED", "Assigned"),
        ("IN_PROGRESS", "In Progress"),
        ("AWAITING_INSPECTION", "Awaiting Inspection"),
        ("COMPLETED", "Completed"),
        ("CLOSED", "Closed"),
    ]

    work_order_number = models.CharField(
    max_length=30,
    unique=True,
    blank=True,
    editable=False
)

    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT
    )

    assigned_employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="MEDIUM"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    reported_by = models.CharField(
        max_length=100
    )

    target_completion = models.DateField()

    completed_at = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.work_order_number
    

def save(self, *args, **kwargs):

    if not self.work_order_number:

        today = timezone.now().strftime("%Y%m%d")

        last_order = WorkOrder.objects.filter(
            work_order_number__startswith=f"WO-{today}"
        ).order_by("-work_order_number").first()

        if last_order:

            last_number = int(last_order.work_order_number.split("-")[-1]) + 1

        else:

            last_number = 1

        self.work_order_number = f"WO-{today}-{last_number:04d}"

    super().save(*args, **kwargs)

