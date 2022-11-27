FROM python:3.10

MAINTAINER weblerson

# Copia as dependências
COPY requirements.txt ./

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./

# Expôe a porta 8000
EXPOSE 8000
