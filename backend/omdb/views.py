from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework import authentication, permissions
from tiagoflix import settings
import requests
import os

# Create your views here.
@api_view()
def listar_filmes():
    data = {}
    if not data:
        data['i'] = 'tt3896198'

    url = url_omdb(request.data)
    r = requests.get(url.base, url.params)
    return Response(r)

def url_omdb(**kwargs):
    url_base = settings.OMDB_URL
    api_key = settings.OMDB_KEY
    payload, retorno = {}
    valid_options_by_id = {'i','t','type','y','plot','r','callback','v'}
    valid_option_by_search= {'s', 'type', 'y', 'r', 'page', 'callback', 'v'}
    
    for parameter, value in kwargs.itens():
        if(parameter in valid_options_by_id): #id ou titulo
            payload[parameter] = value
        if(parameter in valid_option_by_search): #busca 
            payload[parameter] = value
    
    payload['apikey'] = api_key
    retorno['base'] = url_base
    retorno['params'] = payload

    return retorno


    