from django.shortcuts import render, redirect, get_object_or_404

from .models import MaintenanceLog
from .forms import MaintenanceLogForm


def maintenance_list(request):
    logs = MaintenanceLog.objects.all()

    return render(
        request,
        "maintenance_logs/list.html",
        {
            "logs": logs
        }
    )


def maintenance_create(request):
    if request.method == "POST":

        form = MaintenanceLogForm(request.POST)

        if form.is_valid():

            log = form.save()

            workorder = log.work_order

            if workorder.status == "OPEN":
                workorder.status = "IN_PROGRESS"
                workorder.save()

            return redirect("maintenance:list")

    else:
        form = MaintenanceLogForm()

    return render(
        request,
        "maintenance_logs/create.html",
        {
            "form": form
        }
    )


def maintenance_detail(request, pk):
    log = get_object_or_404(
        MaintenanceLog,
        pk=pk
    )

    return render(
        request,
        "maintenance_logs/detail.html",
        {
            "log": log
        }
    )


def maintenance_update(request, pk):
    log = get_object_or_404(
        MaintenanceLog,
        pk=pk
    )

    if request.method == "POST":

        form = MaintenanceLogForm(
            request.POST,
            instance=log
        )

        if form.is_valid():

            form.save()

            return redirect("maintenance:list")

    else:

        form = MaintenanceLogForm(
            instance=log
        )

    return render(
        request,
        "maintenance_logs/update.html",
        {
            "form": form
        }
    )


def maintenance_delete(request, pk):
    log = get_object_or_404(
        MaintenanceLog,
        pk=pk
    )

    if request.method == "POST":

        log.delete()

        return redirect("maintenance:list")

    return render(
        request,
        "maintenance_logs/delete.html",
        {
            "log": log
        }
    )