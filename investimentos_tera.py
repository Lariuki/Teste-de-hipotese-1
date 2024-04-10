# -*- coding: utf-8 -*-
"""Investimentos TERA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gXB4mHBnx_yleisNm4JxLE4bZV61NEcG
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import missingno as msno
from termcolor import colored

dfInvest = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/Tera/Demoday Tera 2022/Edicao_04_RaioX - Base de Dados.xlsx")
dfInvest.head()

dfInvest.info()

dfInvest.dtypes

dfInvest.columns

#Dados nulos por coluna
print("Dados nulos por coluna:")
dfInvest.isnull().sum()

dfInvest.shape

"""**276 colunas deletadas**"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
msno.matrix(dfInvest.sample(3408, replace=False))

"""**Criando uma nova tabela com as Colunas relevantes**

*   NQUEST = ID
*   SEXO = Sexo
*   IDADE1 = Idade Aberta
*   IDADE = Idade
*   CLASSE = Classificação Econômica
*   ESTADO = Estado
*   REGIAO = Região Geográfica
*   METROP = Natureza do município
*   PORTE = Porte do município
*   PF2A = Trabalha atualmente ou já trabalho na área de Pesquisa de Mercado?
*   PF2B = Trabalha atualmente em Agência de Publicidade?
*   PF2C = Trabalha atualmente em veículos de comunicação como jornais, rádios, televisão ou portais da internet?
*   CARRO = Automóveis de passeio exclusivamente de uso particular? Quantos?
*   EMPREG = Empregados mensalistas, considerando apenas os que trabalham pelo menos 5 dias na semana? Quantos?
*   MAQLAV = Máquinas de lavar roupas, excluindo tanquinho? Quantas?
*   DVD = Aparelho de DVD, incluindo qualquer outro dispositivo que leia DVD? Quantos?
*   BANHE = Banheiros? Quantos?
*   GELAD = Geladeira? Quantas?
*   FREEZER = Freezer independente ou aquele que faz parte da geladeira "duplex"? Quantos?
*   COMPUT = Microcomputador, considerando computadores de mesa, lap tops, notebooks e netbooks e excluindo tablets, palms ou smartphones? Quantos?
*   LAVLOU = Máquina de lavar louças? Quantas?
*   MICROON = Fornos de micro-ondas? Quantos?
*   MOROCIC = Motocicletas, desconsiderando as que são utilizadas exclusivamente para fins profissionais? Quantas?
*   SECADORA = Máquina secadora de roup? Quantas?
*   AGUA = A água utilizada no seu domicílio é proveniente de rede geral de distribuição, poço, nascente ou de outro meio?
*   RUA = Considerando o trecho da rua do seu domicílio, você diria que a rua é asfaltada, pavimentada, de terra ou cascalho?
*   ESCOLAC = Escolaridade do chefe da família
*   PONTOS = Soma dos pontos
*   ESCOLA = Escolaridade
*   PEA = Ocupação
*   P8_1 = Cadernet de poupança
*   P8_2 = Fundos de investimentos, como Renda Fixa, Multimercado, Fundo cambial, Fundos de ações, etc.
*   P8_3 = Títulos públicos via tesouro direto (pré-fixados, pós-fixados e de inflação)
*   P8_4 = Títulos privados, como Debentures, CDB, LCI, LCA, LC, Certificados de Operações estruturadas (COE), etc
*   P8_5 = Ações na bolsa de valores
*   P8_6 = Plano de previdência privada
*   P8_7 = Moedas digitais
*   P8_8 = Ouro
*   P8_9 = Compra e venda de imóveis
*   P8_10 = Em casa/ no colchão
*   P8_18 = Moedas estrangeiras
*   P10_1_ANOS = P10 Anos Caderneta de poupança
*   P10_1_MESES = P10 Meses Caderneta de poupança
*   P10_2_ANOS = P10 Anos Fundos de investimentos, como Renda Fixa, Multimercado, Fundo cambial, Fundo de ações, etc
*   P10_2_MESES = P10 Meses Fundos de investimentos, como Renda Fixa, Multimercado, Fundo cambial, Fundo de ações, etc
*   P10_3_ANOS = P10 Anos Títulos públicos via tesouro direto (pré-fixados, pós-fixados e de inflação)
*   P10_3_MESES = P10 Meses Títulos públicos via tesouro direto (pré-fixados, pós-fixados e de inflação)
*   P10_4_ANOS = P10 Anos Ações na bolsa de valores
*   P10_4_MESES = P10 Meses Ações na bolsa de valores
*   P10_5_ANOS = P10 Anos Ações na bolsa de valores
*   P10_5_MESES = P10 Meses Ações na bolsa de valores
*   P10_6_ANOS = P10 Anos Plano de previdência privada
*   P10_6_MESES = P10 Meses Plano de previdência privada
*   P10_7_ANOS = P10 Anos Moedas digitais
*   P10_7_MESES = P10 Meses Moedas digitais
*   P10_8_ANOS = P10 Anos Ouro
*   P10_8_MESES = P10 Meses Ouro
*   P10_9_ANOS = Anos Compra e venda de imóveis
*   P10_9_MESES = Meses Compra e venda de imóveis
*   P10_10_ANOS = Anos Em casa/ no colchão
*   P10_10_MESES = Meses Em casa/ no colchão
*   P10_18_ANOS = Anos Moedas estrangeira
*   P10_18_MESES = Meses Moedas estrangeira
*   P10_981_ANOS = Anos Outras respostas 1° posição
*   P10_981_MESES = Meses Outras respostas 1° posição
*   P10_982_ANOS = Anos Outras respostas 2° posição
*   P10_982_MESES = Meses Outras respostas 2° posição
*   P10_983_ANOS = Anos Outras respostas 3° posição
*   P50A = Retirar dinheiro de aplicações financeiras ou outras reservas que tinham antes da pandemia
*   P50B = Vender algum bem
*   P50C = Pedir empréstimos, usar cheque especial ou rotativo do cartão
*   P13A = 1° Lugar
*   P13B = 2° Lugar
*   P13C = 3° Lugar
*   P14_1 = Presencialmente, ou seja, falando com o gerente ou com o assessor/especialista de investimento
*   P14_2 = Aplicativos de corretoras de investimentos
*   P14_3 = Sites de notícias/Blogs e fóruns de investimentos
*   P14_4 = Consultorias de investimento
*   P14_6 = Amigos/parentes
*   P14_20 = Por telefone, falando com o gerente ou com o assessor/ especialista de investimento
*   P14_98 = Outras respostas
*   P14_981 = P14 Outras respostas 1° posição
*   P14_982 = P14 Outras respostas 2° posição
*   P14_983 = P14 Outras respostas 3° posição
*   P15_1 = Compara o rendimento atual da sua aplicação com a mesma aplicação em períodos anteriores
*   P15_2 = Compara o rendimento atual da sua aplicação com outros índices da economia relacionados ao mesmo período
*   P15_3 = Conversa com gerente/asessor/especialista de investimento regularmente sobre suas aplicações e o momento do mercado
*   P15_4 = Comparar o rendimento atual da sua aplicação com outros tipos de aplicações
*   P15_5 = Compara o rendimento atual da sua aplicação com as aplicações de outras instituições financeiras
*   P15_98 = Outras respostas
*   P15_981 = P15 Outras respostas 1° posição
*   P15_982 = P15 Outras respostas 2 posição
*   P15_983 = P15 Outras respostas 3° posição
*   P15_984 = P15 Outras respostas 4° posição
*   P15_985 = P15 Outras respostas 5° posição
*   P38_1 = Pessoalmente no banco
*   P38_2 = No site do banco
*   P38_3 = No aplicativo do banco
*   P38_4 = No site da corretora de investimentos
*   P38_5 = No aplicativo da corretora de investimento
*   P38_6 = Clubes de investimento
*   P38_7 = Pelo telefone no banco
*   P38_98 = Outras respostas
*   P38_981 = P38 Outras respostas 1° posição
*   P38_982 = P38 Outras respostas 2° posição
*   P38_983 = P38 Outras respostas 3° posição
*   P38_984 = P38 Outras respostas 4° posição
*   P38_985 = P38 Outras respostas 5° posição
*   P41A = A redução das taxas de juros
*   P41B = A pandemia da Covid-19
*   P41C = O risco de desemprego
*   P28A = Não penso em parar de trabalhar, porque não me vejo parado
*   P28B = Não consigo pensar em aposentadoria, porque não tenho dinheiro suficiente para poder parar de trabalhar
*   P28C = Ando preocupado com minha aposentadoria
*   P28D = Já estou planejando minha aposentadoria, porque tenho metas de chegar sossegado à velhice
*   ESTCIVIL = Qual é o seu estado conjugal?
*   INTERNET = Você costuma acessar a internet sempre, de vez em quando ou raramente?
*   NFILHOS = Presença de filhos
*   IDAA = Idade do filho 1
*   IDAB = Idade do filho 2
*   IDAC = Idade do filho 3
*   IDAD = Idade do filho 4
*   IDAE = Idade do filho 5
*   IDAF = Idade do filho 6
*   IDAG = Idade do filho 7
*   IDAH = Idade do filho 8
*   IDAI = Idade do filho 9
*   RENDA = Renda individual mensal
*   RENDAF = Renda familiar mensal



"""

dfInvest_labels = dfInvest[['NQUEST', 'SEXO', 'IDADE1', 'IDADE', 'CLASSE', 'ESTADO', 'REGIAO', 'METROP', 'PORTE', 'PF2A', 'PF2B', 'PF2C', 'CARRO', 'EMPREG', 'MAQLAV', 'DVD', 'BANHE', 'GELAD', 'FREEZER', 'COMPUT', 'LAVLOU', 'MICROON', 'MOTOCIC', 'SECADORA', 'AGUA', 'RUA', 'ESCOLAC', 'PONTOS', 'ESCOLA', 'PEA', 'P8_1', 'P8_2', 'P8_3', 'P8_4', 'P8_5', 'P8_6', 'P8_7', 'P8_8', 'P8_9', 'P8_10', 'P8_18',  'P9A', 'P9B', 'P9C', 'P9D', 'P9E', 'P9F', 'P9G', 'P9H', 'P9I', 'P10_1_ANOS', 'P10_1_MESES', 'P10_2_ANOS', 'P10_2_MESES', 'P10_3_ANOS', 'P10_3_MESES', 'P10_4_ANOS', 'P10_4_MESES', 'P10_5_ANOS', 'P10_5_MESES', 'P10_6_ANOS', 'P10_6_MESES', 'P10_7_ANOS', 'P10_7_MESES', 'P10_8_ANOS', 'P10_8_MESES',
                            'P10_9_ANOS', 'P10_9_MESES', 'P10_10_ANOS', 'P10_10_MESES', 'P10_18_ANOS', 'P10_18_MESES', 'P10_981_ANOS', 'P10_981_MESES', 'P10_982_ANOS', 'P10_983_ANOS', 'P10_983_MESES','P50A', 'P50B', 'P50C', 'P13A', 'P13B', 'P13C', 'P14_1', 'P14_2', 'P14_3', 'P14_4', 'P14_6', 'P14_20', 'P14_98', 'P14_981', 'P14_982', 'P14_983', 'P15_1', 'P15_2', 'P15_3', 'P15_4', 'P15_5', 'P15_98', 'P15_981', 'P15_982', 'P15_983', 'P15_984', 'P15_985', 'P38_1', 'P38_2', 'P38_3', 'P38_4', 'P38_5', 'P38_6', 'P38_7', 'P38_98', 'P38_981', 'P38_982', 'P38_983', 'P38_984', 'P38_985', 'P41A', 'P41C', 'P28A', 'P28B', 'P28C', 'P28D', 'ESTCIVIL', 'INTERNET', 'NFILHOS', 'IDAA', 'IDAB',
                            'IDAC', 'IDAD', 'IDAE', 'IDAF', 'IDAG', 'IDAH', 'IDAI', 'IDAJ', 'RENDA', 'RENDAF', ]]
dfInvest_labels

#Dados nulos por coluna
print("Dados nulos por coluna:")
dfInvest_labels.isnull().sum()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
msno.matrix(dfInvest_labels.sample(3408, replace=False))

"""**Limpeza dos dados**

Deletando dados
"""

#Deletando colunas vazias
dfInvest1 = dfInvest_labels.drop(columns=['IDAH', 'IDAI', 'IDAJ', 'P14_98','P14_981','P14_982', 'P14_983','P15_98', 'P15_981', 'P15_982', 'P15_983', 'P15_984', 'P15_984', 'P15_985', 'P38_98', 'P38_981', 'P38_982', 'P38_983', 'P38_984', 'P38_985', 'P10_981_ANOS', 'P10_981_MESES', 'P10_982_ANOS', 'P10_983_ANOS', 'P10_983_MESES'])

dfInvest1.head(5)

#deletando duplicatas
dfInvest2 = dfInvest1.drop_duplicates(subset=['NQUEST'])
#não temos itens duplicados

"""Identificando valores"""

dfInvest2.isnull().sum()

#DataFrame sendo transformado em csv
dfInvest2.to_excel('Investimentos_novatabela.xlsx', index=False)

from google.colab import drive
drive.mount('/content/drive')

#Idade do filho 5
#999 corresponde a não ter filhos
#997 corresponde recusa
#101 Menos de 1
dfInvest2['IDAE'].value_counts()

#Trabalha atualmente ou já trabalhou na área de Pesquisa de Mercado?
#1-SIM 2-NÃO
dfInvest2['PF2A'].value_counts()

#Trabalha atualmente em Agência de Publicidade?
#1-SIM 2-NÃO
dfInvest2['PF2B'].value_counts()

#Trabalha atualmente em veículos de comunicação como jornais, rádios, televisão ou portais da internet?
#1-SIM 2-NÃO
dfInvest2['PF2C'].value_counts()

#Automóveis de passeio exclusivamente de uso particular? Quantos?
#96 - NÃO POSSUI
dfInvest2['CARRO'].value_counts()

#Empregados mensalistas, considerando apenas os que trabalham pelo menos 5 dias na semana? Quantos?
#96 - NÃO POSSUI
dfInvest2['EMPREG'].value_counts()

#Máquinas de lavar roupas, excluindo  tanquinho? Quantas?
#96 - NÃO POSSUI
dfInvest2['MAQLAV'].value_counts()

#Banheiros? Quantos?
dfInvest2['BANHE'].value_counts()

#Escolaridade do chefe da família
#1- Analfabeto/ Primário/ Fundamental I incompleto
#2- Primário ou Fundamental I completo/ Ginasial ou Fundamental II incompleto
#3- Ginasial ou Fundamental II completo
#4- Colegial ou Ensino Médio incompleto
#5- Colegial ou Ensino Médio completo
#6- Superior incompleto
#7- Superior completo
#8- Pós-graduação
#97- Recusa
dfInvest2['ESCOLAC'].value_counts()

#Escolaridade
#1- Analfabeto/ Primário/ Fundamental I incompleto
#2- Primário ou Fundamental I completo/ Ginasial ou Fundamental II incompleto
#3- Ginasial ou Fundamental II completo
#4- Colegial ou Ensino Médio incompleto
#5- Colegial ou Ensino Médio completo
#6- Superior incompleto
#7- Superior completo
#8- Pós-graduação
#97- Recusa
dfInvest2['ESCOLA'].value_counts()

#Ocupação
#1- Assalariado registrado
#2- Assalariado sem registro
#3- Funcionário público
#4- Autônomo regular (Paga ISS)
#5- Profissional liberal (autônomo universitário)
#6- Empresário
#7- Free-lance/ bico
#8- Estagiário/ aprendiz (remunerado)
#9- Outros PEA
#10- Desempregado (procura emprego)
#17- Autônomos por conta própria (Motoristas, entregadores sem MEI)
dfInvest2['PEA'].value_counts()

#Caderneta de poupança
#1-SIM 2-NÃO
dfInvest2['P8_1'].value_counts()

#Fundos de investimentos, como Renda Fixa, Multimercado, Fundo cambial, Fundos de ações, etc.
#1-SIM 2-NÃO
dfInvest2['P8_2'].value_counts()

#Títulos públicos via tesouro direto (pré-fixados, pós-fixados e de inflação)
dfInvest2['P8_3'].value_counts()

#Títulos privados, como Debêntures, CDB, LCI, LCA, LC, Certificados de Operações estruturadas (COE), etc.
dfInvest2['P8_4'].value_counts()

#Ações na bolsa de valores
dfInvest2['P8_5'].value_counts()

#Plano de previdência privada
dfInvest2['P8_6'].value_counts()

#Moedas digitais
dfInvest2['P8_7'].value_counts()

#Ouro
dfInvest2['P8_8'].value_counts()

#Compra e venda de imóveis
dfInvest2['P8_9'].value_counts()

#Em casa/ no colchão
dfInvest2['P8_10'].value_counts()

#Moedas estrangeiras
dfInvest2['P8_18'].value_counts()

#
#1- Caderneta de poupança
#2- Fundos de investimentos, como Renda Fixa, Multimercado, Fundo cambial, Fundos de ações, etc. (fundos imobiliários)
#3- Títulos públicos via tesouro direto (pré-fixados, pós-fixados e de inflação)
#4- Títulos privados, como Debêntures, CDB, LCI, LCA, LC, Certificados de Operações estruturadas (COE), etc.
#5- Ações na bolsa de valores (Bovespa/ ações de empresas)
#6- Plano de previdência privada (VGBL)
#7- Moedas digitais (Bitcoin/ Criptomoeda)
#8- Ouro
#9- Compra e venda de imóveis/ imobiliário
#10- Em casa/ no colchão
#11- Abrir próprio negócio/ investimentos no negócio próprio/ capital de giro/ empreendedorismo
#12- Consórcio/ carta de crédito
#13- Título de Capitalização/ Pic Itaú/ Pé Quente Bradesco/ Ourocap
#14- Compra e venda de produtos (roupas/ alimentos)
#15- Automóvel/ Compra e venda de automóveis
#16- Agronegócio/ agropecuária (compra e venda de gado)/ agricultura
#17- Conta corrente
#18- Moedas estrangeiras
#19- Empréstimo
#20- Marketing multinível
#21- Opções binárias
#22- Seguros (seguro de vida)
#23- Investir em empresas/ cotas de empresa
#26- Aplicação/ banco/ investimento/ título (sem especificar)
#28- Citou indicadores (CDI/ Selic)
#29- Renda variável (s/ especificar)
#30- Renda Fixa (s/ especificar)
#31- Conta Digital/ bancos digitais (rendimento direto na conta/ Nubank/ Picpay/ PagSeguro)
#32- Mercados futuros
#33- Mercado financeiro
#34- Derivativos
#96- Não utiliza nenhum
#98- Outras respostas
#99- Não lembra/ não sabe
#0 - Campo nulo
dfInvest2['P9A'].value_counts()

#Inserindo valores aos campos nulos
dfInvest2['P9A'].fillna('0', inplace = True)

#Não possuimos mais valores nulos nesta coluna
dfInvest2['P9A'].isnull().sum()

dfInvest2['P9B'].value_counts()

dfInvest2['P9B'].isnull().sum()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9B'].fillna('0', inplace = True)

dfInvest2['P9C'].value_counts()

dfInvest2['P9C'].isnull().sum()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9C'].fillna('0', inplace = True)

dfInvest2['P9D'].value_counts()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9D'].fillna('0', inplace = True)

dfInvest2['P9E'].value_counts()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9E'].fillna('0', inplace = True)

dfInvest2['P9F'].value_counts()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9F'].fillna('0', inplace = True)

dfInvest2['P9G'].value_counts()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9G'].fillna('0', inplace = True)

dfInvest2['P9H'].value_counts()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9H'].fillna(0, inplace = False)

dfInvest2['P9I'].value_counts()

#Inserindo valor 0 para os campos nulos
dfInvest2['P9I'].fillna('0', inplace = False)

# idade
dfInvest2['IDADE1'].value_counts()

# idade
idade = dfInvest2['IDADE'].value_counts()

Idade1 = idade.sort_values(ascending=False)
Idade1

# sexo
sexo = dfInvest2['SEXO'].value_counts()

Sexo1 = sexo.sort_values(ascending=False)
Sexo1

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
msno.matrix(dfInvest2.sample(3408, replace=False))

msno.bar(dfInvest2)

#Retirar
dfInvest3 = dfInvest2.drop(columns=['IDAG', 'IDAF', 'IDAE', 'IDAD', 'IDAC', 'IDAB', 'IDAA', 'P10_18_MESES', 'P10_18_ANOS', 'P10_10_MESES', 'P10_10_ANOS', 'P10_9_MESES', 'P10_9_ANOS', 'P10_8_MESES', 'P10_8_ANOS', 'P10_7_MESES', 'P10_7_ANOS', 'P10_6_MESES', 'P10_6_ANOS', 'P10_6_MESES', 'P10_5_MESES', 'P10_5_ANOS', 'P10_4_MESES', 'P10_4_ANOS', 'P10_3_MESES', 'P10_3_ANOS', 'P10_2_MESES', 'P10_2_ANOS', 'P10_1_MESES', 'P10_1_ANOS'])

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
msno.matrix(dfInvest3.sample(3408, replace=False))

#Criar uma nova coluna especificando 0 para não investidores e 1 para investidores
#Critérios utilizados, primeiramente de acordo com a classificação da coluna 'P9A', para não investidores = 96, 98 e 0 / investidores = todo o resto
#Preenchendo a coluna 'Status_investidor'
import numpy as np
conditions = [
            (dfInvest3['P9A'] == 8.0),
            (dfInvest3['P9A'] == 9.0),
            (dfInvest3['P9A'] == 10.0),
            (dfInvest3['P9A'] == 11.0),
            (dfInvest3['P9A'] == 12.0),
            (dfInvest3['P9A'] == 13.0),
            (dfInvest3['P9A'] == 14.0),
            (dfInvest3['P9A'] == 15.0),
            (dfInvest3['P9A'] == 16.0),
            (dfInvest3['P9A'] == 17.0),
            (dfInvest3['P9A'] == 18.0),
            (dfInvest3['P9A'] == 19.0),
            (dfInvest3['P9A'] == 20.0),
            (dfInvest3['P9A'] == 21.0),
            (dfInvest3['P9A'] == 22.0),
            (dfInvest3['P9A'] == 23.0),
            (dfInvest3['P9A'] == 32.0),
            (dfInvest3['P9A'] == 34.0),
            (dfInvest3['P9A'] == 96.0),
            (dfInvest3['P9A'] == 98.0),
            (dfInvest3['P9A'] == 99.0),
            (dfInvest3['P9A'] == '0'),
            ]
choices = ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
dfInvest3['Status_investidor'] = np.select(conditions, choices, default = 1)
dfInvest3.head()

dfInvest3['P9A'].value_counts()

dfInvest3['Status_investidor'].value_counts()

#Criando coluna classe de acordo com pesquisas (junção da renda familiar e classificando em classe) = 'CLASSEF'
#Salário mínimo R$ 1045,00, juntando todo mundo cuja a soma de todos os rendimentos da família for de até R$ 2090
# 1 - Classe A - Acima de R$ 20.900 (+20 salários)
# 2 - Classe B - Entre R$ 10.450,01 e R$ 20.900 (entre 10 a 20 salários)
# 3 - Classe C - Entre R$ 4.180 e R$ 10.450 (entre 4 e 10 salários)
# 4 - Classe D - Entre R$ 2.090,01 e R$ 4.180 (entre 2 e 4 salários)
# 5 - Classe E - 2 salários mínimos

conditions2 = [
            (dfInvest3['RENDAF'] == 1),
            (dfInvest3['RENDAF'] == 2),
            (dfInvest3['RENDAF'] == 3),
            (dfInvest3['RENDAF'] == 4),
            (dfInvest3['RENDAF'] == 5),
            (dfInvest3['RENDAF'] == 6),
            (dfInvest3['RENDAF'] == 7),
            (dfInvest3['RENDAF'] == 8),
            (dfInvest3['RENDAF'] == 99)
            ]
choices2 = [5, 5, 4, 4, 3, 2, 1, 1, 99]
dfInvest3['CLASSEF'] = np.select(conditions2, choices2, default = 97)
dfInvest3.head()

dfInvest3['RENDAF'].value_counts()

"""# **Correlações**

Link: https://medium.com/omixdata/estat%C3%ADstica-an%C3%A1lise-de-correla%C3%A7%C3%A3o-usando-python-e-r-d68611511b5a

A análise de correlação é uma forma descritiva que mede se há e qual o grau de dependência entre variáveis, ou seja, o quanto uma variável interfere em outra, lembrando que essa relação de dependência pode ou não ser causal.

* ρ = 0,9 a 1 (positivo ou negativo): correlação muito forte;
* ρ = 0,7 a 09 (positivo ou negativo): correlação forte;
* ρ = 0,5 a 0,7 (positivo ou negativo): correlação moderada;
* ρ = 0,3 a 0,5 (positivo ou negativo): correlação fraca;
* ρ = 0 a 0,3 (positivo ou negativo): não possui correlação.
"""

dfInvest4 = dfInvest3[['SEXO', 'IDADE1', 'CLASSEF', 'Status_investidor', 'ESTADO', 'ESCOLA', 'PEA', 'P9A', 'RENDA', 'RENDAF']]

correlation = dfInvest4.corr()

plot = sns.heatmap(correlation, annot = True, fmt=".1f", linewidths=.15)
plot

"""# **Análises primárias**

Quantidade de investidores e não investidores
"""

# Group by do total de investidores e não investidores por sexo

group = dfInvest3.groupby(['Status_investidor']).agg({'Status_investidor': ['count']})
group

Não_investidores = ((1678*100) / (1679+1730))
print("Não investidores:", Não_investidores)
Investidores = ((1730*100) / (1679+1730))
print("Investidores:", Investidores)

"""Total de investidores por sexo"""

# Group by do total de investidores e não investidores por sexo
# 1 Masculino / 2 Feminino
group1 = dfInvest3.groupby(['Status_investidor','SEXO']).agg({'Status_investidor': ['count']})
group1

Homens_investidores = ((899*100)/(899+779))
Homens_não_investidores = ((779*100)/(899+779))
Mulheres_investidoras = ((937*100)/(937+793))
Mulheres_não_investidoras = ((793*100)/(937+793))
print("Homens Investidores:", Homens_investidores)
print("Homens não investidores:", Homens_não_investidores)
print("Mulheres investidoras:", Mulheres_investidoras)
print("Mulheres investidoras:", Mulheres_não_investidoras)

"""Total de investidores por faixa de idade e sexo"""

#Group by de total de investidores por faixa de idade e sexo
group2 = dfInvest2.groupby(['SEXO','IDADE']).agg({'P9A': ['count']})
group2

homens_idade = ((234*100)/(234+437+431+456+278))
homens_idade1 = ((437*100)/(234+437+431+456+278))
homens_idade2 = ((431*100)/(234+437+431+456+278))
homens_idade3 = ((456*100)/(234+437+431+456+278))
homens_idade4 = ((278*100)/(234+437+431+456+278))
print("HOMENS")
print("16 a 24 anos:", homens_idade)
print("25 a 34 anos:", homens_idade1)
print("35 a 44 anos:", homens_idade2)
print("45 a 59 anos:", homens_idade3)
print("60 anos ou mais:", homens_idade4)
mulheres_idade = ((186*100)/(186+367+375+412+232))
mulheres_idade1 = ((367*100)/(186+367+375+412+232))
mulheres_idade2 = ((375*100)/(186+367+375+412+232))
mulheres_idade3 = ((412*100)/(186+367+375+412+232))
mulheres_idade4 = ((232*100)/(186+367+375+412+232))
print("MULHERES")
print("16 a 24 anos:", mulheres_idade)
print("25 a 34 anos:", mulheres_idade1)
print("35 a 44 anos:", mulheres_idade2)
print("45 a 59 anos:", mulheres_idade3)
print("60 anos ou mais:", mulheres_idade4)

"""Total de investidores e não investidores por faixa etária"""

# 0 para não investidores / 1 investidores
group2 = dfInvest3.groupby(['Status_investidor', 'IDADE']).agg({'Status_investidor': ['count']})
group2

investidores_idade = ((257*100)/(257+383+372+404+262))
investidores_idade1 = ((383*100)/(257+383+372+404+262))
investidores_idade2 = ((372*100)/(257+383+372+404+262))
investidores_idade3 = ((404*100)/(257+383+372+404+262))
investidores_idade4 = ((262*100)/(257+383+372+404+262))
print("INVESTIDORES")
print("16 a 24 anos:", investidores_idade)
print("25 a 34 anos:", investidores_idade1)
print("35 a 44 anos:", investidores_idade2)
print("45 a 59 anos:", investidores_idade3)
print("60 anos ou mais:", investidores_idade4)
não_investidores_idade = ((163*100)/(163+421+434+464+248))
não_investidores_idade1 = ((421*100)/(163+421+434+464+248))
não_investidores_idade2 = ((434*100)/(163+421+434+464+248))
não_investidores_idade3 = ((464*100)/(163+421+434+464+248))
não_investidores_idade4 = ((248*100)/(163+421+434+464+248))
print("NÃO INVESTIDORES")
print("16 a 24 anos:", não_investidores_idade)
print("25 a 34 anos:", não_investidores_idade1)
print("35 a 44 anos:", não_investidores_idade2)
print("45 a 59 anos:", não_investidores_idade3)
print("60 anos ou mais:", não_investidores_idade4)

"""Classe por sexo"""

group3 = dfInvest2.groupby(['SEXO','CLASSE']).agg({'P9A': ['count']})
group3

homens_classe = ((130*100)/(130+357+616+425+308))
homens_classe1 = ((357*100)/(130+357+616+425+308))
homens_classe2 = ((616*100)/(130+357+616+425+308))
homens_classe3 = ((425*100)/(130+357+616+425+308))
homens_classe4 = ((308*100)/(130+357+616+425+308))
print("HOMENS")
print("Classe A:", homens_classe)
print("Classe B1:", homens_classe1)
print("Classe B2:", homens_classe2)
print("Classe C1:", homens_classe3)
print("Classe C2:", homens_classe4)
mulheres_classe = ((91*100)/(91+250+507+396+328))
mulheres_classe1 = ((250*100)/(91+250+507+396+328))
mulheres_classe2 = ((507*100)/(91+250+507+396+328))
mulheres_classe3 = ((396*100)/(91+250+507+396+328))
mulheres_classe4 = ((328*100)/(91+250+507+396+328))
print("MULHERES")
print("Classe A:", mulheres_classe)
print("Classe B1:", mulheres_classe1)
print("Classe B2:", mulheres_classe2)
print("Classe C1:", mulheres_classe3)
print("Classe C2", mulheres_classe4)

"""Total de investidores e não investidores, por sexo e classe"""

group4 = dfInvest3.groupby(['SEXO','CLASSE', 'Status_investidor']).agg({'P9A': ['count']})
group4

homens_investidores_classe = ((104*100)/(104+236+337+184+76))
homens_investidores_classe1 = ((236*100)/(104+236+337+184+76))
homens_investidores_classe2 = ((337*100)/(104+236+337+184+76))
homens_investidores_classe3 = ((184*100)/(104+236+337+184+76))
homens_investidores_classe4 = ((76*100)/(104+236+337+184+76))
print("HOMENS - Investidores")
print("Classe A:", homens_investidores_classe)
print("Classe B1:", homens_investidores_classe1)
print("Classe B2:", homens_investidores_classe2)
print("Classe C1:", homens_investidores_classe3)
print("Classe C2:", homens_investidores_classe4)
homens_nao_classe = ((26*100)/(26+121+279+241+232))
homens_nao_classe1 = ((121*100)/(26+121+279+241+232))
homens_nao_classe2 = ((279*100)/(26+121+279+241+232))
homens_nao_classe3 = ((241*100)/(26+121+279+241+232))
homens_nao_classe4 = ((232*100)/(26+121+279+241+232))
print("HOMENS - Não Investidores")
print("Classe A:", homens_nao_classe)
print("Classe B1:", homens_nao_classe1)
print("Classe B2:", homens_nao_classe2)
print("Classe C1:", homens_nao_classe3)
print("Classe C2:", homens_nao_classe4)
mulheres_investidoras_classe = ((67*100)/(67+183+301+159+83))
mulheres_investidoras_classe1 = ((183*100)/(67+183+301+159+83))
mulheres_investidoras_classe2 = ((301*100)/(67+183+301+159+83))
mulheres_investidoras_classe3 = ((159*100)/(67+183+301+159+83))
mulheres_investidoras_classe4 = ((83*100)/(67+183+301+159+83))
print("MULHERES - Investidoras")
print("Classe A:", mulheres_investidoras_classe)
print("Classe B1:", mulheres_investidoras_classe1)
print("Classe B2:", mulheres_investidoras_classe2)
print("Classe C1:", mulheres_investidoras_classe3)
print("Classe C2:", mulheres_investidoras_classe4)
mulheres_nao_investidoras = ((24*100)/(24+67+206+237+245))
mulheres_nao_investidoras1 = ((67*100)/(24+67+206+237+245))
mulheres_nao_investidoras2 = ((206*100)/(24+67+206+237+245))
mulheres_nao_investidoras3 = ((237*100)/(24+67+206+237+245))
mulheres_nao_investidoras4 = ((245*100)/(24+67+206+237+245))
print("MULHERES - Não Investidoras")
print("Classe A:", mulheres_nao_investidoras)
print("Classe B1:", mulheres_nao_investidoras1)
print("Classe B2:", mulheres_nao_investidoras2)
print("Classe C1:", mulheres_nao_investidoras3)
print("Classe C2:", mulheres_nao_investidoras4)

"""Nível escolar por investidores e não investidores"""

group5 = dfInvest3.groupby(['ESCOLA', 'Status_investidor']).agg({'P9A': ['count']})
group5

investidor_escola = ((14*100)/(14+38+39+42+385+156+634+422))
investidor_escola1 = ((38*100)/(14+38+39+42+385+156+634+422))
investidor_escola2 = ((39*100)/(14+38+39+42+385+156+634+422))
investidor_escola3 = ((42*100)/(14+38+39+42+385+156+634+422))
investidor_escola4 = ((385*100)/(14+38+39+42+385+156+634+422))
investidor_escola5 = ((156*100)/(14+38+39+42+385+156+634+422))
investidor_escola6 = ((634*100)/(14+38+39+42+385+156+634+422))
investidor_escola7 = ((422*100)/(14+38+39+42+385+156+634+422))
print("INVESTIDORES - NÍVEL ESCOLAR")
print("1 Analfabeto/ Primário/ Fundamental I incompleto:", investidor_escola)
print("2 Primário ou Fundamental I completo/ Ginasial ou Fundamental II incompleto:", investidor_escola1)
print("3 Ginasial ou Fundamental II completo:", investidor_escola2)
print("4 Colegial ou Ensino Médio incompleto:", investidor_escola3)
print("5 Colegial ou Ensino Médio completo:", investidor_escola4)
print("6 Superior incompleto: ", investidor_escola5)
print("7 Superior completo:", investidor_escola6)
print("8 Pós-graduação:", investidor_escola7)
nao_escola = ((56*100)/(56+105+82+127+622+157+376+153))
nao_escola1 = ((105*100)/(56+105+82+127+622+157+376+153))
nao_escola2 = ((82*100)/(56+105+82+127+622+157+376+153))
nao_escola3 = ((127*100)/(56+105+82+127+622+157+376+153))
nao_escola4 = ((622*100)/(56+105+82+127+622+157+376+153))
nao_escola5 = ((157*100)/(56+105+82+127+622+157+376+153))
nao_escola6 = ((376*100)/(56+105+82+127+622+157+376+153))
nao_escola7 = ((153*100)/(56+105+82+127+622+157+376+153))
print("NÃO INVESTIDORES - NÍVEL ESCOLAR")
print("1 Analfabeto/ Primário/ Fundamental I incompleto:", nao_escola)
print("2 Primário ou Fundamental I completo/ Ginasial ou Fundamental II incompleto:", nao_escola1)
print("3 Ginasial ou Fundamental II completo:", nao_escola2)
print("4 Colegial ou Ensino Médio incompleto:", nao_escola3)
print("5 Colegial ou Ensino Médio completo:", nao_escola4)
print("6 Superior incompleto: ", nao_escola5)
print("7 Superior completo:", nao_escola6)
print("8 Pós-graduação:", nao_escola7)

#Quantidade de possíveis investidores por sexo
ax = sns.barplot(x=sexo.index, y=sexo.values)
plt.xticks(rotation=90)
print(colored('SEXO DOS POSSÍVEIS INVESTIDORES', attrs=['bold']))
print("1 - Masculino")
print("2 - Feminino")

#idade dos investidores em geral
ax = sns.barplot(x=Idade1.index, y=Idade1.values)
plt.xticks(rotation=90)
print(colored('IDADE DOS POSSÍVEIS INVESTIDORES', attrs=['bold']))
print("1 - 16 a 24 anos")
print("2 - 25 a 34 anos")
print("3 - 35 a 44 anos")
print("4 - 45 a 59 anos")
print("5 - 60 anos ou mais")

#DataFrame sendo transformado em csv
dfInvest3.to_csv('Base3.csv', index=False)

"""# **Normalização/padronização dos dados**

Diferença entre normalização e padronização: https://medium.com/data-hackers/normalizar-ou-padronizar-as-vari%C3%A1veis-3b619876ccc9

**Criando matriz da colunas que iremos utilizar**
"""

#A coluna 'REGIAO' foi retirado pois no momento em que fazemos a padronização dos dados o algoritmo não consegue entender colunas que não seja em números
len(dfInvest3[['P9A', 'Status_investidor', 'RENDAF']])

vet_x2 = dfInvest3[['P9A', 'Status_investidor', 'RENDAF']]
vet_x2.head()

x_array2 = np.array(vet_x2)
print(x_array2)

"""**Normalização dos dados - MinMaxScaler**"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

scaler3D = MinMaxScaler()
x_scaled3D = scaler3D.fit_transform(x_array2)
print(x_scaled3D)
X3D = x_scaled3D
df_scaleMinMax = pd.DataFrame(x_scaled3D, columns=vet_x2.columns)
df_scaleMinMax.head()

df_scaleMinMax.head()

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Creating dataset
xMinMax = X3D[:,0]
yMinMax = X3D[:,1]
zMinMax = X3D[:,2]

X = x_scaled3D
print('Dados Padronizados com MinMaxScaler')
# what does it look like without clustering?
plt.scatter(X[:,0], X[:,1])
plt.show()

"""**Padronização dos dados - StandardScaler**"""

from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

scaler = StandardScaler()
scaler.fit(x_array2)
X_scale = scaler.transform(x_array2)
df_scaleStd = pd.DataFrame(X_scale, columns=vet_x2.columns)
# Creating dataset
xStd = X_scale[:,0]
yStd = X_scale[:,1]
uStd = X_scale[:,2]
df_scaleStd.head()

"""**PCA**"""

dfInvest4['ESTADO'].value_counts()

from sklearn.preprocessing import StandardScaler
features = ['P9A', 'Status_investidor', 'RENDAF']
# Separando os recursos
x = dfInvest4.loc[:, features].values
# Separando o destino
y = dfInvest4.loc[:,['Status_investidor']].values
# Padronizando os recursos
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, dfInvest4[['Status_investidor']]], axis = 1)

"""# **Criando clusters**

## **K-means**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.offline as pyo
pyo.init_notebook_mode()
import plotly.graph_objs as go
from plotly import tools
from plotly.subplots import make_subplots
import plotly.offline as py
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
# %matplotlib inline
from warnings import filterwarnings
filterwarnings('ignore')

"""**Método de cotovelo**

O método Elbow se trata de uma técnica interessante para encontrar o valor ideal do parâmetro k. Basicamente o que o método faz é testar a variância dos dados em relação ao número de clusters. É considerado um valor ideal de k quando o aumento no número de clusters não representa um valor significativo de ganho.

Link: https://medium.com/pizzadedados/kmeans-e-metodo-do-cotovelo-94ded9fdf3a9
"""

df_scale3 = df_scaleMinMax.copy()
sse = []
k_list = range(1, 15)
for k in k_list:
    km = KMeans(n_clusters=k)
    km.fit(df_scale3)
    sse.append([k, km.inertia_])

oca_results_scale = pd.DataFrame({'Cluster': range(1,15), 'SSE': sse})
plt.figure(figsize=(12,6))
plt.plot(pd.DataFrame(sse)[0], pd.DataFrame(sse)[1], marker='o')
plt.title('Número ideal de clusters usando o método Elbow (dados em escala)')
plt.xlabel('Número de clusters')
plt.ylabel('Inércia')

vet_x2.describe()

"""**Coeficiente de Silhueta**"""

# Com 2 clusters como melhor resultado
kmeans_scale = KMeans(n_clusters=3, n_init=100, max_iter=400, init='k-means++', random_state=42).fit(df_scale3)
dfInvest3['klusterK3D'] = kmeans_scale.labels_
print('KMeans Scaled Silhouette Score: {}'.format(silhouette_score(df_scale3, kmeans_scale.labels_, metric='euclidean')))
labels_scale = kmeans_scale.labels_
clusters_scale = pd.concat([df_scale3, pd.DataFrame({'cluster_scaled':labels_scale})], axis=1)

"""kmeans_scale.labels_"""

klusterK3D_0 = dfInvest3.loc[dfInvest3.klusterK3D == 0]
klusterK3D_0.head()

pip install sklearn

kmeans = kmeans_scale.fit(X_scale)
fig=plt.figure (figsize=(9,7))

ax1=plt.subplot(1,1,1) # (1, 1, 1) = colum, row, and position

#ax1.bar(valueDate.index, valueDate.values) #bar graph

output = plt.scatter(X_scale[:,0], X_scale[:,1], s = 100, c = dfInvest3['klusterK3D'], marker = 'o', alpha = 1 )
centers =  kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='red', s=200, alpha=1 , marker='o');
plt.title('RENDAF x Status Investidor  -Klustering K-Means')
plt.colorbar (output)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

import plotly.offline as pyo
pyo.init_notebook_mode()
import plotly.graph_objs as go

Scene = dict(xaxis = dict(title  = 'Setor'),yaxis = dict(title  = 'Faixa Valor'),zaxis = dict(title  = 'Região'))
trace = go.Scatter3d(x=xMinMax, y=yMinMax, z=zMinMax, mode='markers', marker=dict(colorscale='Greys', opacity=0.3, size = 10))
layout = go.Layout(margin=dict(l=0,r=0),scene = Scene, height = 1000,width = 1000)
data = [trace]
fig = go.Figure(data = data, layout = layout)
fig.show()

klusterK3D_0['SEXO'].value_counts()

klusterK3D_0['Status_investidor'].value_counts()

klusterK3D_0['CLASSEF'].value_counts()

klusterK3D_0['IDADE1'].value_counts()

klusterK3D_0['RENDAF'].value_counts()

klusterK3D_0['ESCOLA'].value_counts()

klusterK3D_1 = dfInvest3.loc[dfInvest3.klusterK3D == 1]
klusterK3D_1.head()

klusterK3D_1['SEXO'].value_counts()

klusterK3D_1['CLASSEF'].value_counts()

klusterK3D_1['RENDAF'].value_counts()

klusterK3D_1['Status_investidor'].value_counts()

klusterK3D_1['ESCOLA'].value_counts()

klusterK3D_1['IDADE1'].value_counts()