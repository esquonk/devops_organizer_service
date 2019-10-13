from collections import namedtuple
from typing import List


def ceil_div(a, b):
    return -(-a // b)


DataCenter = namedtuple('DataCenter', ['name', 'servers'])


class Distributor:
    """
    Given DM and DE capacity and a list of data centers,
    computes the best data center for DM placement
    and the amount of DEs needed for data center maintenance.
    """
    __slots__ = ['dm_capacity', 'de_capacity', 'data_centers']

    def __init__(self, dm_capacity: int, de_capacity: int, data_centers: List[DataCenter]):
        self.dm_capacity = dm_capacity
        self.de_capacity = de_capacity
        self.data_centers = data_centers

    def _data_center_dm_score(self, dc: DataCenter) -> int:
        """
        Calculates score for placing DM in data center:
        how many DEs positions are saved by placing DM here
        """
        engineers_no_dm = ceil_div(dc.servers, self.de_capacity)
        engineers_with_dm = ceil_div(max(dc.servers - self.dm_capacity, 0), self.de_capacity)
        de_saved = engineers_no_dm - engineers_with_dm
        return de_saved

    def get_dm_data_center(self) -> DataCenter:
        """
        :return: best Data center instance for DM placement (to reduce DEs needed)
        """
        return max(self.data_centers, key=self._data_center_dm_score)

    def get_de_count(self, dm_data_center_name: str):
        """
        :param dm_data_center_name: Name of data center that DM is working at
        :return: Amount of DEs needed for server maintenance
        """
        count = 0
        for dc in self.data_centers:
            servers = dc.servers
            if dc.name == dm_data_center_name:
                servers = max(servers - self.dm_capacity, 0)

            count += ceil_div(servers, self.de_capacity)

        return count
