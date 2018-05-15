# Pokemon Kaggle

O link do problema a ser resolvido: https://www.kaggle.com/terminus7/pokemon-challenge

A resolução do problema foi separada em duas partes: Separação/Cálculo dos dados e a Execução de MLP.

Para o cálculo dos dados, foram removidas as seguintes colunas: Name, Type 2, Generation.

O coluna Legendary foi transformada de true/false para 0.5/-0.5 para facilitar.

A coluna id foi usada apenas na identificação do pokemon, e posterior descartada.

Para o cálculo de valor de relação entre tipos do pokemon que se atacam foi usado como base a tabela a seguir,
(fonte: https://pokemondb.net/type)

![TiposPokemon](https://raw.githubusercontent.com/vitorpola/pokemon-kaggle/master/pokemon_types.png)

Features normalizadas ficaram da seguinte forma:

P1 = Atributo do Pokemon 1;
P2 = Atributo do Pokemon 2;
RATIO = Relação da força entre o Tipo1 do P1 versus Tipo1 do P2;

OBS: O P2 sempre tem o decrescimo de 15% da HP devido ao primeiro ataque do P1;

Attack | Defense | HP | Legendary | Sp. Atk | Sp. Def | Speed 
--- | --- | --- | --- |--- |--- |---
(P1*RATIO)-P2 | P1-P2 | P1-(P2*0.85) | P1-P2 | (P1*RATIO)-P2 | P1-P2 | P1-P2 


Utilizando como base o arquivo combats.csv (50000 linhas), foram gerados 3 arquivos, sendo eles:
- train.csv (32000)
- test.csv (18000 linhas - sem classe)
- winners.csv (18000 linhas - somente classe)

E executando o programa mlp.rb, utilizando a função RandomForestClassifier da biblioteca sklearn, foi feito o treinamento dos 32000 dados de treino (train.csv), e após isso a funcionalidade retorna uma lista de 18000 previsões (test.csv), onde será conferida a sua porcentagem de acertos reais (winners.csv).

A maior porcetagem de acerto atingida foi de 95,23%
