from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication
from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(viewsets.ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    #authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'avaliacoes__nota']
    # lookup_fields = 'nome' #valor precisa ser unico para utilizar

    def get_queryset(self):
        # return PontoTuristico.objects.filter(aprovado=True)
        return PontoTuristico.objects.all()

    # atrelar a um objto já existente

    @action(methods=['post'], detail=True)
    def associar(self, request, id):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=id)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpResponse('ok')
