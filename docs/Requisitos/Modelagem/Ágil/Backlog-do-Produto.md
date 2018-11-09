Data | Versão | Descrição | Responsáveis
-- | -- | -- | --
29/10/2018 | 0.1 | Versão inicial do documento | Mateus de Oliveira e Vinícius Cantuária
08/11/2018 | 0.2 | Reorganização da estrutura do documento | Amanda Bezerra

# Backlog do Prduto

## Tema: Usuário

|  **Identificador** | **Nome** | **Descrição** | **Tarefas** | **Padrões de Projeto** | **Prioridade** | **Pontuação** |
|  :------: | :------: | :------: | :------: | :------: | :------: | :------: |
|  **UC01** | Realizar Autenticação | Tem como objetivo fazer com que o cliente se identifique para o sistema, para que o sistema possa fornecer as informações corretamente a cada cliente. | <ul><li>Login</li><li>Logout</li> | Proxy | A |  |
|  **UC02** | Manter Usuário | A funcionalidade de manter usuário estabelece as operações de CRUD, ou seja, criação, leitura, atualização e exclusão de dados relacionados ao objeto que representa a classe de usuário. Nesse sentido, ela define que o usuário poderá criar uma conta no sistema e, a partir disto, logar , atualizar as suas informações ou excluir os seus registros. | <ul><li>Criar Usuário (Nome, E-mail, senha, pontos de confiança)</li><li>Atualizar Usuário</li><li>Remover Usuário</li><li>Listar Usuário</li> |  | A |  |
|  **UC03** | Visualizar Ranking | Esta funcionalidade compreende a listagem dos 10 usuários com maior número de pontos de confiança |  |  | D |  |
|  **UC04** | Confirmar preço | Tem como objetivo confirmar se o preço de um determinado produto está correto, caso o produto seja dado como confiavel, os usuários ganham 1 ponto de confiança, caso o produto seja dado como não confiavel, os usuários perdem 1 pontos de confiança |  | Observer(Usuário vai seguir o produto, e de acordo com estes updates ele realiza uma função) | B |  |
|  **UC05** | Questionar preço | Tem como objetivo negar se o preço de um determinado produto, reduzindo assim a confiabilidade deste, caso o produto seja dado como não confiavel, os usuaários ganham 1 ponto de confiança, caso o produto seja dado como confiavel, os usuários perdem 1 pontos de confiança |  | Observer(Usuário vai seguir o produto, e de acordo com estes updates ele realiza uma função) | B |  |
|  **UC06** | Pontuar Confiabilidade do Usuário | O usuário recebe pontos de confiança ao adicionar, confirmar ou questionar preços de produtos, ao adicionar um produto confiavel o usuário recebe 10 pontos |  | Strategy: Dependendo do estado do produto, confiavel ou não, ele vai possuir um calculo diferente para adicionar os pontos ou reduzir | C |  |
|  **UC07** | Evoluir para Usuário Premium | Usuários podem utilizar 100 pontos de confiança para se transformarem em usuários premium, o peso de um usuário premium ao questionar ou confirmar um preço é o dobro de um usuário comum, e este usuário também pode realizar funções como montar lista de compras com mais de 15 produtos, porém este recurso consome seus pontos de confiança |  |  | C |  |

## Tema Produto
|  **Identificador** | **Nome** | **Descrição** | **Tarefas** | **Padrões de Projeto** | **Prioridade** | **Pontuação** |
|  :------: | :------: | :------: | :------: | :------: | :------: | :------: |
|  **UC08** | Manter Produto | A funcionalidade de manter produto estabelece as operações de CRUD, ou seja, criação, leitura, atualização e exclusão de dados relacionados ao objeto que representa a classe de produto. Nesse sentido, ela define que um usuário poderá criar um produto e a partir disso adicionar seu preço, foto, data do preço, local e nome |  |  | A |  |
|  **UC09** | Filtrar produto por preço | Esta funcionalidade tem como objetivo filtrar a listagem de um determinado produto pelo seu preço, em ordem crescente ou decrescente  |  |  | C |  |
|  **UC10** | Mostrar Gráfico de preço | Tem como objetivo apresentar o gráfico do preço de um determinado produto em um período de tempo, para assim determinar as melhores datas para aquisição deste |  |  | D |  |
|  **UC11** | Buscar produto | Este caso de uso permite ao usuário pesquisar um determinado produto pelo seu nome |  |  | B |  |
|  **UC12** | Pontuar Confiabilidade do Produto | A confiabilidade do preço de um produto será determinada através das confirmações e questionamentos dos usuários, um usuário normal soma 2 pontos de confiança para um produto, um usuário não confiavel soma 1 ponto de confiança e um usuário premium soma 3 pontos de confiança |  |  | C |  |

## Tema Comércio
|  **Identificador** | **Nome** | **Descrição** | **Tarefas** | **Padrões de Projeto** | **Prioridade** | **Pontuação** |
|  :------: | :------: | :------: | :------: | :------: | :------: | :------: |
|  **UC13** | Manter Comércio | A funcionalidade de manter comércio estabelece as operações de CRUD, ou seja, criação, leitura, atualização e exclusão de dados relacionados ao objeto que representa a classe de comércio. Nesse sentido, ela define que um usuário poderá criar um comércio e a partir disso adicionar seu local e nome e produtos que este comércio possua |  |  | A |  |
|  **UC14** | Buscar comércio | Este caso de uso permite ao usuário pesquisar um determinado comércio pelo seu nome |  |  | B |  |
|  **UC15** | Autenticar comércio | Esta funcionalidade permite que usuários que sejam donos de um comércio confirmem a posse deste, através de documentos, CNPJ, etc |  |  | E |  |
|  **UC16** | Filtrar comércio por distancia | Esta funcionalidade tem como objetivo filtrar a listagem de comércios através da sua distancia |  |  | D |  |
|  **UC17** | Montar Lista de Compras | Permite ao usuário adicionar e remover produtos em um carrinho de compras, o usuário tera direito a 15 produtos, a não ser que gaste 100 pontos de confiança, neste caso terá direito a adicionar até 100 produtos |  |  | A |  |
|  **UC18** | Filtrar lista de compras por preço | Esta funcionalidade apresenta para o usuário o comércio mais barato com todos aqueles produtos |  |  | B |  |