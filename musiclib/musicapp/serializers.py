from rest_framework import serializers
from .models import Albhum, Song

class AlbhumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albhum
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'