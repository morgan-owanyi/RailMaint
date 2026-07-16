from django import forms
from .models import MaintenanceLog


class MaintenanceLogForm(forms.ModelForm):

    class Meta:

        model = MaintenanceLog

        fields = "__all__"

        widgets = {

            "maintenance_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "work_performed": forms.Textarea(
                attrs={
                    "rows": 5
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

        }