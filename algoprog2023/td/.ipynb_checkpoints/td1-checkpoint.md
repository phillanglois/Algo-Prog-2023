# Feuille 1

**Focus**

Fonctions, plutôt numériques et cas scalaire : en-tête, appels,
    corps.

**Compétences**

- utiliser une fonction prédéfinie ou existante
- définir et écrire la spécification d'une fonction qui réalise un traitement décrit en français, ou qui résout un problème (simple) décrit en français  
- définir et écrire des appels simples (tests unitaires) 
- définir et écrire l'implémentation d'une fonction associée à une spécification 

**Rappel de quelques consignes**

- _Dans cet ordre_ :
    1. écrire la spécification (en-tête, signature)
    2. écrire un appel au moins, voire un premier ensemble de tests unitaires
    3. écrire un corps
    4. exécuter le résultat de l'étape 2
    5. corriger si besoin
- _Se souvenir_ :
    - Séparer les entrées-sorties des traitements !    
    - Réduire au minimum l'utilisation des `input()` et des `print()`.  

## Objectif 10

### $\blacksquare$ Exercice

1.  Écrire un algorithme qui calcule et affiche le maximum de 3 valeurs
    entières entrées au clavier.
2.  Écrire l'en-tête d'une fonction `max()` qui calcule et retourne la
    valeur maximale d'un triplet $(x,y,z)$ de valeurs flottantes.
3.  Écrire un algorithme qui réalise les entrées-sorties nécessaires et
    appelle plusieurs fois la fonction `max`.
4.  Écrire le corps de cette fonction.
5.  Proposer les modifications minimales pour que la fonction `max()`
    devienne la fonction `min()`.

### $\blacksquare$ Exercice

1.  Écrire un algorithme qui calcule la moyenne de 4 valeurs entières.
2.  Écrire (l'en-tête, puis l'appel puis le corps d'une fonction `moy()`
    qui calcule et retourne la moyenne de 4 valeurs flottantes. On
    supposera que ces 4 valeurs sont entrées au clavier.

(exo:approx)=
### Exercice 

On reprend l'algorithme qui teste si une année est bissextile, l'année
étant entrée au clavier et un message de type "oui/non" est affiché
après le traitement (voir exercice 4, feuille TD no 2 du semestre 1).

1.  Définir et écrire (d'abord l'en-tête, puis l'appel puis le corps)
    d'une fonction `est_bissextile()` qui vérifie le caractère
    bissextile ou non d'une année. Rappel : cette fonction ne comporte
    *aucun affichage*.
2.  Utiliser cette fonction pour réaliser le traitement de l'exercice du
    semestre 1, entrées et sorties comprises.

### $\blacksquare$ Exercice

1.  Définir et écrire une fonction `est_rectangle()` qui vérifie si un
    triangle est rectangle. Aucune hypothèse est effectuée sur les
    paramètres de ce traitement.
2.  Ecrire un programme qui utilise cette fonction pour traiter un
    nombre arbitraire de triangles entrées au clavier par l'utilisateur.

(exo:suites)= 
###Exercice 

On rappelle quelques suites et séries numériques classiques.

-   $\blacksquare$ La somme des $n$ premiers entiers
    $s_1(n) = 1 + 2 + \cdots + (n-1) + n = \sum_{k=1}^{n} k$ ;

-   $\blacksquare$ la somme des $n$ premiers carrés
    $s_2(n) = 1^2 + 2^2 + \cdots + (n-1)^2 + n^2 = \sum_{k=1}^{n} k^2$ ;

-   la somme des $n$ premiers cubes
    $s_3(n) = 1^3 + 2^3 + \cdots + (n-1)^3 + n^3 = \sum_{k=1}^{n} k^3$.

-   $\blacksquare$ La suite arithmético-géométrique $u_{n+1} = u_n/3 + 2$ avec $u_0=1$.

-   $\blacksquare$ La suite de Fibonacci $u_{n+1} = u_{n}+ u_{n-1}$ et $u_0=u_1=1$.

1.  Pour chacune de ces suites, écrire l'algorithme qui demande
    et lit une valeur de $n$ entrée au clavier, calcule le $n$-ième
    terme de la suite puis l'affiche à l'écran.
2.  Écrire des fonctions (en-tête, appel, corps) qui calculent et
    retournent le $n$-ième terme des suites précédentes. L'appel
    incluera les phases d'entrées et de sorties de l'algorithme
    principal précédent.

### Exercice

Cet exercice utilise la fonction `randint` du module `random`.

1.  $\blacksquare$ Regarder la description de la fonction `randint`.
2.  $\blacksquare$ Ecrire une fonction qui effectue un nombre arbitraire de tirages
    aléatoires d'entiers compris entre 1 et 6 (bornes comprises) et qui
    renvoie le pourcentage de 6 obtenus.
3.  Faire varier le nombre de tirages et vérifier la qualité de la
    fonction `randint`.

(exo:disques)=
### Exercice

(Adapté d'un examen de semestre 1.)

Une machine découpe, dans une plaque carrée de longueur $\ell,$ des
disques de rayon $r_e$ percés d'un trou circulaire de rayon $r_i$, avec
$r_i < r_e$, comme illustré sur le schéma ci-dessous avec 4 disques.

```{figure} ./fig/disques.png
:name: disques
:height: 100px
```

**Rappel :** l'aire d'un disque de rayon $r$ est égale à $\pi r^2$, et en Python une valeur pour $\pi$ est disponible dans le module `math`.

1.  Écrire un programme qui lit au clavier
    la dimension $\ell$ et les rayons $r_e$ et $r_i$ (réels) en cm,
    vérifie $r_i < r_e$ et le cas échéant redemande de nouvelles
    valeurs, puis calcule et affiche la surface (en cm$^2$) d'un unique
    disque découpé (partie grise), puis détermine le nombre maximum de
    disques que la machine pourra découper et la surface de déchet
    (partie hachurée)
2.  Écrire des fonctions `aire_carre()` et `aire_disque()` qui calculent
    et retournent respectivement l'aire d'un carré quelconque et celle
    d'un disque quelconque.
3.  Vérifier expérimentalement la correction de ces fonctions sur des
    exemples bien choisis. Un algorithme est dit *correct* si il
    effectue le traitement défini par sa spécification et pour tout
    argument effectif défini par sa spécification.
4.  Transformer le programme de la
    question 1 en une version qui utilise les fonctions
    précédentes.

(exo:fact)=
### Exercice

La valeur de factorielle (de) $n$, où $n$ est un entier positif, est :
$n ! = 1 \times 2 \times \cdots \ \times (n-1) \times n$. On choisit
$0 ! = 1$.

1.  Écrire un algorithme (itératif) qui calcule $n!$ pour une valeur de
    $n$ arbitraire lue au clavier.
2.  $\blacksquare$ Écrire (l'en-tête, puis l'appel précédent, puis le corps) de la
    fonction `factorielle()` qui calcule et retourne $n!$.
3.  Utiliser la fonction `factorielle()` pour écrire des fonctions qui
    calculent les quantités suivantes.

    1.  Le nombre d'arrangements (listes ordonnées) de $k$ valeurs
        prises dans un ensemble de $n$ valeurs est :
        $\mathcal{A}_n^k = {n
                  !}/{(n-k)!}, (k \le n)$.
    2.  Le nombre de combinaisons (listes non ordonnées) de $k$ valeurs
        prises dans un ensemble de $n$ valeurs est :
        $\left(_k^n\right) =
                {\mathcal{A}_n^k}/{k!}$, $(k \le n)$.



### Exercice 

(Adapté d'un examen de semestre 1)

Le développement limité en 0 de $\ln(1+x)$ est défini de la manière
suivante : $$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots +
(-1)^{n-1}\frac{x^n}{n}.$$

1.  Écrire un programme qui lit au
    clavier une valeur entière $n > 2$ et une valeur réelle
    $x \in [-1,1]$, calcule et affiche la valeur de $\ln(1+x)$ en
    utilisant la formule précédente.
2.  Écrire une fonction `log_1_p_x()` qui effectue le calcul du
    développement limité en 0 de $\ln(1+x)$.
3.  Transformer le programme de la question 1 
    en une version qui utilise la fonction précédente.
4.  S'inspirer de
    l'exercice [](exo:approx) pour proposer une analyse de la pertinence
    de ce développement limité.


## Objectif 20

**Remarque :** Proposer les fonctions les plus générales possibles.

### Exercice

On continue l'exercice [](exo:fact). 

- Utiliser la fonction `factorielle()` pour écrire des fonctions qui  calculent les quantités suivantes.
- En s'inspirant d'un exemple donné au chapitre 1, proposer des
représentations graphiques qui illustrent les approximations mentionnées.

3.  Une approximation de $e \approx \sum_{k=0}^n 1/k !$, puis
    vérifier que l'approximation est d'autant plus précise que $n$
    est grand.
4.  $\blacksquare$ La formule de Stirling $n! \approx \sqrt{2\pi n} (n/e)^n$ qui
    donne un équivalent de la factorielle (et aussi une
    approximation de $\pi$), approximation dont on vérifiera la
    pertinence.
5.  Même question pour $\ln(n!) \approx n\ln(n)-n$ et des $n$ assez
    grands.
    


### Exercice

Reprendre l'exercice [](exo:disques)en définissant une fonction qui calcule la surface d'un disque découpé.


(exo:seconddegre)= 
### Exercice 

Les racines $x_1$ et $x_2$ d'une équation du second degré
$a x^2 + b x + c
=0$ vérifient les relations suivantes.

-   La somme de ses racines est égale à l'opposé du coefficient de degré
    1 de l'équation normalisée, soit : $$x_1+ x_2 = - b/a.$$
-   Le produit de ses racines est égal au coefficient constant de
    l'équation normalisée, soit : $$x_1 \times  x_2 = c/a.$$

1.  Ecrire une fonction `est_racine()` (en-tête, corps) qui vérifie si
    une valeur donnée est racine d'une équation définie par ses 3
    coefficients.

2.  Ecrire les fonctions `somme_sym()` et `prod_sym()` (en-tête, corps)
    qui vérifient chacune des deux propriétés précédentes.

3.  Écrire l'algorithme principal qui teste ces fonctions pour des
    équations et des valeurs arbitrairement choisies au clavier.


### ($\star\star$) Exercice

On souhaite évaluer la valeur d'un polynôme de degré $3$,
$p_3(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3$, en des valeurs $x$ arbitraires.

1.  Écrire (en-tête, corps) d'une fonction `eval()` qui calcule et
    retourne $p_3(x)$.
2.  Ecrire un algorithme qui utilise cette fonction pour des valeurs
    entrées au clavier et affiche le résultat à l'écran.
3.  Détailler le principe d'un algorithme qui calcule une racine d'un
    polynôme sur un intervalle $[a, b]$ donné. La présence d'une racine
    *unique* sur $[a, b]$ sera admise MAIS l'existence d'une racine sera
    vérifiée par cet algorithme. Introduire un paramètre adapté au
    caractère approximatif de la valeur calculée.
4.  Écrire un algorithme principal qui effectue cette recherche pour un
    polynôme $p_3$ de degré $3$ et un intervalle $[a, b]$ donnés. Tous
    les paramètres sont entrés au clavier.
5.  Appliquer cet algorithme pour retrouver, une à une, les racines de
    $p(x)=x(x-1)(x-2)$.

### Exercice

Écrire (en-tête, corps) d'une fonction `est_premier()`
qui retourne un booléen qui indique si un nombre entier donné $n$ est
premier ou non.


### Exercice

Écrire (en-tête, corps) d'une fonction `pgcd()` qui
calcule le PGCD de deux entiers naturels. On utilisera l'algorithme
d'Euclide.

Rappel : l'algorithme d'Euclide utilise la propriété suivante. Le PGCD
de $a$ et $b$, $a > b$, est égal à $b$ si le reste $r$ de la division
euclidienne de $a$ par $b$ est nul, sinon il vaut le PGCD de $b$ et de
$r$. Le PGCD de 2 nombres distincts premiers entre eux (*i.e.* sans
diviseur commun autre que 1) est égal à 1. Cet exercice permet d'écrire
une version itérative de cet algorithme.


### Exercice

Permuter deux variables entières est une procédure : les
variables changent d'état (action) sans qu'il y ait besoin de retourner
une valeur. Une "fonction" python qui réalise une permutation aura donc
l'en-tête suivante.

```python
def permuter(a, b : int) -> None: 
    '''Permute les deux variables entières a et b'''
```

1.  Ecrire le corps cette permutation de deux façons différentes : avec
   ou sans variable supplémentaire.
2.  Les appliquer à deux valeurs arbitraires.
3.  Que constatez-vous ? Utiliser [pythontutor](https://pythontutor.com) et expliquer le comportement observé.
4.  Proposer une alternative qui effectue le traitement attendu.
