from datetime import date
import gzip
import requests
import shutil
import os
import json

extension = '.gz'
hoje = date.today()
filmes_ids = 'movie_ids'
# {"adult":false,"id":3924,"original_title":"Blondie","popularity":2.063,"video":false}
series_ids = 'tv_series_ids'
# {"id":2,"original_name":"Clerks: The Animated Series","popularity":7.037}

filmes_url = 'http://files.tmdb.org/p/exports/' + filmes_ids + hoje.strftime('_%m_%d_%Y') + '.json' + extension
series_url = 'http://files.tmdb.org/p/exports/' + series_ids + hoje.strftime('_%m_%d_%Y') + '.json' + extension

def busca(tipo, quantidade):
    if tipo == 'filme':
        t = filmes_ids
        url = filmes_url
    elif tipo == 'serie':
        t = series_ids
        url = series_url
    else:
        return None

    arquivo = t + hoje.strftime('_%m_%d_%Y') #+ '.json'

    if os.path.isfile(arquivo):
        return ler_arquivo(tipo, quantidade)
    else:
        dirs = os.listdir('./')
        for file in dirs:
            print(file.endswith('_2020.json'))
            print(file)
            exit()
            
        if get_arquivo(tipo):
            return ler_arquivo(tipo, quantidade)




def ler_arquivo(tipo, quantidade):

    if tipo == 'filme':
        t = filmes_ids
        url = filmes_url
    elif tipo == 'serie':
        t = series_ids
        url = series_url
    else:
        return False

    arquivo = t + hoje.strftime('_%m_%d_%Y') + '.json'

    if os.path.isfile(arquivo):
        data = {}
        d = {}
        with open(arquivo, 'rb') as arq:
            for i, item in enumerate(arq.readlines()):
                linha = json.loads(item)
                if linha['popularity'] >= 100.0: # PONTUAÇÂO DA LISTA DE FILMES
                    if tipo == 'filme':
                        d['titulo'] = linha['original_title']

                    if tipo == 'serie':
                        d['titulo'] = linha['original_name']

                    d['pontos'] = linha['popularity']
                    data[linha['id']] = d
                    
                    if len(data) >= quantidade:
                        return data        

    return {}

def get_arquivo(tipo):
    if tipo == 'filme':
        t = filmes_ids
        url = filmes_url
    elif tipo == 'serie':
        t = series_ids
        url = series_url
    else:
        return False

    #Aplicar esse método dentro de uma queue, chama-lo por um cron no servidor rodando todo dia as 08h00
    try:
        arq = requests.get(url)
        with gzip.open(t + hoje.strftime('_%m_%d_%Y') + '.json' + extension, 'rb') as entrada:
            with open(t + hoje.strftime('_%m_%d_%Y') + '.json', 'wb') as saida:
                shutil.copyfileobj(entrada, saida) # seria interessante ao invés de manter em texto subir os dados para o REDIS
        
        os.remove(t + hoje.strftime('_%m_%d_%Y') + '.json' + extension)#incluir validação e resultado em LOG -
        return True

    except:
        return False

