from rest_framework import serializers
from genres.models import Genres


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'
