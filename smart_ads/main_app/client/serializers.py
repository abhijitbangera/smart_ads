from rest_framework import serializers

from client.models import adsDetails
from django.contrib.auth.models import User

class AdsSerializer(serializers.ModelSerializer):
    client_id = serializers.CharField()
    header = serializers.CharField(max_length=300, default="", allow_blank=True)
    left_top = serializers.CharField( max_length=200, default="", allow_blank=True)
    left_bottom = serializers.CharField( max_length=200, default="", allow_blank=True)
    right_top = serializers.CharField( max_length=200, default="", allow_blank=True)
    right_bottom = serializers.CharField( max_length=200, default="", allow_blank=True)
    footer = serializers.CharField( max_length=300, default="", allow_blank=True)
    update_flag = serializers.BooleanField(default=True)

    class Meta:
        model = adsDetails
        fields = '__all__'