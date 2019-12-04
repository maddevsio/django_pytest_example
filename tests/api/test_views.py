import pytest
from django.urls import reverse
from django.conf import settings


@pytest.mark.django_db
def test_fetch_users_returns_emply_list(client):
    """ Make sure that we get valid JSON response if we have no users created """
    response = client.get(reverse('fetch-users'))
    data = response.json()
    assert {"users": []} == data


@pytest.mark.django_db
def test_fetch_user_returns_created_user(client, django_user_model):
    """ Make sure that we get valid response when we have users created """
    django_user_model.objects.create(username='Mark')
    response = client.get(reverse('fetch-users'))
    data = response.json()
    assert 1 == len(data.get('users'))
    assert "Mark" == data.get('users')[0].get('username')


@pytest.mark.vcr()
def test_fetch_forecast(client):
    """ Make sure we can get forecast for Los Angeles """
    response = client.get(reverse('fetch-forecast'), data={"city": "Los Angeles"})
    data = response.json()
    assert {'lat': 34.05, 'lon': -118.24} == data.get('coord')
    assert "Los Angeles" == data.get('name')
