from rest_framework import serializers
from .models import Value, Principle

# Fetches Json data.
class ValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Value
        fields = ('id', 'value_name')

class PrinciplesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Principle
        fields = ('id', 'principle_name')
