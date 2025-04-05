from time import sleep
import requests
from src.utils.telegram import enviar_mensagem

def rastreio(token_encomenda):

    url = f"https://radar.tntbrasil.com.br/radargateway/public/localizacaoSimplificadaDetail/detail/{token_encomenda}.do?doctolms=true"

    requisicao = requests.get(url)
    if requisicao.status_code == 200:
        dados = requisicao.json()
        destino = dados
        previsao_atual = dados['trackingHistory'][0]['timeDate']
        local_a_caminho = dados['trackingHistory'][0]['branch']
        # ocorrencia_atual = 
        atual = dados['eventoAtualInfo']
        status_atual = atual['evento']

        previsao_data_final = atual['previsaoEntrega']
        destino_atual = atual['destino']

        dicionario = {
            
            'status_atual': status_atual,
            'previsao_atual': previsao_atual,
            'local_a_caminho_atual': local_a_caminho,
            
            'destino_final': destino_atual,
            'previsao_data_final': previsao_data_final
        }
        return dicionario
    elif requisicao.status_code == 404: 
        print("Encomenda não encontrada")
    elif requisicao.status_code == 500:
        print("Erro interno do servidor")

    return None
    

while True:

    requisicao = rastreio("I8DwgYEGERO5icEK8ljLyw")

    if requisicao is not None:
    # Enviar mensagem para o Telegram

        enviar_mensagem(f"Encomenda: {requisicao['status_atual'].lower().capitalize()} com previsão de chegada {requisicao['previsao_atual']} no local {requisicao['local_a_caminho_atual']}, destino final está para {requisicao['destino_final']}, com previsao final para a data {requisicao['previsao_data_final']}.")

    sleep(7200)