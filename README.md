# pokemon-kaggle

O link do problema a ser resolvido: https://www.kaggle.com/terminus7/pokemon-challenge

A resolução do problema foi separada em duas partes: Separação/Cálculo dos dados e a Execução de MLP.

Para o cálculo dos dados, foram removidas as seguintes colunas: Name, Type 2, Generation.

O coluna Legendary foi transformada de true/false para 0.5/-0.5 para facilitar.

A coluna id foi usada apenas na identificação do pokemon, e posterior descartada.

Para o cálculo de valor de relação entre tipos do pokemon que se atacam foi usado como base a tabela a seguir,
(fonte: https://pokemondb.net/type)


Features normalizadas ficaram da seguinte forma:

P1 -> Atributo do Pokemon 1
P2 -> Atributo do Pokemon 2
Ratio -> Relação da força entre o Tipo1 do P1 versus Tipo1 do P2

Attack | Defense | HP | Legendary | Sp. Atk | Sp. Def | Speed 
--- | --- | --- | --- |--- |--- |---
(P1*RATIO)-P2 | P1-(P2*0.85) | P1-P2 | P1-P2 | (P1*RATIO)-P2 | P1-P2 | P1-P2 

![alt text](https://raw.githubusercontent.com/vitorpola/pokemon-kaggle/master/pokemon_types.png)

Dividindo o arquivo combats.csv em: 30.000 para treino e 20.000 para teste. Foi alcançado o número de 94.74% de acerto.
