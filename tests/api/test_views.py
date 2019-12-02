import pytest
import json

from django.urls import reverse

pytest.mark.filterwarnings("warning")

@pytest.mark.django_db
def test_empty_list_of_users(client):
    response = client.get(reverse('list-users'))
    data = json.loads(response.content)
    assert {"users": []} == data
