from django.shortcuts import render, redirect, get_object_or_404

from .models import WorkOrder
from .forms import WorkOrderForm


def workorder_list(request):

    workorders = WorkOrder.objects.all()

    return render(
        request,
        "workorders/list.html",
        {
            "workorders": workorders
        }
    )


def workorder_create(request):

    if request.method == "POST":

        form = WorkOrderForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("workorders:list")

    else:

        form = WorkOrderForm()

    return render(
        request,
        "workorders/create.html",
        {
            "form": form
        }
    )


def workorder_detail(request, pk):

    workorder = get_object_or_404(
        WorkOrder,
        pk=pk
    )

    return render(
        request,
        "workorders/detail.html",
        {
            "workorder": workorder
        }
    )


def workorder_update(request, pk):

    workorder = get_object_or_404(
        WorkOrder,
        pk=pk
    )

    if request.method == "POST":

        form = WorkOrderForm(
            request.POST,
            instance=workorder
        )

        if form.is_valid():

            form.save()

            return redirect("workorders:list")

    else:

        form = WorkOrderForm(
            instance=workorder
        )

    return render(
        request,
        "workorders/update.html",
        {
            "form": form
        }
    )


def workorder_delete(request, pk):

    workorder = get_object_or_404(
        WorkOrder,
        pk=pk
    )

    if request.method == "POST":

        workorder.delete()

        return redirect("workorders:list")

    return render(
        request,
        "workorders/delete.html",
        {
            "workorder": workorder
        }
    )