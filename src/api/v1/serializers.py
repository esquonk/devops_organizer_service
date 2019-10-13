from rest_framework import serializers

from devops_distributor.distributor import DataCenter


class DataCenterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    servers = serializers.IntegerField(min_value=1)


class DevopsDistributeRequestSerializer(serializers.Serializer):
    data_centers = DataCenterSerializer(many=True)
    DM_capacity = serializers.IntegerField(min_value=0)
    DE_capacity = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        data = validated_data
        dcs = data.pop('data_centers')
        data['data_centers'] = [DataCenter(**dc) for dc in dcs]
        return data


class DevopsDistributeResponseSerializer(serializers.Serializer):
    DE = serializers.IntegerField(min_value=0)
    DM_data_center = serializers.CharField(max_length=500)
