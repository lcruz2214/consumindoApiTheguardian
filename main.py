import requests
import json
import pandas as pd


def exportarCsv(t, l, nome): # Função para exportar em csv com nome dinamico.
    
    df = pd.DataFrame({'Titulo': t, 'Link': l})
    
    try:
        df.to_csv("%s.csv" % nome, index=False, sep=";", encoding="utf-8-sig")
        print("Arquivo criado com sucesso")
    except:
        print("erro ao criar arquivo.")

def buscarNoticias(dados, assunto):
    titulo = []
    link = []
   
    for keys in dados['response']['results']: # dado é do tipo json, está sendo decomposto até onde possa pegar 

        if keys['pillarName'] == assunto:
            print(keys['webTitle'])
            print(keys['webUrl'])
            titulo.append(keys['webTitle'])
            link.append(keys['webUrl'])
            print(20*"-=-")

    exportarCsv(titulo, link, assunto)

def buscaAssuntos(dados):
    
    tema = input("Informe o assunto que busca, digite \n(E) para esporte \n(N) para noticias\n(A) para arts\n==> ")
    
    if tema == "e":
        buscarNoticias(dados,'Sport')
    elif tema == "n":
        buscarNoticias(dados, 'News')
    elif tema == "a":
        buscarNoticias(dados, 'Arts')   
    else:
        print("Letra digitada sem correspondencia %s" %tema)

def main(): #função main que vai ser chamada logo como prioritaria 
    
    url = "https://content.guardianapis.com/search?api-key=3c07d5e6-e06f-42d5-acd9-7ff44bd15b02" # url da the guardian

    def reqNews(end): # função de requisição dados web
        try:
            return requests.get(end).json() # retorna o dado já no formato json
        except:
            print("ERRO ao conectar")

    r = reqNews(url)

    buscaAssuntos(r)


    '''
    print(2*"\n")
    print(30*"===")
    print (r['response']['results'][5]['webTitle']) # entrando em response, result >> posição 5 e busca pela chave webTitle
    print (r['response']['results'][5]['webUrl'])
    print(30*"===")
    print(2*"\n")
    '''

if __name__ == "__main__":
    main()