from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):

    class Meta:

        model = Asset

        fields = [
            "asset_number",
            "name",
            "category",
            "manufacturer",
            "model",
            "serial_number",
            "year_of_manufacture",
            "purchase_date",
            "location",
            "status",
            "notes",
        ]

        widgets = {

            "purchase_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),
        }