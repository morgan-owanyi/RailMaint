from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            "employee_number",
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "designation",
            "employment_date",
            "status",
        ]

        widgets = {
            "employment_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }