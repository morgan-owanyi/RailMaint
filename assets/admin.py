from django.contrib import admin
from .models import Asset, AssetCategory


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):

    list_display = (
        "asset_number",
        "name",
        "category",
        "location",
        "status",
    )

    list_filter = (
        "category",
        "status",
    )

    search_fields = (
        "asset_number",
        "name",
        "serial_number",
    )