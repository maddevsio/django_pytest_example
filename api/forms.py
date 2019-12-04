from django import forms


class ForecastForm(forms.Form):
    city = forms.CharField()

    def clean_city(self):
        if 'city' not in self.cleaned_data:
            raise forms.ValidationError("Invalid city", "invalid")
        return self.cleaned_data['city']
