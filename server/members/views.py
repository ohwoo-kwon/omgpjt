from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Position, Member
from .serializers import MemberSerializer, PositionSerializer

# Create your views here.

@api_view(['GET',])
def members(request):
    members = get_list_or_404(Member)

    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def positions(request):
    positions = get_list_or_404(Position)

    serializer = PositionSerializer(positions, many=True)
    return Response(serializer.data)