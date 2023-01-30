#!/usr/bin/env python
# coding: utf-8

# (ch:rechercher)=
# # Rechercher
# 
# Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes`
# minutes minimum, PhL.

# In[1]:


# pour python<3.9
#from typing import list


# ## Objectif du chapitre
# 
# Ce chapitre présente des versions de deux algorithmes (déjà connus) pour _rechercher si une valeur est présente ou non dans un ensemble de valeurs_.
# Cet ensemble de valeurs est stocké dans _un tableau_ (1D ou nD selon le type de valeurs).
# 
# Au delà de la question de la recherche de valeur dans un ensemble, l'objectif est ici de _construire des versions itératives et récursives d'un **même algorithme**_.  
# 
# L'analyse de la complexité de ces traitements sera aussi réalisée ainsi ($\star$) qu'une illustration de preuve de terminaison et de correction de ces traitements.
# 
# Les algorithmes concernés sont :
# - la recherche séquentielle  
# - la recherche dichotomique -- lorsque les valeurs sont préalablement triées.

# ## Recherche séquentielle
# 
# ### Principes
# 
# **Objectif**  
# Rechercher si une valeur apparait dans un tableau de valeurs  
# Répondre _vrai_ si la valeur est dans le tableau, _faux_ sinon
# 
# **Hypothèse de départ**  
# Il existe une relation de comparaison entre deux valeurs : égalité. 
#     - on la note `==`  
# Aucune hypothèse sur les valeurs

# **Principe de la recherche séquentielle**  
# Parcourir _séquentiellement_ le tableau de valeurs et comparer à la valeur cherchée.
# 
# - séquentiellement : "valeur après valeur" selon un ordre simple induit par les indices des valeurs dans le t
#     - exemple : du début à la fin du tableau donc pour un ordre croissant des indices 
# - parcours complet : de 0 à `len(t)-1` 
# - parcours optimal : arrêt du parcours dès la valeur trouvée

# **Exemple pour la suite**.
# 
# Un tableau de 10 entiers aléatoirement compris entre 0 et 10 va illustrer notre propos.

# In[2]:


from random import randint, seed

n = 10
t = [0 for i in range(n)]

seed(2)
for i in range(n):
    t[i] = randint(0, n)
print(t)


# #### En-tête "modèle" de la fonction

# ```python
# def rech_seq(val: int, tab: list[int], dim: int) -> bool:
# ```
# - entrées : 
#     - _val_ : la valeur à chercher -- ici un `int`
#     - _tab_ : le tableau 1D qui contient les valeurs -- ici un tableau 1D représenté par une liste python 
#     - _dim_ : `len(tab)` le nombre de valeurs  
# 
# - sortie :
#     - booléen : _True_ ou _False_ 

# Cet en-tête de fonction fixe certaines caractéristiques des paramètres du problème. 
# En effet, la recherche s'effectue ici dans _un ensemble_ représenté par un tableau et _la valeur cherchée_ est un entier. 
# Ces paramètres ensemble et valeur pourraient être différents : par exemple la recherche peut s'effectuer dans une liste de nombres flottants, une chaîne de caractères, un dictionnaire ... 
# Il faudrait alors modifier l'en-tête pour ces types de données.

# Cet en-tête est donc un _modèle_ d'en-tête pour une fonction de recherche. 
# On peut voir _le type des valeurs_ et _la structure de stockage_ comme des paramètres de plus haut niveau d'abstraction de ce traitement. 
# Ceci correspond à la notion de _généricité_ ou de certaines formes de la notion d'héritage dans les langages (dits) objet. 

# ### Algorithmes itératifs

# #### Parcours complet
# 
# **Principe du parcours séquentiel "naif"**:  
# - On parcourt toutes les valeurs `tab[i]` pour `i = 0,.., dim-1`  
# - on compare à la valeur cherchée `val`  
# - on met à jour une variable booléenne `trouve` qui marque la présence ou non de `val`dans `tab`
# - A la fin du parcours, `trouve` indique si `val`a été trouvée ou non
#     - donc on initialise `trouve`à `False` avant de commencer le parcours  

# In[3]:


def rech_seq_for(val: int, tab: list[int], dim: int) -> bool:
    trouve = False
    for i in range(dim):
        if tab[i] == val:
            trouve = True
    return trouve


# Application :

# In[4]:


v = 1
print(v, "dans ", t, "?", rech_seq_for(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", rech_seq_for(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", rech_seq_for(v, t, len(t)))


# **Commentaires.** 
# 
# - Le parcours complet du tableau est d'autant plus inefficace que le nombre de valeurs inutilement parcourues est important : valeur cherchée trouvée tôt dans ce parcours et/ou taille du tableau élevée.   
# 
# - D'un point de vue de complexité, on identifie un meilleur cas (valeur présente tôt) qui n'est pas traité différemment d'un pire cas (valeur absente). 
# 
# - C'est une faiblesse de cette première solution.

# #### Parcours minimal
# 
# Même principe excepté :
# - la mise à jour de `trouve` permet d'arrêter le parcours _dès que_ `val`a été trouvée
# 
# Voilà une première version qui découle de la construction avec `for`.

# In[5]:


def rech_seq_while_v0(val: int, tab: list[int], dim: int) -> bool:
    trouve = False
    i = 0
    while i < dim and trouve == False:
        if tab[i] == val:
            trouve = True
        i = i + 1 
    return trouve


# Application :

# In[6]:


v = 1
print(v, "dans ", t, "?", rech_seq_while_v0(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", rech_seq_while_v0(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", rech_seq_while_v0(v, t, len(t)))


# La variable `trouve` n'est pas nécessaire comme l'illustre la version plus simple suivante.

# In[7]:


def rech_seq_while(val: int, tab: list[int], dim: int) -> bool:
    i = 0
    while i < dim:
        if tab[i] == val:
            return True
        i = i + 1 
    return False


# In[8]:


v = 1
print(v, "dans ", t, "?", rech_seq_while(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", rech_seq_while(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", rech_seq_while(v, t, len(t)))


# **Autre écriture de la condition du `while` où il faut être prudent** :
# Attention à l'ordre des tests dans la condition de la ligne 4

# In[9]:


def autre_rech_seq_while(val, tab, dim):
    i = 0
    # ordre incorrect qui va déclancher IndexError
    # while  (tab[i] != val) and (i < dim):
    #
    # ordre correct où la validité de l'indice est vérifiée avant de l'utiliser
    while (i < dim) and (tab[i] != val):
        i = i + 1 
    if i < dim:
        return True
    else:
        return False


# In[10]:


print(t)
v = 1
print(v, "dans ", t, "?", autre_rech_seq_while(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", autre_rech_seq_while(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", autre_rech_seq_while(v, t, len(t)))


# **Ecriture équivalente avec une boucle `for`**
# 
# La construction suivante permet le même traitement minimal au sein d'une boucle `for` 

# In[11]:


def rech_seq_for_ecourtee(val: int, tab: list[int], dim: int) -> bool:
    trouve = False
    for i in range(dim):
        if tab[i] == val:
            return True
    return trouve


# In[12]:


print(t)
v = 1
print(v, "dans ", t, "?", rech_seq_for_ecourtee(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", rech_seq_for_ecourtee(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", rech_seq_for_ecourtee(v, t, len(t)))


# #### Cas du tableau vide
# 
# Ce cas extrême mérite souvent une attention particulière.
# 
# - Les versions avec la boucle `for` avec la borne `len(t)` s'adaptent "automatiquement" à ce cas grâce à la fonction `range()` -- et retournent `False`.
# - En revanche, les écritures avec `while` ne sont pas satisfaisantes en l'état :
#     - la condition d'arrêt `i < dim` n'est jamais satisfaite si `dim == 0`.
#     - un traitement spécifique du tableau vide est toujours possible
# 
# On verra que l'analyse de la correction de cet algorithme donne une autre solution.

# In[13]:


def rech_seq_while_2(val: int, tab: list[int], dim: int) -> bool:
    '''traite le cas du tableau vide'''
    assert dim == len(tab)

    # cas du tableau vide
    if dim == 0:
        return False
    
    # autres cas
    i = 0
    while i < dim:
        if tab[i] == val:
            return True
        i = i + 1 
    return False


# In[14]:


v = 1
t_vide = []
print(v, "dans ", t_vide , "?", rech_seq_while_2(v, t_vide, len(t_vide)))


# ### Algorithme récursif

# **Principe**  
# 
# - _Récursion_ : Rechercher `val` dans `tab` de `0` à `dim-1`, c'est :
#     1. regarder si `val` est en première position du tableau `tab`, cad. en `tab[0]`,   
#     2. si c'est le cas, on a trouvé et on peut répondre : _terminaison_
#     3. si ce n'est pas le cas, on recommence _récursivement_ en 1. avec la partie restante de `tab`, cad. le sous-tableau "à droite" de la première position.  

# - _Syntaxe plus générale pour un traitement récursif_ :  
# On va introduire `g` (pour gauche) et `d` (pour droite) pour désigner le premier et le dernier+1 indice de `tab`, cad. `tab[g, d[`   
# On reprend la description précédente :
#     - Récursion : Rechercher `val` dans `tab` de `g` à `d` exclus, c'est :
#     1. regarder si `val` est en première position du tableau `tab`, c-a-d. en `tab[g]`,   
#     2. si c'est le cas, on a trouvé et on peut répondre : : _terminaison_
#     3. si ce n'est pas le cas, on recommence _récursivement_ (en 1.) avec le sous-tableau "à droite" de la première position, cad. `tab[g+1, d[`.   
#     

# - _Terminaison_ : 2 cas  
#     1. on a trouvé : item 2.  
#     2. si `tab` est vide, c-a-d. si `g >= dim` : on n'a pas trouvé
# 
# 
# - _Initialisation_ :   
#     1. `g = 0` et `d = dim` ou `len(tab)` en python

# **Mise en oeuvre**  
# 
# - On traite les terminaisons (`return` des lignes 4 et 6) avant l'appel récursif (avec le `return` de la ligne 8)   
# - L'initialisation correspond à l'appel récursif principal qui "passe" le problème à résoudre à l'algorithme de résolution.
#     - remarquons ici qu'on définit une fonction dont l'en-tête est similaire à celle des versions itératives : 3 paramètres (la valeur, le nom du tableau et sa taille)
#     - cette fonction _encapsule_ l'appel principal à la fonction récursive

# In[15]:


def rech_seq_rec_gd(val: int, tab: list[int], g: int, d:int) -> bool:
    '''recherche val dans tab[g,d['''
    if g == d:
        return False
    if t[g] == val:
        return True
    else:
        return rech_seq_rec_gd(val, tab, g+1, d)
    
def rech_seq_rec(val: int, tab: list[int], dim: int) -> bool:
    return rech_seq_rec_gd(val, tab, 0, len(tab))


# In[16]:


v = 1
print(v, "dans ", t, "?", rech_seq_rec(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", rech_seq_rec(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", rech_seq_rec(v, t, len(t)))


# <div class="alert alert-block alert-warning">
# L'ordre du traitement des terminaisons (lignes 3 et 5) est important : ici l'accès `t[g]` est susceptible de lever une exception (débordement de tableau). 
# </div>

# **Remarques :** 
# - Quelle version de recherche séquentielle (parcours complet vs. minimal) correspond à l'écriture récursive ici proposée ?  
#     - Ecrire l'autre version de façon récursive.  

# ## Recherche dichotomique dans un tableau trié  
# 
# Dans le cas où **les valeurs sont triées**, on peut introduire un traitement plus efficace.  
# Ce traitement, _par dichotomie_, peut s'écrire de façon itérative ou récursive.  
# On va ainsi illustrer l'application du principe _diviser pour régner_.  

# ### Principes 
# 
# **Objectif**  
# Rechercher si une valeur apparait dans un tableau de valeurs **triées**  
# Répondre _vrai_ si la valeur est dans le tableau, _faux_ sinon
# 
# **Hypothèse de départ**  
# Les valeurs sont rangées de façon **triée** (on ne le dira jamais assez !)  
# par ordre croissant par exemple 

# Trions `t` pour continuer selon ces hypothèses.

# In[17]:


# En attendant le chapitre suivant, utilisosn les fonctions prédéfinies de python
t.sort()
print(t)


# **Principe**  
# Un algorithme _diviser pour régner_ où chaque division réduit la recherche à un ensemble de taille moitié, l'autre ensemble n'étant plus considéré  
# 
# 1. diviser :
#   -  on partage en 2 par la moitié le tableau trié
#  
# 1. régner :
#     - on compare la valeur cherchée à la valeur médiane du tableau 
#     - si besoin, on en déduit la moitié gauche ou droite du tableau qui contient la valeur cherchée 
#     - on recommence la recherche sur la "bonne moitié" 

# ### Algorithme itératif
# 
# **Analyse**
# 
# Il faut :
# 1. _itérer_ :
#     - le test de la valeur de l'indice milieu 
#     - le découpage en 2 du tableau  
# 
# 2. _arrêter_ :
#     - quand on a trouvé la valeur cherchée
#     - ou si la taille du tableau est égale à zéro (tableau vide) 
# 
# 3. _retourner_ un booléen

# **Codage**
# 
# - L'appel s'effectue en indiquant :  
#     * la valeur cherchée  
#     * le tableau  
#     * sa taille  
# 
# - Le nombre d'itérations n'est a priori pas connu (il est borné en revanche)  donc boucle `while`
# - L'indice milieu est obtenu avec une division entière `//` sachant que le milieu entre $a$ et $b$ est $(a+b)//2$  
#     - Rappel : la division entière `//` retourne le quotient de la division euclidienne  
# - D'une itération à l'autre :
#     * choisir la partie gauche ou droite du tableau revient à changer l'indice de début et de fin du prochain tableau à traiter : on introduit des indices `g`, `d` et `m` pour désigner les indices de gauche, de droite et du milieu   
#     * la taille est divisée par 2  

# In[18]:


def dichotomie_iterative(val, t, dim_t):
    '''recherche dichotomique : version itérative
    entrées - val :int cherché
            - t : tableau d'int de taille dim_t, trié par ordre croissant
    sortie : vrai si val est dans t, faux sinon
            
    '''
    g = 0          # indice de gauche du tableau exploré
    d = dim_t - 1  # indice de droite du tableau exploré
    
    while g <= d:
        m = (g + d)//2   # indice milieu de t[g,d]
        if t[m] == val:
            return True
        elif t[m] > val: # val est dans la partie gauche : t[g,m-1]
            d = m - 1
        else:            # val est dans la partie droite : t[m+1,d]
            g = m + 1
    return False               


# <div class="alert alert-block alert-warning">
# Ici aussi, l'ordre du traitement des terminaisons (lignes 14 et 16) est important : l'accès `t[m]` est susceptible de lever une exception (débordement de tableau). 
# </div>

# In[19]:


v = 1
print(v, "dans ", t, "?", dichotomie_iterative(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", dichotomie_iterative(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", dichotomie_iterative(v, t, len(t)))


# ### Algorithme récursif
# 
# **Analyse**  
# 
# 1. Récursion 
#     * il faut appeler récursivement la recherche sur le **sous-**tableau (gauche ou droite) qui va bien  
#     
# 2. Terminaison : 2 cas  
#     * on a trouvé la valeur cherchée
#     * le tableau est vide  

# **Codage**
# 
# Récursion : "le sous-tableau (gauche ou droite) qui va bien"
# 
# * il faut pouvoir préciser les indices gauche et droit du sous-tableau traité
#     - donc paramètres formels : `g` et `d`
# * et sa taille (parce qu'on manipule un tableau)
#     - donc paramètre formel `n` 
#     
# Rmq.: A la place de `n`,  on pourrait déduire la taille effective du tableau traité à partir de `g`et `d`. Mais on convenu d'ajouter systématiquement la taille d'un tableau passé en argument d'un sous-programme.  

# In[20]:


def dichotomie(val: int, t: list[int], dim_t: int, g: int, d: int) -> bool:
    '''recherche dichotomique : version récursive
    recherche val dans t[g, d] et retourne True ou False
    entrées. val : int, t: tableau d'int de taille n,
    g, d : int indices gauche et droite
    '''
    if g > d:
        return False # t est vide
    m = (g + d) // 2 
    if t[m] == val:
        return True
    elif val < t[m]: # val est dans la partie gauche
        dim_t = (m-1) - g + 1 
        return dichotomie(val, t, dim_t, g, m-1)
    else:            # val est dans la partie droite
        dim_t = d - m
        return dichotomie(val, t, dim_t, m+1, d)
        
def dichotomie_recursive(val: int, t: list[int], dim_t: int) -> 0:
    '''recherche dichotomique de val dans t de taille dim_t
    pour ressembler ) la version iterative en utilisant dichotomie
    '''
    return dichotomie(val, t, dim_t, 0, dim_t-1)
    


# <div class="alert alert-block alert-warning">
# Ici encore, l'ordre du traitement des terminaisons (lignes 10 et 12) est important : l'accès `t[m]` est susceptible de lever une exception (débordement de tableau). 
# </div>

# In[21]:


v = 1
print(v, "dans ", t, "?", dichotomie_recursive(v, t, len(t)))
v = 3
print(v, "dans ", t, "?", dichotomie_recursive(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", dichotomie_recursive(v, t, len(t)))


# **Remarque**
# * Observer et bien comprendre pourquoi le traitement récursif `dichotomie` comporte 4 `return`
#     - Essayer par exemple de supprimer les 2 derniers
# * L'_encapsulation_ de `dichotomie` dans `dichotomie_recursive` permet un appel de plus haut niveau similaire à la version itérative. Dans l'absolu, il n'est pas nécessaire : c'est l'_appel principal_ de `dichotomie` qui résout le problème..
# 
# 
# **Exercices**
# * Instrumenter le code (ajouter des `print()` :) pour exhiber l'évalution de `g`, `d` et `m`
# * Effectuer les 2 recherches précédentes sans utiliser `dichotomie_recursive` mais seulement `dichotomie`
# 

# ## Complexité des algorithmes de recherche
# 
# Nous allons montrer que la recherche séquentielle est un algorithme de complexité linéaire tandis que la recherche dichotomique est de complexité logarithmique. Ce qui justifie l'intérêt l'approche dichotomique pour des tableaux **triés** de grande taille.   

# ### Les paramètres de l'analyse de la complexité
# 
# **Paramètre de complexité :** le nombre de valeurs présentes, c-a-d. la taille `dim` du tableau de stockage. 
# 
# Notons **$n$** ce paramètre et `t` ce tableau.
# 
# **Mesure de la complexité :** la comparaison `t[i] == val` dans le cas séquentiel itératif, ou  `t[g] == val` dans le cas séquentiel récursif ou enfin `t[m] == val` dans le cas dichotomique.
# 
# On va donc chercher la quantité $C(n)$  qui compte le nombre de ces comparaisons comme une fonction de la taille $n$ du tableau de stockage. 

# ### Analyse de la recherche séquentielle itérative
# 
# Le nombre de comparaisons dépend de la position de `val` dans `t` : 
# -  meilleur cas : `val` est présent à l'indice 0 et 1 comparaison suffit
# -  pire cas : `val` est absent de `t` donc le parcours du tableau est complet (quelque soit l'écriture) et comporte $n$ comparaisons
# -  dans le cas général : traitement effectué avec un nombre de comparaisons inférieur ou égal à $n$
# 
# Donc $C(n) \le n$.
# 
# La complexité en temps de la recherche séquentielle dans un tableau de $n$ valeurs est au pire **linéaire en $n$**.
# 
# Sa complexité asymptotique est telle que : $C(n) = \cal{O}(n)$.

# ### Analyse de la recherche dichotomique, version itérative
# 
# La dichotomie effectue des divisions successives de la taille du tableau dans laquelle la recherche est effectuée. Il est _commode_ de commencer l'analyse avec $n = 2^p$ pour obtenir des tailles successives entières.
# 
# Remarquons dès maintenant :
# - si $n = 2^p$ alors $p = \log_2(n)$
# - si $2^p \le n < 2^{p+1}$ alors $p =$ `int`($\log_2(n)$).
# 
# Cette dernière ligne explicite l'intérêt de commencer avec $n = 2^p$. 

# **Principe de l'analyse**.
# 
# Le nombre de comparaisons dépend de la position de `val` dans `t` : 
# 
# Meilleur cas : `val` est présent à l'indice `m == n//2` et 1 comparaison suffit
# 
# Pire cas : `val` est absent de `t`
# - la recherche s'effectue successivement sur des tableaux de taille $n, n/2, n/4, \dots, 4, 2, 1$ jusqu'à terminaison avec `g == d`, c-a-d. un tableau vide, soit donc $p = \log_2(n)$ divisions par 2 avant terminaison
# - pour chacune de ces tailles, une comparaison `t[m] == val` est effectuée
# 
# Donc $C(n) = p = \log_2(n)$ dans le pire des cas pour $n = 2^p$.
# 
# Et pour le pire cas d'une taille $n$ quelconque, `int`$(\log_2(n)) \le C(n) <$  `int`$(\log_2(n))+1$. 
# 
# La complexité en temps de la recherche séquentielle dans un tableau de $n$ valeurs est au pire majorée par le **logarithme de $n$**.
# 
# Sa complexité asymptotique est telle que : $C(n) = \cal{O}(\log(n))$.
# 

# **Rmq.** 
# Les valeurs successives de la taille des tableaux traités sont celles de la suite géométrique de raison $1/2$  et de premier terme $n$.
# Une telle suite converge vers 0. 
# Ce qui permettra de prouver la terminaison de l'algorithme. 

# **Exercice.** 
# 
# La complexité logarithmique de la recherche dichotomique en version itérative peut aussi se démontrer en prouvant (par récurrence) que la taille de l'intervalle après $k$ itération de $[g, d[$, $|d - g| < n / 2^k$. 

# ### Analyse de la recherche dichotomique, version récursive
# 
# On retrouve facilement la complexité logarithmique de la recherche dichotomique dans sa version récursive. 
# 
# On simplifie l'analyse en observant un pire cas et $n = 2^p$.
# 
# Soit $C(n)$ le nombre de comparaisons effectuées par la recherche dichotomique dans $n$ valeurs.
# 
# Une étape de récursion de cette recherche :
# - effectue une comparaison : `t[m] == val`
# - "appelle" la récursion pour $n/2$.
# 
# La terminaison est obtenue dans le pire cas pour $C(1) = 1$ (ou $C(0) = 0$).
# 
# Soit donc, directement :
# $C(n) = 1 + C(n/2)$ et $C(1) = 1$.
# 
# On développe cette relation de récurrence pour $n, n/2, ..., 1$. 
# 
# Ce qui donne :
# $C(n) = 1 + 1 + \dots + 1 = \log_2(n)$.
# 
# On remarque que l'analyse de la version récursive conduit naturellement à une relation de récurrence.

# **Exercice**. 
# 
# De façon similaire, retrouver la complexité linéaire de la recherche séquentielle en version récursive. 

# ## ($\star$) Preuves de terminaison et de correction 
# 
# Nous illustrons comment prouver :
# - qu'un algorithme termine
# - qu'un algorithme est correct, c-a-d. qu'il termine en trouvant bien la solution du problème.
# 

# ### Terminaison de la recherche séquentielle : version itérative
# 
# Il s'agit de montrer que l'exécution de l'algorithme termine son exécution quelques soient les entrées de l'instance. Dans un premier temps, on ne s'intéresse pas à la validité de la solution ainsi trouvée.
# 
# Dans le cas d'un algorithme itératif, une technique classique pour prouver la terminaison de l'algorithme est d'identifier **un variant de boucle** ou _variant de l'itération_.
# 
# **Variant de boucle** : une quantité _entière_ et _positive_ qui _décroît_ strictement à chaque itération de la boucle.
# 
# La terminaison de l'algorithme itératif est prouvé si ce _variant arrête la répétition_ (la boucle) -- et ce quelques soient les entrées de la répétition.
# 

# Reprenons une version itérative de la recherche séquentielle.
# 
# Celle avec le `while` est la plus simple pour commencer.
# 
# ```python
# def rech_seq_while(val: int, tab: list[int], dim: int) -> bool:
#     i = 0
#     while i < dim:
#         if tab[i] == val:
#             return True
#         i = i + 1 
#     return False
# ```

# **Exemple de preuve de terminaison**
# 
# Aucune quantité de l'algo ainsi écrit est _explicitement_ un variant.
# 
# Cependant  La condition d'arrêt `i < dim` permet de ré-écrire une variable d'itération **`j = dim - i`** que l'on va prouver être un variant de la boucle.
# - avant la première itération boucle : l'entier `j == dim` qui est positif si le tableau `t` n'est pas vide
# - chaque itération de la boucle décrémente `j` de 1 (car elle incrémente `i` de 1)
# - `j` est donc un entier, positif qui décroît par pas de 1 à partir de `dim`,
# - **donc, à terme** (i.e. à un certain moment), `j` vaut  0.
#     - mathématiquement les valeurs de `j` suivent une suite arithmétique de raison -1 et de premier terme  `dim` > 0. 
# - Quand `j == 0`, `i == dim`, valeur qui ne vérifie pas la condition de test de la ligne 5 et qui arrête donc la répétition.
#     
# On a bien identifié un variant qui prouve la terminaison de cette recherche séquentielle (version itérative `while`).   
#     
# **Rmq.** 
# - Ceci est aussi vrai pour un tableau vide : `dim == 0`.
# - Ce qui permet d'écrire une solution valide avec tout tableau même vide, sans traitement spécifique de ce cas.

# Ainsi, on écrit l'algorithme avec une répétition `while` contrôlée par ce variant `j` : c-a-d. en prenant `j` comme indice, initialisé à `dim` et la condition d'arrêt `j > 0`. 
# Cette ré-écriture est un changement de variable "classique".  

# In[22]:


def rech_seq_while_variant(val: int, tab: list[int], dim: int) -> bool:
    '''recherche équentielle itérative : s'il fallait n'en garder qu'une !'''
    assert dim == len(tab)

    j = dim
    while j > 0:
        if tab[j - 1] == val:
            return True
        j = j - 1 
    return False


v = 0
print(v, "dans ", t, "?", rech_seq_while_variant(v, t, len(t)))
v = 7
print(v, "dans ", t, "?", rech_seq_while_variant(v, t, len(t)))
v = 10
print(v, "dans ", t, "?", rech_seq_while_variant(v, t, len(t)))

# cas du tableau vide
v = 1 # par exemple
t_vide = []
print(v, "dans ", t_vide, "?", rech_seq_while_variant(v, t_vide, len(t_vide)))


# **Exercice** 
# 
# - Adapter cette preuve de terminaison à la version avec une boucle `for`.
# 

# ### Correction de la recherche séquentielle :  version itérative
# 
# Il s'agit maintenant de prouver que l'algorithme (qui termine) calcule la solution attendue -- et ce quelques soient les instances de problèmes concernées. 
# 
# La preuve de la correction d'un algorithme itératif repose souvent sur la notion **d'invariant de boucle**.
# 
# Un **invariant de boucle** est une propriété vérifiée tout au long de l'exécution d'une boucle et qui exhibe la correction de l'algorithme à la terminaison de la boucle.
# 
# La preuve s'effectue en 3 étapes.
# En notant (P) cette propriété :
# 1. **initialisation** : (P) est vraie avant la première itération du corps de la boucle
# 2. **conservation** : On suppose (P) vraie avant la i-ème itération. On montre que la i-ème itération conserve (P).	
# C-a-d. que (P) vraie avant la i-ème itération reste vraie avant la (i+1)-ème itération.
# 3. **terminaison** : (P) est vraie après la dernière itération. 

# En pratique :
# - la propriété appliquée à la sortie de boucle (terminaison) prouve que celle-ci a effectué le traitement prévu 
#     - exemple : la recherche séquentielle étant "réduite" à une boucle, son invariant prouvera que la solution retournée par le traitement est exacte : soit `True` si la valeur est présente dans `t` et `False` sinon.
# - l'initialisation, c-a-d. avant la boucle, prouve que les variables sont correctement initialisées
# - la conservation et la terminaison prouvent que l'indice de boucle et le nombre d'itérations sont corrects.
# - initialisation et conservation constituent une preuve par récurrence "classique"

# Prouvons que la propriété suivante :
# > (P) Avant l'itération `i`, si `val` est présent dans `t`, il est présent dans `t[i, dim-1]`
# 
# est un invariant de la boucle de la recherche séquentielle :
# ```python
#     i = 0
#     while i < dim:
#         if t[i] == val:
#             return True
#         i = i + 1 
#     return False
# ```
# La contraposée de (P) est :
# > (P) Avant l'itération `i`, si `val` est absent de `t[i, dim-1]`, il est absent de `t`.

# 1. Initialisation.
# Avant la première itération, `i==0` et `t[0,dim-1]` est le tableau tout entier. Donc (P) est trivialement vraie.
# 
# 2. Conservation.
# D'après (P), avant la i-ième itération pour `val` présent dans `t`, `val` est dans `t[i, dim-1]`.
# Donc `val == t[i]` ou `val = t[j]` pour `i+1 <= j < dim`.    
# - si `i < dim`, l'itération s'effectue et `t[i]` est valide.
#     - si `t[i] != val`, `val` est donc dans `t[i+1, dim-1]` d'après (P). 
#     `i` est incrémenté donc (P) est bien conservée après l'itération `i`.   
#     - si `t[i] == val`, `val` est bien dans `t[i, dim-1]`. `i` n'est pas modifié, l'itération s'arrête  et (P) reste vrai.
# 
#     
# 3. Terminaison : 2 cas.
# - Si  `i==dim` alors la conservation de (P) à l'itération précédente dit que si `val` est présent dans `t`, il est présent dans `t[dim, dim-1]`, ce qui est impossible car `t[dim, dim-1]` est vide. 
# Donc `val` est absent dans `t` selon la contraposée de (P). 
# - Sinon (cas déjà vu), `val` est présent en position `i` dans `t` (et est bien dans `t[i, dim-1]`).   

# **Rmq.** 
# - L'identification de l'invariant est plus difficile que sa preuve. 
# - **L'invariant est une propriété caractéristique de l'algorithme itératif**. 
#     - Dit simplement, _l'invariant formalise "ce qui fait marcher" l'algorithme_.  
#     - Il n'y a pas qu'un seul invariant possible, bien sûr.

# ### Terminaison de la recherche dichotomique
# 
# Lors de l'analyse de complexité de la recherche dichotomique, on a indiqué **pour le pire cas** :
# - que la condition d'arrêt `g >= d` _commune aux formulations itérative et récursive_
#  correspond à un tableau vide, i.e. de taille 0,
# - que la taille `d - g` des tableaux successifs de la dichotomie suivaient la suite géométrique de raison $1/2$  et de premier terme $n$.
# 
# Cette suite de termes positifs converge vers 0. 
# Ce qui prouve la terminaison de l'algorithme par vérification de la condition d'arrêt :
# - de façon explicite dans le cas récursif
# - en considérant `d-g` (entier positif) comme variant dans le cas itératif. 
# 

# ### ($\star\star$) Correction de la recherche dichotomique : version itérative
# 
# Prouvons que la propriété suivante est un invariant de la boucle de la recherche dichotomique.
# 
# Invariant (P) : 
# > si `val` est présent dans `t` alors il est dans `t[g,d]`.
# 
# Avant de prouver (P), énonçons _sa contraposée_ :
# > si `val` n'est pas dans `t[g,d]` alors `val` n'est pas présent dans `t`.   
# 
# Par commodité, on rappelle l'algorithme concerné (sans la spécification de la fonction).
# 
# ```python
#     g = 0          # indice de gauche du tableau exploré
#     d = dim_t - 1  # indice de droite du tableau exploré    
#     while g <= d:
#         m = (g + d)//2   # indice milieu de t[g,d]
#         if t[m] == val:
#             return True
#         elif t[m] > val: # val est dans la partie gauche : t[g,m-1]
#             d = m - 1
#         else:            # val est dans la partie droite : t[m+1,d]
#             g = m + 1
#     return False   
# 
# ```
# 
# Dans l'énoncé de (P), "est présent" correspond à la valeur renvoyée `True`, et inversement pour la contraposée.  

# Sans perdre de généralité, on facilite l'écriture de la preuve en supposant que toutes les valeurs de `t` sont différentes (ce qui donne des inégalités strictes) et on note `n = dim_t`.
# 
# Appelons _pivot_ la valeur de `t[m]` où `m = (g+d)//2`.   
# Chaque itération effectuée teste donc si la valeur du pivot est celle cherchée, et sinon continue le traitement sur une des deux parties à droite ou à gauche du pivot (d'où son nom).
# 
# La preuve de l'invariant repose sur la propriété simple suivante :
# - les valeurs "à gauche" du pivot sont inférieures au pivot,
# - et inversement pour celles "à droite" du pivot.
# 
# Ce qui ce formalise comme suit :
# - `t[i] < pivot` pour `g <= i < m`
# - `t[i] > pivot` pour `m < i <= d`
# 
# ![](./fig/dichotomie.png)

# **Preuve de (P).**
# 
# Globalement, l'algorithme met à jour `g` ou `d` jusqu'à avoir trouvé `val` ou ... être sûr de ne plus pouvoir le trouver. Ces 4 aspects sont les clés de la preuve de : 
# > (P) si `val` est présent dans `t` alors il est dans `t[g,d]`.
# 
# 1. Initialisation 
# - Avant la première itération, `g==0` et `d==n-1`donc `t[g,d] == t[0,n-1]`, c-a-d. le tableau `t` (en entier). Donc (P) est (trivialement) vraie.
# 
# 2. Conservation : 
# Au début d'une itération donnée, (P) assure que si `val` est présent, il existe `j` tel que `t[j]==val` avec `g <= j <= d`.
# - si `j == (g+d)//2 == m` alors ni `g` ni `d` sont modifiés par l'itération et (P) reste donc vraie au début de l'itération suivante avec `g <= m <= d`. 
# - si `val < pivot (== t[m])` alors `d=m-1`. Montrons que `val` présent est dans `t[g, m-1]`. On sait que `t[i] < pivot` pour `g <= i < m` et `t[i] > pivot` sinon. Donc `val < pivot` présent est bien dans `t[g,m-1]==t[g,d]` et non dans le reste de `t`.
# (P) reste vraie au début de l'itération suivante.
# - si `val > pivot (== t[m])` alors `g=m+1` et cette fois `val` est présent dans `t[m+1,d]`. En effet, `t[i] > pivot` pour `m < i <= d` et `t[i] < pivot` sinon.
# Donc `val > pivot` est présent dans `t[m+1,d] == t[g,d]` et non dans le reste de `t`. (P) reste aussi vraie au début de l'itération suivante.
# 
# 3. Terminaison : La boucle `while` se termine dans 2 cas.
# - cas a : on a trouvé `m` dans tel que `val == t[m]` sans modifier `g` et `d` depuis l'itération précédente. Donc `val` est présent en `t[m]` avec `g <= m <= d` donc (P) est vrai pour `t[g,d]` après la dernière itération.
# - cas b : si `g > d`, `t[g,d]` est vide donc `val` n'est pas dans `t[g,d]`. La conservation de la contraposée de (P) prouve que `val` n'est pas présente dans `t` après la dernière itération. Ce qui prouve (P) dans ce cas de terminaison aussi.

# **Conclusion**.
# Les 2 cas de la terminaison prouvent la correction de l'algorithme étudié.

# **Rmq.** 
# 
# - Dans la preuve précédente, la validité de (tous les) `t[g,d]` est implicite :  aucun indice ne se trouve à l'extérieur du tableau `t[0, dim_t]`. Si besoin, on peut compléter chaque encadrement avec `0 <= g` et `d < dim_t`, se convaincre que `0 <= g <= m <= d < dim_t` et compléter la formulation de l'invariant comme suit :
# > (P) si `val` est présent dans `t` alors il est dans `t[g,d]` avec `0 <= g` et `d < dim_t`.

# ## Synthèse
# 
# - Deux algorithmes simples de recherche : séquentielle et dichotomique sur tableau trié
#     - complexité linéaire vs. logarithmique  
#     - meilleurs cas, pire cas  
# - Exemples d'écritures itératives ou récursives du même algorithme  
#     - en-têtes identiques par encapsulation de l'appel récursif principal
# - Exemples d'analyse de complexité
# - ($\star$) Exemples de preuve de terminaison et de correction
#     - algo itératif : variant et invariant de boucle 
# 
