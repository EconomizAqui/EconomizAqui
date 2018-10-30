Data | Versão | Descrição | Responsáveis
-- | -- | -- | --
16/09/2018 | 0.1 | Criação do índice analítico | Vinícius Cantuária
18/09/2018 | 0.2 | Criação do Posicionamento, tópico 2 | Vinícius Cantuária
20/09/2018 | 0.3 | Retirada de alguns tópicos do índice analítico | Matheus Roberto e Vinícius Cantuária
20/09/2018 | 0.4 | Criação da Faixa de Qualidade, tópico 7 | Vinícius Cantuária
20/09/2018 | 0.5 | Criação de Restrições, tópico 6 | Matheus Roberto
20/09/2018 | 0.6 | Criação de Visão geral do produto, tópico 4 | Matheus Roberto
20/09/2018 | 0.7 | Criação da Introdução, tópico 1 | Matheus Roberto
20/09/2018 | 0.8 | Criação da Descrições da Parte Interessada e do Usuário, tópico 3 | Vinícius Cantuária
22/09/2018 | 0.9 | Alinhamento do texto e complemento em tópicos. | Eduardo Júnio
24/09/2018 | 0.10 | Criação de Recursos do Produto, tópico 5 | Matheus Roberto

# Documento de Visão

## 1 Introdução

### 1.1 Propósito
<p align="justify"> O objetivo deste documento é apresentar a aplicação EconomizAqui e determinar a sua utilidade e funcionalidade. Com esse propósito, será realizada uma exposição detalhada do projeto, de modo a abranger as inovações ofertadas pela aplicação, através de tópicos relativos à descrição do problema, oportunidade de negócios, descrição dos envolvidos, restrições do projeto e outros. Dessa forma, espera-se que o leitor seja capaz de entender a proposta e as suas aplicabilidades.</p>

### 1.2 Escopo
<p align="justify"> Tendo em vista as dificuldades em se comparar os preços dos produtos em diferentes comércios, que não disponibilizam informações por meio da internet, surge a necessidade de uma aplicação para centralizar as informações sobre os produtos desejados, apresentando ao consumidor os estabelecimentos que tem os menores preços.</p>

### 1.3 Definições, acrônimos e abreviações
  - FGA - Faculdade do Gama
  - UnB - Universidade de Brasília

### 1.4 Referências
  - IBM. Documento de Visão. Disponível em: <https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html>. Acesso em: 16 de setembro de 2018.
  - Falko. Documento de Visão. Disponível em: <https://github.com/fga-eps-mds/Falko-2017.2-BackEnd/wiki/Documento-de-Visão>. Acesso em 18 de setembro de 2018.
  - Matrícula Web. Documentação Suplementar. Disponível em:  <https://github.com/requisitos-de-software-2018-1-grupo-1/matricula-web/wiki/Documentação-Suplementar>. Acesso em 20 de setembro de 2018.

### 1.5 Visão Geral
<p align="justify"> A organização do documento dá-se de maneira a possibilitar ao leitor uma melhor visualização das informações expostas. Com essa finalidade, apresenta-se inicialmente a motivação por trás da implementação, que culminou no desenvolvimento dessa proposta. Em segunda instância, são expostos os envolvidos no projeto, explicitando a equipe responsável pela gestão e desenvolvimento do software e evidenciando o valor que este irá agregar aos usuários. Logo, o arquivo retrata todas as funcionalidades do sistema e demais requisitos fundamentais para a documentação do mesmo.</p>

## 2 Posicionando

### 2.1 Oportunidade de Negócios
<p align="justify"> Periodicamente, são feitas compras de produtos de limpeza e alimentos para lares e comércios. Com isso, o consumidor acaba deixando de economizar por não saber quais são os lugares com os preços mais baixos. Vendo essa necessidade de economizar, a aplicação mostrará os preços dos itens com valores mais baixos dos mercados mais próximos.</p>

### 2.2 Instrução do Problema
| | |
| -- | -- |
| O problema de | haver uma grande variação de preços dos ítens domésticos em diversos mercados |
| afeta | todos que fazem compras periodicamente. |
| O impacto do problema é | aumentar os gastos no orçamento mensal. |
| Uma solução bem sucedida incluiria | um comparativo de preços dos ítens domésticos dos  mercados mais próximos. |

### 2.3 Instrução de Posição do Produto
| | |
| -- | -- |
| Para o | comprador doméstico ou comerciário, |
| quem | precisa fazer compras periodicamente. |
| O | EconomizAe |
| é uma | aplicação _web_ |
| que | gera um lista com os menores preços de ítens domésticos dos mercados mais próximos. |
| De outro modo | Mercado Livre,|
| nosso produto | comparará preços de ítens doméstico que são comprados periodicamente.|

## 3 Descrições da Parte Interessada e do Usuário

### 3.1 Demográficos de Mercado
<p align="justify"> O mercado de comércio eletrônico é precário em relação à aplicação que faz comparações de preços de produtos domésticos. Com isso, visamos preencher esse lacuna com nossa aplicação para que os consumidores possam economizar no seu orçamento.</p>

### 3.2 Resumo da Parte Interessada
Nome | Descrição | Responsabilidade
-- | -- | --
Equipe de Desenvolvimento e Gerenciamento | Estudantes da disciplina de Arquitetura e Desenho de Software ministrada na FGA, UnB. | Gerenciar, desenvolver, testar e implantar o software descrito nesse documento.

### 3.3 Resumo do Usuário
Nome | Descrição
-- | --
Consumidor | Indivíduo que faz compras de produtos domésticos periodicamente.

### 3.4 Ambiente do Usuário
A aplicação poderá ser utilizada em todos dispositivo com navegador e acesso a internet.

### 3.5 Perfis das Partes Interessadas
| | |
| -- | -- |
| Representantes | Amanda Bezerra |
| | Caio Gabriel |
| | Eduardo Junio |
| | João Saliba |
| | Mateus de Oliveira |
| | Matheus Roberto |
| | Rafael Bragança |
| | Vinícius Bandeira |
| | Vinícius Cantuária |
| Descrição | Desenvolvedores e gerentes de software. |
| Tipo | Estudantes da disciplina de Arquitetura e Desenho de Software ministrada na FGA, UnB. |
| Responsabilidades | Gerenciar, desenvolver, testar e implantar o software descrito nesse documento. |
| Critérios de sucesso | Entregar os artefatos e funcionalidades solicitados dentro do prazo. |
| Envolvimento | Alto |
| Problemas/Comentários | Relacionar a disponibilidade dos membros da equipe aos prazos estabelecidos |

### 3.6 Perfis do Usuário
| | |
| -- | -- |
| Representantes | Consumidor |
| Tipo | Indivíduo que faz compras de produtos domésticos periodicamente. |
| Responsabilidades | Manter o cadastro atualizado. |
| Critérios de sucesso | Economizar dinheiro. |
| Envolvimento | Alto |
| Problemas/Comentários | - |

### 3.7 Principais Necessidades da Parte Interessada ou do Usuário

#### 3.7.1 Divulgação
<p align="justify"> A forma de divulgação mais comum utilizada por comércios é o panfleto, porém algumas vezes eles se encontram desatualizados e para alterar isto deve se criar um novo, sem contar que alguns lugares não divulgam os preços.</p>

#### 3.7.2 Deslocamento
<p align="justify"> Para a comparação de preços é necessário ir de comércio em comércio procurando o melhor preço para comprar o produto desejado, isso demanda tempo e custo de locomoção.</p>

#### 3.7.3 Recordação
<p align="justify"> Para fazer a comparação de preços as pessoas costumam confiar em suas lembranças e os mais cuidados anotar em papéis, porém quando se trata de vários produtos é difícil lembrar o preço de cada um, tanto para fazer uma comparação entre comércios quanto para comparar com o mês anterior.</p>

### 3.8 Alternativas e Concorrência
Não há alternativas e concorrência para esse tipo de aplicação.

## 4 Visão Geral do Produto

### 4.1 Perspectiva do produto

<p align="justify"> O sistema terá a função de auxiliar os consumidores, identificando os melhores preços entre os comércios. O mesmo fornecerá comparações sobre produtos iguais de diferentes comércios, indicando ao consumidor qual é o comércio mais econômico para ele realizar as compras.</p>

### 4.2 Resumo dos recursos

| **Benefício para o Cliente** | **Recursos de suporte** |
| --- | --- |
| Visualização de preços de um único produto em diferentes comércios | Informações sobre o preço de um produto em diferentes comércios  |
| Análise da lista de compra mais econômica | Lista de compra que compara o preço de cada produto em vários comércios e mostra em qual local saí mais barato o conjunto de compras |
| Visualização do histórico do preço de um produto | Gráfico indicando o comportamento do preço do produto no decorrer de um intervalo |
| Avaliação do usuário sobre o preço do produto | Espaço reservado para que o usuário possa avaliar a veracidade dos preços |

## 5 Recursos do Produto

* Pesquisar produto ou comércio desejado
* Visualizar histórico de pesquisas
* Visualizar menor preço dentre os comércios de uma determinada região
* Criar lista de compras
* Sugerir comércio com o menor custo para a lista de compras
* Cadastrar produto ou comércio
* Atualizar preço de um produto
* Seguir um produto ou comércio
* Notificar alterações de preços em um produto seguido
* Visualizar histórico de preços de um produto ou comércio

## 6 Restrições

Para a utilização do produto descrito, o usuário deverá ter acesso aos dados do sistema que são disponibilizados por outros usuários, implicando assim em certas limitações, tais como:

- O usuário deve dispor de acesso a internet
- O usuário deve dispor de um navegador

## 7 Faixas de Qualidade

### 7.1 Usabilidade
- RU01 - Tempo mínimo para a execução de uma atividade

  É preciso que o tempo de execução das atividades não ultrapassem o tempo de 1 minuto. Em caso deste tempo ser ultrapassado, a plataforma deve apresentar mensagem informando que o tempo de execução foi esgotado.

- RU02 - Recuperação à falhas

  É preciso que o sistema se recupere de possíveis falhas em pelo menos 50% dos casos.

- RU03 - Baixo número de erros na execução de uma tarefa

  Espera-se que o sistema apresente um número máximo de 3 erros por atividade desenvolvida pelo usuário.

- RU04 - Número pequeno de passos para realização de um processo

  Deve ser necessário o máximo de 10 passos para conseguir iniciar e finalizar uma tarefa no sistema.

- RU05 - Facilidade de Uso

  Espera-se que o sistema seja de fácil uso ao usuário, de modo que não seja preciso uso de documentação externa para execução das atividades.

### 7.2 Confiabilidade
- RC01 - Segurança

  Os dados de autenticação do usuário devem ser criptografados para serem guardados no banco de dados.

- RC02 - Disponibilidade

<p align="justify"> O sistema deve permanecer disponível por todo o tempo, 24/7. Para isso, o servidor deve ficar em um ambiente preparado para tal, afim de evitar possíveis contra tempos. A manutenção deve ser feita em um período fora do horário de pico, pela madrugada.</p>

- RC03 - Tempo Médio entre Falhas (MTBF)

  O tempo médio entre falhas do sistema de ser de um mês.

- RC04 - Tempo Médio para Reparo (MTTR)

  O tempo médio de reparo de ser de um dia.

- RC05 - Taxa de erros ou defeitos

| Categoria | Erro |
| -- | --
| Pouca importância | Sistema demorar para responder.
| Média importância | Sistema ficar fora do ar fora do período de matrícula e ajustes.
| Muita importância | Perda total dos dados de autenticação.
| | Vazamento dos dados de autenticação.
| | Total incapacidade da funcionalidade de login.
| | Sistema ficar fora do ar no período de matrícula e ajustes.

### 7.3 Desempenho
- RD01 - Otimização de acessos

  Devido o grande número de acessos durante o início do mês por causa da liberação dos salários, o sistema deve utilizar um balanceamento de cargas para otimizar e garantir o acesso por todos os usuários.

- RD02 - Tempo de processamento

  O sistema não deve ultrapassar 30 segundos para processar a requisição de uma atividade.

- RD03 - Tempo de resposta

  O tempo de resposta de uma pesquisa no sistema não deve ultrapassar o prazo máximo de 1 minuto.

### 7.4 Suportabilidade

A aplicação poderá ser acessado por qualquer dispositivo com navegador e conectividade com a internet.

### 7.5 Restrições de Design

- Processo de software

  Deseja-se que o sistema seja desenvolvido utilizando a metodologia ágil de modo que cada incremento seja testado devidamente antes de ser incorporado.

- Design

  O sistema deve possuir um design intuitivo, utilizando um formato de posicionamento de informações claro e que facilite a visualização.
