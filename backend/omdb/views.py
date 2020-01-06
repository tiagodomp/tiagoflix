from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from tiagoflix import settings
import requests

class Omdb(APIView):

    url_base = settings.OMDB_URL
    api_key = settings.OMDB_KEY

    # Create your views here.
    def listar_filmes(self, request):
        url = url_omdb(request)
        r = requests.get(url.string, url.params)

    def url_omdb(self, request):
        params = request.data
        payload, retorno = {}
        valid_options_by_id = {'i','t','type','y','plot','r','callback','v'}
        valid_option_by_search= {'s', 'type', 'y', 'r', 'page', 'callback', 'v'}
        
        for parameter, value in params.itens():
            if(parameter in valid_options_by_id): #id ou titulo
                payload[parameter] = value
            if(parameter in valid_option_by_search): #busca 
                payload[parameter] = value
        
        payload['apikey'] = api_key
        retorno['string'] = url_base
        retorno['params'] = payload

        return retorno


    