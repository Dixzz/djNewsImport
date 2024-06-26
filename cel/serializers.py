from rest_framework import serializers
from .models import AlertMasterModel


class AlertMasterSerializer(serializers.ModelSerializer):
    """list of State """
    # country_name = serializers.StringRelatedField()

    class Meta:
        model = AlertMasterModel
        fields = '__all__'