
# Connaissances

-   tableaux 2D et traitements associés : images, matrices

-   boucles imbriquées

-   fonctions avec tableaux multi-dimensionnels

# Objectif 10

**Exercice .** **()**

1.  Écrire un algorithme qui calcule les tables de multiplications entre
    entiers compris en 1 et 10, les stocke dans un tableau 2D puis les
    affiche. Ainsi la case $(i,j)$ du tableau contient le résultat de
    $i \times j$.

**Exercice .**[]{#exo:verif label="exo:verif"} **()**

Ecrire les algorithmes de vérification suivants pour une matrice $M$
donnée, carrée de taille $n$ et à valeurs flottantes.

1.  $M$ est diagonale ?

2.  $M$ est symétrique ?

3.  $M$ est égale à l'identité ?

4.  $M$ est l'inverse d'une autre matrice donnée $N$ ?

**Exercice .**[]{#exo:ttmt label="exo:ttmt"}

1.  **()** Ecrire les algorithmes des traitements suivants pour une
    matrice $M$ donnée, carrée de taille $n$ et à valeurs flottantes.

    1.  Générer, puis afficher, la matrice transposée de $M$.

    2.  Générer la matrice symétrique à partir de la partie triangulaire
        supérieure de $M$.

    3.  Calculer les opérations matricielles suivantes en veillant à la
        cohérence des dimensions :

        1.  addition de matrices : $A+B$,

        2.  produit matrice-vecteur : $A \cdot U$,

        3.  produit de matrices : $A \times B$.

2.  Compter le nombre d'opérations arithmétiques de ces traitements.
    Exprimer ce nombre comme une fonction de $n$. Qu'en déduire si la
    taille $n$ est doublée ?

**Exercice .**

**()** Calculer, puis afficher, les 15 premières lignes du triangle de
Pascal. Veiller à séparer traitement et affichage.

**Exercice .**[]{#exo:ttmt2 label="exo:ttmt2"}

**()** Reprendre tous les exercices précédents et ré-écrire le
traitement sous la forme d'un appel à une fonction à définir en trois
temps -- comme d'habitude !.

1.  Préciser l'en-tête de la fonction sans oublier les obligations liées
    à des paramètres tableaux.

2.  Ecrire l'appel de la fonction pour des tableaux préalablement
    définis.

3.  Ecrire le corps de la fonction.

# Objectif 20

**Exercice .**

On veut résoudre le système linéaire $Tx=b$ où la matrice $T$ est une
matrice triangulaire inférieure carrée de taille $n$ et $b$ un vecteur
second membre (de taille $n$). La matrice $T$ et et le vecteur $b$ sont
supposés donnés (au clavier ou avec une valeur d'initialisation).

Fonctions et transformation d'image de taille arbitraire.\
On considère la dernière transformation (1) $\to$ (3) où la partie
triangulaire inférieure est noircie. Selon la forme de la matrice, cette
partie noircie est un triangle (matrice rectangulaire "allongée"
horizontalement) ou un trapèze (matrice rectangulaire "allongée"
verticalement). On va définir cette transformation sous la forme d'une
fonction.

1.  Analyse d'une image de taille arbitraire.

    1.  Ecrire une fonction `nbpixblc()` qui compte et retourne le
        nombre de pixels blanc d'une image de taille arbitraire

    2.  Que retourne l'application de cette fonction à l'image (4) de la
        question [\[que:im4\]](#que:im4){reference-type="ref"
        reference="que:im4"}.

2.  Complexité de cette analyse

    1.  ($\star$) Préciser le paramètre de complexité de `nbpixblc()`,
        la mesure de cette complexité et l'expression la plus précise
        possible de sa complexité. Justifier votre réponse.

    2.  ($\star$) Soit $C$ la complexité du traitement par ` nbpixblc()`
        d'une image donnée $\mathcal{I}$. On double le nombre de lignes
        de $\mathcal{I}$. Quelle est la complexité $C_1$ du traitement
        de cette nouvelle image ?

    3.  ($\star$) On double le nombre de lignes et de colonnes de
        $\mathcal{I}$. Quelle est la complexité $C_2$ du traitement de
        cette nouvelle image.

    4.  ($\star$) Donner l'expression la plus précise possible de sa
        complexité asymptotique.

**Exercice .** Cet exercice sera en partie repris en TP de
programmation.\
De façon similaire à
l'exercice [\[exo:imnb\]](#exo:imnb){reference-type="ref"
reference="exo:imnb"}, on définit des images à niveaux de gris par un
tableau 2D d'entiers compris en 0 (noir) et 255 (blanc). La taille de
l'image $L \times C$ est arbitraire.\
Ecrire les algorithmes des traitements suivants. On pourra commencer en
introduisant un tableau supplémentaire pour l'image transformée. Selon
les cas, on essaiera ensuite une solution "en place" : la transformation
s'effectue sur le tableau de l'image d'origine.

1.  Générer le négatif (*reverse video*) d'une image NB ou par niveaux
    de gris.

2.  Générer une image NB à partir d'une image niveau de gris.

3.  Augmenter le contraste de la transformation précédente.\
    Principe : fixer un seuil et remplacer les pixels plus clairs que le
    seuil par des pixels blancs, et inversement les plus sombres que le
    seuil par des pixels noirs.

4.  Générer une image miroir vertical (le haut se retrouve en bas et
    réciproquement) ou horizontal d'une image NB.

5.  Augmenter la luminosité (ou luminance) d'une image à niveau de
    gris.\
    Principe : ajouter ou retrancher une constante de la valeur des
    pixels.

6.  Générer les contours significatifs d'une image.\
    Principe : on remplace par un pixel noir chaque pixel dont la
    variation des valeurs de ses 4 voisins varient au delà d'un certain
    seuil, sinon on le remplace par un pixel blanc.

7.  Réduire par 2 la taille d'une image à niveau de gris.\
    Principe : chaque carré de 2x2 pixels est remplacé par 1 pixel de
    valeur la moyenne des pixels du carré.

**Exercice .** ($\star\star$) Cet exercice sera repris en TP de
programmation.\
Ecrire les algorithmes qui, à partir de l'image originale (à gauche),
génèrent les images zébrées horizontales ou verticales ou quadrillées (à
droite). Le nombre de découpages horizontaux ou verticaux sont des
paramètres de l'algorithme. On veillera aux cas où la taille de l'image
n'est pas divisible par ces paramètres.\
![image](fig/jap.png){height="25mm"}
![image](fig/jap-18NBzebreH.png){height="25mm"}
![image](fig/jap-NBzebreVert.png){height="25mm"}
![image](fig/jap-damier15.png){height="25mm"}
