from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication
from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(viewsets.ModelViewSet):

    #authentication_classes = [TokenAuthentication]
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        # return PontoTuristico.objects.filter(aprovado=True)
        return Avaliacao.objects.all()
