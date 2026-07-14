from django.shortcuts import render, redirect, get_object_or_404

from .models import Asset
from .forms import AssetForm


def asset_list(request):

    assets = Asset.objects.all()

    return render(
        request,
        "assets/list.html",
        {
            "assets": assets
        }
    )


def asset_create(request):

    if request.method == "POST":

        form = AssetForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("assets:list")

    else:

        form = AssetForm()

    return render(
        request,
        "assets/create.html",
        {
            "form": form
        }
    )


def asset_detail(request, pk):

    asset = get_object_or_404(
        Asset,
        pk=pk
    )

    return render(
        request,
        "assets/detail.html",
        {
            "asset": asset
        }
    )


def asset_update(request, pk):

    asset = get_object_or_404(
        Asset,
        pk=pk
    )

    if request.method == "POST":

        form = AssetForm(
            request.POST,
            instance=asset
        )

        if form.is_valid():

            form.save()

            return redirect("assets:list")

    else:

        form = AssetForm(
            instance=asset
        )

    return render(
        request,
        "assets/update.html",
        {
            "form": form
        }
    )


def asset_delete(request, pk):

    asset = get_object_or_404(
        Asset,
        pk=pk
    )

    if request.method == "POST":

        asset.delete()

        return redirect("assets:list")

    return render(
        request,
        "assets/delete.html",
        {
            "asset": asset
        }
    )