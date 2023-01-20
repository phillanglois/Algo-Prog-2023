

**Trier**





Trier : une longue histoire

Rappel de la séance 3

Trier = classer, ordonner des valeurs, des objets

\- trier des copies par notes

\- trier des copies par ordre alphabétique des candi

\- trier des livres dans une bibliothèque

\- trier des containers sur un port

Un pre

e :

Version 2018 (PhL).





Tri avec comparaisons, tri sans

comparaison

Trier => comparer des valeurs 2 à 2 ... toujours ?

trier des copies par note croissante avec le tri par insertion-

permutation

je compare et j'ordonne (en permutant) les deux premières copies. J'insère

la troisième copie de sorte que les 3 premières copies soient correctement

ordonnées. J'insère la copie suivante (4ème) de sorte que ces premières

copies soient correctement ordonnées ... et je répète ce traitement jusqu'à

insérer la dernière copie à sa bonne place

il est possible de trier des valeurs sans les comparer

trier des copies, notées de 0 20, par note croissante

... avec un tri par dénombrement :

je "prépare" 21 boites numérotées de 0 à 20, et je répartie successivement

chaque copie dans la boite correspondant à sa note, puis j'empile

successivement les copies des boites 0, 1, ... , 19, 20.

Version 2018 (PhL).

3





Tris par comparaison et tris par comparaison rapides

Tris "lents"

je compare et j'ordonne (en permutant) les deux premières copies. J'insère la

troisième copie de sorte que les 3 premières copies soient correctement ordonnées.

J'insère la copie suivante (4ème) de sorte que ces premières copies soient

correctement ordonnées ... et je répète ce traitement jusqu'à insérer la dernière

copie à sa bonne place

\- tri par sélection, tri par insertion, tri-bulle, ...

\- complexité en temps quadratique dans le pire cas ou en moyenne

**= O(n2) comparaisons**

\- tris en place : complexité en espace = O(1)

Morale : faciles à implanter, efficace pour des petites tailles (n<15)

Tris rapides

\- tri fusion, tri rapide (\*), tri par ABR, tri par tas ...

\- complexité en temps semi-logarithmique dans le pire cas ou en moyenne (\*)

**= O(n . log(n)) comparaisons**

\- complexité en espace facilement plus gourmande

Morale : efficacité **optimale**

à on ne peut pas faire mieux !

Version 2018 (PhL).

4





Suite (aussi dans notebook python)

Tri par insertion

\- principe, exemple

\- algorithme

\- correction : invariant de boucle

Diviser-pour-régner à Tri fusion

\- principe, exemple

\- algorithme

\- correction : récurrence

Tri rapide : quicksort

\- principe, exemple

\- algorithme

\- complexité : pire cas vs. en moyenne

Version 2018 (PhL).

5





Tr i par insertion

comme exemple de tri en place et de complexité quadratrique

Version 2018 (PhL).

6





Trier des cartes

Exemple en pratique : trier une main de cartes.

Vocabulaire :

\- une **main de cartes** est l'ensemble des cartes que je tiens dans

ma main. Le nombre de cartes d'une main est variable selon les

jeux, les moments du jeu, ...

\- trier => ordre. il existe plusieurs ordres pour trier une main de

cartes : couleurs, valeurs, peut dépendre du jeux, ...

Lorsqu'on parle de tri sur des cartes et que rien n'est mentionné,

on suppose un jeu de cartes d'une seule couleur et de n valeurs

différentes et uniques.

**Trier ... par ordre croissant des valeurs** (par exemple) :

\- au début, ma main contient aucune carte

\- je reçois une carte, l'une après l'autre et je veux la ranger en

ordre dans ma "main"

\- une fois la main complète (n cartes), les cartes sont rangées par

ordre croissant : chaque carte est plus grande que sa voisine de

gauche (si elle existe), et plus petite que sa voisin de droite (si

elle existe)

Version 2018 (PhL).

7





Tri par insertion

Principe :

\- je parcours la partie triée de la main de cartes

\- et j'insère à sa bonne place la carte à classer

Remarque : il est difficile d'être exhaustif et précis avec cette description en

français

\- je parcours : il faut décider d'un début et d'un sens de parcours

. de la carte la plus à gauche jusqu'à la dernière la plus à droite à gauche -> droite

. ce sens est celui des cartes à classer

. le contraire est possible

\- j'insère : pour insérer la carte, je fais de l'espace à l'endroit où je vais la ranger

. je rend un espace disponible avec la carte à ranger,

. puis je déplace les cartes une à une vers la droite à droite -> gauche ... pourquoi

ce sens ?

. jusqu'à que l'espace (qui se déplace vers la gauche) permette l'insertion à la bonne

. autre solution possible

place

\- la bonne place :

Version 2018 (PhL).

8

la position du placement est-elle définitive ?





Tri par insertion

De l'analyse du cas abstrait à l'algorithme :

\- tas de cartes, main de cartes : définir une structure de données adaptée

\- cartes, valeurs : choisir un type adapté

un tableau d'entiers ... sa taille ? son initialisation ?

\- taille : le nombre total de cartes

\- initialisation : toutes les cartes sont présentes dans le tableau avant le début

du tri

\- ordre ... naturel sur les entiers : ≤

\- parcours :

\- parcours principal : itérer avec for sur tous les indices du tableau

\- parcours interne sur le sous-tableau déjà trié :

. itérer avec while jusqu’à la bonne place

Déf: le tri par insertion est un tri en place :

\- on utilise qu'un seul tableau, celui des valeurs à trier

\- sa complexité en espace (supplémentaire) est constante : elle est en O(1)

Version 2018 (PhL).

9





Suite sur notebook python

• algorithme

• pire cas et meilleurs cas

• expérimentations :

• décompte du nombre de comparaisons

Version 2018 (PhL).

10





Tr i rapide quicksort

comme premier exemple de tri récursif très efficace en pratique

Version 2018 (PhL).

11





Principe

Ranger une valeur à sa place définitive

• toutes celles à sa gauche sont plus petites

• toutes celles à sa droite sont plus grandes

• ces sous-tableaux gauche et droit ne sont pas (encore) triés

Récursion

• on place correctement une des valeurs du tableau, en t[p] par

exemple

• le tableau initial t[0..n] est partagé en 2 sous-tableaux :

t\_gauche[0.. p-1] et t\_droit[p+1 .. n]

• et on trie chacun de ces sous-tableaux en appliquant le même

principe

àrécursion

• terminaison : quand on a un sous-tableau trié

le sous-tableau est de taille 1 : réduit à 1 élément

Version 2018 (PhL).

12





Quicksort : étape 1

**Placer correctement une des valeurs du tableau, en t[p] par**

**exemple**

• choisir une valeur : un pivot

par exemple v = t[0]

• parcourir et comparer chaque élément du tableau à t[0] : t[i] ≤ v (= t[0]) ?

• si t[i] ≤ v, le laisser « à gauche de v »

• sinon, le déplacer « à droite de v »

ainsi la partie gauche contient tous les éléments de t ≤ t[0]

et inve

tous les t[i] ≤ v

v

tous les t[i] > v

En pratique : une première solution simple

• on utilise 2 tableaux : tableau source à tableau destination

• o

s contraire

Version 2018 (PhL).

13





Quicksort : étape 2

**Récursion :**

**procéder de la même façon sur chaque sous-tableau gauche**

**et droit**

tous les t[i] ≤ t[0]

tous les t[i] > t[0]

t[0]

Remarque : le pivot est bien placé dans le « tableau complet »

**t[\*]**

t[\*]

**t[\*]**

Remarque : les 2 nouveaux pivots sont bien placés dans le « tableau complet »

**Terminaison:**

**le sous-tableau est vide, ou**

**le sous-tableau est composé de son seul pivot … qui est bien placé**

**dans le**

**tableau final**

Version 2018 (PhL).

14





Quicksort : exemple

tableau source

pivots

tableau destination

4, 3, 5, 8, 2, 6, 7

3, 5, 8, 2, 6, 7

5, 8, 2, 6, 7

8, 2, 6, 7

vide

vide

3

début

4

4

4

4

4

4

4

.

3, 7

6

.

3

5

2, 6, 7

3

3, 2

3, 2

8, 5

8, 5

6, 7

niveau 1

7

6, 8, 5

vide

vide

3, 2, . , 7, 6, 8, 5

2, . , . , 6, 5, . , 8

. , . , . , 5, 6, . , .

3, 2 7, 6, 8, 5

3, 2, 4, 7, 6, 8, 5

2, 3, . , 6, 5, 7, 8

. , . , . , 5, 6, . , .

2, 3, 4, 5, 6, 7, 8

niveau 2

niveau 3

fin

Version 2018 (PhL).

15





Suite sur notebook python

• algorithme

• pire cas et meilleurs cas

• expérimentations :

• décompte du nombre de comparaisons

Version 2018 (PhL).

16





Principe

Fusionner 2 tableaux triés pour obtenir un tableau unique trié

• c’est facile !! il suffit de comparer les premiers éléments de chacun

Obtenir 2 tableaux triés ?

• on divise le tableau t[0..n[ en 2 sous-tableaux de taille moitié :

t\_gauche[0..n/2[ et t\_droit[n/2 .. n[

• et on trie chacun de ces sous-tableau en appliquant le même

principe

àrécursion

• terminaison : quand on a un sous-tableau trié

le sous-tableau est de taille 1 : réduit à 1 élément

Version 2018 (PhL).

17





Fusionner 2 tableaux triés

tableau gauche

1, 3, 5, 8, 11

1, 3, 5, 8, 11

3, 5, 8, 11

3, 5, 8, 11

3, 5, 8, 11

3, 5, 8, 11

5, 8, 11

tableau fusionné

tableau droit

2, 6, 7

2, 6, 7

2, 6, 7

2, 6, 7

6, 7

1

1

1, 2

1, 2

6, 7

1, 2, 3

6, 7

5, 8, 11

1, 2, 3

6, 7

8, 11

8, 11

8, 11

vide

1, 2, 3, 5

1, 2, 3, 5, 6

1, 2, 3, 5, 6, 7

**1, 2, 3, 5, 6, 7, 8, 11**

6, 7

7

**VIDE**

vide

Version 2018 (PhL).

18





Complexité de ces tris

Complexité optimale du tri par comparaisons = O(n.log n)

Version 2018 (PhL).

19





Complexités en temps (et en espace)

**Complexité :**

**Tri insertion**

**Tri Quicksort**

**Tri fusion**

**en nombre de**

**tri en place : oui**

**tri en place : oui**

**tri en place : NON**

**comparaisons**

**pour n valeurs à trier**

dans le pire cas

**quadratique**

**O(n2)**

n2/2

**quadratique**

**O(n2)**

n2/2

**semi-logarithmique**

**O(n . log2n)**

n . log2n

double boucle

imbriquée for/while

C(n) = n-1 + C(n-1)

C(1) = 0

C(n) = C(n/2) + f(n)

f(n) : fusion = n-1

dans le meilleur cas

complexité moyenne

**linéaire**

O(n)

n

**semi-logarithmique**

O(n . log2n)

**semi-logarithmique**

O(n . log2n)

n . log2n

n/2 . log2n

C(n) = n-1 + 2.C(n/2)

C(1) = 0

C(n) = C(n/2) + f(n)

f(n) : fusion = n/2

**quadratique**

O(n2)

n2/4

**semi-logarithmique**

O(n . log2n)

2 n . log2n

**semi-logarithmique**

O(n . log2n)

n . log2n





(\*) Prouver ces tris

terminaison et correction

Version 2018 (PhL).

21





Tri insertion : preuve

Invariant :

Avant l’itération i, le sous-tableau t[0, i] est trié

Version 2018 (PhL).

22





Tri rapide quicksort : preuve

Invariant de partition(t, g,d) :

au début de l’itération i : pour tout k dans [g, d], on a

\1. si g ≤ k ≤ m

\2. si m+1 ≤ k < i

\3. si g = d-1

alors t[k] ≤ v

alors t[k] > v

alors t[k] = v

Remarque : on ne dit rien sur la tranche t[i, d-2] qui sont a

priori quelconques

Version 2018 (PhL).

23





Tri fusion: preuve

Invariant de la boucle for dans fusion(t, g, m, d) :

au début de l’itération i :

\- le sous-tableau t[g, k[ contient en ordre trié les (k-g) plus

petits éléments de G[0, m-g[ et D[0, d-m[ ;

\- G[i1] et D[i2] sont les plus petits éléments respectifs de G et

D a ne pas avoir été copiés dans t.

Version 2018 (PhL).

24

