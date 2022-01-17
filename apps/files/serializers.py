# Rest framework serializer
from rest_framework import serializers

# models
from .models import Files

# serializer for files model
class FilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files
        fields = '__all__'