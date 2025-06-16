# DESIGUALDADE SOCIAL NO MERCADO DE DADOS NO BRASIL

Rafael Silvestre da Silva, rafael.silva.1548493@sga.pucminas.br

Eduardo Velloso Landeiro, eduardo.landeiro@sga.pucminas.br

---

**Professores:**

Hugo Bastos de Paula

Hayala Nepomuceno Curto

---

Curso:
_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

## Sumário

- [Resumo](#resumo)
- [Introdução](#introdução)
  - [Contextualização](#contextualização)
  - [Problema](#problema)
  - [Objetivo geral](#objetivo-geral)
  - [Objetivos específicos](#objetivos-específicos)
  - [Justificativas](#justificativas)
  - [Público alvo](#público-alvo)
- [Análise exploratória dos dados](#análise-exploratória-dos-dados)
  - [Dicionário de dados](#dicionário-de-dados)
  - [Descrição de dados](#descrição-de-dados)
  - [Pergunta 1](#pergunta-1)
  - [Pergunta 2](#pergunta-2)
  - [Pergunta 3](#pergunta-3)
  - [Pergunta 4](#pergunta-4)
- [Preparação dos dados](#preparação-dos-dados)
- [Indução de modelos](#indução-de-modelos)
  - [Modelo 1: Random Forest Classifier](#modelo-1-random-forest-classifier)
    - [Justificativa do Modelo](#justificativa-do-modelo)
    - [Explicação do código](#explicação-do-código)
  - [Modelo 2: Classificador Árvore de Decisão](#modelo-2-classificador-árvore-de-decisão)
    - [Justificativa do Modelo](#justificativa-do-modelo-1)
    - [Explicação do código](#explicação-do-código-1)
- [Resultados](#resultados)
  - [Resultados do modelo 1](#resultados-obtidos-com-o-modelo-1)
  - [Interpretação do modelo 1](#interpretação-do-modelo-1)
  - [Resultados do modelo 2](#resultados-obtidos-com-o-modelo-2)
  - [Interpretação do modelo 2](#interpretação-do-modelo-2)
- [Análise comparativa dos modelos](#análise-comparativa-dos-modelos)
- [Conclusão](#8-conclusão)
- [Referências](#referências)
- [Apêndices](#apêndices)


---

## Resumo 

Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução

A elaboração desse trabalho busca usar conhecimentos de ciência de dados para resolver problemas de relevância social. Desse modo, aplicamos técnicas de aprendizado de máquina para construir dois modelos de agente inteligente, que identifica padrões em diferentes bases de dados, servindo de apoio à tomada de decisão de um problema social.

Nesse contexto, utilizamos a base de dados "State of Data Brasil 2023", que analisa o mercado de trabalho e o perfil do profissional na área de dados. Ao analisar essa base, observamos problemas sociais, bem como a desigualdade social no mercado, prova da discrepância salarial entre grupos étnicos. Além disso, nos apoiamos em uma base de dados auxliar, a "IBGE Estatísticas Brasil", de modo a enriquecer nossos dados. Tal base foi encontrada no Kaggle, e ela diz respeito a indicadores sociais e geográficos de cada Estado do país.


###    Contextualização

A desigualdade social no mercado de trabalho da área de Ciência de Dados no Brasil é um reflexo das profundas disparidades históricas que marcam a sociedade brasileira, especialmente no que diz respeito ao acesso às oportunidades profissionais. Apesar do crescimento expressivo do setor de tecnologia e da alta demanda por cientistas de dados, nem todos os grupos sociais têm acesso equitativo às formações, certificações e experiências que possibilitam a ascensão profissional nesse campo. Fatores como raça, gênero, origem socioeconômica e localização geográfica ainda influenciam significativamente as chances de alguém prosperar na área.

Nesse contexto, nosso trabalho propõem o uso da metodologia de ciência de dados, com a definição de um problema, análise exploratória e treinamento de modelos de Machine Learning, de modo a discutir as desigualdades sociais presentes no mercado de dados. Assim, a partir dos resultados das análises e dos modelos, buscamos evidenciar padrões de disparidade salarial com base em características sociais dos profissionais, como gênero, raça, escolaridade e experiência.

Nessa perspectiva, fizemos o projeto a partir da base de dados "State of Data Brasil 2023", uma pesquisa anual que mapeia o mercado de dados e inteligência artificial no Brasil. Além dessa, utilizamos a base de dados auxiliar "IBGE Estatísticas Brasil", de modo a enriquecer a base de dados principais, a partir do atributo de IDH (Índice de desenvolvimento humano) de cada estado do país. 



###    Problema

O problema a ser analisado é a desigualdade social na área de dados. Nesse contexto grupos minoritários não recebem as mesmas oportunidades no mercado de trabalho, surgindo assim uma discrepância salarial entre grupos étnicos. Dessa forma, elaboramos dois modelos de Machine Learning, que foram induzidos a partir de uma pergunta: “Como associar a desigualdade no mercado de trabalho com a discrepância salarial na área de dados”.

Feito tal pergunta, nosso grupo se apoiou na base de dados State of Data Brasil 2023 e na base de dados do IBGE para tentar respondê-la. Logo, nossos modelos se baseiam em atributos dessas bases, gerando resultados a partir de técnicas de análise de dados e aprendizado de máquina. 

###    Objetivo geral

O objetivo geral do trabalho é identificar desigualdades sociais na área de dados. Nessa perspectiva, nos orientamos a partir da pergunta "Como as desigualdades sociais afetam os salários dos profissionais no mercado de trabalho de dados?". Dessa forma, para responder tal pergunta, baseamos nos atributos: gênero, cor/raça/etnia, PCD, nível de ensino, área de formação, nível, tempo de experiência na área de dados, faixa salarial e IDH.

####    Objetivos específicos

- Como a faixa salarial média varia entre profissionais de diferentes gêneros em cada região do Brasil?
- Existe disparidade salarial entre profissionais com o mesmo nível e tempo de experiência, considerando gênero e raça?
- Qual é a relação entre nível de escolaridade e faixa salarial em diferentes regiões do Brasil?
- Existe correlação entre o IDH do estado e o salário médio dos profissionais de dados que residem nesses estados?



###    Justificativas

Visto que o mercado de trabalho da área de dados apresenta desigualdades sociais relevantes, optamos por criar um modelo que busca analisar essas desigualdades, evidenciando-as. Tal abordagem foi escolhida por conta da relevância social, conversando com as ODSs 9 (indústria, inovação e infraestrutura) e 10 (redução das desigualdades), servindo de incentivo para o nosso trabalho.



###    Público alvo

O público-alvo da aplicação será o governo, especialmente os órgãos responsáveis pela formulação de políticas educacionais e sociais. Os usuários terão, em sua maioria, conhecimento técnico sobre o setor, mas com diferentes níveis de familiaridade com ferramentas tecnológicas. Eles buscam soluções que ajudem a embasar decisões para combater as desigualdades, geralmente ocupando cargos intermediários ou superiores na hierarquia pública.

---

## Análise exploratória dos dados

###    Dicionário de dados

_**Base de dados: State of Data Brasil 2023**_

| Código          | Descrição                                              | Tipo                      |
|----------------|------------------------------------------------------|---------------------------|
| **P1_a** | Idade                                   | Numérico                   |
| **P1_b** | Gênero                    | Categórico Binominal      |
| **P1_c** | Cor/Raça/Etnia                 | Categórico Multivalorado  |
| **P1_d** | PCD - Pessoa com deficiência (Sim/Não)                        | Categórico Binominal        |
| **P1_i** | Estado onde mora | Categórico Multivalorado |
| **P1_l** | Nível de ensino                                           | Categórico Multivalorado  |
| **P2_g** | Nível na empresa | Categórico Multivalorado |
| **P2_h** | Faixa salarial                                           | Numérico Discreto              |
|**P2_i** | Tempo de experiência na área de dados | Numérico Discreto |


###    Descrição de dados

_**Base de dados: State of Data Brasil 2023**_

**Idade:**

![image](https://github.com/user-attachments/assets/f2dfe131-361e-4d6f-9225-b28b5f58040c)


**Gênero:**

![image](https://github.com/user-attachments/assets/da089828-b5e7-46ff-8acf-a91b65334279)


**Cor/Raça/Etnia:**

![image](https://github.com/user-attachments/assets/341adab7-7162-43e9-9bd2-f842350462f0)


**PCD:**

![image](https://github.com/user-attachments/assets/8a050aee-02c4-4b94-8b86-a3a06f940ae1)


**Estado onde mora:**

![image](https://github.com/user-attachments/assets/b6398acd-9dd8-4663-ab9c-3fbda25ddeaa)



**Nível de ensino:**

![image](https://github.com/user-attachments/assets/3e0529bf-526d-4014-9641-38edf069642f)


**Nível na empresa:**

![image](https://github.com/user-attachments/assets/edc6e967-9f53-4ef7-8161-713c03c8afae)


**Faixa Salarial:**

![image](https://github.com/user-attachments/assets/f566c827-1f11-4b7d-9930-59af63429472)


**Tempo de experiência:**

![image](https://github.com/user-attachments/assets/4ad4b9e2-65db-4600-b695-4588c253e8d5)



### Pergunta 1

_**Como a faixa salarial média varia entre profissionais de diferentes gêneros em cada região do Brasil?**_

_**Base de dados: State of Data Brasil 2023**_


| Código          | Descrição                                              | Tipo                      |
|----------------|------------------------------------------------------|---------------------------|
| **P1_b** | Gênero                    | Categórico Binominal      |
| **P1_i** | Estado onde mora | Categórico Multivalorado |
| **P2_h** | Faixa salarial                                           | Numérico Discreto              |

**Salário Médio por Gênero em cada região do Brasil**

![image](https://github.com/user-attachments/assets/1b7c5711-ade2-4fa7-b767-be6335694478)


### Pergunta 2

_**Existe disparidade salarial entre profissionais com o mesmo nível e tempo de experiência, considerando gênero e raça?**_

_**Base de dados: State of Data Brasil 2023**_


| Código          | Descrição                                              | Tipo                      |
|----------------|------------------------------------------------------|---------------------------|
| **P1_b** | Gênero                    | Categórico Binominal      |
| **P1_c** | Cor/Raça/Etnia                 | Categórico Multivalorado  |
| **P2_g** | Nível na empresa | Categórico Multivalorado |
| **P2_h** | Faixa salarial                                           | Numérico Discreto              |
|**P2_i** | Tempo de experiência na área de dados | Numérico Discreto |

**Boxplots de Salário por Gênero e Nível**

![image](https://github.com/user-attachments/assets/8de0a19c-11f1-4daf-a1eb-d043a215c296)

**Salário Médio Por Nível De Cargo Gênero**

![image](https://github.com/user-attachments/assets/b091da52-4ff3-4fca-90ba-86c05058632c)

**Salário Médio Por Nível De Cargo E Raça/Cor/Etnia**

![image](https://github.com/user-attachments/assets/0d52d33f-c36d-497f-ae91-210780812c1f)

**Mapa De Calor: Salário Médio Por Raça × Gênero × Nível**

![image](https://github.com/user-attachments/assets/3bc4054d-1a73-4940-b8f9-ccdcaf10211e)



### Pergunta 3

_**Qual é a relação entre nível de escolaridade e faixa salarial em diferentes regiões do Brasil?**_

_**Base de dados: State of Data Brasil 2023**_

| Código          | Descrição                                              | Tipo                      |
|----------------|------------------------------------------------------|---------------------------|
| **P1_i** | Estado onde mora | Categórico Multivalorado |
| **P1_l** | Nível de ensino                                           | Categórico Multivalorado  |
| **P2_h** | Faixa salarial                                           | Numérico Discreto              |

**Heatmap: Região Sudeste**

![image](https://github.com/user-attachments/assets/1f1b926a-43a2-47c1-8c03-19cff44a471d)

**Gráfico de barras: Região Sudeste**

![image](https://github.com/user-attachments/assets/b7c5989c-f3ad-4d98-9d67-407e0ad607b2)

**Heatmap: Região Sul**

![image](https://github.com/user-attachments/assets/e4d38574-dcd9-4f46-b596-91358cde71f2)

**Gráfico de barras: Região Sul**

![image](https://github.com/user-attachments/assets/c70fb0db-c327-4a20-acca-e8ae77710e63)

**Heatmap: Região Centro-Oeste**

![image](https://github.com/user-attachments/assets/5c2818e2-8fae-46d8-a240-37107b6beead)

**Gráfico de barras: Região Centro-Oeste**

![image](https://github.com/user-attachments/assets/44690de3-5460-47f9-93a9-e4d9e5fc84a3)

**Heatmap: Região Nordeste**

![image](https://github.com/user-attachments/assets/2dedabc8-7d77-49f6-b67f-53e49aef4b4e)

**Gráfico de barras: Região Nordeste**

![image](https://github.com/user-attachments/assets/ebcfaf5a-d157-461e-ba8f-6b71c222d4c0)

**Heatmap: Região Norte**

![image](https://github.com/user-attachments/assets/640254c6-7544-4eb5-9482-2c9d6fc23229)


**Gráfico de barras: Região Norte**

![image](https://github.com/user-attachments/assets/3a7aa66c-90be-494e-8bd6-1e561823d5b2)

### Pergunta 4

_**Existe relação entre o IDH do estado e o salário médio dos profissionais de dados que residem nesses estados?**_

_**Base de dados principal Tratada**_

| Código          | Descrição                                              | Tipo                      |
|----------------|------------------------------------------------------|---------------------------|
| **P1_i** | Estado onde mora | Categórico Multivalorado |
| Salário (R$) | Salário do respondente | Numérico |
| IDH do estado | Índice de desenvolvimento humano do estado onde mora o respondente | Numérico |

**Gráfico de dispersão: IDH x Salário Médio**

![image](https://github.com/user-attachments/assets/77a7db08-76c1-4be3-9d45-3a90e24a5372)

---

## Preparação dos dados

### Base de dados original 

### Seleção dos atributos

Criação de outra planilha no Excel, contendo os atributos principais:

### Limpeza e transformação de dados: 

- Tratamento dos valores nulos: -1512 linhas 
- Tratamento dos outliers: -142 linhas 
- Conversão dos dados da coluna “Faixa salarial” para números contínuos 
- Conversão dos dados da coluna “Tempo de experiência” para números contínuos

### Base de dados tratada

--- 

## Indução de modelos

### Modelo 1: Random Forest Classifier 

#### Justificativa do Modelo 

Foi usado o modelo Random Forest Classifier com o objetivo de prever o salário dos respondentes em alto ou baixo. Desse modo, o modelo se baseia em outros atributos da base de dados como idade, raça, gênero, nível de escolaridade e tempo de experiência na área, para prever o salário do trabalhador. Assim, o modelo reflete o que acontece na realidade, na qual fatores sociais influenciam no salário. 

Dessa forma, o Random Forest foi escolhido por ser um modelo mais robusto, com o objetivo de alcançar uma acurácia melhor. Além disso, é um modelo que não exigiu muitas mudanças e transformações na base de dados o que facilita sua aplicação e interpretação. Assim, mais do que apenas prever salários, o modelo ajuda a revelar padrões sociais importantes que podem servir de base para reflexões e ações voltadas à equidade.

#### Explicação do código 

A construção e o treinamento do modelo foram feitos utilizando a linguagem de programação Python, uma das mais usadas na área de ciência de dados. Nosso código faz uso das bibliotecas pandas, scikit-learn e matplotlib, que facilitam desde o tratamento e análise dos dados até a construção, avaliação e visualização de modelos preditivos.

O nosso código começa com a importação das referidas bibliotecas, a leitura da nossa base de dados e ajustes em alguns atributos:

![image](https://github.com/user-attachments/assets/85336cdd-7550-4ef6-985d-faac4a95e9ee)

O passo 4 codifica as variáveis categóricas em numéricas, pois o random forest não consegue trabalhar diretamente com texto. Desse modo, o código: 

- seleciona automaticamente todas as colunas que têm dados em formato de texto a partir do comando `df.select_dtypes(include='object')`
- Para cada uma dessas colunas, cria-se um `LabelEncoder()`, que transforma cada categoria (string) em um número.
	- Por exemplo, na coluna genero, "Masculino" pode virar 1 e "Feminino" virar 0.
- Substitui os valores originais das colunas por seus respectivos códigos numéricos.
- Salva cada encoder em um dicionário `label_encoders`, o que permite reverter os códigos para texto no futuro, se necessário.

![image](https://github.com/user-attachments/assets/ac91f7b3-1cf2-43a3-b4e5-fb1a2c79f933)

No passo 5, foi definido o target, a coluna "Salario" (atributo que o modelo vai tentar prever).

![image](https://github.com/user-attachments/assets/d4dc9662-e4ed-4d27-b7a3-842693230650)

No passo 6, a base de dados foi dividida em treinamento (90%) e teste (10%). Tal divisão foi feita com o objetivo de fornecer uma grande quantidade de dados para o treinamento do modelo, de modo que ele aprenda melhor e sua precisão seja maior.

![image](https://github.com/user-attachments/assets/0528bc56-5d52-4a09-8899-ac496715ae97)

No passo 7 é onde de fato o modelo de Machine Learning é treinado, ou seja, ele aprende padrões nos dados de treino para conseguir prever o salário ("Alto" ou "Baixo") com base nos atributos sociais e profissionais dos trabalhadores. Os parâmetros utilizados foram:

- `n_estimators=100` → Cria 100 árvores de decisão. Quanto mais árvores, mais estável e robusto tende a ser o modelo (até certo ponto).
- `max_depth=10` → Limita a profundidade máxima de cada árvore. Isso evita que o modelo fique muito complexo e superajuste (overfitting) os dados.
- `min_samples_split=10` → Uma divisão interna da árvore (um nó) só será feita se houver pelo menos 10 amostras. Isso também ajuda a reduzir o overfitting.
- `random_state=42` → Garante que o resultado seja reprodutível: as mesmas árvores serão criadas sempre que o código for executado.

![image](https://github.com/user-attachments/assets/7818ba6a-80c2-4fce-b0a6-99095d41fcb9)

Essa parte do código realiza a etapa final de um modelo de Machine Learning supervisionado: prever, avaliar e interpretar os resultados. 

 ---

### Modelo 2: Classificador Árvore de Decisão
### Justificativa do Modelo
Foi utilizado o modelo Decision Tree Classifier com o objetivo de prever se o salário dos entrevistados é classificado como "Alto" ou "Baixo". O modelo utiliza como base atributos da base de dados como idade, gênero, raça, nível de escolaridade, tempo de experiência na área e outros fatores sociais para fazer essa previsão.

A escolha pela Árvore de Decisão se dá principalmente por sua simplicidade e interpretabilidade. Este modelo oferece uma estrutura de decisão em que cada divisão da árvore representa um critério claro e compreensível, o que facilita não apenas a previsão, mas também a análise dos padrões sociais e profissionais que influenciam o salário.
Além disso, a Árvore de Decisão funciona bem mesmo em bases de dados com variáveis categóricas e não requer transformações muito complexas, tornando o processo de construção mais direto.

### Explicação do código
A construção e o treinamento do modelo foram feitos em Python, utilizando as bibliotecas pandas, scikit-learn, matplotlib e seaborn, muito comuns em ciência de dados. Essas bibliotecas ajudam desde o tratamento dos dados até a construção, visualização e avaliação do modelo.

### Passo 1: Importação das bibliotecas e leitura da base de dados
Primeiramente, foram importadas as bibliotecas e lida a base de dados "Base de dados principal TRATADA ATUALIZADA.xlsx". Algumas colunas foram renomeadas para facilitar o trabalho com o DataFrame.

### Passo 2: Codificação das variáveis categóricas
Assim como no modelo de Random Forest, as variáveis categóricas foram transformadas em variáveis numéricas utilizando a técnica de Label Encoding:

- O código seleciona automaticamente todas as colunas com dados do tipo "object" (texto);

- Um LabelEncoder é criado para cada coluna categórica, convertendo categorias como "Masculino" e "Feminino" em valores numéricos (exemplo: 1 e 0);

- Esses codificadores foram armazenados em um dicionário `label_encoders`, permitindo reverter os códigos para texto se necessário.

### Passo 3: Definição da variável alvo
A coluna "Salário" foi definida como variável alvo (target), com o objetivo de prever sua classificação ("Alto" ou "Baixo").

### Passo 4: Divisão dos dados em treino e teste
A base foi dividida em dois conjuntos:

- Treinamento: 90% dos dados, para o modelo aprender os padrões;

- Teste: 10% dos dados, para avaliar o desempenho do modelo em dados novos.

### Passo 5: Treinamento do modelo
Foi utilizado um DecisionTreeClassifier com as seguintes configurações:

- `max_depth=5` → Limita a profundidade da árvore a 5 níveis. Isso evita que o modelo fique muito complexo e reduza o risco de overfitting (quando o modelo "decorar" os dados de treinamento);

- `min_samples_split=10` → Um nó só será dividido se houver pelo menos 10 amostras, também uma técnica para evitar overfitting;

- `random_state=42` → Garante que o resultado seja reprodutível.

### Passo 6: Avaliação do modelo
Após o treinamento, o modelo foi avaliado com os dados de teste:

- Foi calculada a acurácia do modelo;

- Foi gerada a matriz de confusão para entender melhor como o modelo acerta ou erra as previsões;

- Foi gerada uma curva ROC para visualizar a performance do classificador.

Além disso, o modelo foi visualizado com a função plot_tree, permitindo ver claramente como as decisões são tomadas — uma das grandes vantagens das Árvores de Decisão.

---

## Resultados

### Resultados obtidos com o modelo 1:

**Acurácia no treino**: 82.41%

**Acurácia no teste**: 78.02%

- Acurácia é uma métrica de avaliação que indica quantas previsões o modelo acertou em relação ao total de casos.
- A diferença entre treino e teste é pequena (aproximadamente 4,4 pontos percentuais), o que é um bom sinal. Isso mostra que o modelo não está memorizando os dados (overfitting), nem está com desempenho muito baixo (underfitting).
- Ele conseguiu capturar relações relevantes entre os atributos sociais/profissionais e o salário. Isso significa que, sim, características sociais ajudam a prever se o salário será mais alto ou mais baixo.

![image](https://github.com/user-attachments/assets/e2ac28f2-ca71-4da8-9e2d-7449544716c8)


- **Classe Alto:**
	- Precision (0.71): Quando o modelo prevê que o salário é "Alto", ele acerta 71% das vezes.
	- Recall (0.73): De todos os trabalhadores com salário "Alto", o modelo identifica corretamente 73%.
	- F1-score (0.72): Média harmônica entre precision e recall, indica um equilíbrio moderado para esta classe.
- **Classe Baixo:**
	- Precision (0.83): Quando o modelo prevê "Baixo", ele acerta 83% das vezes.
	- Recall (0.81): De todos os trabalhadores com salário "Baixo", o modelo acerta 81%.
	- F1-score (0.82): Desempenho forte nessa classe, indicando que o modelo está mais confiável para salários baixos.

![image](https://github.com/user-attachments/assets/323d5482-f476-492f-bed9-4fe357d33371)

- Verdadeiro Positivo (VP) = 103 → O modelo previu "Alto" e era realmente "Alto"

- Verdadeiro Negativo (VN) = 181 → O modelo previu "Baixo" e era realmente "Baixo"

- Falso Positivo (FP) = 42 → O modelo previu "Alto", mas era "Baixo"

- Falso Negativo (FN) = 38 → O modelo previu "Baixo", mas era "Alto"

---

### Interpretação do modelo 1

---

#### Overfitting 

Após realizar os primeiros testes no modelo Random Forest, foi detectado um overfitting (discrepância da acurácia de treinamento comparada à acurácia de teste). No caso do nosso modelo, o resultado foi o seguinte:

**Acurácia (Treino):** 0.95

**Acurácia (Teste):** 0.75

Dessa maneira, o modelo aprendeu os dados de treinamento demais, a ponto de não conseguir generalizar bem para os dados de teste. Assim, tais medidas foram tomadas: 

- Diminuir a base de teste de **30%** para **10%**: assim, o modelo tem mais dados para aprender
- Implementar o parâmetro `max_depth`, que limita a profundidade de cada árvore 
- Implementar o parâmetro `min_samples_split`, na qual uma divisão interna da árvore (um nó) só será feita se houver pelo menos 10 amostras.

Logo, o overfitting foi corrigido:

**Acurácia do treino:** 0.82

**Acurácia do teste:** 0.78

---

#### Remoção da coluna "nivel"

A variável "nível" (Júnior, Pleno, Sênior) tem forte correlação direta com o salário — o que torna sua presença no modelo quase uma "resposta pronta". Ou seja, prever salário com base no nível do cargo é óbvio e pouco revelador para entender os mecanismos mais sutis da desigualdade.

- Remoção da coluna no código: `df = df.drop("nivel", axis = 1)`

Quando essa variável foi removida e a acurácia caiu apenas 5%, o modelo continuou acertando bem mesmo sem essa "pista óbvia". Assim, o modelo ainda conseguiu prever salários com boa precisão com base apenas em fatores sociodemográficos, ou seja, características que não deveriam influenciar diretamente o salário em um mercado idealmente meritocrático. Isso sugere que as outras variáveis estão, na prática, associadas ao nível salarial — o que é um indício de discriminação sistêmica e desigualdade de oportunidades.

---

#### Interpretação do resultado 

A partir do classification report, é possível concluir que o modelo acerta mais ao prever o salário baixo. Tal funcionalidade indica que esses profissionais compartilham características comuns que os mantêm em posições menos valorizadas economicamente, o que pode refletir desigualdades históricas e estruturais no acesso a oportunidades e progressão na carreira.

Por outro lado, a menor precisão nas previsões de salários altos pode revelar que a ascensão a rendas mais elevadas depende de múltiplos fatores menos previsíveis ou mais diversos, como networking, experiências informais ou oportunidades específicas de carreira — elementos que talvez não estejam completamente representados nos dados coletados.

Essa assimetria na performance do modelo fortalece a hipótese de que a desigualdade no mercado de trabalho de ciência de dados no Brasil não é apenas uma questão de mérito, mas está fortemente ligada a fatores sociais estruturantes. Assim, o modelo não apenas prevê salários, mas também ajuda a revelar os mecanismos sociais que mantêm a desigualdade.

---

### Resultados obtidos com o modelo 2.

Acurácia no treino: 85,30%

Acurácia no teste: 80,15%

Assim como no primeiro modelo, a acurácia é uma métrica de avaliação que mostra a proporção de previsões corretas feitas pelo modelo em relação ao total de casos.

Neste caso, a diferença entre treino e teste é pequena (cerca de 5,1 pontos percentuais), o que novamente indica que o modelo não está sofrendo de overfitting severo, nem de underfitting.
O modelo conseguiu capturar relações significativas entre variáveis sociais/profissionais e a variável de interesse (salário alto ou baixo).

Métricas de Classificação - Relatório detalhado:

### Classe Baixo:

- Precisão: 0,74 → Quando o modelo prevê "Baixo", ele acerta 74% das vezes.

- Recall: 0,77 → De todos os salários que são realmente "Baixo", o modelo acerta 77%.

- F1 Score: 0,75 → Boa harmonia entre precisão e recall, desempenho equilibrado.

 ### Classe Alto:

- Precisão: 0,84 → Quando o modelo prevê "Alto", ele acerta 84% das vezes.

- Recall: 0,82 → De todos os salários que são realmente "Alto", o modelo acerta 82%.

- F1 Score: 0,83 → Excelente desempenho nesta classe.

### Matriz de confusão:

- Verdadeiro Positivo (VP) = 106 → Predito "Alto", realmente "Alto"

- Verdadeiro Negativo (VN) = 185 → Predito "Baixo", realmente "Baixo"

- Falso Positivo (FP) = 40 → Predito "Alto", mas era "Baixo"

- Falso Negativo (FN) = 35 → Predito "Baixo", mas era "Alto"

---

### Interpretação do modelo 2

### Sobreajuste:
O modelo 2 também foi treinado com estratégias para evitar o overfitting. Foram usados:

- Parâmetro `max_depth`, limitando a profundidade da árvore.

- Parâmetro `min_samples_split`, limitando o número mínimo de amostras necessárias para que um nó seja dividido.

Esses ajustes ajudaram a manter o modelo generalizável, com desempenho bastante próximo entre treino (85%) e teste (80%).
Este é um indicativo de que o modelo não está apenas memorizando os dados, mas conseguindo aprender padrões consistentes.

### Remoção da variável "nível_carreira":
Assim como no primeiro modelo, foi avaliada a variável "nível_carreira", que tem relação direta com o salário (junior/pleno/sênior).
A sua inclusão ou exclusão impacta fortemente o modelo. Ao testar sem essa variável, o modelo perdeu um pouco de acurácia (~5%), mas ainda se manteve funcional.
Isso reforça a ideia de que fatores sociais e demográficos isoladamente conseguem explicar uma parcela importante da desigualdade salarial, mesmo sem pistas óbvias como o nível da carreira.

### Interpretação final:
- O modelo 2 mostra ótima capacidade de prever salários altos (precisão 84%, recall 82%).

- Para salários baixos, o desempenho também é bom e equilibrado.

- A árvore de decisão nos permite visualizar regras claras e interpretáveis — um ponto positivo deste tipo de modelo, pois podemos identificar quais variáveis sociais estão mais associadas a salários baixos ou altos.

- Assim como no primeiro modelo, a desigualdade identificada não é puramente meritocrática: variáveis como gênero, etnia, escolaridade e experiência acabam sendo preditoras relevantes, o que sugere mecanismos sociais estruturantes de desigualdade no mercado de trabalho da área de dados no Brasil.

---


## Análise comparativa dos modelos

### Desempenho dos modelos

| Métrica                     | Random Forest | Árvore de Decisão |
|----------------------------|----------------|--------------------|
| Acurácia no teste          | 78,02%         | **80,15%**         |
| F1-score (Classe Alto)     | 0,72           | **0,83**           |
| F1-score (Classe Baixo)    | **0,82**       | 0,75               |

Embora o Random Forest tenha apresentado melhor desempenho para a classe Baixo, a Árvore de Decisão superou nas métricas da classe Alto e na acurácia geral.

---

### Forças e fragilidades

**Random Forest**

- Forças:
  - Alta capacidade preditiva em bases complexas e com ruído.
  - Menor propensão a overfitting que uma única árvore.
  - Melhor desempenho para classe "Baixo", indicando robustez para identificar padrões em populações mais homogêneas (socialmente desfavorecidas).
- Fragilidades:
  - Menos interpretável: não permite ver regras claras, o que dificulta análise explicativa.

**Árvore de decisão**

- Forças:
  - Alta interpretabilidade: é possível visualizar regras explícitas de decisão (ex.: “se experiência > 5 anos e nível_ensino = superior, então salário = alto”).
  - Bom desempenho para prever salários altos, possivelmente por capturar melhor interações pontuais entre variáveis.
  - Ideal em contextos com necessidade de transparência para justificar decisões (por exemplo, políticas públicas ou empresas com critérios éticos de remuneração).
- Fragilidades:
  - Tende a overfitting se não for bem podada (aqui foi limitada por max_depth=5).
  - Menor generalização quando há muito ruído nos dados.

---

### Aplicação de cada modelo

| Cenário                                                              | Modelo Ideal        | Justificativa                                                                                   |
|----------------------------------------------------------------------|---------------------|--------------------------------------------------------------------------------------------------|
| Diagnóstico social e formulação de políticas públicas                | **Árvore de Decisão** | Permite visualizar como variáveis como gênero e etnia influenciam a remuneração                 |
| Explicação individual de decisões para RH ou auditoria salarial      | **Árvore de Decisão** | Clareza nas decisões é fundamental                                                              |
| Otimização contínua de predição em cenários complexos e atualizados | **Random Forest**     | Melhor escalabilidade e mais robusto, tolera bem ruído e dados incopletos                             |


---

### Interpretação

A árvore de decisão combina atributos para prever o salário, detectando desigualdades. Por exemplo, combinando nível de escolaridade com região (Pessoas com pós-graduação ganham mais em média, mas só quando moram na região Sudeste, onde há mais oportunidades de trabalho bem remunerado). As desigualdades não se manifestam isoladamente (apenas por gênero ou apenas por escolaridade), mas em intersecções entre características sociais. E a árvore de decisão, por sua estrutura hierárquica, consegue representar essas intersecções de forma muito clara.

Já modelos como o Random Forest, por agregarem várias árvores e usarem média dos resultados, tendem a suavizar essas combinações, o que pode reduzir o desempenho em identificar essas situações mais específicas — como os casos em que a escolaridade só leva a salários altos em certos contextos regionais ou raciais.

Além disso, a base de dados usada era simples, com poucos atributos e poucos registros. Sendo assim, o benefício da robustez da Random Forest foi limitado, e como a Árvore de decisão trabalha bem com dados mais simples, ela apresentou um melhor resultado.


---

## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria


# REFERÊNCIAS

Como um projeto de sistema inteligente não requer revisão bibliográfica, 
a inclusão das referências não é obrigatória. No entanto, caso você 
tenha utilizado referências na introdução ou deseje 
incluir referências relacionadas às tecnologias, padrões, ou metodologias 
que serão usadas no seu trabalho, relacione-as de acordo com a ABNT.

Verifique no link abaixo como devem ser as referências no padrão ABNT:

http://www.pucminas.br/imagedb/documento/DOC\_DSC\_NOME\_ARQUI20160217102425.pdf

Por exemplo:

**[1]** - _ELMASRI, Ramez; NAVATHE, Sham. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, c2019. E-book. ISBN 9788543025001._

**[2]** - _COPPIN, Ben. **Inteligência artificial**. Rio de Janeiro, RJ: LTC, c2010. E-book. ISBN 978-85-216-2936-8._

**[3]** - _CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. Rio de Janeiro, RJ: Elsevier, Campus, c2012. xvi, 926 p. ISBN 9788535236996._

**[4]** - _SUTHERLAND, Jeffrey Victor. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. 2. ed. rev. São Paulo, SP: Leya, 2016. 236, [4] p. ISBN 9788544104514._

**[5]** - _RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**. Rio de Janeiro: Elsevier, c2013. xxi, 988 p. ISBN 9788535237016._



# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).




