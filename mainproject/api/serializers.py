from rest_framework import serializers
from core.models import Insult

class InsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insult
        fields = '__all__'