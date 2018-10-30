Data | Versão | Descrição | Responsáveis
-- | -- | -- | --
29/10/2018 | 0.1 | Versão inicial do documento | Amanda Bezerra

# Configuração de Software e Políticas de Repositório

# Introdução
<p align="justify"> Este documento apresenta as configurações e políticas mais relevantes, afim de garantir a integridade e organização do projeto. Seu objetivo é servir como guia e material de consulta para os interessados no projeto.
Serão detalhadas as ferramentas, políticas de repositório, gerenciamento de documentação e monitoria e controle que auxiliarão no bom desenvolvimento e manutenção do projeto. </p>

# Itens de Configuração
Os artefatos utilizados no projeto que serão tratados como itens de configuração e, portanto, necessitam de gerenciamento são:
- **Documentos:** arquivos de texto utilizados para documentar e registrar planejamentos, reuniões, descrição de produtos, artefatos de desenvolvimento, processos, entre outros.
- **Código:** conjunto de arquivos de texto que reúne código de uma ou mais linguagens de programação ou marcação.

# Ferramentas
A tabela a seguir descreve as ferramentas que serão utilizadas no desenvolvimento e manutenção do projeto, bem como suas respectivas utilizações.

| Ferramenta | Descrição do uso |
| :--: | :--: |
| Git | Utilizada para controle de versão e gerenciamento de código do projeto |
| Github | Utilizada para hospedar o código e documentos do projeto |
| Zenhub | Utilizada para gerenciar e acompanhar progresso das issues |
| Docker | Utilizada para empacotar a aplicação e os ambientes que serão utilizados no projeto |
| Travis | Utilizada para garantir a integração contínua do projeto |
| Heroku | Utilizada para hospedar a aplicação em nuvem |
| Codeclimate | Utilizada para monitorar e garantir a qualidade do código do projeto |

# Políticas de Repositório

## Política de Commits
Para commits no repositório do projeto, as seguintes regras devem ser seguidas:
- Os commits para o repositório do projeto devem estar em inglês.
- A mensagem do commit deve ser curta e expressar uma ação de forma clara e significativa.
- O commit deve iniciar com letra maiúscula.
- O commit deve iniciar com um verbo no infinitivo.

Exemplo:
```
git commit -m "Create new home Screen"
```
- Caso o commit tenha sido realizado por mais de um autor, deve-se utilizar _co-authored_ na mensagem do commit

Exemplo:
```
$ git commit -m "Refactor usability tests.
>
>
Co-authored-by: name <name@example.com>
Co-authored-by: another-name <another-name@example.com>"
```

## Política de Branches
Os nomes das branches devem estar em inglês e serem curtos e objetivos.

O repositório do projeto terá os seguintes tipos de branch:

- **master:** branch única que mantém uma versão estável do projeto
- **develop:** branch única que mantém uma versão atualizada do projeto
- **USX_nome_da_usa** ou **TSX_nome_da_ts**: branch utilizada para desenvolver uma única _feature_, história de usuário ou história técnica
- **fix_nome_da_correcao:** branch utilizada para correção de um defeito

![](https://wac-cdn.atlassian.com/dam/jcr:b5259cce-6245-49f2-b89b-9871f9ee3fa4/03%20.svg?cdnVersion=k)

## Política de Issues
<p align="justify"> As issues devem ser abertas no repositório para relatar <i>bugs</i> a serem corrigidos, descrever histórias de usuário ou histórias técnicas a serem implementadas ou solicitar suporte.

As issues relacionadas a correções e histórias devem ser pontuadas e assinadas, afim de determinar o esforço necessário para que sejam implementadas, bem como identificar os desenvolvedores responsáveis pela implementação.

É recomendado a utilização de _labels_ para melhorar a identificação e organização das issues. </p>

Para criação de uma _issue_, deve ser utilizado este [template](https://github.com/DSW-2018/projetoDesenho/blob/master/.github/ISSUE_TEMPLATE.md).

## Política de aprovação
<p align="justify"> As alterações realizadas por implementação de <i>features</i> e correções de <i>bugs</i> são incorporadas ao projeto através de pull requests. Para que um pull request seja aceito, este deve estar em conformidade com os padrões de commit e estilo de código estabelecidos. Outro critério de aceitação de um pull request é que a <i>build</i> da ferramenta de integração contínua deve ser aprovada, constando como "passed", salvo casos específicos que devem ser devidamente justificados. </p>

Para criação de um pull request, deve ser utilizado este [template](https://github.com/DSW-2018/projetoDesenho/blob/master/.github/PULL_REQUEST_TEMPLATE.md).

# Gerenciamento de documentação
Toda documentação do projeto deve estar disponível na [wiki](https://github.com/DSW-2018/projetoDesenho/wiki) do projeto.

## Políticas de commits e branches de documentos
<p align="justify"> As mesmas políticas para commits de código são aplicadas para commits de documentos, mas no que diz respeito a branches, não há padrões estabelecidos para sua criação e manutenção, exigindo apenas que toda documentação estável esteja na branch <i>master</i>. </p>

## Versionamento de documentos
É recomendado que todos os documentos possuam uma tabela de histórico de versão no topo do documento como esta:

| Data | Versão | Descrição | Responsáveis |
| :--: | :--: | :--: | :--: |
| Dia/Mês/Ano da alteração | X.0..., onde cada versão representa uma mudança significativa no documento| Descreve a alteração e a seção modificada | Nome do responsável pela alteração |


# Monitoramento e controle
<p align="justify"> Toda a equipe é responsável por revisar frequentemente todos os artefatos produzidos para garantir que estão de acordo com as configurações e políticas estabelecidas e, caso não estejam, alertar o responsável/autor para que as correções sejam realizadas imediatamente, podendo também realizar a correção, desde que o responsável/autor seja avisado.</p>
