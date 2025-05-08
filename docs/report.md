# DESIGUALDADE SOCIAL NO MERCADO DE DADOS NO BRASIL

Rafael Silvestre da Silva, rafael.silva.1548493@sga.pucminas.br

Eduardo Velloso Landeiro, eduardo.landeiro@sga.pucminas.br

Iosef Juan Gonçalves Chebile Candido, ijgccandido@sga.pucminas.br

---

**Professores:**

Hugo Bastos de Paula

Hayala Nepomuceno Curto

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

Nesse contexto, utilizamos a base de dados State of Data Brasil 2023, que analisa o mercado de trabalho e o perfil do profissional na área de dados. Ao analisar essa base, observamos problemas sociais, bem como a desigualdade social no mercado, prova da discrepância salarial entre grupos étnicos. **falar da base de dados secundária*

###    Contextualização

A discrepância salarial entre grupos étnicos no mercado de dados no Brasil reflete um problema estrutural histórico do país. O acesso desigual à educação de qualidade, preconceitos e barreiras socioeconômicas enfrentadas por determinados grupos impactam diretamente a inserção e a progressão na carreira dentro desse setor, que é um dos mais promissores e bem remunerados da economia digital. Assim, nosso modelo associa as desigualdades no mercado de trabalho com a discrepância salarial, relacionando-as a partir da análise da dados e técnicas de aprendizado de máquina.

Dessa maneira, as técnicas e análises do nosso modelo foram feitas usando como referência a base de dados State of Data Brasil 2023, uma pesquisa anual que mapeia o mercado de dados e inteligência artificial no Brasil. Além dessa, utilizamos a base de dados auxiliar **falar da base de dados secundária*


###    Problema

O problema a ser analisado é a desigualdade social na área de dados. Nesse contexto grupos minoritários não recebem as mesmas oportunidades no mercado de trabalho, surgindo assim uma discrepância salarial entre grupos étnicos. Dessa forma, faz-se necessário a pergunta “Como associar a desigualdade no mercado de trabalho com a discrepância salarial na área de dados”.

Feito tal pergunta, nosso grupo se apoiou nas bases de dados State of Data Brasil 2023 e **falar da base de dados secundária* para tentar respondê-la. Logo, nosso modelo se baseia em atributos dessas bases, gerando resultados a partir de técnicas de análise de dados e aprendizado de máquina. 

###    Objetivo geral

O objetivo geral do trabalho é identificar desigualdades sociais na área de dados. Nessa perspectiva, nos orientamos a partir da pergunta "Como as desigualdades sociais afetam os salários dos profissionais no mercado de trabalho de dados?". Dessa forma, para responder tal pergunta, baseamos nos atributos: gênero, cor/raça/etnia, PCD, nível de ensino, área de formação, nível, tempo de experiência na área de dados e faixa salarial.

####    Objetivos específicos

- Como a faixa salarial média varia entre profissionais de diferentes gêneros em cada região do Brasil?
- Existe disparidade salarial entre profissionais com o mesmo nível e tempo de experiência, considerando gênero e raça?
- Qual é a relação entre nível de escolaridade e faixa salarial em diferentes regiões do Brasil?



###    Justificativas

Visto que o mercado de trabalho da área de dados apresenta desigualdades sociais relevantes, optamos por criar um modelo que busca analisar essas desigualdades, evidenciando-as. Tal abordagem foi escolhida por conta da relevância social, conversando com as ODSs 9 (indústria, inovação e infraestrutura) e 10 (redução das desigualdades), servindo de incentivo para o nosso trabalho.



##    Público alvo

O público-alvo da aplicação será o governo, especialmente os órgãos responsáveis pela formulação de políticas educacionais e sociais. Os usuários terão, em sua maioria, conhecimento técnico sobre o setor, mas com diferentes níveis de familiaridade com ferramentas tecnológicas. Eles buscam soluções que ajudem a embasar decisões para combater as desigualdades, geralmente ocupando cargos intermediários ou superiores na hierarquia pública.


## Análise exploratórida dos dados

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

_**Base de dados: incluir base de dados auxiliar**_


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



_**Base de dados: incluir base de dados auxiliar**_


### Pergunta 1


### Pergunta 2

_**Existe disparidade salarial entre profissionais com o mesmo nível e tempo de experiência, considerando gênero e raça?**_


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




