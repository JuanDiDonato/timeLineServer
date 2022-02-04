from rest_framework import serializers

# model
from .models import Posts

# serializer
from ..camera.serializers import CameraSerializer
from ..files.serializers import FilesSerializer

class postsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Posts
        fields = '__all__'

    # get images
    def get_images(self,instance):
        image_list = []
        images = CameraSerializer.Meta.model.objects.filter(post=instance.id)
        for image in images:
            image_list.append(f'http://127.0.0.1:8000/media/{str(image.picture)}')
        return image_list

    def get_files(self,instance):
        file_list = []
        files = FilesSerializer.Meta.model.objects.filter(post=instance.id)
        for file in files:
            file_list.append(f'http://127.0.0.1:8000/media/{str(file.file)}')
        return file_list

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "title": instance.title,
            "description": instance.description,
            "user": instance.user.username,
            "pictures" : self.get_images(instance),
            "files": self.get_files(instance)
        }