(td:td5)=
# Feuille 5

- Le symbole $\blacksquare$ indique les exercices ou questions obligatoires. Commencez pas ceux-là.
- Les symboles $\star$ et $\star\star$ indiquent les exercices ou questions de difficulté relative plus importante.


**Focus**

-   récursivité et notions associées : arbre et pile des appels,
    environnements
-   recherche dichotomique

**Compétences**

- Savoir conduire une approche diviser pour régner et en déduire une solution récursive : application à des exemples calculatoires simples -- comme ceux vus en cours, _e.g_. factorielles, exponentiation entière, exponentiation rapide.
- Savoir identifier la (ou les) terminaison, la récursion et l'initialisation d'un traitement avec un algorithme récursif : application à des exemples simples -- comme ceux vus en cours, _e.g_. factorielles, exponentiation entière, exponentiation rapide.
- Savoir exprimer la complexité d'un algorithme récursif 
- Savoir écrire sous la forme d'une fonction de même signature les versions itérative et récursive d'un traitement calculatoire simple
- Construire la pile des appels et son évolution lors d'un traitement récursif

## Objectif 10

(exo:fibo)=
### $\blacksquare$ Exercice.

On rappelle la suite de Fibonacci : 

$F(0)=F(1)=1$ et $F(n+1) = F(n)+F(n-1)$. 

Elle permet entre autres de modéliser l'évolution d'une
population de lapins.

1.  Ecrire une version itérative du calcul de $F(n)$ et calculer les premières valeurs de $F$ pour se convaincre qu'elles
    augmentent rapidement.
    
2.  Rappeler l'algorithme récursif du calcul de $F(n)$.

3.  Expliciter l'arbre des appels récursifs du calcul de $F(4)$ puis de
    $F(5)$ --- prévoir une feuille A4 en largeur. Dénombrer le nombre
    des appels nécessaires dans les 2 cas.

4.  Détailler l'exécution du calcul de $F(3)$ en explicitant l'évolution
    de la pile des appels.

```{image} ./fig/FibonacciRabbit.png
:align: center
:alt: <https://commons.wikimedia.org/w/index.php?curid=11104228>
```


(exo:sumrec)=
### $\blacksquare$ Exercice.

1. Écrire puis coder une version itérative des calculs suivants.

    1.  la somme $s(n)$ des $n$ premiers entiers

    2.  la valeur $u(n)= 2^n$ pour $n>0$

1. Écrire puis coder une version récursive des calculs suivants.

    1.  la somme $s(n)$ des $n$ premiers entiers

    2.  la valeur $u(n)= 2^n$ pour $n>0$

2.  Expliciter l'arbre des appels et les calculs associés lors de
    l'évaluation de $s(4)$. Combien d'appels récursifs à $s$ sont
    nécessaires ?

3.  Même question pour $u(5)$.

(exo:expo)=
### $\blacksquare$ Exercice.

On souhaite calculer la
valeur de $x^n$ où $n$ et un entier positif, et $x$ un flottant. On
rappelle que $x^0 = 1.0$.

1.  1.  Écrire un algorithme itératif qui calcule $x^n$.

    2.  Combien de multiplications sont nécessaires à ce calcul ?

2.  1.  Utiliser la propriété $x^p = x \times x^{p-1}$ pour écrire un
        algorithme récursif qui calcule $x^n$.

    2.  Combien de multiplications sont nécessaires à ce calcul ?

3.  1.  Utiliser la propriété $x^p \times x^p = x^{2p}$ pour écrire un
        algorithme récursif qui calcule $x^n$. On pourra utiliser
        l'opérateur python `divmod`.

    2.  Combien de multiplications sont nécessaires à ce calcul pour
        $n=2, 4, 8, 16, \dots, 2^p$ ?

4.  Que pensez vous de ces deux versions récursives ?

5.  Dans ces deux cas, compter le nombre d'appels récursifs pour les
    valeurs suivantes de $n = 4, 7, 8, 9, 63, 64, 65$.

(exo:forrec)=
### $\blacksquare\blacksquare$ Exercice.
**Si il n'y avait qu'un seul exercice à faire, c'est celui-ci !**.\

1.  Donner la forme récursive qui produit le même traitement que
    celui d'une boucle for qui (parcourt et) affiche les indices entiers
    successifs de 11 à 1.

2.  Même question pour obtenir l'affichage : 1, 2, ..., 10, 11.

(exo:dicho)=
### $\blacksquare$ Exercice.

1.  Écrire un algorithme itératif qui calcule un booléen
    indiquant si un tableau d'entiers **donné trié** par ordre croissant
    contient une valeur donnée. La recherche sera effectuée par
    dichotomie.

2.  Écrire une fonction récursive `trouve` (c'est-à-dire son
    en-tête, puis l'appel puis le corps) qui retourne le booléen
    précédent en appliquant aussi une recherche par dichotomie.


(exo:dicho2)=
### $\blacksquare$ Exercice.

1.  Dérouler l'algorithme de recherche dichotomique (version itérative)
    pour rechercher la valeur 3 dans la tableau \[0,1,2,3,4,5,6,7,8,9\].

2.  Donner une valeur à rechercher qui minimise le nombre d'itérations
    de la recherche.

3.  Même question pour celle qui maximise ce nombre.

4.  Coder ces traitements et vérifier votre analyse.


## Objectif 20

(exo:fibo2)=
### Exercice.
Fibonacci (encore).

1.  Tracer les appels successifs en ajoutant un `print`.

2.  Tester pour `fibo(5)`.

(exo:exporapide2)=
### Exercice.
Exponentiation rapide (encore).

1.  Tracer les appels successifs en ajoutant un `print`

2.  Quels sont appels à `expo(x,n)` évités par `expo_rapide(x,n)` ?
    Commencer avec des valeurs de $n$ arbitrairement choisies.

(exo:syracuse)=
### $\star$ Exercice. 

La suite de Syracuse $s$ d'un nombre $N$ donné est
définie de façon récursive comme suit.

On commence avec $s(0) = N$, puis :

- $s(n+1) =  s(n)/2$,    si $s(n)$ est pair,  
- $s(n+1) =  3s(n)+1$,   si $s(n)$ est impair.


Ainsi définie, $s$ est une suite infinie de valeurs entières construites
à partir de la valeur de départ $N$.

1.  A la main pour commencer.

    1.  Calculer à la main les valeurs de la suite pour les valeurs de
        départ $N = 4, 2, 1$. Qu'en déduire ?

    2.  Calculer à la main les valeurs de la suite pour les valeurs de
        départ $N = 3, 5, 6, 7, 8, 16, 32$. Il peut être utile de
        représenter les valeurs obtenues sous la forme d'un tableau où
        chaque colonne (ou ligne) à la forme $N u_1 u_2 \dots u_n \dots$
        où les $u_i$ sont les valeurs de la suite pour la valeur de
        départ $N$. Qu'en déduire et en particulier que penser de la
        terminaison de cette suite ?

2.  La coder de façon récursive et observer son comportement pour
    l'une de ces valeurs de $N$. Attention !!!

3.  Terminaison : on arrête la suite $s(n)$ quand on rencontre
    $n = 1$ (c'est-à-dire $s(2)$). D'après la conjecture de Collatz, cette
    valeur est rencontrée quelque soit le terme de départ $N$.

    1.  Compléter votre code précédent avec cette condition d'arrêt.

    2.  Compléter votre code précédent avec l'affichage de chaque valeur
        calculée avant la terminaison.

4.  Écrire des fonctions qui calculent les notions suivantes
    (source Wikipédia) :

    1.  le temps de vol qui est le plus petit indice $n$ tel que
        $s(n) = 1$, *i.e.* jusqu'à la terminaison.

    2.  le temps de vol en altitude qui est le plus petit indice $n$ tel
        que $s(n) \le N$.

    3.  l'altitude maximale qui est la valeur maximale $s(n)$ de la
        suite.

5.  Coder ces fonctions et proposer des graphiques instructifs.

6.  Coder ces fonctions et proposer des graphiques instructifs.

7.  Coder le calcul avec terminaison de façon itérative.

(exo:euclide2)=
### $\star$ Exercice. 
(Euclide encore) 

Wikipédia décrit l'algorithme d'Euclide
pour calculer le pgcd de deux entiers ($a > b$) comme suit.

> *Soient deux entiers naturels a et b, dont on cherche le PGCD. Le cas
> où a ou b est nul ne nécessite aucun algorithme ; on l'exclut. Une
> suite d'entiers $(a_n)_n$ est définie par récurrence de pas 2, plus
> précisément par divisions euclidiennes successives ; la suite est
> initialisée par $a_0 = a, a_1 = b$, puis propagée par la règle de
> récurrence : tant que $a_{n+1}$ est non nul, $a_{n+2}$ est défini
> comme le reste de la division euclidienne de $a_n$ par $a_{n+1}$.*
>
> On commence donc par calculer le reste de la division de a par b,
> qu'on note r ; puis on remplace a par b, puis b par r, et on
> ré-applique le procédé depuis le début.
>
> On obtient ainsi une suite, qui vaut 0 à un certain rang ; le PGCD
> cherché est le terme précédent de la suite.

1.  Ecrire (à nouveau) un algorithme itératif qui calcule ce pgcd.

2.  Écrire un algorithme récursif qui calcule ce pgcd.

3.  Proposer une formulation synthétique de l'algorithme d'Euclide (qui
    remplacerait avantageusement l'extrait de Wikipédia).

4.  Profiter de la page Wikipédia pour lire comment sont prouvées la
    correction et la terminaison l'algorithme d'Euclide, ainsi que sa
    complexité (problème beaucoup plus difficile).


(exo:addint)=
### $\star$ Exercice. 

On souhaite additionner deux entiers de $p$ chiffres
décimaux. On dispose pour cela d'une fonction `add(c1,c2)` qui calcule
et retourne un couple `(r,s)` où :

-   `c1, c2, s` sont des entiers compris entre 0 et 9,

-   `r` est égal à 0 ou à 1, et

-   `c1 + c2 = 10 r + c`.

Ainsi `r` est la retenue de l'addition des chiffres `c1` et `c2` et `s`
est la valeur "des unités" de cette somme. Par exemple : `add(2,3)`
retourne `(0,5)` et `add(8,5)` retourne `(1,3)`.

On représente un entier $n$ à $p$ chiffres décimaux par un tableau $N$
de longueur $p$. On peut choisir par exemple
$n = \sum_{i=0}^{p-1} N[i]\cdot 10^i$. Dit plus simplement dans ce cas,
le dernier chiffre de $n$ (celui des unités) est stocké en position 0
dans le tableau $N$, l'avant-dernier (celui des dizaines) en position 1,
... --- et on notera qu'il est ainsi plaisant que les tableaux soient
indicés à partir de 0. Il est aussi possible de choisir une écriture
plus classique où les chiffres sont stockés dans l'ordre des puissances
décroissantes (numération de position habituelle).

1.  Utiliser la fonction `add` pour écrire un algorithme qui calcule la
    somme de deux entiers $n1$ et $n2$ respectivement représentés par
    les tableaux $N1$ et $N2$. Le résultat $s = n1+n2$ sera aussi
    représenté par un tableau adapté.

2.  Soient $n1 = 1234$, $n2=4567$ et $n3=9876$. Dérouler l'algorithme
    pour les deux calculs $n1+n2$ et $n1+n3$.

3.  Coder et valider ces fonctions.
