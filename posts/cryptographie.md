---
title: Introduction à la cryptographie
author: Raphaël Goutmann & Louise Marsollier
date: 01/12/2023
tags: Mathématiques Informatique Cryptographie
---

[TOC]

## Qu’est ce que la cryptographie ? 

La cryptographie est l’art de chiffrer des informations. 

Elle a pour but principal de permettre le transfert d’une information d’une personne A à une personne B sans qu’une tierce personne ne puisse la lire et la comprendre. Elle est utilisée de nos jours pour sécuriser les communications sur internet, protégeant la vie privée des utilisateurs et évitant toute sorte de piratage.

## Modes de chiffrements "intuitifs"

La cryptographie est apparue bien avant l’informatique (ex: tablette d’argile qui à été retrouvée en mésopotamie (-1500), ou la scytale spartiate durant l’antiquité). 

L’un des premiers systèmes de chiffrement de l’histoire a été conçu par César lui-même pour permettre des communications sécurisées avec ses armées. Lorsque l'empereur leur transmettait des messages, il était en effet essentiel qu’en cas d’interception par un ennemi, celui-ci ne puisse en exploiter des informations stratégiques qui pourraient compromettre l’empire romain.

Ce procédé, dit “chiffrement de César” est particulièrement simple à mettre en œuvre. Admettons que Bruno souhaite transmettre un message à Alice, disons le mot “bonjour”. Il commence par s’accorder avec Alice sur une clé secrète, correspondant à un entier k compris entre 1 et 26 puis décale chaque lettre composant son message de k rang dans l’alphabet. Si Alice et Bruno se s’accordent sur une clé k = 2, le message “bonjour” se chiffre alors en “dqplqwt”. Pour déchiffrer ce message, il suffit de répéter le processus dans le sens inverse en décalant les lettres du message chiffré d’un rang -k. 

Le chiffrement César présente toutefois une sécurité très faible. Il existe en effet 26 choix possibles de clés. Un tiers malveillant ayant intercepté le message et ayant connaissance du système utilisé pourrait alors tester toutes les possibilités de clés et déchiffrer le message en un rien de temps. On dit alors que l’espace de clés (c'est-à-dire l’ensemble des clés possibles) est petit. 

Un autre système de ce type est le chiffrement par substitution. On associe cette fois-ci à chaque lettre une autre lettre en laquelle elle sera transformée. La clé à communiquer est alors une table des correspondances entre les différentes lettres et le décryptage se fait en partant des lettres d’arrivées pour revenir sur les lettres de départ. 

L’avantage de ce système, outre sa simplicité, est son espace de clés gigantesque.
Lorsque nous construisons la clé, nous commençons par la lettre A. Nous avons alors 26 choix de correspondances possibles. Une fois choisi, nous avons 25 possibilités pour la lettre B, 24 pour la lettre C etc. Le nombre de choix possibles est alors de 26 x 25 x 24 x … x 2 x 1 = 26! (26 “factorielle”) soit près de 4 x 10^26 clés. Avec un espace de clés si vaste, même les ordinateurs les plus puissants dont nous disposons actuellement seraient incapable de toutes les tester. La méthode d’attaque vue précédemment dans le cas du chiffrement César ne peut donc être utilisée. 

Le chiffrement par substitution présente toutefois une faille majeure. Chaque lettre est toujours chiffrée de la même manière. Si je décide d’associer la lettre A à la lettre Y, chaque A du message initial apparaîtra sous forme de Y dans le message chiffré. Mais dans une langue donnée, toutes les lettres n’apparaissent pas selon la même fréquence. Le E, par exemple, est la lettre la plus souvent rencontrée dans la langue française, loin devant le S, le A etc. En analysant les fréquences des différentes lettres et en usant d’un peu de bon sens, nous pouvons donc déchiffrer le message.

## Enigma et Turing 

La machine Enigma a été inventée par l'ingénieur électricien allemand Arthur Scherbius, d’après un brevet de l'inventeur néerlandais Hugo Koch déposé en 1919. C’est une machine qui permet, à travers plusieurs réglages, de crypter des messages. Pour pouvoir décrypter le message, il faut disposer d’une autre machine enigma . Elle est largement utilisée par les allemands durant la seconde guerre mondiale et attire l’attention des services secrets français et polonais, qui parviennent à tordre certains de ses secrets. Pour autant, l’armée allemande réussit à complexifier encore davantage sa machine, en changeant de protocole : elle augmente notamment le nombre de rotors et donc de transpositions, rebouchant la faille identifiée auparavant par les chercheurs.
Les américains vont à leur tour essayer de résoudre tous ces mystères en lançant  l’opération "Ultra".  Sept mille personnes s'attèlent à cette tâche dans le manoir de Bletchley Park, parmi lesquelles le mathématicien Alan Turing.
Ils font notamment construire d'énormes engins électromécaniques appelés "bombes" qui 
permettent ainsi de tester toutes les clés de chiffrement possible, en essayant en parallèle jusqu’à vingt mille configurations par seconde.
Alan Turing parviendra finalement à “casser” Enigma, permettant aux alliés d’intercepter les communications ennemies. Cette prouesse technologique leur donnera un avantage considérable, réduisant - d’après certains historiens - la guerre de près de 2 ans et sauvant par la même occasion des millions de vies. Alan Turing, condamné quelques années plus tard pour son homosexualité, sera retrouvé mort le 7 juin 1954 avec à ses côtés une pomme, probablement un suicide. Il laissera derrière lui une œuvre mathématique considérable à l’origine, entre autres, de l’ordinateur moderne et de l’intelligence artificielle.

## Cryptographie asymétrique

Les systèmes de cryptographie que nous venons de voir nécessitent le partage d’une clé. Toute la sécurité du système repose donc sur ce partage qui ne peut être parfaitement invulnérable. Le problème est d’autant plus important sur internet où le partage d’une clé ne peut se faire physiquement et impose donc de partager la clé par réseau, les interlocuteurs s'exposent - de fait - au risque qu’un pirate intercepte la clé et puisse déchiffrer les futurs messages. 

Une solution à ce problème est l’utilisation d’un chiffrement dit “asymétrique”. Le principe de ce système repose sur l’utilisation d’un chiffrement “à sens unique”. 

Pour communiquer avec Bruno, Alice commence par générer deux clés : une clé publique qu’elle partagera librement à Bruno et une clé privée qu’elle gardera pour elle. Bruno chiffre ensuite son message avec la clé publique partagée par Alice à l’aide d’un chiffrement à sens unique. La particularité d’un tel chiffrement est que la clé pour chiffrer un message et celle pour le déchiffrer est différente. Ainsi, une fois le message chiffré avec la clé publique dont dispose Bruno, seule Alice disposant de sa clé privée pourra le déchiffrer. Bruno peut ainsi librement envoyer son message sur internet sans craindre d’être intercepté puisque seule la clé privée d’Alice (qu’elle a gardée secrète) permet de le déchiffrer. Si Alice souhaite à son tour envoyer un message à Bruno, il suffit de réitérer le processus dans l’autre sens : Bruno génère une clé publique et une clé privée, partage sa clé publique, Alice l’utilise pour chiffrer son message, l’envoie sur internet, Bruno l’intercepte et le déchiffre avec sa clé privée.

Bien que les processus mis en œuvre derrière de tels chiffrement soient assez complexes, il est facile d’en saisir intuitivement le fonctionnement. 

Prenons le nombre 15. Il est relativement aisé d’en déterminer la factorisation en nombre premiers : 3 x 5. De même, une fois les facteurs premiers trouvés, il est très facile de retrouver le nombre de départ (une simple multiplication suffit) : 3 x 5 = 15. Mais admettons que nous prenions des nombres plus grands, bien plus grands, gigantesques même avec plusieurs centaines de chiffres. La seule méthode dont nous disposions pour décomposer ce nombre en produit de facteurs premiers est de tester toutes les possibilités. Cette décomposition, facile pour de petits nombres, devient alors terriblement complexe. Même les ordinateurs les plus puissants dont nous disposions auraient besoin de plusieurs milliards d’années pour déterminer cette décomposition. Toutefois, disposant des facteurs, il est toujours très facile de retrouver le nombre initial. Il suffit de calculer une simple multiplication, réalisable en quelques secondes par un ordinateur. Le processus est donc rapide dans un sens et lent dans l’autre. Il est “facile” de multiplier et “complexe” de décomposer. Et c’est là dessus que repose le chiffrement asymétrique. Le chiffrement à l’aide de la clé publique est un processus “facile” mais le déchiffrement de ce même message à l’aide de la clé publique est “complexe” à moins de disposer de la clé privée qui agit comme une “trappe” secrète pour retrouver le message initial. (voir ce lien pour plus de détails sur le chiffrement RSA, principale système de chiffrement asymétrique)

## Annexe

Voici quelques ressources pour approfondir le sujet. 

Chacune d’entre elle est précédée d’un certain nombre d’étoiles suivant sa complexité, allant d’une  étoile (\*) pour les plus faciles à trois  étoiles (\*\*\*) pour les plus complexes.

- (\*\*) Pour en savoir d'avantage sur le chiffrement César et sa formalisation mathématique (avec en bonus une implémentation du système en Python). [Exo7Math — Cryptographie - partie 1 : chiffrement de César](https://www.youtube.com/watch?v=g8RmT-CwTMo&list=PL024XGD7WCIEii2U_HKeprCTJA4xb-uJ6&index=2)


- (\*\*) Pour en savoir plus sur le chiffrement par substitution et un chiffrement semblable dit "de Vigenère" ainsi que leur formalisation mathématique. [Exo7Math — Cryptographie - partie 2 : chiffrement de Vigenère](https://www.youtube.com/watch?v=rUlqxHGKJ68&list=PL024XGD7WCIEii2U_HKeprCTJA4xb-uJ6&index=3)

- (\*\*) Pour un savoir plus sur le principe de cryptographie à clé publique / asymétrique et sa formalisation mathématique. [Exo7Math — Cryptographie - partie 4 : cryptographie à clé publique](https://www.youtube.com/watch?v=6KfJXl-Kvws&list=PL024XGD7WCIEii2U_HKeprCTJA4xb-uJ6&index=5)

- (\*\*\*) Pour comprendre en profondeur le fonctionnement du chiffrement RSA, l'un des principaux système de chiffrement asymétrique. RSA est particulièrement complexe, c'est pourquoi deux vidéos vous sont proposées : une présentation des outils arithmétiques utilisés dans la conception de RSA et le système en lui même.
	- Partie 1 (outils arithmétiques pour RSA) : [Exo7Math — Cryptographie - partie 5 : arithmétique pour RSA](https://www.youtube.com/watch?v=M7vOxKVLsVY&list=PL024XGD7WCIEii2U_HKeprCTJA4xb-uJ6&index=6)
	- Partie 2 (chiffrement RSA en tant que tel) : [Exo7Math — Cryptographie - partie 6 : chiffrement RSA](https://www.youtube.com/watch?v=Xlal_d4zyfo&list=PL024XGD7WCIEii2U_HKeprCTJA4xb-uJ6&index=7)


- (\*\*) Pour comprendre le principe général de la Blockchain (à l'origine notamment des cryptomonnaies), largement basé sur la cryptographie. [Maths Adultes — Blockchain : Comment ça marche ?](https://www.youtube.com/watch?v=SccvFbyDaUI)

- (\*) Pour en connaitre davantage sur Alan Turing, le film *Imitation Game*. Sans doute l'un des meilleurs films de mathématiques jamais réalisé.

- (\*) Pour découvrir le mystère qui entoure Satoshi Nakamoto, à l'origine d'une révolution mathématique et économique en ayant créé la Blockchain et le Bitcoin. Sans doute l'un des meilleurs reportages Arte jamais réalisé. [Arte — Le mystère Satoshi : enquête sur l'inventeur du bitcoin](https://www.youtube.com/watch?v=0ETcLj5jBy4)

