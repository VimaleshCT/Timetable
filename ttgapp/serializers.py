from rest_framework import serializers
from ttgapp.models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= Admin
        fields=('Facultyid','Password','Email')
        