import json
from datetime import datetime
from loguru import logger 
from tweepy import OAuthHandler, Stream, StreamListener

# Cadastrar as chaves de acesso, para isso você deve consultar a documetação da api do twiiter e gerar as suas chaves de acesso 
consumer_key = "" 
consumer_secret = "" 
access_token = ""
access_token_secret = "" 

# Definir um arquivo de saida para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%M-%d-%H-%M-%S")
out = open(f'collected_tweets{data_hoje}.txt', "w")

# classe para conexão com o twitter
class MyListener(StreamListener):

    def on_data(self, data):
        logger.info(f'Tweets {data}')
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self, status):
        logger.info(f'Erro: {status}')

if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    Stream = Stream(auth, l)
    Stream.filter(track=["Bolsonaro"])
    