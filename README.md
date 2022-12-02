# GetUrls
**API que tem como objetivo retornar todas as urls de um arquivo html e string.**

## Tecnologias Utilizadas
- Python
- FastAPI
- Docker

## Modo de usar:
**É recomendado usar linux para seguir exatamente os passos**

**É necessário ter o docker e o docker compose instalado na sua máquina**

**Para cada requisição do tipo POST, é necessário passar nos headers o seguinte objeto:**

```json
{
  "Content-type": "application/json",
  "Accept": "application/json"
}
```

1. Clone o repositório com o comando ```git clone https://github.com/weblerson/GetUrls.git```
2. Na raíz do projeto, crie um arquivo chamado **.env** e escreva ```PROD=False``` para habilitar o Swagger ou 
```PROD=True``` para desabilitá-lo.
3. Ainda na raiz do projeto, abra um terminal e digite o comando ```docker compose build```
para criar a imagem do projeto.
4. Após terminar de criar a imagem, digite ```docker compose up``` para subir a API para o seu localhost.

## Rotas
- **/urls (POST)**:

Nessa rota, você deve passar no corpo da requisição o valor de html.

Ex.:

```json
{
  "html": "<a href='https://google.com'>Google</a>"
}
```

Como resposta, a API deve retornar, caso haja sucesso na requisição, uma lista de objetos que possuem o trecho em html
do qual foi retirado a url juntamente com a url:

```json
{
  "success": true,
  "body": [
    {
      "html": "<a href='https://google.com'>Google</a>",
      "url": "https://google.com"
    }
  ]
}
```

- **/files (POST)**

Nesta rota, você deve enviar os bytes de um arquivo html na requisição usando a chave "file".

Ex.:
```json
{
  "file": "bytes_do_seu_arquivo_html"
}
```

Em Python:

```python
from typing import Dict, BinaryIO
from requests import Response

import requests

url: str = 'http://127.0.0.1:8000/files'

files: Dict[str, BinaryIO] = {
    "file": open('index.html', 'rb')
}

res: Response = requests.post(url, files=files)
```

Como resposta, a API deve retornar, caso haja sucesso na requisição, uma lista de objetos que possuem o trecho em html
do qual foi retirado a url juntamente com a url, consoante acontece na rota /urls:

```json
{
  "success": true,
  "body": [
    {
      "html": "<a href='https://google.com'>Google</a>",
      "url": "https://google.com"
    }
  ]
}
```