#  Streaming de Tweets

<p align="center">
  <img src="https://rockcontent.com/wp-content/uploads/2018/06/web_crawler.png"/>
</p>

---

Consiste em web crawling é usado para indexar as informações em uma página web usando bots, também chamados de crawlers. Web Crawlers são basicamente utilizados pelos principais motores de busca como o Google, Bing e Yahoo. No nosso caso estamos usando API do twitter que disponibiliza parte dos dados da rede social, em nosso caso estamos usando para extrair dados de tweets de um termo específico. O arquivo python usamos para extrair os dados da rede social e no jupyter notebook usamos para explorar, transformar os nossos dados e fazer a ingestão desses dados no PostgreSQL.

## Requisitos

A precisa ter, primeiramente, uma conta ativa no ambiente do twitter para desenvolvedores. Uma vez que sua solicitação é aceita e você já possue sua conta de desenvolvimento ativa, você precisa ir no Dashboard de sua conta e criar um App. Ao criar um App vinculado a sua conta, o Twitter irá gerar credenciais que serão usadas para realizar as chamadas à API deles, então guardem bem essas credencias e não compartilhem na internet. Link abaixo:

https://developer.twitter.com/en

Você precisará de python 3.9 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

Linux/macos

    pip3 install virtualenv
    virtualenv ../venv -p python3
    source ../venv/bin/activate 
    pip install -r requirements.txt

Windows

    pip3 install virtualenv
    virtualenv ..\venv -p python3
    ..\venv\Scripts\activate
    pip install -r requirements.txt
    
## Como executar o crawnler?

```bash

$ python3 get_tweet.py

```
[Alt Text](https://github.com/Douglas-cc/streaming-de-tweets/blob/main/2021-01-30%2021-11-24.gif)

## E o notebook ?

```bash

$ jupyter-lab

```
[Alt Text](https://github.com/Douglas-cc/streaming-de-tweets/blob/main/2021-01-30%2021-15-48.gif)

    
