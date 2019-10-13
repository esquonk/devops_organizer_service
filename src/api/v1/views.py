from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.v1.serializers import DevopsDistributeRequestSerializer, DevopsDistributeResponseSerializer
from devops_distributor.distributor import Distributor


class DevopsOrganizerViews(ViewSet):
    basename = 'organizer'

    @action(detail=False, methods=['POST'])
    def distribute(self, request):
        request_serializer = DevopsDistributeRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        request_data = request_serializer.save()

        distributor = Distributor(
            dm_capacity=request_data['DM_capacity'],
            de_capacity=request_data['DE_capacity'],
            data_centers=request_data['data_centers']
        )

        dm_datacenter = distributor.get_dm_data_center()
        de_count = distributor.get_de_count(dm_datacenter.name)
        response_data = DevopsDistributeResponseSerializer(instance={
            'DE': de_count,
            'DM_data_center': dm_datacenter.name
        }).data

        return Response(response_data)
