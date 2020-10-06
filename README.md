<p align="center"><a href="https://i.imgur.com/vfPsmkj.png" target="_blank"><img width="600"src="https://i.imgur.com/vfPsmkj.png"></a></p>
<p align="center">

  <!-- <a href="https://travis-ci.org/fga-eps-mds/2018.1_Gerencia_mais"><img src="https://travis-ci.org/fga-eps-mds/2018.1_Gerencia_mais.svg?branch=master" alt="Build"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://codeclimate.com/github/fga-gpp-mds/2018.1_Gerencia_mais/maintainability"><img src="https://api.codeclimate.com/v1/badges/4aff97e7847e842ef8be/maintainability" /></a>
    <a href='https://coveralls.io/github/fga-gpp-mds/2018.1_Gerencia_mais?branch=development'><img src='https://coveralls.io/repos/github/fga-gpp-mds/2018.1_Gerencia_mais/badge.svg?branch=development' alt='Coverage Status' /></a>
     [![Codacy Badge](https://api.codacy.com/project/badge/Grade/b6ba54118ec74854bf82605dc1760a8f)](https://www.codacy.com/app/Eduardojvr/2018.1_Gerencia_mais?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fga-gpp-mds/2018.1_Gerencia_mais&amp;utm_campaign=Badge_Grade)
  <a href="https://codeclimate.com/github/fga-gpp-mds/2018.1_Gerencia_mais"><img src="https://codeclimate.com/github/fga-gpp-mds/2018.1_Gerencia_mais/badges/issue_count.svg" alt="Issue Count"></a> <a href='https://www.python.org/'><img src='https://img.shields.io/badge/Made%20with-Python-1f425f.svg' alt='python' /></a> 
 
</p> -->
[![Build Status](https://travis-ci.org/EconomizAqui/EconomizAqui.svg?branch=development)](https://travis-ci.org/EconomizAqui/EconomizAqui)

<bt>
<br>
 

## ℹ️ Sobre o projeto

<p align="justify">Projeto desenvolvido por alunos de graduação em Engenharia de Software da Universidade de Brasília, campus Gama.</p>

<p align="justify">Tem como objetivo aplicar alguns padrões de projeto aprendidos durante a disciplina de Desenho e Arquitetura de Software.</p>

<br>

<br>

## 💻 Tecnologias

<p>
<a href="image" target="_blank"><img width="100"src="https://i.imgur.com/c2We7zg.jpg"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/TravisCI-Mascot-1.png"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/codeclimate.jpg"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/css-logo-400x400.png"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/docker.gif"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/drive.gif"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/github.gif"></a><a href="image" target="_blank"><img width="80"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/heroku.svg"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/html.png"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/python-django.png"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/telegram.gif"></a><a href="image" target="_blank"><img width="100"src="https://github.com/fga-gpp-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/imagens/Tecnologias/zenhub.jpg"></a>


</p>


<br>

## 🐳 Guia de Uso do Docker

* ### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Instalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

* ### Comandos básicos 

 &emsp;&emsp; Para a utilização do ambiente em background, basta dar o comando abaixo e ele irá ligar o container:
 
 ```terminal
  docker-compose up -d
 ```
 &emsp;&emsp; Caso queira utilizar o ambiente com logs:

 ```terminal
  docker-compose up 
 ```
 &emsp;&emsp; Para a visualização dos logs quando em modo de execução background, use o comando abaixo:

 ```terminal
  docker-compose logs -f
 ```

 &emsp;&emsp; Para pausar o container:

  ```terminal
  docker-compose stop
 ```
 &emsp;&emsp; E para religar um container parado use o comando: 
 
 ```terminal
  docker-compose start 
 ```

 &emsp;&emsp; Para listar os containers que estão em execução:
 
 ```terminal
  docker ps
 ```
 &emsp;&emsp; Para listar todos os containers já executados na sua máquina:
 
 ```terminal
  docker ps -a
 ```
 &emsp;&emsp; Para executar comandos dentro do container:
 
 ```terminal
  docker-compose exec -it  "id do container"  "comandos"
 ```
 Para acessar o [bash](https://www.gnu.org/software/bash/) do container, substitua "comandos" por "bash".

* ## Rodando a aplicação

Para rodar a aplicação, entre na pasta do projeto em que está localizado o __docker-compose__ e digite no terminal:

```
  docker-compose up -d
```
Espere até que todos os serviços estejam disponíveis, acesse a página inicial do projeto com o seguinte endereço: https://localhost:8000

##  ℹ️ Deploy

<p align="justify">O deploy da aplicação é feito de forma automatizada por meio da integração contínua (Travis CI) que utiliza como ambiente de hospedagem o Heroku.


</p>

<br>

## 🌎 Acessando a aplicação

<p align="justify">Acesse nosso servidor utilizando o endereço apresentado abaixo:</p>

* Servidor: https://economizaqui.herokuapp.com/


##  Acessando a Wiki

<p align="justify">Acesse nossa Wiki utilizando o endereço apresentado abaixo:</p>

* Wiki: https://economizaqui.github.io/EconomizAqui/ 

##  Acessando o Repositório

<p align="justify">Acesse nosso repositório utilizando o endereço apresentado abaixo:</p>

* Repositório: https://github.com/EconomizAqui/EconomizAqui 


<br>
