import pytest

from devops_distributor.distributor import Distributor
from .data import test_data


@pytest.mark.parametrize("dm_capacity,de_capacity,data_centers,expected_dm_dc,expected_de", test_data)
def test_distributor(dm_capacity, de_capacity, data_centers, expected_dm_dc, expected_de):
    d = Distributor(dm_capacity=dm_capacity,
                    de_capacity=de_capacity,
                    data_centers=data_centers)

    dm_dc_name = d.get_dm_data_center().name
    assert dm_dc_name == expected_dm_dc
    assert d.get_de_count(dm_dc_name) == expected_de
