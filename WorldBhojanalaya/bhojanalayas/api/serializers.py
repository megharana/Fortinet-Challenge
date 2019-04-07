from rest_framework import serializers
from bhojanalayas.models import Address, Details


class BhojanalayaAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['rest_id_id', 'city', 'address']


class BhojanalayaDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = [
            'resturant_id', 'rest_name', 'cuisines', 'votes', 'avg_cost_ofTwo',
            'aggregate_rating'
        ]
