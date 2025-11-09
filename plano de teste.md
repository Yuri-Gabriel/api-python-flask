# Plano de Teste

**API Python Flask**

*versão 1.0*

## Histórico das alterações

   Data    | Versão |    Descrição   | Autores
-----------|--------|----------------|-----------------
08/11/2025 |  1.0   | Release incial | Arthur Gabriel Palmeira Teixeira<br>Emilly Silva Marques dos Santos<br>Isabel de Oliveira Passos Alves<br>Vitor de Jesus dos Santos<br>Yuri Gabriel Ferreira de Jesus Menezes


## 1 - Introdução

**Modificar texto**
Este documento descreve os requisitos a testar, os  tipos de testes definidos para cada iteração, os recursos de hardware e software a serem empregados e o cronograma dos testes ao longo do projeto. As seções referentes aos requisitos, recursos e cronograma servem para permitir ao gerente do projeto acompanhar a evolução dos testes.

Com esse documento, você deve:
- Identificar informações de projeto existentes e os componentes de software que devem ser testados.
- Listar os Requisitos a testar.
- Recomendar e descrever as estratégias de teste a serem empregadas.
- Identificar os recursos necessários e prover uma estimativa dos esforços de teste.
- Listar os elementos resultantes do projeto de testes.

## 2 - Tipos de teste

**Modificar texto**
Esta seção deve contém os tipos de testes escolhidos para cada iteração do projeto.
Pode-se definir inicialmente apenas os tipos de testes que serão usadas na próxima iteração, mas é possível também já registrar eventuais tipos de teste que se espera utilizar nas demais iterações. 
Com base no guia de testes, indique os tipos de testes que melhor se adéquam aos requisitos, tipo da aplicação e seus recursos disponíveis e, caso necessário complemente ou forneça mais detalhes da técnica e dos critérios de completude sugeridos no guia para cada tipo de teste indicado.

- Teste de carga;
- Teste de integração;
- Teste de instalação;
- Teste de performance;
- Teste unitário.

### 3.1 - Teste de carga

Objetivo de avaliar como um sistema se comporta sob uma carga de trabalho esperada, simulando o uso real e simultâneo de usuários para identificar gargalos, medir o tempo de resposta, garantir a estabilidade e determinar se os padrões de desempenho do sistema são atendidos.

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

Objetivo de verificar se o software está instalado como planejado, em diferentes hardwares e sob diferentes condições, como pouco espaço  de memória, interrupções de rede, interrupções na instalação.

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

| Tipo de teste | data de início | data de término |
|:---:          |:---:           |:---:            |
planejar teste     | 05/11/2025     | 05/11/2025   |
projetar teste     | 06/11/2025     | 06/11/2025   |
implementar teste  | 07/11/2025     | 07/11/2025   |
executar teste     | 08/11/2025     | 08/11/2025   |
avaliar teste      | 08/11/2025     | 08/11/2025   |