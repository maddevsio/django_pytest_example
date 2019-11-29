from django import forms


class ForecastForm(forms.Form):
    city = forms.CharField()

    def clean_city(self):
        if not self.cleaned_data.get('city'):
            raise forms.ValidationError("Invalid city", "invalid")
        return self.cleaned_data.get('city')
