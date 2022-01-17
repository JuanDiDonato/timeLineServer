# Rest framework serializer
from rest_framework import serializers

# Model
from .models import Camera

# Camera serializer
class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Camera
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id":instance.id,
            "date_of_picture": instance.date_of_picture,
            "picture": f'http://127.0.0.1:8000/media/{str(instance.picture)}',
            "user": instance.user.username
        }