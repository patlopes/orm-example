from django.http import HttpResponse
from django.views import View
from .models import UsuarioModel
from django.forms.models import model_to_dict
from django.core import serializers
import json

class Usuario(View):
    def get(self, request):
        id = request.GET["id"]
        userDict = model_to_dict(UsuarioModel.objects.get(id=id))
        userJson = json.dumps(userDict)
        return HttpResponse(userJson)

    def post(self, request):
        response = json.loads(request.body.decode())
        nome = response['nome']
        ano = response['ano']
        UsuarioModel.objects.create(nome=nome, ano=ano)
        return HttpResponse()

class UsuarioLista(View):
    def get(self, request):
        query = UsuarioModel.objects.all()
        responseJson = serializers.serialize("json", query)
        return HttpResponse(responseJson)