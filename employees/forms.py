from django import forms
from django.contrib.auth.models import Group

from .models import Employee


class EmployeeForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        help_text="Login username"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Temporary password"
    )

    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select Role"
    )

    class Meta:
        model = Employee

        fields = [
            "employee_number",
            "first_name",
            "last_name",
            "department",
            "position",
            "phone",
            "email",
            "status",
            "username",
            "password",
            "role",
        ]