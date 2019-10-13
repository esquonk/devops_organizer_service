import jsonschema
import pytest
from rest_framework.test import APIClient

from api.v1.tests.data import bad_arguments
from devops_distributor.tests.data import test_data

response_value_schema = {
    'type': 'object',
    'additionalProperties': False,
    'required': ["DE", "DM_data_center"],
    'properties': {
        'DE': {'type': 'number'},
        'DM_data_center': {'type': 'string'},
    }
}
response_schema = {
    'type': 'object',
    'required': ['value'],
    'properties': {
        'value': response_value_schema
    }
}


@pytest.fixture
def api_client():
    return APIClient()


URL = '/api/v1/organizer/distribute/'


@pytest.mark.parametrize("dm_capacity,de_capacity,data_centers,expected_dm_dc,expected_de", test_data)
def test_view(api_client, dm_capacity, de_capacity, data_centers, expected_dm_dc, expected_de):
    response = api_client.post(URL, {
        'DM_capacity': dm_capacity,
        'DE_capacity': de_capacity,
        'data_centers': [{'name': dc.name, 'servers': dc.servers} for dc in data_centers]
    }, format='json')

    assert response.status_code == 200

    jsonschema.validate(response.json(), response_schema)
    assert response.json()['value']['DE'] == expected_de
    assert response.json()['value']['DM_data_center'] == expected_dm_dc


@pytest.mark.parametrize("post_data", bad_arguments)
def test_view_bad_arguments(api_client, post_data):
    response = api_client.post(URL, post_data, format='json')

    assert response.status_code == 400
