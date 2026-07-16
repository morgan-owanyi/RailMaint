from django import forms
from .models import WorkOrder


class WorkOrderForm(forms.ModelForm):

    class Meta:

        model = WorkOrder

        fields = [
    "asset",
    "assigned_employee",
    "priority",
    "status",
    "title",
    "description",
    "reported_by",
    "target_completion",
    "completed_at",
]

        widgets = {

            "target_completion": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "completed_at": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5
                }
            ),

        }