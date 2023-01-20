#!/usr/bin/env python
# coding: utf-8

# (ch:fonctions-tableaux)=
# # Fonctions et tableaux 

# Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.

# Dans ce chapitre, nous complétons l'étude des fonctions en python en présentant le cas des **fonctions avec paramètre de type tableau**, c-a-d. le cas de fonctions qui manipulent des arguments `list`.
# 
# Les tableaux mis en oeuvre avec des listes python sont entre autres rapellés dans l'annexe [a0 Boucles avancées](#ann:boucle-tableaux). 

# <div class="alert alert-block alert-info">
# <b>Vocabulaire.</b> distinguer la dimension d'un tableau <em>vs.</em> la taille d'un tableau
# </div>

# **Dimension.** 
# 
# * Un tableau peut être unidimensionnel (un vecteur), bidimensionnel (une matrice), tridimensionnel (une image 2D en couleurs (R,G,B)), ... 
# * Sa dimension est donc le _nombre d'indices_ nécessaires pour localiser une de ses valeurs.
# 
# **Taille.**
# * Chacune des dimensions d'un tableau est composée d'un certain nombre de _valeurs de l'indice de cette dimension_.
# * La taille de ce tableau est _l'ensemble ordonné_ de chacun de ces nombres pour chacune de ses dimensions.

# **Exemples et conventions.**
# 
# Le vecteur $(2, 4, 6)$ est de dimension 1 et de taille 3.  
# 
# La matrice 
# 
# $$
# \begin{pmatrix}
#     1 & 2 & 3 \\
#     1 & 4 & 9 \\
# \end{pmatrix}
# $$
# 
# est de dimension 2 et de taille (2, 3) : 
# elle contient 6 valeurs organisées en 2 lignes et 3 colonnes.  
# 
# - La première valeur de sa taille est son nombre de lignes.
# - La seconde valeur de sa taille correspond à son nombre de colonnes.
# - Ce choix ligne, puis colonne, (puis ...) est arbitraire mais usuel en maths, en algo, ...  
# 
# 
# Le vecteur colonne 
# 
# $$
# \begin{pmatrix}
#     1 \\
#     0 \\
#     0 \\
# \end{pmatrix}
# $$
# 
# représente souvent le premier vecteur de la base orthonormée $(i, j, k)$ de $\mathbb{R}^ 3$ est  de taille (3, 1).
# 
# Excepté le terme _tableau_, ces notions sont indépendantes de tout choix informatique.          

# **Ce qu'il ne faut pas faire :** on pourrait _être tenté_ d'écrire : 
# 
# ```python 
# c = [[0] * n] * n
# ```
# 
# Cette construction utilise le sens particulier du symbole `*`  appliqué à des listes 1D qui correspond à la répétition de _concaténation de listes_. 
# La concaténation de deux listes peut s'écrire en python avec le symbole `+`.

# In[1]:


l1 = [3]
l2 = [4, 5]
l = l1 + l2
print("l=", l)

l3_zeros = [0] * 3
print(l3_zeros)

l3_uns = [1] * 3
print(l3_uns)

l3 = l3_zeros + l3_uns 
print("l3=", l3)


# Avant d'indiquer pourquoi il ne faut pas utiliser aveuglement cette définition par concaténation, présentons :
# 
# :::{Admonition} **Ce qu'il faut faire**
# :class: important
# Pour définir et initialiser un tableau mono- ou multi-dimensionnel, utiliser systématiquement la _construction d'une liste par compréhension_.
# 
# ```python 
# c = [[0 for i in range(n)] for j in range(n)]
# ```
# :::

# ($\star$) **Pourquoi ?** 
# 
# 
# Le code suivant _à éviter_ reprend la construction d'une liste 1D par concaténation et le fait qu'un tableau 2D est une liste de listes.  

# In[2]:


# à ne pas faire
l34_zeros = [[0] * 3] * 4
print(l34_zeros)

# à ne pas faire
l34_uns = [l3_uns] * 4
print(l34_uns)


# L'affichage et des tests trop naïfs ne permettent pas d'exhiber pourquoi cette construction est dangereuse.

# In[3]:


# definition de liste 2D en compréhension
oui_comme_ca = [[0 for i in range(3)] for j in range(4)]

print(oui_comme_ca)
print(oui_comme_ca == l34_zeros)


# Il y a pourtant danger :

# In[4]:


l34_zeros[1][2] = 1 # je modifie UNE valeur de ce tableau

print(l34_zeros)
print("Aie ! ")


# :::{danger}
# Quatre termes de la matrice ont été modifiées alors l'écriture désigne **un seul terme** de cette matrice.
# :::

# Ce comportement assez piégeux peut être particulièrement long à identifier lors d'une phase de debug ...

# **Visualiser pour bien comprendre.** 
# 
# Merci pythontutor !
# - [tableau 1D](http://pythontutor.com/visualize.html#code=v%20%3D%20%5B1,%202,%203%5D%0Anon%20%3D%20%5B0%5D%20*%203%0Aoui%20%3D%20%5B0%20for%20_%20in%20range%283%29%5D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) : OK par concaténation et compréhension.
# - [tableau 2D](http://pythontutor.com/visualize.html#code=%23%20tableau%202D%0Am%20%3D%20%5B%5B1,%202%5D,%20%5B3,%204%5D,%20%5B5,%206%5D%5D%0A%23%20bien%20regarder%20l'effet%20de%20la%20construction%20suivante%0Anon2%20%3D%20%5B%5B0%5D%20*%202%5D%20*%203%0A%23et%20de%20celle-ci%0Aoui2%20%3D%20%5B%5B0%20for%20i%20in%20range%282%29%5D%20for%20j%20in%20range%283%29%5D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) : Oui par compréhension, NON par concaténation de listes !
# 
# 

# **Conclusion**
# Il vaut mieux s'interdire toute mauvaise habitude -- même pour les listes 1D ou tableaux 1D.

# :::{important}
#     
# Utiliser la définition de **listes en compréhension :**
# 
# - 1D : OUI à `[i for i in range(3)]`
# - 2D : OUI à `[[0 for i in range(3)] for j in range(5)]`
# 
# Ne pas utiliser le symbole `*` de concaténation répétée pour créer et initialiser une liste.
# 
# - ~~`[[0] * 3] * 5`~~
# 
# :::

# ## Spécifications de fonctions avec paramètre `list`  en python
# 
# La spécification d'une fonction doit comporter le type de ses paramètres formels.  
# On s'était limité aux paramètres formels de types scalaires `bool`, `int`, `float`, `complex`.

# **Pourquoi introduire cette notion maintenant ?**
# 
# - la fonction est la construction élémentaire pour regrouper un traitement éventuellement complexe qui dépend de paramètres (d'entrée)
# - la vérification de la correction d'un traitement (à l'aide de tests unitaires) est facile à mettre en oeuvre lorsqu'il est défini sous la forme d'une fonction 
#     - il suffit d'appeler la fonction pour des paramètres bien choisis -- c-a-d. pour lesquels le traitement attendu est connu.
# - une fonction doit être décrite par sa spécification (son en-tête, sa signature)
# 
# Nous allons écrire des traitements un peu complexes sur des tableaux. 
# Donc nous avons besoin de _fonctions_ qui manipulent des _tableaux_, et donc de leur _spécification_.

# ### Comment indiquer le type d'un paramètre formel d'une fonction lorsque celui-ci est une liste ?

# :::{important} Evolutions des annotations de typage
# 
# - python $<$ 3.9 : module `typing` nécessaire pour définir `List[...]` avec une majuscule
# - python $\ge$ 3.9 : possibilité d'utiliser le type `list[...]` sans majuscule et sans importer le module `typing`
# - python $\ge$ 3.10 : le symbole `|` pour désigner l'union de types (ex `Union`)
# :::
# 
# :::{note}
# La suite de ce chapitre utilise les possibilités de python 3.9.
# :::

# Le type d'un tableau (représenté par une liste) sera décrit avec la syntaxe `list[type_val]` où `type_val` est le type des valeurs du tableau. 
# 
# _Exemples._
# 
# - `list[int]` : un tableau 1D d'entiers
# - `list[float]` : un tableau 1D de flottants  
# - `list[str]` : un tableau 1D de caractères _ou_ de chaîne de caractères.  
# - `list[list[int]]` : un tableau 2D d'entiers représenté par une liste de listes  
# 
# 
# Cette syntaxe permet d'expliciter le type (unique) des valeurs contenues dans un tableau.  

# ### Comment spécifier une fonction avec des paramètres formels de type tableau ?
# 
# Pour chaque paramètre formel de type tableau (représenté par une liste python), on _complète_ la spécification de la fonction _avec_ autant de _paramètres_ nécessaires à la définition de _la dimension du tableau_ : un paramètre supplémentaire pour un tableau 1D, deux pour un tableau 2D, ...  
# 
# Montrons avec des exemples comment préciser la (ou les) taille(s) fixe(s) d'un tableau.   

# **Exemple :**
# la fonction `min1()` doit retourner la valeur minimale d'un tableau 1 D `t`, d'entiers (par exemple) et de taille `n` quelconque. 
# 
# La spécification de cette fonction s'écrira :
# 
# ```python
# def min1(t: list[int], n: int) -> int:
#     '''retourne la valeur minimale du tableau d'entiers t de taille n'''
# 
# ```
# 
# - La taille `n` est définie ici comme second paramètre de cette fonction.
#     - C'est bien un entier
# - Ce paramètre supplémentaire n'est pas nécessaire en python mais **il est obligatoire dans cet enseignement** 

# Nous étendons cette pratique aux tableaux multidimensionnels.  
# 
# Par exemple, la spécification de la fonction qui identifie et retourne la valeur minimale dans un tableau 2D s'écrit par exemple (pour un tableau 2D d'entiers) :
# 
# ```python
# def min2(t: list[list[int]], n: int, m: int) -> int:
#     '''retourne la valeur minimale du tableau 2D d'entiers t de taille n x m'''
# ```
# Remarquons :
# - l'annotation du type de `t`, paramètre formel de "type tableau 2D", comme une liste de listes d'entiers,
# - et les 2 paramètres de taille `n` et `m`, qui désignent respectivement le nombre de lignes et de colonnes de `t`.  
# 

# <div class="alert alert-block alert-info">
#     <b>Convention à appliquer dans cet enseignement.</b> 
# 
# Lorsqu'une fonction admet un paramètre formel de type tableau (ou plus d'un), on convient que les paramètres de taille de chaque paramètre tableau suivent sa définition dans la spécification de la fonction.
# </div>    
#     

# **Exemples.** 
# 
# - si il y a 1 paramètre tableau 1D, on écrit dans l'ordre les types de `tab1, taille_de_tab1`  
# - si il y a 2 paramètres tableaux 1D, on écrit dans l'ordre les types de  `tab1, taille_de_tab1, tab2, taille_de_tab2`  
# - si il y a 1 paramètre tableau 2D, on écrit dans l'ordre les types de `tab1, nb_lignes_de_tab1, nb_colonnes_de_tab1`,
# - ...
#     

# ## Exemples
# 
# On présente ici la fonction `min1()` qui calcule la valeur minimale d'un tableau 1D d'entiers.
# 
# Se référer ensuite à l'annexe [a0 - Boucles avancées](ann:boucles) dont **tous** les exemples définissent des fonctions avec des paramètres tableaux.
# 
# - `min2()` calcule la valeur minimale d'un tableau 2D
# - `prod_mat_carrees()` calcule C = A $\times$ B ou A,B,C sont des matrices entières carrées de taille n $\times$ n
# - `existe_doublon()` calcule si il existe ou non une valeur qui apparaît au moins deux fois dans un tableau. 
# 

# ### `min1()`

# La fonction `min1` qui retourne la valeur minimale d'un tableau 1 D d'entiers (par exemple) et de taille $n$ quelconque. 

# In[5]:


def min1(t: list[int], n: int) -> int:
    '''retourne la valeur minimale du tableau d'entiers t de taille n'''
    val_min = t[0]
    for i in range(1, n):
        if t[i] < val_min:
            val_min = t[i]
    return val_min 


# In[6]:


#un appel de test sur un tableau de taille 3
u = [3, 1, 2]
un = min1(u, 3)
print(un)


# **Obligation _pédagogique_ de définir le(s) paramètre(s) pour la taille d'un paramètre tableau.**
# 
# python permet en effet de se dégager de cette obligation, entre autres grâce à la fonction prédéfinie `len()`. 

# In[7]:


def min1_bis_moche(t: list[int]) -> int:
    '''retourne la valeur minimale du tableau d'entiers t de taille n'''
    val_min = t[0]
    for i in range(1, len(t)):
        if t[i] < val_min:
            val_min = t[i]
    return val_min 


# Ce qui n'empêche pas de se servir de `len()` _dans l'appel_. Et c'est ce qu'on fera en général.

# In[8]:


u = [3, 1, 2]

print(min1(u, len(u)) == min1(u, 3))


# **Exercice.** 
# - Ecrire la spécification et le corps d'une fonction qui retourne la valeur minimale d'un tableau de `float`. 
# - ($\star$)  Qu'en pensez-vous ?  
# - ($\star$) Quelles conditions satisfaire pour une généralisation (correcte) de ce traitement ?
#     - La [section](#genericite) de ce chapitre aborde cette question.  

# :::{dropdown} Réponse
# 
# - Il suffit de remplacer l'indication de type `int` par `float` dans l'en-tête et le corps des fonctions précédentes. 
# - En revanche en python, si on veut distinguer les 2 traitements, il faut que les fonctions aient des noms différents.
# - Le traitement (chercher le min de ...) est identique dès qu'une relation d'ordre est définie pour le type des valeurs présentes dans le tableau.
# 
# :::

# (genericite)=
# ## ($\star\star$) Quelle spécification pour une fonction générique ? 
# 
# <div class="alert alert-warning">
# 
# Objectif 20 : compléments. 
#     
# Sauter cette section en première lecture.
# 
# </div>

# ### Généricité
# 
# Cette section s'est d'abord appelée : 
# 
# > "Comment spécifier un traitement générique ?"
# 
# Commençons par expliquer cette formulation un peu plus compliquée que le titre actuel.
# 
# - _spécifier_ : écrire la spécification (d'une fonction)
# - _spécifier un traitement_ : suppose que le traitement est réalisé par une fonction dont on doit écrire la spécification 
# - _un traitement générique_, ou une fonction générique : un traitement qui **s'applique** de façon similaire à des valeurs de **types différents**.

# Exemple : 
# 
# - les _corps_ des fonctions qui retournent le min de deux entiers ou deux flottants, sont identiques. OK ?
# - en revanche leurs spécifications sont, jusqu'à présent, différentes :
#     ```python
#     def min_int(a : int, b: int) -> int:
#     def min_float(a : float, b: float) -> float:
#     ```
#     

# En python, on peut écrire une _seule_ fonction `mon_min()` qui accepte indifféremment des paramètres entiers ou flottants.  
# Cette fonction `mon_min()` est générique.  
# Il est facile de l'écrire avec une seule fonction _python_ mais sans indication de spécification -- ce qui est _mal_ :) 

# ### `Union` dans le module `typing` ou `|` pour python $\ge$ 3.10
# 
# **Question.** Comment écrire sa spécification sans perdre d'information par rapport aux deux spécifications ci-dessus ?
# 
# **Réponse.** 
# 
# - Pour python $<$ 3.10 : on a besoin du module `typing` qui définit `Union` avec le sens de l'union d'ensembles en mathématique.  
# - Pour python $\ge$ 3.10 : le symbole `|`  remplace `Union` (et l'import de `typing` n'est plus nécessaire).

# :::{note} La suite de ce chapitre utilise les possibilités de python 3.9. :::

# In[9]:


from typing import Union


# Ainsi `Union[int, str]` permet de désigner toute valeur de type `int`  ou de type `str`.
# 
# De façon similaire, on peut utiliser `Union[int, float]`  pour spécifier notre fonction  générique `mon_min` qui traite indifféremment des paramètres entiers ou flottants.

# In[10]:


def mon_min(a : Union[int, float], b : Union[int, float]) -> Union[int, float]:
    if a < b:
        return a
    else:
        return b

res1 = mon_min(3, 2)
res2 = mon_min(3.0, 2.0)
res3 = mon_min(3.0, 2)

print(res1, res2, res3)


# **Syntaxe.** Attention aux `[ ]` -- et non pas des `( )` -- dans l'annotation de types -- comme pour `list[]`.
# 
# **($\star$) Attention.** 
# - Pourquoi je n'ai pas écrit que `Union[int, float]` avait le sens l'union (mathématique) des ensembles  d'entiers et de flottants ?
# - Parce qu'en python (et plus généralement en informatique avec _la notion de type_ ) :  
# ```python
# Union[int, float] != float
# ```
# On le vérifie :

# In[11]:


print(Union[int, float] == float)


# ### A lire
# 
# - Sur les annotations de types : cet [article](https://inventwithpython.com/blog/2019/11/24/type-hints-for-busy-python-programmers/) (déjà mentionné plus haut) est l'un des plus intéressants que j'ai rencontré sur le web en préparant ce cours.  En effet, la documentation de réference sur les [annotations python](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) est assez peu commode à exploiter dans ce cas.   

# :::{dropdown} Réponses.
# 
# Cherchez un peu svp ! Ensuite allez vérifier [ici](rep:doublonwhile)
# :::

# ## Synthèse
# 
# ### Ce qui a été vu

# **Spécifier pour vérifier** une fonction avec paramètre(s) de type tableau : 
# - avant python 3.9 : `from typing import List`  # avec un `L` majuscule 
# - depuis python 3.9 : `tab2D: [list[list[int]]` # avec un `l` minuscule  
# - ajouter les paramètres de dimension 
#     - appel avec la fonction préféfinie `len()` 

# ### Ce qui n'a pas été vu
# 
# Les `ndarray` du module `numpy` sont très utilisés en pratique et présentés dans [une annexe dédiée](ann:ndarray)    

# ### Exercice de synthèse
# 
# Dans un notebook jupyter dédié, s'intéresser aux problèmes de l'égalité, de la similarité et de la comparaison de deux tableaux 1D.  
# 
# **Définitions**
# 
# - Deux tableaux sont _égaux_ si ils contiennent les mêmes valeurs aux mêmes positions.  
# - Deux tableaux sont _similaires_  si ils contiennent les mêmes valeurs avec le même nombre d'occurrences -- indépendamment de leurs positions.  
# - Deux tableaux sont comparables si ils contiennent les mêmes valeurs   si ils contiennent les mêmes valeurs avec le même nombre d'occurrences -- indépendamment de leurs nombres d'occurrences et de leurs positions.  
