from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm
from .models import Employee
from .services import EmployeeService


@login_required
def employee_list(request):

    employees = Employee.objects.select_related(
        "department",
        "user"
    ).all().order_by("employee_number")

    return render(
        request,
        "employees/list.html",
        {
            "employees": employees
        }
    )


@login_required
def employee_create(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():

            EmployeeService.create_employee(form)

            messages.success(
                request,
                "Employee created successfully."
            )

            return redirect("employee_list")

    else:

        form = EmployeeForm()

    return render(
        request,
        "employees/create.html",
        {
            "form": form
        }
    )


@login_required
def employee_detail(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    return render(
        request,
        "employees/detail.html",
        {
            "employee": employee
        }
    )


@login_required
def employee_update(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Employee updated successfully."
            )

            return redirect("employee_list")

    else:

        form = EmployeeForm(instance=employee)

    return render(
        request,
        "employees/update.html",
        {
            "form": form,
            "employee": employee
        }
    )


@login_required
def employee_delete(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    if request.method == "POST":

        if employee.user:
            employee.user.delete()
        else:
            employee.delete()

        messages.success(
            request,
            "Employee deleted successfully."
        )

        return redirect("employee_list")

    return render(
        request,
        "employees/delete.html",
        {
            "employee": employee
        }
    )