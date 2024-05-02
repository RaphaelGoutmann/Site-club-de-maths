---
title: Exploration des fondements des mathématiques
author: Louise Marsollier & Raphaël Goutmann
date: 03/05/2024
---

[TOC]

> “La mathématique est l'art de donner le même nom à des choses différentes.” — Henri Poincaré

# Notations

Nous adopterons, dans cet atelier, quelques notations relatives à la
logique mathématique.

-   $\Rightarrow$ signifie "implique"
-   $\forall$ signifie "pour tout" ou "quelque soit"
-   $\exists$ signifie "il existe"
-   $\exists !$ signifie "il existe un unique"
-   $\vee$ signifie "ou"
-   $\wedge$ signifie "et"
-   $\neg$ signifie "non"\

Par ailleurs, on appellera *assertion* une affirmation soit *vraie*,
soit *fausse*.

En notant, par exemple, $A$ l'assertion "Socrate est un homme", $B$
l'assertion "Tous les hommes sont mortels" et C l'assertion "Socrate est
mortel" on a : $$(A \wedge B) \Rightarrow C$$

# Axiomatisation des mathématiques

## Structure des mathématiques

Les mathématiques occupent une place particulière au sein de la grande
famille des sciences.

Une science a toujours pour objet la connaissance. Les mathématiques se
distinguent des autres sciences dans leur manière d'accéder à cette
connaissance.
 
Une science dite *empirique* (la biologie, la physique, la médecine
etc.) recherche la connaissance dans l'expérience. Il s'agit de
construire des *modèles* qui puissent prévoir au mieux les phénomènes
réels. Pour cela, le scientifique émet des hypothèses quant aux lois qui
régissent ces phénomènes et construit des expériences pour tester ces
hypothèses. Deux possibilités se présentent alors : les résultats de
l'expérience peuvent confirmer les prédictions, auquel cas l'hypothèse
est renforcée (mais non prouvée), ou bien l'expérience contredit
l'hypothèse qui doit donc être ajustée. Ainsi, la notion de *preuve* ou
de *vérité absolue* dans les sciences empiriques n'a pas de sens. Une
théorie ne peut être que plus vraisemblable qu'une autre.

Les mathématiques, *a contrario*, reposent sur l'idée d'une vérité
absolue. La vérité mathématique est accessible par la preuve, qui
consiste en une succession logique d'étapes menant à une conclusion
*irréfutable*. Plus précisément, il s'agit de combiner, selon les lois
de la logique, des résultats vrais pour aboutir à d'autres résultats
vrai. Une question se pose alors : quel est le point de départ ? En
effet, si les démonstrations consistent en une combinaison logique de
résultats, arrive inévitablement un moment où le mathématicien doit
admettre un résultat, une base, à partir de laquelle construire le
reste. Ces résultats *admis* comme constituant la brique fondamentale de
l'édifice mathématique sont appelés *axiomes*. Les mathématiques peuvent
alors être vue comme une pyramide reposant sur un certain nombre
d'axiomes desquels sont déduis, par inférence logique, théorèmes,
lemmes, propositions et corollaires.

L'enjeu consiste alors à déterminer le "meilleur" système d'axiomes, le
meilleur ensemble d'axiomes, pour établir une base solide à l'ensemble
des mathématiques.

À noter ici que la démarche d'axiomatisation ne cherche pas à donner un
sens aux objets manipulés. Elle distingue en effet la *nature* des
objets leurs *propriétés*. Les mathématiques sont ici perçus comme un
jeu logique de symboles, les objets définis n'ayant de sens que celui
que nous leur donnons.

## Axiomes d'Euclide

Proposés dans le livre 1 des *Élements*, les axiomes d'Euclide
constituent le premier système d'axiomes de l'histoire des
mathématiques. Euclide se basera par la suite dessus pour construire
l'ensemble de sa théorie géométrique.

Les axiomes d'Euclide sont au nombre de cinq :

1.  Deux points définissent un et un seul segment.
2.  Tout segment entre deux points peut être prolongé en une et une
    seule droite.
3.  Un point et une longueur définissent un et un seul cercle.
4.  Tous les angles droits sont égaux.
5.  Par un point, il passe toujours une et une seule droite parallèle à
    une droite donnée.

Ces cinq propositions, évidente au premier abord, suffisent à construire
l'ensemble de la théorie géométrique classique.

Le dernier postulat (dit postulat des parallèles) a fait l'objet de
nombreux débats dans au sein de la communauté mathématiques. Les
mathématiciens se sont en effet longtemps interrogé sur le caractère
*axiomatique* de ce dernier : n'est-il pas possible de le démontrer à
partir des autres axiomes ? Auquel cas il s'agirait d'un théorème et non
d'un axiome. Cette question a donné naissance aux géométries
non-euclidiennes, des géométries dont le système d'axiomes n'admet pas
le postulat des parallèles (nous aurons l'occasion d'explorer d'avantage
ce sujet dans un prochain atelier). De cette manière les mathématicien
ont pu prouver qu'il s'agissait bien d'un axiome et non d'un théorème.

## Axiomes de Peano

La géométrie euclidienne, aussi élégante soit-elle, montre rapidement
certaines faiblesses. Limitée au cadre de la géométrie, elle ne permet
pas de formaliser les nouvelles branches des mathématiques qui se
développent alors, que ce soit l'analyse, l'algèbre ou encore
l'arithmétique.

Dans cette ambition d'élargir le champ de l'axiomatisation, le
mathématicien italien Giuseppe Peano répertoria, en 1889, les propriétés
structurelles de l'ensemble des entiers naturels $\mathbb{N}$ afin de
donner une construction axiomatique de l'arithmétique.

L'arithmétique de Peano repose sur deux idées fondamentales : l'objet 0
et le concept de successeur. Les entiers naturels sont en effet définis
par ceci qu'ils *succèdent* tous (à l'exception de 0) à un autre entier
naturel. Une fois le 0 définit, ils peuvent ainsi tous être décrit par
une relation de succession par rapport à un précédent entier.

Les axiomes de l'arithmétique de Peano sont les suivants :

-   $\forall x, \neg (S(x) = 0)$ (aucun entier ne possède 0 pour
    successeur ou, autrement dit, 0 n'a pas de prédécesseur)
-   $\forall x, \exists y, \neg (x = 0) \Rightarrow (S(y) = x)$ (tout
    entier non nul est le successeur d'un autre entier)
-   $\forall x, \forall y, (S(y) = S(x) \Rightarrow x = y)$ (deux
    entiers de même successeur sont égaux)

Une fois définis les objets de l'arithmétique de Peano (les entiers), il
s'agit de définir des opérations sur ces derniers, là encore à partir
d'axiomes. L'addition dans un premier temps :

-   $\forall x, (x + 0 = x)$ (0 est un élément *neutre* pour l'addition)
-   $\forall x, \forall y, (x + S(y) = S(x + y))$ (l'addition d'un successeur est le successeur de l'addition)

À noter ici que l'addition est définie de façon récursive. Additionner
deux entiers revient à dérouler une procédure aboutissant *in fine* au
résulat. De la même manière, il est possible de définir la
multiplication à partir de l'addition et de façon récursive :

-   $\forall x, (x \times 0 = 0)$ (0 est un élément *absorbant* pour la
    multiplication)
-   $\forall x, \forall y, (x \times S(y) = x \times y + x$ (multiplier
    $x$ par un successeur revient à ajouter $x$ à la multiplication)

Le dernier axiome, enfin, et sans doute le plus important, est celui
permettant de raisonner par récurrence. Il se définit comme suit :

-   ($\phi(0) \wedge (\forall x, \phi(x) \Rightarrow \phi(S(x))) \Rightarrow \forall x, \phi(x) )$

Autrement dit, si une propriété est vérifiée en $0$ et que sa vérité
pour un certain rang *implique* celle du successeur, alors elle est
vraie pour tout entier naturel.

Combinés aux axiomes de la logique, il est alors possible, à partir de
ces quelques axiomes, de réécrire (non sans peine néanmoins) toute
l'arithmétique de façon rigoureuse.

Démontrons, pour illustrer ces notions, l'égalité $1 + 1 = 2$ ou, selon
les notations de l'arithmétique de Peano : $$S(0) + S(0) = S(S(0))$$

D'après l'axiome n°5 (qui définit l'addition par récurrence) :
$$S(0) + S(0) = S(S(0) + 0)$$

Puis d'après axiome n°4 (qui définit le 0 comme élément neutre de
l'addition) : 
$$S(S(0)+0) = S(S(0))$$

Enfin, par transitivité de l'égalité (qui est un axiome de la logique) :
$$S(0) + S(0) = S(S(0))$$

Ainsi, l'arithmétique de Peano permet de décrire l'ensemble de
l'arithmétique dans un système d'une étonnante simplicité. Cepandant, il
présente la même limite soulevée dans le cadre des axiomes d'Euclide :
il se limite à l'étude de l'arithmétique.

C'est dans ce contexte que naît au au sein de la communauté mathématique
du XXe siècle la volonté de construire un système d'axiomes universel,
pouvant établir une base solide à l'ensemble des mathématiques.

## Axiomes ZFC

ZFC, nommé ainsi en hommage aux mathématiciens Ernst Zermelo et Abraham
Fraenkel qui en sont à l'origine, est un système d'axiomes ayant pour
ambition de décrire toutes les mathématiques. En particulier, ZFC
contient l'arithmétique de Peano et la géométrie euclidienne, mais
premet également de décrire l'analyse, les probabilités etc.

Développé au XXe siècle, ZFC a été le point de départ des travaux du
groupe Bourbaki, décidé à reconstruire toutes les mathématiques sur des
fondements nouveaux, donnant naissances aux mathématiques "modernes".

Le système ZFC repose entièrement sur le concept d'ensemble. Tout objet
mathématique se ramène, dans ZFC, à un ensemble. De même, toute
opération sur ces objets, se rapport à des opérations ensemblistes
d'inclusion, d'appartenance, d'union et d'intersection.

ZFC est ajourd'hui admis, grâce au travaux de Bourbaki, comme le système
d'axiomes de référence.

# Théorèmes de Gödel

## Complétude et cohérence d'un système

Mais ZFC est-il parfait ? Sommes nous réellement parvenus à établir des
bases inébranlables à toutes les mathématiques ?

Pour répondre à cette question, définissons dans un premier temps les
caractéristiques nécessaires à un système d'axiomes *parfait*.

La première caractéristique est la *complétude* du système. Étant donné
une certaine affirmation $A$ formulée dans le système en question, il
doit être possible de démontrer $A$ ($A$ est alors dite *démontrable*)
ou de réfuter $A$, c'est à dire de démontrer $\neg A$ ($A$ est alors
dite *réfutable*) au sein du système d'axiomes. Aucune assertion ne doit
être *indécidable*, c'est à dire ni démontrable, ni réfutable. Un
système d'axiomes *parfait* doit être en capacité de démontrer ou de
réfuter toutes les assertions formulées dans son langage.

La seconde caractéristique est la *cohérence* du système. Un système est
*incohérent* lorsqu'une proposition peut à la fois être démontrée et
réfutée, qu'elle peut être à la fois *vraie* et *fausse*. Un tel système
est nécessairement inconsistant et ne peut donc être utilisé pour
établir une base solide à quelque théorie que ce soit. *A contrario* un
système est dit cohérent si toute affirmation $A$ est soit *vraie*, soit
*fausse* mais jamais les deux à la fois.

Intuitivement, il semble que l'incohérence d'un système apparaît
clairement dans son système d'axiomes. Mais de subtiles paradoxes
peuvent rendre incohérente une théorie pourtant joliment construite.
L'ancêtre de ZFC, une théorie axiomatique générale également basée sur
des ensembles, s'est par exemple vue entièrement détruite par un
paradoxe soulevé par Bertrand Russel. En effet, étant donné une
propriété $P$, ce système autorisait de construire l'ensemble E de tous
les objets vérifiant cette propriété $P$. Il est par exemple possible de
définir $\mathbb{R^+}$ comme l'ensemble réels supérieurs ou égaux à $0$.
Mais un problème surgit lorsque l'on considère des ensembles d'ensembles
et en particulier "l'ensemble des ensembles qui ne se contiennent pas
eux mêmes". E
appartient-il à lui-même ? Si $E$ n'appartient pas à lui-même, alors il
respecte la propriété et doit donc appartenir à lui-même. De la même
manière, si $E$ appartient à lui-même, alors il doit être supprimé
puisqu'il ne vérifie plus la propriété. Autrement dit :

$$E \in E \Longleftrightarrow E \notin E$$

Une contradiction. Ce système d'axiomes était donc *incohérent*.

Ainsi, le système d'axiomes parfait se doit d'être à la fois *cohérent*,
*complet* et capable de décrire l'ensemble des mathématiques.

## Théorèmes de Gödel

Kurt Gödel, mathématicien et logicien autrichien, publie ainsi en 1931
dans son article *Über formal unentscheidbare Sätze der Principia
Mathematica und verwandter Systeme* (« Sur les propositions formellement
indécidables des Principia Mathematica et des systèmes apparentés »),
ses théorèmes d'incomplétude, établissant qu'un système d'axiomes
parfait ne peut exister.

Le premier théorème d'incomplétude de Gödel affirme que tout système
d'axiomes suffisamment puissant pour représenter l'arithmétique est
nécessairement incomplet ou, autrement dit, pourra formuler des
affirmations *indécidables*.

Le second théorème d'incomplétude de Gödel affirme quand à lui que tout
système d'axiomes suffisamment puissant pour représenter l'arithmétique
ne peut démontrer sa propre cohérence. Un système d'axiomes peut
démontrer la cohérence d'un autre système, ou d'une restriction de
lui-même, mais pas sa propre cohérence. Étant donné que le système
d'axiomes parfait est censé représenter la totalité des mathématiques,
il apparaît absurde d'envisager de se placer dans un système plus large
pour démontrer la cohérence du premier.

Ainsi, la complétude est fondamentalement impossible, quelque soit le
système choisit, et la cohérence indémontrable, contraignant les
mathématiciens à travailler sous une épée de Damoclès, ne pouvant
qu'espérer que leurs mathématiques soient consistantes.

John Von Neumann, mathématicien américano-hongrois, sans doute l'un des
plus important de l'histoire, notamment pour sa contribution dans la
théorisation des ordinateurs (avec son *architecture de Von Neumann*)
déclara en découvrant les résultats de Gödel "C'est fini." L'espoir
d'une génération de mathématiciens d'établir des bases solides aux
mathématiques s'effondrait.

## Le cas ZFC

Qu'en est-il alors de ZFC ?

D'une part, il est peu probable que ZFC soit *incohérent*. Bien qu'il
soit impossible de prouver sa cohérence, les mathématiciens s'accordent
à dire que si ZFC était incohérent, une telle incohérence aurait déjà
été découverte, tant ZFC a été éprouvé en tout sens.

L'incomplétude, toutefois, est plus problématique. Les mathématiciens
travaillent désormais en connaissance de cause. Certains théorèmes, tels
que l'hypothèse du continu (affirmant qu'il n'existe aucun ensemble de
cardinal compris entre $\mathbb{N}$ et $\mathbb{R}$), ne peuvent être
*décidés* au sein de ZFC. Les mathématiciens doivent faire preuve
d'humilité en acceptant que certains théorèmes n'admettent pas de
démonstration.


