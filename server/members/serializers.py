from django.db.models import fields
from rest_framework import serializers
from .models import Position, Member

class PositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Position
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'