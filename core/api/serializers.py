from rest_framework.serializers import ModelSerializer
#from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico, DocIdentificacao
from atracoes.models import Atracao
from enderecos.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    
    atracoes = AtracaoSerializer(many=True)
    #comentarios = ComentarioSerializer(many=True)
    #avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer()
    doc_identificacao = DocIdentificacaoSerializer()
    
    
    class Meta:
        model = PontoTuristico
        fields = ( 'descricao_completa','id','nome','descricao', 
                  'aprovado', 'atracoes','endereco','doc_identificacao')
       # Many to many 
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
        
    def create(self,validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        
        endereco = validated_data['endereco']
        del validated_data['endereco']
        
        documento = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
    
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        
        # OneToOne
        doc = DocIdentificacao.objects.create(**documento)
        
        #Forengkey
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doc
        
        ponto.save()
        
        return ponto
        
   
