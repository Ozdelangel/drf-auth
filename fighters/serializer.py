from rest_framework import serializers
from .models import Fighters

class FightersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','owner', 'name', 'description', 'created_at', 'updated_at',)
        model = Fighters 