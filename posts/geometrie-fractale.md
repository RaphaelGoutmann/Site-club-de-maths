---
title: Introduction à la géométrie fractale
author: Raphaël Goutmann & Louise Marsollier & Lucas Pessard
date: 01/03/2024
hidden: true
---

[TOC]

> “Les nuages ne sont pas des sphères, les montagnes ne sont pas des cônes, les rivages ne sont pas des arcs de cercle, l'écorce d'un arbre n'est pas lisse et l'éclair ne trace pas de ligne droite. La nature est complexe et la géométrie fractale rend compte de cette complexité et permet de l'étudier.” — Benoît Mandelbrot

## Introduction 

Au X-ième siècle, apparaissent en mathématiques des objets pour le moins... étranges... Infiniment complexes, ils bouleversent la géométrie  euclidienne en vigueur jusqu'à lors amenant progressivement au développement d'une nouvelle théorie géométrique, la *géométrie fractale*. 

Le but de cet atelier est de présenter les principaux objets fractales rencontrés en mathématiques et de définir le plus clairement possible ce terme. Cette étude nous donnera l'occasion d'appréhender une nouvelle branche des mathématiques, l'analyse complexe.

## La fonction de Weierstrass

En 1872, le mathématicien Allemand Karl Weierstrass présente à l'académie prussienne des sciences ce qui sera plus tard considéré comme le premier exemple de fractale. La *fonction de Weiestrass* se distingue en ceci qu'elle qu'elle est continue partout mais dérivables nul part. 

Elle est définit comme suit :
$$ f(x) = \sum_{n=1}^{+\infty} b^n \cos(a^nx\pi) $$

où $a$ est un entier impair, $b \in \left[0, 1\right[$ et $ab > 1 + \frac{3}{2} \pi$

Outre ces considérations purement *analytiques*, son graphe présente d'étranges propriétés géométriques.

![Représentation graphique de la fonction de Weierstrass](img/weierstrass.png)

La fonction apparaît en effet infiniment détaillée et présente surtout une remarquable *auto-similarité*. Agrandir le graphe sur un point précis dévoile systématiquement une version plus petite du graphe global et ce à l'infini.

## Les poussières de Cantor

Moins d'une décennie plus tard, le mathématicien Allemand Georg Cantor présente une autre construction autrement plus simple mais aux propriétés similaires : *les poussières de Cantor*.

Considérons le segment $C_0 = [0,1]$.

À la première étape nous divisons notre segment en trois parties égales ($[0, \frac{1}{3}], [\frac{1}{3}, \frac{2}{3}], [\frac{2}{3}, 1]$) et supprimons la partie centrale.  La figure ainsi obtenue correspond au segment $C_1 = [0, \frac{1}{3}] \cup [ \frac{2}{3}, 1]$

![Étapes de construction des poussières de Cantor](img/cantor-set.png)

De façon similaire, à la deuxième étape, nous divisons chacun des segments obtenus en trois parties et retirons celles du milieu, pour finalement aboutir au segment $C_2$ à 4 morceaux. 

De manière générale, pour passer du segment $C_k$ au segment $C_{k+1}$, nous divisions en $3$ les $2^k$ morceaux obtenus à l'étape $C_k$ et retirons les parties du milieu, obtenant ainsi $2^{k+1}$ morceaux.

Il s'agit là d'une construction dite "itérative" où le résultat de chaque étape sert de matériaux à l'étape suivante. 

Les poussières de Cantor sont alors obtenues en réalisant cette procédure un nombre infini de fois ou, de manière plus formelle :

$$ C = \bigcap_{i=1}^{+\infty} C_i $$ 

[^1]

[^1]: Le symbole $\bigcap$ est l'équivalent du symbole $\sum$ pour l'intersection. Ainsi, $\bigcap_{i=1}^{+\infty} = C_1 \cap C_2 \cap C_3 \cap C_4 \ldots $

Une nouvelle fois, l'ensemble de Cantor présente la propriété d'auto-similarité (ce qui apparaît d'ailleurs clairement dans sa définition).


## Le flocon de Von Koch

Le mathématicien suédois Helge von Koch publie en 1904 ce qui sera appelé plus tard la *courbe de Von Koch*. 

Cette fractale reprend la construction itérative des poussières de Cantor tout en présentant les propriétés de continuité et de non dérivabilité de la fonction de Weierstrass. 

Partons  d'un segment $V_0$ d'une unité de longueur. 

Pour passer à l'étape suivante, nous découpons $V_0$ en trois parties, retirons la partie centrale et plaçons de part et d'autre du trou ainsi formé des segments de même longueurs que la partie retirée de sorte à former un triangle équilatéral. Nous obtenons alors $V_1$

![Étapes de construction du flocon de Von Koch](img/von-koch.png)

De la même manière, pour passer de l'étape $V_1$ à $V_2$, nous appliquons à chaque segment de $V_1$ cette même transformation. 

De façon générale, en notant $f$ la fonction qui à une certaine étape associe l'étape suivante et en notant $f^k$ la composée k-ième de f, [^2] la *courbe de Von Koch* V est : 

[^2]: de sorte que $f(V_0) = V_1$, $f(V_1) = f^2(V_0) = V_2$ et, de manière générale $f^k(V_0) = V_k$

$$V = \lim_{k \rightarrow +\infty} \left(f^k(V_0)\right)$$

À nouveau, et par construction, la courbe de Von Koch présente cette propriété d'auto-similarité. 


## Le triangle de Sierpinski

Le mathématicien Polonais Waclaw Sierpinski découvre en 1915 le triangle de Sierpinski. 

Partons d'un triangle équilatéral plein $S_0$.

Pour passer à l'étape suivante, nous traçons le triangle équilatéral reliant les milieux des côtés de $S_0$  et supprimons le triangle ainsi formé. Nous obtenons alors $S_1$ composé de 3 copies de $S_0$ réduites d'un facteur 2. 

![Étapes de construction du triangle de Sierpinski](img/sierpinski-triangle.png)

De manière générale, pour passer de $S_k$ à $S_{k+1}$, nous supprimons le triangle central des $3^k$ triangles restants, donnant ainsi à naissance à $3^{k+1}$ triangles. 

En notant $f$ la fonction permettant de passer de l'étape $S_k$ à l'étape $S_{k+1}$, le triangle de Sierpinski S est alors définit comme : 

$$ S = \lim_{k \to+\infty} \left(f^k(S_0)\right) $$

À nouveau, le triangle de Sierpinski présente, par construction, cette propriété d'auto-similarité. 

## Fractales Aléatoires

Il est également possible de générer des fractales de façon aléatoire / stochastique. Ce type de modèle est en particulier utilisé dans la modélisation de phénomènes physiques où la "régularité" des méthodes précédentes ne permet pas de représenter correctement les réalités du monde réel. 

L'une des fractales aléatoires les plus simples consiste en une généralisation d'une fractale déterministe, le "tapis de Sierpinski". 
Considérons un carré $C_0$ de côté $1$. 

À la première étape, nous découpons $C_0$ en 9 sous-carrés égaux de côtés $\frac{1}{3}$. Nous fixons alors une probabilité $0 < p < 1$ et choisissons de supprimer chacun des sous-carrés selon cette probabilité. De la même manière, pour passer de $C_1$ à $C_2$, nous découpons chacun des sous-carrés restants en 9 parts égales et répétons pour chacun d'entre eux cette expérience aléatoire. 

De manière générale, en notant $f$ la fonction permettant de passer de l'étape $C_k$ à l'étape $C_{k+1}$ , \textbf{un} tapis de Sierpinski associé à la probabilité $p$ correspond alors à : 

$$ T = \lim_{n\to+\infty} f^k(C_0)$$

![Trois exemples de tapis de Sierpinski aléatoires](img/random-sierpinski-carpet.png)

La notion de fractales aléatoires est par exemple particulièrement utile en informatique dans la génération de paysages aléatoires. 
Pensons par exemple au jeu vidéo minecraft dont la structure du monde peut s'apparenter à un objet fractale. 

## Définition d'une Fractale

Avec tous ces exemples en tête, il est désormais possible d'approcher une définition du concept de "fractale" comme possédant une ou plusieurs des propriétés suivantes : 

- Présence de détails à une échelle arbitrairement petite ;
- Une structure trop irrégulière pour être décrite avec les outils de la géométrie traditionnelle ; 
- Propriété d'auto-similarité

Par ailleurs, il est possible de distinguer dans ce large éventail d'objets mathématiques trois "catégories" générales de fractales : 

- Fractales aléatoires (telles que le tapis de Sierpinski aléatoire) 
- Fractales construites sur des fonctions itérées (telles que le flocon de Von Koch, les poussières de Cantor etc.) 
- Fractales construites sur des relations de récurrences (telles que les ensembles de julia et l'ensemble de Mandelbrot)

## Les ensembles de Julia

Les mathématiciens français Pierre Fatou et Gaston Julia développent au début du XXe siècle une nouvelle branche des mathématiques, la dynamique holomorphe, ouvrant la porte à de nouvelles constructions fractales, parmi lesquelles les ensemble de Julia et de Fatou. 

Il s'agit de deux ensembles complémentaires définis dans un cadre très large que nous restreindront à un cas particulier. 

Considérons la suite à valeurs complexes $(z_n)$ telle que $z_0 \in \mathbb{C}$ et
$$z_{n+1} = z_n^2 + c$$
Pour $c\in\mathbb{C}$ fixé, les différentes valeurs de $z_0$ peuvent donner naissance soit à une suite bornée soit à une suite dont les termes tendent progressivement vers l'infini. 

L'ensemble de Julia pour un certain $c\in\mathbb{Z}$ est alors définit comme *la frontière* de l'ensemble des $z_0 \in \mathbb{C}$ tels que la suite $(z_n)$ associée est bornée. 

Il est alors possible de représenter cet ensemble dans le plan en coloriant d'une certaine couleur les points de l'ensemble, et d'une autre les points du complémentaire. Mieux encore, nous pouvons étudier la vitesse avec laquelle la suite diverge vers l'infini et colorier les points du complémentaire selon cette valeur. 

![Ensemble de Julia pour $c = 0,3 + 0,5 i$.](img/julia-1.png)
![Ensemble de Julia pour $c = 0,285 + 0,01 i$.](img/julia-2.jpg)
![Ensemble de Julia pour $c = –1,41 + 0,010 i$.](img/julia-3.jpeg)
![Ensemble de Julia pour $c = –0,038 + 0,975 i$.](img/julia-4.jpeg)
![Ensemble de Julia pour $c = −0,4 + 0,6 i$](img/julia-5.png)
![Ensemble de Julia pour $c = −0,8+0,156 i$.](img/julia-6.png)
![Ensembles de Julia pour différentes valeurs de c.](img/julia-7.png)



L'ensemble de Julia dépend de la valeur de $c$ choisie. Nous pourrions dès lors imaginer faire varier ce paramètre, obtenant ainsi un "film", dont chaque image représente un ensemble de julia pour un certain paramètre $c\in\mathbb{C}$.

<video controls width="100%">
  <source src="https://upload.wikimedia.org/wikipedia/commons/transcoded/9/9b/Julia-noe-cercle.ogg/Julia-noe-cercle.ogg.720p.vp9.webm" type="video/webm" />
</video>

## Ensemble de Mandelbrot


L'ensemble de Julia est une fractale, en ce sens qu'elle présente une structure infiniment détaillée (sans pour autant être auto-similaire). 

De la notion d'ensemble de Julia naît celle d'ensemble de Mandelbrot, du nom du mathématicien polono-franco-américain Benoît Mandelbrot. 


Plutôt que d'observer le comportement de $(z_n)$ lorsque l'on fait varier $z_0$, on se propose ici de fixer $z_0 = 0$ et de faire varier le paramètre $c$. De la même manière que précédemment, l'ensemble de Mandelbrot peut alors être définit comme l'ensemble de toutes les valeurs de $c$ pour lesquelles la suite $z_n$ est bornée, en posant $z_0 = 0$. 

Dans ce contexte, chaque point du plan complexe est associé à une fractale de Julia. En particulier, il est possible de démontrer qu'un point $z\in\mathbb{C}$ appartient à l'ensemble de Mandelbrot si et seulement si la fractale de Julia associée est connexe, i.e d'un seul morceau. 

À nouveau, il est possible de tracer l'ensemble de Mandelbrot dans le plan, en faisant varier les couleurs des points du complémentaire suivant leur vitesse de divergence. ([explorer l'ensemble de mandelbrot](https://mandel.gart.nz/))

![Ensemble de Mandelbrot](img/mandelbrot.jpeg)

Contrairement aux ensembles de Julia, l'ensemble de Mandelbrot présente la propriété (ultime) d'auto-similarité. Il est alors possible de retrouver dans l'ensemble de Mandelbrot un version miniature mais strictement identique à l'ensemble global. 

La construction de l'ensemble de Mandelbrot peut se généraliser en prenant comme suite support non plus $z^2 + c$ mais $z^d + c$ avec $d > 2$. Nous obtenons alors des "multibrot". 

![Multibrot associé à la puissance 3](img/multibrot-3.png)
![Multibrot associé à la puissance 4](img/multibrot-4.png)
![Multibrot associé à la puissance 5](img/multibrot-5.png)
![Multibrot associé à la puissance 6](img/multibrot-6.png)


## Annexe

Voici quelques ressources pour approfondir le sujet.

Chacune d’entre elle est précédée d’un certain nombre d’étoiles suivant sa complexité, allant d’une étoile (\*) pour les plus faciles à trois étoiles (\*\*\*) pour les plus complexes : 

- (*) Une vidéo d'introduction au concept de fractales [Les fractales - Mickaël Launay](https://www.youtube.com/watch?v=iFA3g_4myFw)
- (**) Une vidéo sur les fractales de Julia et l'ensemble de Mandelbrot [Deux (deux ?) minutes pour Mandelbrot — El Jj](https://www.youtube.com/watch?v=Y4ICbYtBGzA)
- (***) La page Wikipedia consacrée aux ensembles de Julia [Ensemble de Julia — Wikipedia](https://fr.wikipedia.org/wiki/Ensemble_de_Julia)
- (***) La page Wikipedia consacrée à l'ensemble de Mandelbrot [Ensemble de Mandelbrot — Wikipedia](https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot)
- (**) La page Wikipedia consacrée à la notion de Fractales [Fractales — Wikipedia](https://fr.wikipedia.org/wiki/Fractale)
- (***) Une conférence sur les fractales aléatoires [Vincent Beffara, Fractales aléatoires — Institut Henri Poincaré](https://www.youtube.com/watch?v=klaTVO7u5-M)
- (***) Un papier introduisant les concepts mathématiques sous-jacents à la théorie des fractales (en anglais) [Introduction to Fractals and Julia Sets — Fergus Cooper](https://www.cs.ox.ac.uk/people/fergus.cooper/site/publications/2011Cooper_IntroductionToFractals.pdf)