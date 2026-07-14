from django.db import models

class AssetCategory(models.Model):

    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    


class Asset(models.Model):

    STATUS_CHOICES = [

        ("ACTIVE","Active"),

        ("UNDER_MAINTENANCE","Under Maintenance"),

        ("OUT_OF_SERVICE","Out of Service"),

        ("RETIRED","Retired"),

    ]

    asset_number = models.CharField(max_length=30, unique=True)

    name = models.CharField(max_length=150)

    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.PROTECT
    )

    manufacturer = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    serial_number = models.CharField(max_length=100)

    year_of_manufacture = models.PositiveIntegerField()

    purchase_date = models.DateField()

    location = models.CharField(max_length=100)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.asset_number} - {self.name}"
