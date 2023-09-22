from files.models import UploadFile
from rest_framework import serializers


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = "__all__"
