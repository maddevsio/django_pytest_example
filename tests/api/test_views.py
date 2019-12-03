import pytest
import json

from django.urls import reverse
from django.conf import settings


@pytest.mark.django_db
def test_empty_list_of_users(client):
    response = client.get(reverse('list-users'))
    data = json.loads(response.content)
    assert {"users": []} == data


@pytest.mark.django_db
def test_list_of_users_returns_created_user(client, django_user_model):
    django_user_model.objects.create(username='Mark')
    response = client.get(reverse('list-users'))
    data = json.loads(response.content)
    assert 1 == len(data.get('users'))
    assert "Mark" == data.get('users')[0].get('username')


@pytest.mark.vcr()
def test_weather_forecast(client):
    response = client.get(reverse('forecast'), data={"city": "Los Angeles"})
    data = json.loads(response.content)
    assert {'lat': 34.05, 'lon': -118.24} == data.get('coord')
    assert "Los Angeles" == data.get('name')
