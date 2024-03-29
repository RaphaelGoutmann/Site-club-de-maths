---
title: Principaux résultats de théorie des nombres
author: Raphaël Goutmann & Isabella Mathias-Forni
date: 29/03/2024
hidden: true
---

[TOC]

## Introduction

La théorie des nombres, branche des mathématiques étudiant les propriétés relatives aux nombres premiers, est généralement étudiée en classe de terminal. Les principaux résultats y sont brièvement exposés, passant sous silence leur démonstration pourtant fondamentale, tant par leur esthétique mathématique que pour leur intérêt dans la compréhension profonde des concepts.

Cet article constitue donc un tour d'horizon des principaux résultats de théorie des nombres, ainsi que de leur démonstration.

Il peut être lu sans pré-requis particuliers.

## Rappels

Soit $n\in\mathbb{N}$. $n$ est dit premier si et seulement si $n$ n'est divisible que par $1$ **et** par lui-même.

En particulier, $1$ **n'est pas** un nombre premier.

Nous noterons par la suite $\mathbb{P}$ l'ensemble des nombres premiers, de sorte que : 

$$ \mathbb{P} = \{ 2, 3, 5, 7, 11, 13, 17 ... \} $$

On dit de deux entiers qu'ils sont premiers entre eux si leur seul diviseur commun est $1$. En particulier, tout nombre premier est premier avec tous les entiers inférieurs (strictement) à lui-même.

Le théorème de Bachet-Bézout affirme que deux entiers $a$ et $b$ sont premiers entre eux si et seulement si il existe deux entiers $u$ et $v$ tels que :

$$au + bv = 1$$

La factorielle d'un certain entier $n$ correspond au produit de cet entier par tous les entiers inférieurs à lui-même. Par exemple, $9! = 9 \times 8 \times \ldots \times 2 \times 1$. On admet par convention que $0! = 1$.

Soient $k$ et $n$ deux entiers. On appelle *coefficient binomial* et on note $\binom{n}{k}$ le nombre de parties (non ordonnées) de $k$ éléments dans un ensemble à $n$ éléments.

On a par définition :

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

Ces coefficients binomiaux apparaissent dans la formule du binôme de Newton affirmant que pour tout réels $a$ et $b$ et pour tout entier naturel $n$ : 

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$$

En particulier :

$$(a+1)^n = \sum_{k=0}^{n} \binom{n}{k} a^k$$

## Théorème fondamental de l'arithmétique

L'intérêt de l'étude des nombres premiers réside en ceci qu'ils sont le ciment des nombres entiers. Le théorème fondamental de l'arithmétique affirme en effet que

<div class="theorem" data-name="Théorème fondamental de l'arithmétique">
    Tout entier naturel $n$ peut s'écrire sous forme unique (à l'ordre près) comme produit de nombres premiers.
</div>

Autrement dit, les nombre premiers permettent de construire tous les nombres et ce, de manière unique.

Par exemple $20 = 2^2 \cdot 5$ ou encore $65 = 13 \cdot 5$.

La démonstration de ce théorème se décompose en deux parties : démontrer d'une part *l'existence* de cette décomposition et d'autre part *l'unicité*.

**Existence**

Soit un entier naturel $n$.

Si $n$ est premier, alors nous n'avons rien à démontrer.

Dans le cas contraire, $n$ possède des diviseurs compris entre $1$ et $n$. Posons $m$ le plus petit de ces diviseurs, il est alors premier. Si ce n'était pas le cas, il existerai un certain entier $l$ tel que : 

$$1 < l < m $$ 

et :

$$l | m$$ 

Mais puisque $l|m$ et $m|n$ nous aurions en particulier $l|n$, ce qui contredit la définition de $m$ comme étant le plus petit diviseur de $n$. Donc $m$ est nécessairement premier d'où $n$ est divisible par un nombres premier.

Nous pouvons donc réécrire :

$$n = p_1 n_1, 1 < n_1 < n$$

À nouveau, si $n_1$ est premier, la démonstration s'achève et, si il ne l'est pas, il est divisible par un nombre premier $p_2$ de sorte que :

$$n = p_1 n_1 = p_1 p_2 n_2, 1 < n_2 < n_1 < n$$

En répétant l'opération suffisamment de fois, et comme le $n_i$ restant diminue à chaque itération, nous obtenons finalement :

$$n = p_1 p_2 \ldots p_n $$

qui correspond bien à la forme recherchée. L'existence est donc prouvée.

Comme les $p_i$ ne sont pas nécessairement distincts les uns des autres, il est possible de réécrire cette forme de façon plus commode : 

$$n = p_1^{\alpha_1} p_2^{\alpha_2} \ldots p_n^{\alpha_n} $$

Nous appellerons cette forme la *forme standard* de l'entier $n$.

**Unicité**

Il est clair, d'après, la première partie de la démonstration, que si un nombre premier $p$ divise un produit de facteurs premiers $p_1 \ldots p_n$ alors $p$ est nécessairement l'un des $p_i$.

Appuyons nous sur ce résultat pour démontrer l'unicité de la *forme standard*.

Supposons par l'absurde dans un premier temps qu'il existe deux décompositions en facteurs premiers, de sorte que : 

$$n = p_1^{\alpha_1} p_2^{\alpha_2} \ldots p_k^{\alpha_k} = q_1^{\beta_1} q_2^{\beta_2} \ldots q_j^{\beta_j} $$

Puisque les deux membres sont égaux et que tout $p_i$ divise le membre de gauche, alors en particulier tout $p_i$ divise le membre de droite, de sorte que, d'après le lemme précédent, tous les $p$ sont des $q$ et, de la même manière, tous les $q$ sont des $p$. Nous avons donc $k=j$ et $p_i = q_i$ et ce, pour tout $i$.

Il reste alors à démontrer que les exposants sont eux aussi identiques, i.e que $\alpha_i = \beta_i$ pour tout $i$. Supposons par l'absurde que $\alpha_i > \beta_i$. En divisant des deux côtés par $p_i^{\beta_i}$ nous obtenons : 

$$p_1^{\alpha_1} \ldots p_i^{\alpha_i - \beta_i} \ldots p_k^{\alpha_k} = p_1^{\beta_1} \ldots p_{i-1}^{\beta_{i-1}} p_{i+1}^{\beta_{i+1}} \ldots p_{k}^{\beta_{k}}$$

Le membre de gauche est divisible par $p_i$ mais pas le membre de droite. Les deux membres étant égaux, il s'agit là d'une contradiction. Nous aurions obtenu la même contradiction en supposant $\beta_i > \alpha_i$. Nous avons donc nécessairement $\alpha_i = \beta_i$, ce qui achève la démonstration.

À noter que considérer $1$ comme un nombre premier n'aurait pas permis d'avoir une décomposition unique.

Un corollaire clair à ce théorème porte le nom de *lemme d'euclide* et affirme que :

<div class="lemma" data-name="Lemme d'Euclide">
    Soient $a$ et $b$ deux entiers et $p$ un nombre premier. Si $p|ab$ alors $p|a$ ou $p|b$.
</div>

## Infinité des nombres premiers

L'étude des nombres premiers mène rapidement à s'interroger sur leur répartition et en particulier sur leur quantité.

Euclide affirme, dans ses *Éléments* (proposition 20 du livre IX), qu'il en existe une infinité et en propose une démonstration, sans doute l'une des plus importante de l'histoire des mathématiques.

<div class="theorem" data-name="Théorème d'Euclide sur les nombres premiers">
    Il existe une infinité de nombres premiers.
</div>

Raisonnons pour cela par l'absurde.

Supposons dans un premier temps qu'il en existe un nombre fini, disons un nombre $n$. Autrement dit : 

$$\mathbb{P} = \{ p_1, p_2, \ldots, p_n \}$$

Posons alors $p = p_1 p_2 \ldots p_n + 1$.

$p$ est un entier et donc, d'après le théorème fondamental de l'arithmétique, divisible par au moins un facteur premier $p_i$.

Ainsi, $p_i | p_1 p_2 \ldots p_n $ et $p_i | p =  p_1 p_2 \ldots p_n + 1$ donc $p_i | p_1 p_2 \ldots p_n + 1 - p_1 p_2 \ldots p_n = 1$, ce qui est absurde.

Donc quelque soit la liste finie de nombres premiers donnée, il sera toujours possible d'en construire un n'appartenant pas à cette liste. $\mathbb{P}$ elle est donc nécessairement de cardinal (de taille) infini.

Une autre manière de démontrer l'infinité des nombres premiers consiste à approximer leur répartition à l'aide d'une fonction.

Considérons la fonction $\pi(x)$ de $\mathbb{N}$ dans $\mathbb{N}$ qui associe à chaque entier le nombre de nombres premiers inférieurs ou égaux à $x$.

Par exemple, $\pi(2) = 1$, $\pi(3) = 2$ et $\pi(4) = 2$.

Le théorème des nombres premiers affirme alors que

<div class="theorem" data-name="Théorème des nombres premiers">
    $$\pi(x) \sim \frac{x}{\ln(x)}$$
</div>

Ou autrement dit que
$$\lim_{x\to\infty} \pi(x) \cdot \frac{ln(x)}{x} = 1$$
La fonction $\pi(x)$ se comporte donc de façon similaire à $\frac{x}{\ln(x)}$, qui diverge clairement vers l'infini.

Nous ne nous attarderons pas plus sur le sujet.

## Lemme de Gauss

Un autre résultat fondamental de théorie des nombres est dû au mathématicien Gauss, mathématicien allemand du XIXe reconnu comme "Le Prince des mathématiques".

Le lemme de Gauss affirme que : 

<div class="lemma" data-name="Lemme de Gauss">
    Soient $a$, $b$, $c$ trois entiers. Si $a|bc$ et si $a$ et $b$ sont premiers entre eux alors $a|c$.
</div>

## Démonstration 

Soient $a$, $b$ et $c$ trois entiers relatifs. 

Supposons que $a|bc$ et que $a$ et $b$ sont premiers entre eux.

Puisque $a|bc$, il existe un certain entier $k$ tel que :

$$bc = ka$$

Par ailleurs, d'après le théorème de Bachet-Bézout (ou théorème de Bézout), et puisque $a$ et $b$ sont premiers entre eux, il existe deux entiers $u$ et $v$ tels que :

$$au + bv = 1$$

En multipliant les deux membres de l'égalité par $c$ nous obtenons :

$$cau + cbv = c$$

D'où, sachant que $bc = ka$ : 

$$cau + kav = c$$

En factorisant par $a$ nous obtenons finalement :

$$a(cu + kv) = c$$

Autrement dit, $a$ divise $c$ (ce qu'il fallait démontrer). 

## Petit théorème de Fermat

Un autre résultat fondamental en théorie des nombres, concernant cette fois-ci les congruences, est dû à Pierre de Fermat, mathématicien français sans doute le plus important dans cette branche des mathématiques.

L'énoncé du petit théorème de fermat est le suivant :

<div class="theorem" data-name="Petit théorème de Fermat">
    Soient $p$ un nombre premier et $a$ un entier naturel quelconque. Alors $a^p - a$ est divisible par $p$.
</div>

De plus, si $p$ et $a$ sont premiers entre eux alors $a^{p-1} - 1$ est divisible par $p$.

Par exemple, $8^3 - 8 = 504$ qui est divisible par $3$.

Le petit théorème de Fermat peut également être formulé de la façon suivante, faisant intervenir explicitement son lien avec les congruences :

<div class="theorem" data-name="Petit théorème de Fermat (version congruences)">
   Soient $p$ un nombre premier et $a$ un entier naturel quelconque. Alors $a^p \equiv a \pmod p$.
</div>

Et si de plus $p$ et $a$ sont premier entre eux alors $a^{p-1} \equiv 1 \pmod p$

Nous donnerons ici une démonstration due à Euler. 

Démontrons dans un premier temps un lemme dont nous aurons besoin par la suite pour démontrer le petit théorème de Fermat. 

Soient $p$ un nombre premier et $k \in \{1, \ldots, p-1 \}$ alors $p|\binom{p}{k}$.

En effet :

$$ \binom{p}{k} = \frac{p!}{k!(p-k)!} = \frac{p}{k} \times \frac{(p-1)!}{(k-1)!\left((p-1)-(k-1)\right)!} = \frac{p}{k} \binom{p-1}{k-1}$$

D'où :

$$p \binom{p-1}{k-1} = k\binom{p}{k} $$

Donc $p$ divise $k\binom{p}{k}$.

De plus, $p$ et $k$ étant premiers entre eux, nous avons, d'après le lemme de Gauss, $p|\binom{p}{k}$, ce qu'il fallait démontrer. 

Démontrons maintenant le petit théorème de Fermat. 
Nous raisonnerons pour cela par récurrence. 

On cherche donc à prouver que pour tout $a \in \{1, \ldots, p-1\}$,  $a^p \equiv a \pmod p$. Il est en effet suffisant de prouver cette affirmation pour $a \in \{1, \ldots p-1\}$ car nous raisonons ici par congruence. 

**Initialisation** : On a $0^p \equiv 0 \pmod p$, donc la propriété est initialisée.

**Hérédité**: Soit $a\in \{1, \ldots p-2\}$, supposons que $a^p \equiv a \pmod p$. Montrons que cette assertion est encore vraie pour $a+1$.

D'après le binôme de Newton,

$$(a+1)^p = \sum_{k=0}^{p} \binom{p}{k} a^k$$

Extrayons alors respectivement le premier et dernier terme de la somme ($k=0$ et $k=p$),

$$(a+1)^p = a^p + 1 + \sum_{k=1}^{p-1} \binom{p}{k} a^k$$

En passant aux congruences nous avons donc (puisque la somme est multiple de $p$ et d'après l'hypothèse de récurrence) : 

$$(a+1)^p  \equiv a + 1 + 0 \pmod p$$

Ou autrement dit : 

$$(a+1)^p  \equiv a + 1 \pmod p$$

Ce qui achève la démonstration. 

De plus, si $a$ et $p$ sont premiers entre eux alors $p|a^p-a$ implique que $p|a(a^{p-1}-1)$ et d'après le théorème de Gauss $p|a^{p-1} - 1$ ou autrement dit $a^{p-1} \equiv 1 \pmod p$, qui correspond au corollaire présenté ci-dessus.

## Le crible d'Ératosthène

Lorsque l'on cherche à lister les nombres premiers, la méthode consistant à les considérer un par un apparaît rapidement laborieuse et inefficace.

Il est toutefois très facile de construire la liste des nombres premiers inférieurs à un certain entier $N$ en utilisant un algorithme connu sous le nom de "Crible d'Ératosthène" (mathématicien grec du 2ème siècle avant J.C).

Fixons donc un certain $N\in \mathbb{N}$ et notons tous les entiers inférieurs ou égaux à N.

$$2, 3, 4, 5, 6, \ldots N$$

Le crible d'Ératosthène consiste à supprimer successivement les multiples pour ne garder que les nombres premiers.

Il se déroule comme suit :

- Entourer 2 et supprimer tous ses multiples (4, 6, 8, ...)
- Entourer 3 et supprimer tous ses multiples restants (9, 15, 21, 27, ...)
- Entourer 5 et supprimer tous ses multiples restants (25, 35, 55, 65, ...)

De manière générale, la n-ième étape consiste à entourer le dernier nombre à gauche non encore entouré et à supprimer tous ses multiples restants. 

Une fois arrivé à $\sqrt{N}$, les nombres restants sont les nombres premiers inférieurs ou égaux à $N$.

Appliquons cette méthode au cas $N = 20$.

Comme $\sqrt{20} \approx 4.7$, il nous suffira de répéter l'opération jusqu'à ce que le dernier nombre restant à gauche soit supérieur à 5.

Écrivons donc la liste des entiers inférieurs ou égaux à $N$ :

$$2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20$$

Nous supprimons donc tous les multiples de 2 (excepté lui-même) :

$$2, 3, 5, 7, 9, 11, 13, 15, 17, 19$$

Puis de 3 : 

$$2, 3, 5, 7, 11, 13, 17, 19$$

Le dernier nombre restant à gauche étant 5 ($> 
 \sqrt{20}$), la procédure est terminée.

Les nombres obtenus sont les nombres premiers inférieurs ou égaux à $20$.

## Introduction à la fonction zêta

La fonction zêta ($\zeta$) est une fonction définie pour tout réel [^1] $x$ par : 

[^1]: Il est également tout à fait possible, et c'est en réalité le cas le plus fréquent dans la littérature mathématique, de définir $\zeta$ sur $\mathbb{C}$.

$$\zeta(x) = 1 + \frac{1}{2^x} + \frac{1}{3^x} + \frac{1}{4^x} + \ldots$$

ou de manière condensée :

$$\zeta(x) = \sum_{n=1}^{+\infty} \frac{1}{n^x} $$

Par exemple, $\zeta(1) = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \ldots = +\infty$ ou $\zeta(2) = 1 + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \ldots = \frac{\pi^2}{6}$ .

Cette fonction revêt d'une importance toute particulière pour son lien avec les nombres premiers.

En effet :

$$\zeta(x) = \prod_{p\in\mathbb{P}} \frac{1}{1-p^{-x}} $$

Autrement dit, un produit infini faisant intervenir l'ensemble des nombres premiers peut s'évaluer comme image de la fonction zêta.

**Démonstration**

Soit $x$ un nombre réel.

On a :

$$\zeta(x) = 1 + \frac{1}{2^x} + \frac{1}{3^x} + \frac{1}{4^x} + \frac{1}{5^x} + \frac{1}{6^x} + \frac{1}{7^x} + \frac{1}{8^x} + \frac{1}{9^x} + \ldots$$

En divisant par $2^x$ des deux côtés de l'égalité nous obtenons :

$$ \frac{\zeta(x)}{2^x} = \frac{1}{2^x} \left( 1 + \frac{1}{2^x} + \frac{1}{3^x} + \frac{1}{4^x} + \frac{1}{5^x} + \frac{1}{6^x} + \frac{1}{7^x} + \frac{1}{8^x} + \frac{1}{9^x} + \ldots \right) $$

d'où :

$$\frac{\zeta(x)}{2^x} = \frac{1}{2^x} + \frac{1}{4^x} + \frac{1}{6^x} + \frac{1}{8^x} + \ldots $$

En soustrayant la deuxième égalité à la première nous obtenons :

$$\left( 1 - \frac{1}{2^x} \right) \zeta(x) = 1 + \frac{1}{3^x} + \frac{1}{5^x} + \frac{1}{7^x} + \frac{1}{9^x} \ldots$$

Observons ici que les dénominateurs pairs (multiples de 2) ont été supprimés.

Répétons l'opération en divisant l'égalité obtenue par $3^x$ :

$$\frac{1}{3^x} \left( 1 - \frac{1}{2^x} \right) \zeta(x) = \frac{1}{3^x} + \frac{1}{9^x} + \frac{1}{15^x} + \frac{1}{21^x} + \frac{1}{27^x} \ldots$$

En soustrayant à nouveau cette égalité à l'égalité de départ nous obtenons :

$$\left(1-\frac{1}{3^x} \right)\left( 1 - \frac{1}{2^x} \right) \zeta(x) = 1 + \frac{1}{5^x} + \frac{1}{7^x} + \frac{1}{11^x} + \frac{1}{13^x} \ldots$$

Nous avons cette fois-ci supprimés les dénominateurs multiples de $3$.

Il apparaît alors clair que cette procédure est celle du crible d'Ératosthène.

En répétant le processus à l'infini nous obtenons finalement :

$$\zeta(x) \left( 1 - \frac{1}{2^x} \right) \left(1-\frac{1}{3^x} \right) \left(1-\frac{1}{5^x} \right) \ldots  = 1$$

D'où nous pouvons extraire $\zeta$ :

$$\zeta(x) = \frac{1}{\left( 1 - \frac{1}{2^x} \right) \left(1-\frac{1}{3^x} \right) \left(1-\frac{1}{5^x} \right) \ldots}$$

Soit de façon condensée

$$\zeta(x) = \prod_{p\in\mathbb{P}} \frac{1}{1-p^{-x}} $$

## Annexe

Voici quelques ressources pour approfondir le sujet.

Chacune d’entre elle est précédée d’un certain nombre d’étoiles suivant sa complexité, allant d’une étoile (\*) pour les plus faciles à trois étoiles (\*\*\*) pour les plus complexes : 

- (***) Une vidéo d'introduction à la fonction zêta et à la conjecture de Riemann [Devenir RICHE grâce aux maths (La fonction Zeta de Riemann) — Axel Arno](https://www.youtube.com/watch?v=KKoxMe2T7zo)
    
- (***) Un livre de référence en théorie des nombres [An Introduction To The Theory Of Numbers — G. H. Hardy](https://www.amazon.com/Introduction-Theory-Numbers-G-Hardy/dp/0199219869)

