# Plano de Teste

**API Python Flask**

_versão 1.0_

## Histórico das alterações

| Data       | Versão | Descrição      | Autores                                                                                                                                                                       |
| ---------- | ------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 08/11/2025 | 1.0    | Release inicial | Arthur Gabriel Palmeira Teixeira<br>Emilly Silva Marques dos Santos<br>Isabel de Oliveira Passos Alves<br>Vitor de Jesus dos Santos<br>Yuri Gabriel Ferreira de Jesus Menezes |

## 1 - Introdução

Este documento descreve os requisitos a testar no projeto Book API, os tipos de testes definidos para cada iteração, os recursos de hardware e software a serem utilizados e o cronograma de execução ao longo do desenvolvimento da aplicação. A Book API, desenvolvida com o microframework Flask (python), tem como objetivo gerenciar livros, permitindo operações de consulta, cadastro, edição e exclusão.

Com esse documento, deve ser:

- Identificado as informações do projeto e os componentes de software da API a serem testados.
- Listado os requisitos relacionados às funcionalidades de gerenciamento de livros.
- Visualizado forma como ocorreu testes unitários, de performance e de carga.
- Identificado os recursos necessários para a execução dos testes.
- Listado os resultados obtidos através dos testes.

## 2 - Tipos de teste

Os testes foram selecionados considerando as funcionalidades principais: consultar, cadastrar, editar e deletar livros; bem como os requisitos de desempenho, integração e confiabilidade da aplicação.

- Teste de carga;
- Teste de integração dos componentes;
- Teste de instalação;
- Teste unitário.

### 3.1 - Teste de carga

Tem como objetivo avaliar o comportamento da API sob múltiplas requisições simultâneas, verificando se mantém estabilidade, tempo de resposta adequado e disponibilidade durante picos de uso.

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            Teste de carga
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            ( ) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema (x)
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsáveis
        </th>
        <th colspan="4">
            Equipe de testes
        </th>
    </tr>
    <tr>
        <th>
            Quantos usuários simultâneos são permitidos?
        </th>
        <th colspan="4">
            500 usuários
        </th>
    </tr>
    <tr>
        <th>
            Quantas transações pode-se lidar durante um período específico?
        </th>
        <th colspan="4">
            Durante um período de 5 minutos, 296 usuários e 21.961 requisições, sendo que 50% das requisições falharam.
        </th>
    </tr>
    <tr>
        <th>
            Qual é o ponto de ruptura?
        </th>
        <th colspan="4">
            1 milhão de acessos simultâneos
        </th>
    </tr>
    <tr>
        <th>
            Qual o tempo médio de todas as requisições?
        </th>
        <th colspan="4">
            Tempo médio entre 36 a 41ms, sendo que 95% das requisições abaixo de 70ms.
        </th>
    </tr>
    <tr>
        <th>
            Qual o Endpoint mais rápido e o com maior latência?
        </th>
        <th colspan="4">
            Endpoint mais rápido POST /livros e Endpoint com maior latência GET /livros (lista completa)
        </th>
    </tr>
</table>
<br/>

### 3.2 - Integração dos Componentes

Objetivo de descobrir falhas de interface e garantir que as partes do sistema funcionem juntas corretamente, complementando os testes de unidade que verificam os componentes isoladamente.

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            Teste de integração
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            ( ) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração (x)
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsáveis
        </th>
        <th colspan="4">
            Equipe de testes
        </th>
    </tr>
    <tr>
        <th>
            Existem obstáculos potenciais que precisam ser identificados e corrigidos?
        </th>
        <th colspan="4">
            Não foram identificados obstáculos
        </th>
    </tr>
</table>
<br/>

### 3.3 - Teste de instalação

Objetivo de verificar se o software está instalado como planejado, em diferentes hardwares e sob diferentes condições, como pouco espaço de memória, interrupções de rede, interrupções na instalação.

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            Teste de instalação
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            (x) manual
        </th>
        <th colspan="2">
            ( ) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema (x)
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsáveis
        </th>
        <th colspan="4">
            Equipe de testes
        </th>
    </tr>
    <tr>
        <th>
            Quais são os requisitos de configuração do ambiente para o teste?
        </th>
        <th colspan="4" style="text-align:justify">
            <ul>
                <li>Versão do python ^3.12</li>
                <li>Sistema Operacional Linux</li>
                <li>Baixar as dependências do projeto</li>
            </ul>
        </th>
    </tr>
    <tr>
        <th>
            Os testes da API foram realizados corretamente?
        </th>
        <th colspan="4">
            Sim
        </th>
    </tr>
    <tr>
        <th>
            Quais ferramentas podem ser usadas para o teste?
        </th>
        <th colspan="4">
            Postman e Locust
        </th>
    </tr>
    <tr>
        <th>
            Como lidar com cenários de erro e casos extremos?
        </th>
        <th colspan="4">
            Realizar a leitura do log de erro e fazer a depuração do código
        </th>
    </tr>
</table>
<br/>

### 3.4 - Teste unitário

Teste unitário de software é o processo de testar as menores partes de um programa (unidades, como funções ou métodos) isoladamente para garantir que funcionem corretamente.

<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            Teste unitário
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            ( ) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema (x)
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsáveis
        </th>
        <th colspan="4">
            Equipe de testes
        </th>
    </tr>
    <tr>
        <th>
            O teste inclui lógica desnecessária, variáveis ou código de configuração excessivos?
        </th>
        <th colspan="4">
            Não
        </th>
    </tr>
    <tr>
        <th>
            O teste inclui cenários de sucesso (entradas válidas)?
        </th>
        <th colspan="4">
            Sim
        </th>
    </tr>
    <tr>
        <th>
            Existem testes para garantir a proteção contra regressão (bugs que reaparecem)?
        </th>
        <th colspan="4">
            Não
        </th>
    </tr>
    <tr>
        <th>
            O nome do teste é claro e descreve o método, o cenário e o comportamento esperado?
        </th>
        <th colspan="4">
            Sim
        </th>
    </tr>
    <tr>
        <th>
            O teste segue um padrão claro como "arrange-act-assert" (preparar-agir-validar)?
        </th>
        <th colspan="4">
            Sim
        </th>
    </tr>
    <tr>
        <th>
            O teste é fácil de ler e entender sem precisar olhar o código da função testada?
        </th>
        <th colspan="4">
            Sim
        </th>
    </tr>
    <tr>
        <th>
            Ele é independente, sem depender de outros testes, do estado do banco de dados ou de serviços externos?
        </th>
        <th colspan="4">
            Sim
        </th>
    </tr>
</table>
<br/>

## 4 - Recursos

### 4.1 - Ambiente de teste - Software e Hardware

Foi utilizado como sistema operacional Linux debian em um athlon 3000G 3.5GHz com 16GB ram ddr4 2666mhz.

### 4.2 - Ferramenta de teste

As ferramentas usadas foram o locust (teste de carga) e o pytest (demais testes)

## 5 - Cronograma

|   Tipo de teste   | data de início | data de término |
| :---------------: | :------------: | :-------------: |
|  planejar teste   |   05/11/2025   |   05/11/2025    |
|  projetar teste   |   06/11/2025   |   06/11/2025    |
| implementar teste |   07/11/2025   |   07/11/2025    |
|  executar teste   |   08/11/2025   |   08/11/2025    |
|   avaliar teste   |   08/11/2025   |   08/11/2025    |
