# DESIGUALDADE NA EDUCAÇÃO E DISCREPÂNCIA SALARIAL ENTRE GRUPO ÉTNICOS NO MERCADO DE DADOS NO BRASIL

Luis Filipe Melo Lisboa, lfmlisboa@sga.pucminas.br

Rafael Silvestre da Silva, rafael.silva.1548493@sga.pucminas.br

Eduardo Velloso Landeiro, eduardo.landeiro@sga.pucminas.br

Matheus Tamietti, matheus.tamietti@sga.pucminas.br

Iosef Juan Gonçalves Chebile Candido, ijgccandido@sga.pucminas.br

---

Professores:
Hugo Bastos de Paula

---

Curso:
_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---


## Introdução

A elaboração desse trabalho busca usar conhecimentos de ciência de dados para resolver problemas de relevância social. Desse modo, aplicamos técnicas de aprendizado de máquina para construir um modelo de agente inteligente, que identifica padrões em diferentes bases de dados, servindo de apoio à tomada de decisão de um problema social.

Nesse contexto, utilizamos a base de dados State of Data Brasil 2023, que analisa o mercado de trabalho e o perfil do profissional na área de dados. Ao analisar essa base, observamos problemas sociais, bem como a desigualdade social no mercado, prova da discrepância salarial entre grupos étnicos. Assim, buscamos associar esse problema com outra área social relevante, a educação, buscando dados sobre essa em uma base de dados auxiliar, o Censo da Educação Superior 2023.

###    Contextualização

A desigualdade na educação e a discrepância salarial entre grupos étnicos no mercado de dados no Brasil refletem um problema estrutural histórico do país. O acesso desigual à educação de qualidade e as barreiras socioeconômicas enfrentadas por determinados grupos impactam diretamente a inserção e a progressão na carreira dentro desse setor, que é um dos mais promissores e bem remunerados da economia digital. Assim, nosso modelo associa a desigualdade no mercado de trabalho com a desigualdade na educação, relacionando-as a partir da análise da dados e técnicas de aprendizado de máquina.

Dessa maneira, as técnicas e análises do nosso modelo foram feitas usando como referência a base de dados State of Data Brasil 2023, relacionando-a ainda com o Censo da Educação Superior 2023. Assim, os atributos dessas bases geraram insights valiosos para abordarmos o problema da desigualdade na educação e no mercado de dados. 

###    Problema

O problema a ser analisado é a desigualdade social na área de dados. Nesse contexto grupos minoritários não recebem as mesmas oportunidades de educação e qualificação para o mercado de dados, surgindo assim uma discrepância salarial entre grupos étnicos. Dessa forma, faz-se necessário a pergunta “Como associar a desigualdade no mercado de trabalho com a desigualdade na educação na área de dados”.

Feito tal pergunta, nosso grupo se apoiou nas bases de dados State of Data Brasil 2023 e Censo da Educação Superior 2023 para tentar respondê-la. Logo, nosso modelo se baseia em atributos dessas bases, gerando resultados a partir de técnicas de análise de dados e aprendizado de máquina. 

###    Objetivo geral

O objetivo geral do trabalho é identificar relações entre a desigualdade étnica no mercado de trabalho e a desigualdade no acesso à educação na área de dados. Dessa forma, para atingir tal objetivo, baseamos nos atributos: gênero, cor/raça/etnia, PCD, experiência profissional prejudicada, atividades profissionais, remuneração/salário, área de formação.

####    Objetivos específicos

- Relacionar dados de bases diferentes
- Elaborar modelos que encontrem padrões nas bases de dados.


###    Justificativas

Visto que o mercado de trabalho da área de dados apresenta desigualdades sociais relevantes, optamos por criar um modelo que busca relação dessas desigualdades com a educação no Brasil. Tal abordagem foi escolhida por conta da relevância social da área da educação junto à área de dados, que conversam com as ODSs 4 (educação de qualidade), 9 (indústria, inovação e infraestrutura) e 10 (redução das desigualdades), servindo de incentivo para o nosso trabalho.



##    Público alvo

Descreva quem serão as pessoas que usarão a sua aplicação indicando os diferentes perfis. 
O objetivo aqui não é definir quem serão os clientes ou quais serão os papéis dos usuários 
na aplicação. A ideia é, dentro do possível, conhecer um pouco mais sobre o perfil dos 
usuários: conhecimentos prévios, relação com a tecnologia, relações
hierárquicas, etc.

Adicione informações sobre o público-alvo por meio de uma descrição textual, 
diagramas de personas e mapa de stakeholders.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)


## Análise exploratórida dos dados

###    Dicionário de dados

**Base de dados: State of Data Brasil 2023**

| Código          | Descrição                                              | Tipo                      |
|----------------|------------------------------------------------------|---------------------------|
| **P1_a (Idade)** | Idade do respondente                                  | Inteiro                   |
| **P1_b (Gênero)** | Identidade de gênero do respondente                   | Categórico Multivalorado      |
| **P1_c (Cor/Raça/Etnia)** | Auto declaração de raça/etnia                 | Categórico Multivalorado  |
| **P1_d (PCD)** | Pessoa com deficiência (Sim/Não)                        | Categórico Binário        |
| **P1_l** | Nível de ensino                                           | Categórico Multivalorado  |
| **P2_a** | Situação de trabalho                                      | Categórico Multivalorado  |
| **P2_h** | Faixa salarial                                           | Qualitativo               |



###    Descrição de dados

**Base de dados: State of Data Brasil 2023**

**Idade:**
- **Idade Média**: 32,38 anos
- **Desvio Padrão**: 8,40 anos
- **Idade Mínima**: 18 anos
- **Idade Máxima**: 73 anos
- **Idade Mediana**: 31,00 anos
- **Percentil 25 (Q1)**: 26,00 anos
- **Percentil 50 (Mediana)**: 31,00 anos
- **Percentil 75 (Q3)**: 38,00 anos

**Gênero:**
- **Masculino**: 76.7%
- **Feminino**: 22.2%
- **Prefiro não informar**: 0.8%
- **Outro**: 0.2%

**Cor/Raça/Etnia:**
- **Branca**: 72.4%
- **Parda**: 22.4%
- **Preta**: 4%
- **Amarela**: 0.9%
- **Indígena**: 0.15%
- **Outra**: 0.15%
- **Prefiro não informar**: 0.30%

**PCD:**
- **Sim**: 1.96%
- **Não**: 98.04%


## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

> - Seleção dos atributos
> - Tratamentos dos valores faltantes ou omissos: remoção, substituição, indução, etc.
> - Tratamento dos valores inconsistentes: conversão, remoção de dados duplicados, remoção ou tratamento de ouliers.
> - Conversão de dados: p. ex. numérico para categórico, categórico para binário, etc.


## Indução de modelos

### Modelo 1: Algoritmo

Substitua o título pelo nome do algoritmo que será utilizado. P. ex. árvore de decisão, rede neural, SVM, etc.
Justifique a escolha do modelo.
Apresente o processo utilizado para amostragem de dados (particionamento, cross-validation).
Descreva os parâmetros utilizados. 
Apresente trechos do código utilizado comentados. Se utilizou alguma ferramenta gráfica, apresente imagens
com o fluxo de processamento.

### Modelo 2: Algoritmo

Repita os passos anteriores para o segundo modelo.


## Resultados

### Resultados obtidos com o modelo 1.

Apresente aqui os resultados obtidos com a indução do modelo 1. 
Apresente uma matriz de confusão quando pertinente. Apresente as medidas de performance
apropriadas para o seu problema. 
Por exemplo, no caso de classificação: precisão, revocação, F-measure, acurácia.

### Interpretação do modelo 1

Apresente os parâmetros do modelo obtido. Tentre mostrar as regras que são utilizadas no
processo de 'raciocínio' (*reasoning*) do sistema inteligente. Utilize medidas como 
o *feature importances* para tentar entender quais atributos o modelo se baseia no
processo de tomada de decisão.


### Resultados obtidos com o modelo 2.

Repita o passo anterior com os resultados do modelo 2.

### Interpretação do modelo 2

Repita o passo anterior com os parâmetros do modelo 2.


## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


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




