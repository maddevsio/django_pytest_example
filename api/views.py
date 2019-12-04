import requests

from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from api.forms import ForecastForm

def fetch_users(request):
    return JsonResponse({"users": [{
        "username": u.username, "first_name": u.first_name,
        "last_name": u.last_name, "id": u.pk} for u in User.objects.all()]})


def fetch_forecast(request):
    form = ForecastForm(request.GET or None)
    if form.is_valid():
        r = requests.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={"q": form.cleaned_data.get('city'), "apikey": settings.API_KEY}
        )
        return JsonResponse(r.json())
    return JsonResponse({"errors": form.errors}, status=400)
