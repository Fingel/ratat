from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from ratat.players.models import Race, Dass
from ratat.players.serializers import RaceSerializer, DassSerializer, CharacterSerializer


class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class DassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dass.objects.all()
    serializer_class = DassSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.character_set.all()

    def create(self, request):
        character_serializer = CharacterSerializer(data=request.data)
        if character_serializer.is_valid():
            character = character_serializer.save(user=request.user)
            return Response(CharacterSerializer(character).data, status=status.HTTP_201_CREATED)
        else:
            return Response(character_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
