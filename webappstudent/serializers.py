from rest_framework import serializers
from .models import emplStud

class studentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = emplStud
        fields = ('id', 'firstname', 'lastname', 'grade')