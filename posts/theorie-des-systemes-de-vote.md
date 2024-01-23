---
title: Introduction à la théorie des systèmes de votes
author: Raphaël Goutmann & Louise Marsollier
date: 12/01/2024
---

[TOC]

## Définitions générales

La question du vote est omniprésente dans nos sociétés, que ce soit entre amis pour décider quel film choisir ou à l’échelle d’un pays dans le choix d’un président. De par leur aspect transversal, touchant aussi bien à la politique, à l’économie qu’aux mathématiques, les systèmes de votes font l’objet d’études poussées depuis plusieurs siècles.

Un système de vote, ou mode de scrutin, est un système par lequel agréger les préférences collectives des électeurs pour en déduire une préférence de groupe vis-à-vis d’un certain nombre d’alternatives ou candidats. 

Nous nous limiterons ici au cas d’une élection simple aboutissant au choix d’une seule alternative parmi l’ensemble des alternatives possibles (un président parmi les candidats, un restaurant parmi l’ensemble de ceux dans un rayon d’un kilomètre etc.) 

Nous négligeons par ailleurs les cas d'égalité entre candidats, dans la mesure où ils sont hautement improbables à l’échelle réelle.

Une façon simple de définir les préférences d’un individu est de définir une relation d’ordre totale sur l’ensemble des alternatives possibles, autrement dit une classification des différentes alternatives possibles. 

Dans le cas d’une élection à trois candidats A, B et C, la préférence d’un électeur pourrait par exemple s’exprimer comme “A préféré à B, préféré à C”, ou, de la même manière, “B préféré à A, préféré à C”. 

Nous appellerons cette classification individuelle une “liste de préférence” et nous noterons “A préféré à B” avec la notation usuelle A > B. 

Nous pouvons alors rassembler l’ensemble de ces listes de préférences dans un “profil de préférences”. Imaginons une élection à 3 candidats A, B et C et 10 électeurs parmis lesquels : 
- 5 préfèrent A à B à C 
- 3 préfèrent B à A à C
- 2 préfèrent C à B à A

Le profile de préférence de l’élection peut alors se représenter de la manière suivante :

|5|3|2|
|-|-|-|
|A|B|C|
|B|A|B|
|C|C|A|

L’enjeux est alors d'agréger un profil de préférence en une préférence collective.  

## Panorama des principaux modes de scrutins 

Nous disposons pour cela de nombreux modes de scrutin plus ou moins complexes. 

### Le scrutin majoritaire

Le plus évident d'entre eux est le scrutin majoritaire.
Pour définir le gagnant de l’élection, nous comptons le nombre de fois où chaque candidat apparaît comme premier choix des électeurs. Si l’un d’entre eux obtient plus d’une stricte majorité des voies (plus de 50%), il gagne.

Par exemple, cette élection : 

|6|2|2|
|-|-|-|
|A|B|C|
|B|A|B|
|C|C|A|

verrait le candidat A élu. En effet, il y a en tout 8 électeurs, le candidat A apparait premier choix chez 6 d’entre eux, il s’agit d’une majorité et le candidat A est élu. 
Mais un problème surgit immédiatement : dans ce système, il n’y a pas toujours de vainqueur. En effet, pour peu que les voies soient correctement réparties, il se peut qu’aucun candidat n'obtienne de majorité. 
Nous devons donc améliorer ce système de manière à ce qu’il fournisse un vainqueur à chaque élection. 

### Le scrutin majoritaire modifié

Une autre solution peut alors consister à compter le nombre de fois où chaque candidat apparaît comme premier choix des électeurs et à élire le candidat présentant le plus de voix. Ainsi, le cas suivant : 

|4|3|3|
|-|-|-|
|A|B|C|
|B|C|B|
|C|A|A|

pour lequel il n’y aurait pas eu de vainqueur dans le système précédent, mène dans le scrutin majoritaire modifié à l’élection du candidat A. 
Ce système fournit toujours un vainqueur qui semble représenter la volonté du groupe. 

Toutefois ce système présente deux principales limites. 

Premièrement, il ne prend en compte que les premiers choix des électeurs, ignorant totalement le reste de la liste de préférence. Le fait d’ignorer le reste des préférences mène à des cas où un candidat est élu alors même que celui-ci est dernier sur la liste de préférence d’une majorité stricte d’électeurs. C’est par exemple le cas dans l’élection précédente où A, bien que premier dans 4 listes, est dernier dans les 6 listes restantes. A ne semble pas véritablement représenter la “préférence collective”, le choix de B aurait dans ce cas semblé plus judicieux. 

Une autre limite est la question de la dépendance aux alternatives non pertinentes. Imaginons une élection où deux partis sont présents : le parti A aux idées de gauche et la partie B aux idées de droite. 

Un profil de préférence pourrait alors être le suivant. 

|6|4|
|-|-|
|A|B|
|B|A|

Dans ce contexte, A gagnerait 6 contre 4. Imaginons maintenant qu’un deuxième parti de gauche C se présente. Davantage en accord avec certaines idées de C, certains électeurs de A pourraient se diriger vers C de sorte à obtenir le profile de préférence suivant : 

|3|4|3|
|-|-|-|
|A|B|C|
|B|A|A|
|C|C|B|

Dans ce contexte, c’est B qui est élu. L’introduction du candidat C a eu pour effet de “diviser” les voies à gauche, provoquant l’élection du candidat de droite, alors même qu’une majorité des électeurs étaient favorable à l’élection d’un candidat de gauche. 

Cette absence d’indépendance aux alternatives non pertinentes est une menace sévère au pluralisme politique, fondement d’une démocratie qui fonctionne. Elle entraîne par ailleurs les électeurs à voter utile / stratégique plutôt que selon leurs véritables préférences.

Il nous faut donc améliorer ce système.

### Le scrutin à deux tours

Une idée pourrait alors être d’organiser une élections en plusieurs “étapes” / “tours” , permettant aux électeurs d’ajuster au fur et à mesure leurs votes pour refléter au mieux leur volonté. 


Le manière la plus commune de procéder est d’organiser deux tours : deux candidats sont élus au premier tour selon un scrutin majoritaire modifié et ces derniers s’affrontent dans un scrutin majoritaire au second tour. C’est le système dans les élections présidentielles en France.


Cette manière de procéder, bien que légèrement meilleure que le scrutin majoritaire classique,  ne règle pas entièrement le problème. Imaginons une élection entre deux parties de droite D1, D2 et trois parties de gauche G1, G2, G3.

Le profile de préférence suivant : 

|4|4|3|3|3|
|-|-|-|-|-|
|D1|D2|G1|G2|G3|
|D2|D1|G2|G1|G1|
|G1|G1|G3|G3|G2|
|G2|G2|D1|D1|D1|
|G3|G3|D2|D2|D2|

Mènerait les deux candidats de droite au second tour (et donc à l’élection d’un candidat de droite), alors même qu’une majorité de la population vote à gauche. C’est pour pallier ce phénomène de division que les partis politiques organisent des primaires (qui ne font en fin de compte que repousser le problème au moment des primaires).

### Le système de Hare

Nous pourrions alors pousser l’idée à l’extrême en organisant autant de tour que de candidats. Autrement dit, nous éliminerons à chaque tour le candidat ayant reçu le moins de premier choix des listes de préférences jusqu’à ce qu’il n’en reste qu’un seul. Il s’agit de la méthode de Hare. 

Nous pouvons par exemple imaginer l’élection suivante : 

|4|5|3|2|
|-|-|-|-|
|A|C|B|A|
|B|B|D|D|
|C|D|C|C|
|D|A|A|B|

Au premier tour, le candidat D est éliminé puisqu’il ne reçoit aucune voix.
Le profile de préférence devient alors : 

|4|5|3|2|
|-|-|-|-|
|A|C|B|A|
|B|B|C|C|
|C|A|A|B|

À nouveau, le candidat B est éliminé puisqu’il ne reçoit que 3 voix contre 6 pour A et 5 pour C. 
Le profile de préférence devient donc : 

|4|5|3|2|
|-|-|-|-|
|A|C|C|A|
|C|A|A|C|

Dont on peut fusionner les colonnes de manière à obtenir : 

|6|8|
|-|-|
|A|C|
|C|A|

Le candidat C gagne au final avec une majorité stricte de 8 contre 6. 
La force de ce système vient de sa prise en compte non plus seulement des premières préférences des individus mais également du reste de la liste. 

Toutefois, en analysant le système en profondeur, une limite apparaît rapidement : le système n’élit pas toujours le vainqueur de Condorcet.
Considérons l’élection suivante : 

|4|6|5|
|-|-|-|
|A|B|C|
|B|A|A|
|C|C|B|

En utilisant le système de Hare, nous éliminerions A au premier tour puis C au second pour finalement obtenir B vainqueur. 

Toutefois, en observant les préférences plus en détail un fait saute aux yeux : A est préféré par une majorité d'électeurs à tous les candidats en lice. En effet : 
- A est préféré à B par 9 électeurs (une majorité)
- A est préféré à C par 10 électeurs (une majorité)

A est dit “vainqueur de Condorcet” et il apparaît absurde de ne pas élire A. 

### Le système de Borda

Nous pourrions également envisager le système suivant : considérons une élection entre trois candidats A, B et C. Chaque fois qu’un candidat apparaît à la première place il reçoit deux points et chaque fois qu’il apparaît à la deuxième place, il reçoit un point. 
Le candidat élu est alors le candidat ayant reçu le plus de points. 

Ainsi dans le profile de préférence suivant : 

|4|5|7|
|-|-|-|
|C|A|B|
|B|C|C|
|A|B|A|

A recevrait $2 \times 5  = 10$ points.
B recevrait $1 \times 4 + 2 \times 7 = 18$ points.
C recevrait $4 \times 2 + 5 + 7 = 20$ points.
C serait donc élu (20 > 18 > 10). 

Bien que séduisant à première vue, il présente un défaut majeur : les électeurs peuvent avoir intérêt à ne pas voter selon leurs préférences réelles pour favoriser l’élection de leur candidat. 

Par exemple, si dans l’élection précédente les 7 électeurs B > C > A avaient votés B > **A** > **C**, le profil aurait alors été :

|4|5|7|
|-|-|-|
|C|A|B|
|B|C|A|
|A|B|C|

A aurait alors reçu $52 + 7 = 17$ points.
B : $4 + 2 \times 7 = 18$ points.
C : $4 \times 2 + 5 = 14$ points
B serait donc élu. 
Autrement dit, les électeurs B > A > C ont eu intérêt à mentir sur leurs préférences réelles pour faire élire leur candidat préféré. Ils ont voté utile pour manipuler le résultat du scrutin. C’est là encore un problème.

### Le système de Combs

Le système de Combs est similaire au système de Hare, à la seule différence qu’il ne s’agit pas à chaque tour d’éliminer le candidat ayant reçu le moins de première place mais le candidat ayant reçu le plus de dernière place. Est éliminé non plus le moins apprécié mais le plus détesté des candidats. 

Dans le profil suivant :

|5|5|3|2|
|-|-|-|-|
|A|C|B|A|
|B|B|D|D|
|C|D|C|C|
|D|A|A|B|

A serait éliminé puisque dernier chez 8 électeurs :

|5|5|3|2|
|-|-|-|-|
|B|C|B|D|
|C|B|D|C|
|D|D|C|B|

Puis D serait éliminé puisque dernier chez 10 électeurs.

|5|5|3|2|
|-|-|-|-|
|B|C|B|C|
|C|B|C|B|

Et enfin C serait éliminé. Le vainqueur de l’élection est donc B. 

À noter que malgré ses similitudes avec le système de Hare, tous deux ne produisent pas toujours le même résultat. 

Le système de Combs, de part sa construction, présente également certaines limites. 
Un candidat adulé par une majorité stricte d’électeurs mais détesté par un minorité d’entre eux peut se voir éliminer dès le premier tour, bien que celui-ci semble refléter la volonté du peuple. 

Ainsi, aucun des systèmes de votes présentés jusqu’à présent n’est parfait, si bien que nous pouvons nous interroger sur l’existence même d’un mode de scrutin “absolu”. Le problème est d’autant plus grand que ces systèmes peuvent, pour un même profil de préférence, produire des résultats différents, ce qui empêche de les départager.

Existe-t-il donc un mode de scrutin parfait ?


## Vers un mode de scrutin parfait

Pour répondre à cette question, définissons dans un premier temps ce que nous attendons d’un tel système. À quels critères devrait-il répondre pour être qualifié de “bon” ?

Nous nous plaçons ici dans un cadre plus général. Imaginons que notre système de scrutin ne délivre non plus seulement un unique vainqueur mais une liste de préférences des candidats en lice reflétant la volonté du groupe.
Pour une élection entre trois candidats A, B et C, un résultat pourrait - par exemple - être A > B > C si le système considère que le peuple, dans sa globalité, préfère A à B à C. 

### Critère de Condorcet

Le critère de condorcet peut s’exprimer de la façon suivante :
“Si un candidat est préféré en duel à n’importe quel autre candidat alors celui-ci doit être élu. On le nomme alors vainqueur de Condorcet.” 

### Critère de monotonie 

Le critère de monotonie s’énonce comme suit : 
“Si un ou plusieurs électeurs changent leurs préférences de manière à placer un candidat plus haut, alors la préférence globale de groupe ne peut être affectée que par une montée de ce candidat ou par l’absence de changements.”

Autrement dit, si un électeurs décide de mieux placer un candidat dans sa liste de préférences, celui-ci ne peut pas descendre dans la préférence globale. 

Le scrutin à deux tours par exemple ne respecte pas le critère de monotonie.
Dans le cas suivant : 

|11|2|7|4|4|
|-|-|-|-|-|
|A|B|B|C|C|
|B|A|C|A|B|
|C|C|A|B|A|

Le second tour opposerait A à B et A gagnerait 15-13. Si toutefois les deux électeurs B > A > C décidaient de modifier leurs votes en plaçant A à la première place, le profil obtenu : 

|13|7|4|4|
|-|-|-|-|
|A|B|C|C|
|B|C|A|B|
|C|A|B|A|

verrait B éliminé au premier tour et C gagnerait 15-13. Autrement dit, améliorer la place de A dans les votes lui a porté préjudice. 

### Critère de Pareto ou Unanimité 

Le critère de Pareto (ou critère d’unanimité) s’énonce comme suit :
“Si tous les électeurs préfèrent A à B, alors le système ne peut pas dire que la population préfère B à A”. 

Autrement dit, si la population est unanime sur le fait que A est préférable à B, alors cette préférence doit se manifester au niveau de la préférence globale. 

### Critère de Strategy-Proofness

Un système est dit strategy proof (ou non manipulable) si un électeur ne peut jamais améliorer les chances de son candidat favoris en votant de manière stratégique. Un électeur obtiendra toujours le meilleur résultat en votant selon ses préférences réelles. C’est donc dans l'intérêt de l’électeur de voter selon ses préférences réelles.

### Critère D'indépendance aux alternatives non pertinentes

Le critère d’indépendance aux alternatives non pertinentes (ou IIA pour independence of irrelevant alternatives) s’énonce comme suit : 
“Supposons que l’élection conclut que la population préfère dans l’ensemble A à B, et supposons que certains électeurs venaient à changer leurs votes. Si aucun électeur ne change les positions relatives de A et de B (tous ceux qui plaçaient initialement A au dessus de B continuent de le faire et de la même manière pour ceux qui plaçaient B au dessus de A) alors le système doit toujours considérer que A est préféré à B”.

### Critère de non-imposition 

“Le critère de non-imposition signifie que toutes les configurations possibles de préférences globales peuvent être obtenues, pour peu que l’on choisisse le bon profil de préférence.”

En pratique l’indépendance aux alternatives non pertinentes, la monotonicité et la non-imposition impliquent le critère de pareto, si bien que tout théorème valable dans le cas du critère de pareto le sera également dans le cas où l’iia, la monotonicité et la non-imposition sont simultanément valables. 

Ainsi, un système parfait devrait a minima respecter ces critères qui semblent raisonnables. 

### Le théorème d'impossibilité de Arrow

Mais la réalité nous rattrape et Kenneth Arrow (économiste né en 1921, mort en 2017 prix nobel d’économie) publie en 1951 son théorème d’impossibilité qui s’énonce comme suit : 

> “Quand il y a trois alternatives ou plus, la seule manière de combiner des préférences individuelles en une préférence de groupe avec unanimité et indépendance aux alternatives non pertinentes est la dictature.” 

Nous donnerons ici la démonstration proposée par John Geanakoplos dans son article Three brief proofs of Arrow’s impossibility Theorem. Il est intéressant d’observer qu’il ne s’agit pas là de la preuve originale proposée par Arrow mais d’une re-démonstration. Il est en effet fréquent en mathématiques de “re-démontrer” des théorèmes de manière simple ou plus élégante.

Supposons ici que nous ayons 3 candidats { A, B, C } et N électeurs (le raisonnement pouvant se généraliser à un nombre plus important d’électeurs). 

Dans le cadre de la théorie des systèmes de votes, dire d’un électeur qu’il est dictateur de l’élection signifie qu’il dicte par son vote la volonté du groupe. Autrement dit, la volonté du groupe sera la volonté de l’électeur / la préférence globale du groupe sera la préférence individuelle de l’électeur, quelle que soit la répartition des votes. 
Par analogie, on dit d’un électeur qu’il est dictateur de pair s’il dicte la préférence entre A et B. 

Nous cherchons donc ici à démontrer que dans tout système de vote respectant le critère d’unanimité et l’indépendance aux alternatives non pertinentes il existe un électeur n* tel que n* est dictateur. 

Avant de démontrer le théorème de Arrow en tant que tel, nous allons démontrer un théorème “intermédiaire” que nous utiliserons par la suite. Un tel théorème utilisé comme outil pour en démontrer un autre est appelé lemme. Au même titre que l'homme fabrique des outils pour mieux construire sa maison, le mathématicien fabrique des lemmes pour mieux construire ses théorèmes. 

Le lemme en question, dit “lemme extremal” s’énonce comme suit : 
> “Considérons un candidat b quelconque. Dans n’importe quel profil de préférences où chaque électeurs place b en première ou en dernière position dans sa liste de préférence, la préférences collective doit de même placer b en première ou en dernière position”

Autrement dit, un profil de préférence de la forme : 


|10|4|5|8|
|-|-|-|-|
|b|...|...|b|
|...|...|...|...|
|...|b|b|...|

Où b est systématiquement placé dans une position extrême, le système de vote, pour peu qu’il respecte l’iia et le critère d’unanimité, placera également b dans une position extrême, i.e premier ou dernier.

Pour démontrer cela, nous raisonnerons par l’absurde. Supposons donc que ce ne soit pas le cas, qu’il existe un profil de préférences où b est systématiquement placé dans une position extrême mais que ce ne soit pas le cas au niveau de la préférence collective, autrement dit qu’il existe deux alternatives a et c telles que a > b > c.
Par iia, échanger a et c n’a d’effet ni sur la préférence a > b ni sur la préférence b > c.
Nous pouvons dès lors échanger les ac de sorte à placer tous les c au-dessus des a. Par unanimité, a étant maintenant toujours préféré à c, la préférence collective considère de même que a > c. Mais nous avons toujours (par iia) a > b et b > c donc a > c (par transitivité). Nous avons alors d’une part a > c et d’autre part c > a, un résultat absurde qui invalide donc l’hypothèse selon laquelle le théorème serait faux. Le théorème est donc vrai.

Entrons maintenant dans le cœur de la démonstration.
Nous partirons d’un profil particulier que nous généraliserons progressivement à l'ensemble des profils possibles. 

Imaginons donc un profil de préférence où le candidat b est systématiquement placé en dernière position. 

|1|2|...|n-1|n|
|-|-|-|-|-|
|...|...|...|...|...|
|b|b|b|b|b|

(ce tableau représente les listes de préférences des n électeurs, numérotés de 1 à n) 

Puisque chaque candidat est unanimement préféré à b, b est nécessairement placé dernier dans la liste de préférences collectives.

Partant de ce profil de préférences, nous allons, candidat par candidat, faire passer b de la dernière à la première position, en laissant le reste des préférences inchangées. 

Ainsi au premier tour nous obtiendrons  

|1|2|...|n-1|n|
|-|-|-|-|-|
|b|...|...|...|...|
|...|b|b|b|b|

Puis au second tour 

|1|2|...|n-1|n|
|-|-|-|-|-|
|b|b|...|...|...|
|...|...|b|b|b|

*etcetera*, *etcetera* jusqu’au nième tour ou nous obtiendrons finalement

|1|2|...|n-1|n|
|-|-|-|-|-|
|b|b|b|b|b|
|...|...|...|...|...|

b étant préféré unanimement dans ce profil à n’importe quel autre candidat en lice, il est (par critère d’unanimité) nécessairement vainqueur. 

Puisque b reste tout au long du processus dans un position extrême dans les préférences individuelles, il l’est également - d’après le lemme extremal énoncé précedemment - dans la préférence collective. 
Il existe donc un électeur n* responsable du “basculement” du candidat b de la dernière à la première position. 
Autrement dit, le profil suivant (que nous appellerons profil (I) ) 

|1|2|...|n*|...|n-1|n |
|-|-|-|-|-|-|-|
|b|b|b|...|...|...|...|
|...|...|...|b|b|b|b|

b est donné perdant tandis que dans le profil suivant (que nous appellerons profil (II) ) 

|1|2|...|n*|...|n-1|n |
|-|-|-|-|-|-|-|
|b|b|b|b|...|...|...|
|...|...|...|...|b|b|b|

b est donné gagnant. 

n* est donc pivot dans la mesure où son choix va dicter la position de b dans le résultat de l’élection. 

Nous allons maintenant montrer que ce n* est dictateur de pair pour toutes les paires n’impliquant pas b et quel que soit le profil considéré. 

Considérons donc un couple de candidats a et c et choisissons l’un d’entre eux, disons a. 

Nous construisons alors un profil (III), similaire au profil (II) à la différence que n\* place a au-dessus de b de sorte que a > b > c. 
Puisque les positions relatives de a et c sont les mêmes que dans le profil (I), la préférence collective est (par iia) a > c. 
De même, puisque les positions relatives de b et c sont les mêmes que dans le profil (II), la préférence collective est (par iia) c > b. 
Par transitivité nous avons donc a > c > b  a > b
Puisque la préférence entre a et b est fixée, les électeurs peuvent placer c où bon leur semble sans modifier la relation ab, dévoilant ainsi l’ensemble des profils possibles (a et b étaient déjà placés de façon arbitraire et c l’est désormais également).
Ainsi, quelque soit le profile considéré, n\* dicte la préférence globale entre toutes les paires n’impliquant pas c. Il ne reste dès lors plus qu’à prouver que c’est également le cas pour celles impliquant c. 
Il suffit pour cela de réitérer le raisonnement et d’observer qu’un dictateur de paires impliquant c dicte également des paires dont n\* est dictateur, de sorte que ces derniers ne sont en fait qu’un unique dictateur, l’élection présente donc bien un dictateur. (QED) 


Nous pouvons toutefois noter deux choses. Premièrement, le théorème de Arrow ne s'applique que dans le cas où la préférence collective s'exprime comme une liste de préférence. Qu'en est-il alors des modes de scrutins qui n'ont pour objectif que d'élire un seul représentant ? 
Deuxièmement, le critère d'indépendance aux alternatives non pertinentes peut être critiqué puisqu'il ne prend en compte que la position relative des candidats dans les votes et non l'écart qui les sépare. 

### Le théorème d'impossibilité de Gibbard-Satterthwaite

C'est dans ce contexte que Allan Gibbard et Mark Satterthwaite démontrent séparément dans les années 70 un théorème plus "fort" que le théorème de Arrow, le théorème dit de Gibbard-Satterhwaite (que nous admettrons sans démonstration) : 

> “Pour trois alternatives ou plus, le seul scrutin qui respecte l'unanimité et le critère de strategy-proofness est la dictature”

Ainsi, il n'existe aucun mode de scrutin ordinal (c'est à dire qui se base sur une liste de préférence des électeurs) qui puisse respecter conjointement tous ces critères.

### Vers le jugement majoritaire

Malgré tout, ces théorèmes ne s'appliquent qu'au cas des scrutins ordinaux et nous pouvons parfaitement contourner cette difficulté en mettant en oeuvre un autre système pour exprimer les préférences de l'électorat. 

L'une d'entre elle consiste à noter les candidats selon une certaine échelle. 
Dans une élection à trois candidats A, B et C, un électeur pourrait par exemple attribuer les notes suivantes aux candidats 
- 3/20 à A
- 13/20 à B
- 17/20 à C

Deux problèmes surgissent alors immédiatement. Premièrement, chacun possède sa manière de noter. Un excellent candidat pourrait, chez certain électeurs, mériter une note de 15/20, tandis que chez d'autre il s'agirai d'un 18/20. Cela risquerai alors de fausser les résultats et il est donc nécessaire de "normaliser" les notes (ce qui a pour effet de dénaturer les voix). Deuxièmement, un électeur aura tout intérêt à exagérer ses notes pour favoriser ses candidats préférés au détriment des autres.  
L'électeur ci-dessus aurait alors tout intérêt à voter : 
- 0/20 à A
- 0/20 à B
- 20/20 à C

Il s'agit là encore d'un vote stratégique. Une manière de régler ce problème est alors de considérer non pas la moyenne des notes obtenues mais la répartition de ces dernières, en utilisant par exemple une médiane. 

C'est ainsi que naît en 2007 le "jugement majoritaire", un système de vote qui constitue encore aujourd'hui le meilleur système de vote connu. 
Le jugement majoritaire ne respecte pas tous les critères mais une grande partie d'entre eux et les quelques critères restant sont, en règle générale, bien respectés. Il n'est en particulier pas totalement strategy-proofness. 

En conclusion, les sytèmes de votes mis en oeuvre dans nos sociétés présentent de nombreuses limites : dilemme du vote utile, indépendance aux alternatives non pertinentes etc. Bien que les théorèmes d'imposibilité de Arrow et de Gibbard-Satterthwaite démontrent qu'un système parfait n'existe pas, nous pouvons largement rendre nos systèmes de votes "moins pire" pour davantage représenter la volonté du peuple et espérer qu'un jour le mot démocratie puisse enfin prendre tout son sens.  

## Annexe

Voici quelques ressources pour approfondir le sujet.

Chacune d’entre elle est précédée d’un certain nombre d’étoiles suivant sa complexité, allant d’une étoile (\*) pour les plus faciles à trois étoiles (\*\*\*) pour les plus complexes : 

- (*) Une excellente série de vidéos sur les mathématiques de la démocratie [La démocratie sous l'angle de la théorie des jeux - Science4All](https://www.youtube.com/playlist?list=PLtzmb84AoqRSmv5o-eFNb3i9z64IuOjdX)
- (*) Un vidéo de présentation du jugement majoritaire (entre autre) [Réformons l'élection présidentielle ! — ScienceEtonnante](https://www.youtube.com/watch?v=ZoGH7d51bvc)
- (**) Un papier de l'association mathématique du Québec pour approfondir la théorie des systèmes de vote [Mathématiques Électorales — AMQ](https://www.amq.math.ca/wp-content/uploads/bulletin/vol60/no3/07-maitre-choix-social.pdf)
- (***) L'article original de la démonstration du théorème de Arrow présentée ci-dessus [Three Brief Proofs of Arrow's Impossibility Theorem — John Geanakopolos](http://dido.econ.yale.edu/~gean/art/p1116.pdf)
- (***) Un livre très complet (et relativement court) sur la théorie des systèmes de votes [The Mathematics of Elections and Voting — W.D Wallis](https://www.amazon.com/Mathematics-Elections-Voting-W-D-Wallis/dp/3319098098)