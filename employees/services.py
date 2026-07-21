from django.contrib.auth import get_user_model
from django.db import transaction

from .models import Employee

User = get_user_model()


class EmployeeService:

    @staticmethod
    @transaction.atomic
    def create_employee(form):

        data = form.cleaned_data

        # Create User
        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )

        # Assign Role
        role = data["role"]
        user.groups.add(role)

        # Create Employee
        employee = Employee.objects.create(
            user=user,
            employee_number=data["employee_number"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            department=data["department"],
            position=data["position"],
            phone=data["phone"],
            email=data["email"],
            status=data["status"],
        )

        return employee

    @staticmethod
    @transaction.atomic
    def update_employee(employee, form):

        data = form.cleaned_data

        employee.employee_number = data["employee_number"]
        employee.first_name = data["first_name"]
        employee.last_name = data["last_name"]
        employee.department = data["department"]
        employee.position = data["position"]
        employee.phone = data["phone"]
        employee.email = data["email"]
        employee.status = data["status"]
        employee.save()

        if employee.user:

            user = employee.user

            user.username = data["username"]
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]

            if data["password"]:
                user.set_password(data["password"])

            user.groups.clear()
            user.groups.add(data["role"])

            user.save()

        return employee

    @staticmethod
    @transaction.atomic
    def delete_employee(employee):

        if employee.user:
            employee.user.delete()
        else:
            employee.delete()