#!/usr/bin/env python
# coding: utf-8

# # Sous-programme et affectation -- aspects avancés
# 
# version 2021, PhL (v2.2)

# Nous abordons maintenant les aspects des fonctions qui dépendent des langages de programmation. Nous insistons surtout sur les choix de python3.
# 
# **Rappel.**  Le terme _paramètre effectif_, et son compagnon _paramètre formel_, sont des termes "langage-indépendant". En python, le terme _argument_ est utilisé à la place du terme _paramètre effectif_. Ainsi argument et paramètre effectif sont des synonymes, et seront utilisés comme tel dans ce qui suit.
# 

# ## Le passage des paramètres : un problème générique
# 
# Le corps de la fonction ne connaît que les paramètres formels.  
# L'appel de la fonction définit les paramètres effectifs . 
# - Comment le paramètre effectif devient-il connu par la fonction appelée ?   
# - Qu'est-ce qui est connu dans l'appel, en particulier _lorsque le paramètre effectif est une variable_ ?
#     - _la valeur_ du paramètre effectif  ? 
#     - _la variable_ paramètre effectif  ?  
#     
# Se sont les questions du passage de paramètres appelant->appelé
# 
# ### Comment est transmis un paramètre effectif ?
# 
#  * Si c'est une constante :  `y = f(3)`  
#     OK : la valeur constante est connue et utilisée dans l'appel  
#     
#  * Si c'est une variable : `x = 3 ; y = f(x)`  
#     - `f` connaît la valeur de `x` et seulement sa valeur ?
#     - `f` connaît la variable `x`, ce qui permet de _lire_ sa valeur et aussi de _la modifier_ a priori ?
#     
#  * Cette distinction s'étend aux paramètres (formels et effectifs) de type composé comme les tableaux, les listes, les chaînes de caractères, les enregistrements (ou structures) ... 
#  
# 
# ### Deux modes _matériels_ de passage des paramètres
# 
# 1. __passage par valeur__ ou __copie__ :  seules les _valeurs_ des paramètres effectifs sont connus par la fonction.  
# Ainsi, **les paramètres effectifs**, qui sont des variables dans le programme appelant, **ne sont pas modifiés**. Bien sûr, ce n'est pas le cas du/des paramètre/s de sortie).
# 
# 2. __passage par adresse__ ou __référence__ : les _adresses_ des paramètres effectifs sont connues et sont manipulées par la fonction.  
# Ces paramètres effectifs sont donc _les_ variables de l'appelant -- et aussi de l'appel.  
# La fonction peut donc **modifier les variables de l'appelant _indépendamment_ du `return`**.
# 
# <div class="alert alert-block alert-info">
# Pros/cons : la copie de la valeur d'une "grosse" variable coûte plus cher que la copie de son adresse (c'est un `int`)  
# </div>
# 
# Les modes appliqués dépendent :   
# - des langages de programmation 
# - du _type_ des paramètres
# 
# C-a-d. que les 2 modes peuvent coexister dans un même langage.  
# 

# ### Trois modes _logiques_ de passage des paramètres
# 
# Certains langages (Ada par exemple) se sont dégagés des aspects matériels pour définir des modes _logiques_.  
# Bien sûr, l'implantation de ces modes logiques repose sur l'une ou l'autre des 2 modes physiques.  
# 
# 1. mode `in` : le paramètre est uniquement utilisé en lecture, c-a-d. seule la transmission de sa valeur est nécessaire
# 2. mode `in-out` : le paramètre est utilisé en lecture et en écriture, ici encore son adresse est nécessaire dans l'appel  
# 3. mode `out` : le paramètre est uniquement utilisé en écriture, c-a-d. sa valeur est (formellement) inconnue dans la fonction ; cette dernière détermine sa valeur et la transmet (par valeur ou par adresse) à l'appelant.
# 
# Ces modes sont facilement vérifiables lors de la compilation. 
# Le mode `in` correspond aux paramètres d'entrée d'une fonction.
# Le mode `out` correspond à la valeur retournée par une fonction.
# le mode `in-out` correspond aux paramètres d'une _procédure_ : les paramètres effectifs existent avant l'appel, celui-ci les modifient et ils subsistent au retour dans l'appelant.

# ## Et pour python ?
# 
# Le [tutoriel python.org](https://docs.python.org/fr/3/tutorial/controlflow.html#id2) dit :
# > Les paramètres effectifs (arguments) d'une fonction sont introduits dans la table de symboles locale de la fonction appelée lorsqu'elle est appelée ; par conséquent, __les passages de paramètres__ se font par valeur, la valeur étant toujours une __référence à un objet__, et non la valeur de l'objet lui-même.
# 
# Rassurez-vous : cette définition est difficile à comprendre _en l'état_. 
# La suite de ce chapitre va permettre de mieux voir de quoi il s'agit.  
# 
# Mentionnons qu'**en python**, le passage de paramètres est en fait similaire à celui de l'_affectation_. 
# Il nous faut donc détailler ce qu'il y a "derrière" l'affectation en python.
# C'est l'objet de la [section suivante](#revisiter_les_variables_et_l'affectation).
# 
# Cependant indiquons dès maintenant **ce qu'il faut retenir** concernant le passage de paramètres.

# <div class="alert alert-block alert-info">
#     
# Le passage des paramètres ( et de l'affectation ) en python <b>dépend</b> du caractère <b>mutable</b> ou <b>non mutable de l'argument</b> (i.e. paramètre effectif) concerné.
# 
# </div>

# <div class="alert alert-block alert-info">
# 
# Un paramètre effectif <b>non mutable</b> est traité comme une <b>variable locale</b> à la fonction. 
# 
# <ul>
# <li> Ainsi la variable argument est connue dans la fonction mais elle <b>n'est pas modifiée dans l'appelant</b> par le traitement de la fonction
# </li>
#     <li> Il n'y a <b>pas d'effet de bord</b> de la fonction sur un paramètre effectif <b>non mutable</b>. 
# </li>
#     </ul>
#     
# </div>
#     

# <div class="alert alert-block alert-info">
#     
#     
# Un paramètre effectif <b>mutable</b> est "entièrement et directement accessible" par la fonction, comme une variable globale de l'appelant.     
#     
# <ul>    
# <li>  Ainsi une variable-argument mutable <b>pourra être modifiée dans l'appelant</b> par le traitement de la fonction appelée.</li>
# <li> Un paramètre effectif <b>mutable d'une fonction est susceptible d'un <em>effet de bord</em></b> suite à l'appel de la fonction. </li>
# </ul>    
# 
# </div>

# Dans ce dernier cas (argument mutable), une variable-argument peut être modifiée partiellement ou complètement. Par exemple, une liste peut-être allongée, écourtée, concaténée, ses valeurs peuvent être modifiées globalement ; ce qui sera différent de modifications ponctuelles de certaines de ses valeurs.  

# <div class="alert alert-block alert-info">
# 
# <ul> 
# <li>Une <b>modification partielle</b> d'une variable-argument mutable et <em>non concernée par le `return`</em>  provoquera un <b>effet de bord</b> malvenu dans l'appelant.</li>
# <li> Une modification complète de cet argument mutable n'aura pas un tel effet.</li>
# </ul>    
# 
# </div>   

# En pratique, il est très fortement conseillé d'éviter tout effet de bord d'une fonction _qui n'est pas une procédure_. 
# **Il appartient au programmeur d'être attentif au caractère mutable ou non mutable des paramètres des appels de fonctions** -- surtout dans le contexte de typage dynamique de python : rappelons que les annotations de type des paramètres ne sont que des indications pour le lecteur ou des outils spécialisés mais sont ignorées de l'interpréteur python.   

# ## ($\star$) Variable et affection : aspects avancés 
# 
# <div class="alert alert-block alert-success">
#     Cette section relève de <b>l'objectif 20</b>
# </div>
# 
# Commençons par revenir sur les notions de __variable__ et d'__affectation__.
# Puis comment ces notions existent en python.
# 
# ### Notions importantes
# 
# #### Variable, valeur, espace de stockage, adresse en mémoire, référence
# 
# - une _variable_ permet d'accéder, en lecture ou en écriture, à une _valeur_ qui est stockée en mémoire
#     - une _variable_ est définie par son _identifiant_ : son nom de variable : `n, t, ma_liste, ...`  
# - une _valeur_ est stockée à un emplacement en mémoire aussi appelé _espace de stockage_
#     - il est unique et test repéré par son _adresse_  
#     - une adresse est (similaire à) un `int`
#     - la taille de l'espace mémoire dépend du type des valeurs à stocker : `int` (par exemple 32 bits) vs `float`(64 bits) vs. une `list` de `float` 
# 
# Ainsi l'identifiant d'une variable peut-être vue comme un symbole associé à un espace de stockage.  
# L'identifiant de la variable est ainsi **une référence** à un espace de stockage.
# 
# Attention :
# 
# - la difficulté de la notion de variable vient du fait que ce terme désigne, selon les cas, la valeur stockée en mémoire ou l'espace de stockage lui-même.  
# - la notion de _référence_ prend des sens différemment subtils selon les langage de programmation.  
#   

# #### Affectation et évaluation  
# 
# L'_affectation d'une valeur à une variable_ correspond à une modification de l'espace de stockage associé à la variable.  
# 
# - La _valeur_ affectée est le résultat de l'_évaluation_ du membre du droite de l'affectation.  
# - Ce membre de droite peut être :
#     - une valeur d'initialisation : `x = 3` ou `t = [1,2,3]`, 
#     - une variable : `x = y`, 
#     - une expression : `x = y + 5`, 
#     - un appel de fonction `x = cos(alpha)`
#     - ou d'autres combinaisons plus compliquées.  
# 
# Dans tous les cas, l'évaluation retourne _une valeur_.
# 
# Mais cette valeur peut prendre deux formes très différentes que nous introduisons avec l'exemple de l'affectation  
# > `x = y` où `x` et `y` sont deux variables.
# 
# 
# L'association variable `x` <-> variable `y` peut être en effet réalisée de 2 façons :
# - par **copie** : la variable `x` prend comme valeur _la valeur_ de `y` (la répétition de "valeur" est voulue)  
#     - la valeur de `y` est dupliquée à une nouvelle adresse mémoire
#     - la valeur à cette nouvelle adresse est maintenant accessible par l'identifiant `x`.  
# - par **référence** : la variable `x` prend comme valeur _l'adresse de la valeur de `y`_ (emplacement mémoire où est stockée la valeur de `y`)  
#     - la valeur de `y` n'est _pas dupliquée_  
#     - `x` et `y` référencent _le même endroit en mémoire._
# 
# Dans les 2 cas :  
# - la valeur de `x` avant l'affectation, si il y en avait une, est perdue.  
# 

# #### Déclaration _vs._ affectation
# 
# Dans la plupart des langages de programmation **mais pas en Python**, une variable doit être déclarée _avant_ d'être utilisée.  
# 
# Typiquement, la déclaration d'une variable contient la définition de son identifiant, _de son type_, d'une valeur initiale (l'initialisation) et éventuellement d'autres propriétés diverses.  
# 
# Une fois déclarée, la variable existe.
# _Affecter une valeur à cette variable_ est une des premières actions que l'on effectue avec cette variable.
# 
# **En python** : 
# > Pas de déclaration    
# > Une variable est définie (elle commence à exister) par sa première affectation.   
# > Cette première affectation définit le type de cette variable et sa valeur (et donc son caractère mutable ou non mutable).
# 
# Une variable python _est donc créée par l'affectation d'une valeur_.  

# ### Variables et affectation en python
# 
# #### Variables en python : mutable ou non mutable ?
# 
# On a écrit qu'une variable python est une référence. 
# Mais une référence à quoi ? A une valeur ? A une adresse de la mémoire ?
# 
# Les deux cas existent en python et dépendent du caractère mutable ou non mutable de la variable.  
# 
# <div class="alert alert-block alert-info">
# 
# <ul> 
# <li>Une variable non mutable est une référence à une valeur.  </li>
# <li>Une variable mutable est une référence à l'adresse d'un espace de stockage. </li>
# </ul>
# 
# </div> 
# 
# > python : 
# > - les types non-mutables : `int, float, string, tuple `  
# > - les types mutables : `list, set, dict(ionnaire)`
# 

# **pythontutor.** Illustrons cette importante différence avec cet 
# [exemple](http://pythontutor.com/visualize.html#code=x%20%3D%203%0At%20%3D%20%5B1,%202,%203%5D%0A&cumulative=false&curInstr=2&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).
# 
# - `x` est une variable non mutable (c'est un `int`) et son identifiant correspond bien à la valeur d'initialisation, ici `3`. `x` est bien une (référence à) une valeur : la valeur `3`.
# - En revanche, `t`  est une liste python qui représente le tableau 1D de longueur 3 initialisé par les valeurs entières '1, 2, 3'. _Une liste python est une variable mutable_. Ainsi, on voit que la variable `t` est représentée par une flèche qui désigne une (la) zone mémoire où sont stockés les 3 valeurs du tableau `t`.  `t` est encore une valeur mais cette fois, cette valeur est une adresse (vers les valeurs de la variable mutable).
# 
# Cette différence va prendre tout son sens avec l'affectation (et le passage de paramètre pour les fonctions).  

# In[1]:


# à essayer aussi dans pythontutor
x = 3
s = "bonjour"
e0 = (1, 2, 3) # un tuple est non mutable
l0 = [1, 2, 3] # une liste est mutable


print(s)


# #### Dupliquer des valeurs par référence :  mutable _vs._ non mutable
# 
# <div class="alert alert-block alert-info">
# 
# **Cas mutable :** l'affectation par référence **ne duplique pas la valeur**.  
#     
# </div>

# Ainsi si cette valeur est déjà associée à une autre variable (cas de l'affectation `x = y` où `y` a été initialisée précédemment) alors `x` **et** `y` référencent le même emplacement en mémoire.  
# La modification ultérieure de l'une ou de l'autre des variables nécessite de lever l'ambiguïté suivante.   

# <div class="alert alert-block alert-info">
# 
# **Effet de bord :**
#     
# `x` est une variable introduite par l'affectation `x = y` où `y` est une autre variable pré-existante.
#  
# - Modifier <b>ultérieurement</b> `x`  a-t-il aussi un effet sur `y` ?
#     
# - Modifier <b>ultérieurement</b> `y`  a-t-il aussi un effet sur `x` ?
# </div>

# Un tel effet est appelé un **effet de bord** ; ce qui peut être choquant d'un point de vue algorithmique.    
# 
# En python, il est clair maintenant que la réponse à cette question dépend du caractère _mutable_ ou _non mutable_ du type de la variable.

# **Rmq.** La fonction prédéfinie `id()` est définie au paragraphe suivant.  Elle retourne l'adresse "en mémoire" de son argument.

# In[2]:


def aff(v1, v2 : None) -> None:
    '''affichage adapté
    Rmq : l'annotation None pour v1 et v2 veut dire Any
    '''
    CAS_VRAI = "emplacements mémoire identiques"
    CAS_FAUX = "emplacements mémoire différents"

    if id(v1) == id(v2):
        print(v1, v2, CAS_VRAI)
    else:
        print(v1, v2, CAS_FAUX)

# les int sont non mutables
x = 3
y = x
aff(x, y)
y = 5
aff(x, y)
x = 6
aff(x, y)
# gardons ce cas particulier pour plus tard
#x = 5
#aff(x, y)
print()

# les strings sont non mutables
s1 = "aa"
s2 = s1
aff(s1, s2)
s2 = "bb"
aff(s1, s2)
s1 = "ab"
aff(s1, s2)
print() 

# les listes sont mutables
l = [1,1]
m = l
aff(l, m)
m = [2,2]
print("je modifie complètement m :")
aff(l, m)
print()

print("je recommence avec l = [1,1] et m = l ")
l = [1,1]
m = l
print("mais je modifie partiellement m sans penser à l :")
m[0] = 0 
aff(l, m)



# Comme déjà évoqué, le dernier résultat (modification partielle de mutable) est assez surprenant.
# Je vous laisse imaginer la recherche de bug ...

# <div class="alert alert-block alert-danger">
#     
# L'affectation python `x = y` avec des variables <b>mutables</b> <em>ne crée pas</em> un nouvel emplacement mémoire pour `x`.  
#     
# Elle créée <em>une nouvelle référence</em> pour `x` (ou met à jour une référence existante) <em>vers un emplacement qui existait précédemment</em> : celui de `y`.  
#     
# Ainsi cet emplacement est accessible par plusieurs références -- ici `x` et `y` sont des références vers le <b>même emplacement mémoire</b>.
#     
# </div>

# En pratique, l'environnement python connaît le nombre de références qui désignent le même emplacement mémoire. 
# Ce qui lui permet le cas échéant de récupérer les zones qui ne sont plus désignées (mécanisme de _garbage collector_ ou _ramasse miettes_ en français).

# ### Approfondissons par _introspection_
# 
# Nous verrons plus tard que les "entités python" sont des _objets_.  
# python fait partie des langages de programmation appelés __langage objet__ ou __langage orienté objet__.  
# Un _objet_ est un ensemble d'_attributs_ (des valeurs nommées) et de _méthodes_ (des fonctions qui s'appliquent à _tout_ ou _partie_ de cet objet), cet ensemble étant accessible par un _identifiant_ (le nom de l'objet).  
# Nous verrons qu'en fait un objet est (très souvent) associé à une notion plus générale, la notion de _classe d'objets_.  
# Une _classe_ d'objets est un modèle d'objets et ainsi un objet d'une classe donnée est aussi appelé _une instance_ de cette classe.  
# 
# **Rmq.** Pour l'instant, pas d'énorme différence entre objet et variable telle que présentée jusqu'à présent.   
# 
# #### Les fonctions  `type( )` et `id( )`
# 
# Parmi les méthodes de tout objet python, certaines permettent _l'introspection_, c-a-d. permettent d'obtenir des informations sur l'objet et sur son état.  
# 
# Nous allons présenter ici :
# - les fonctions  `type()` et `id()` qui retournent, respectivement, le type et l'adresse (mémoire) unique  de l'argument.  
# 

# In[3]:


a = 1
b = 1.1

l = [0]*10
t = [1,1]

print(a, type(a), id(a))
print(b, type(b), id(b))
print(l, type(l), id(l))
print(t, type(t), id(t))
print(id(l[0]), id(l[1]))


# **Autres fonctions d'introspection**
# 
# D'autres fonctions d'introspection très utiles existent. Essayez-les ! 
# - la fonction `help()`  déjà connue  
# - les fonctions  `locals()` et `globals()` qui retournent la liste des variables locales, resp. globales, au contexte de leur appel ;
# - la fonction `dir()`

# In[4]:


help(locals)
help(globals)
help(dir)


# In[5]:


locals() == globals()
#print(locals())


# In[6]:


dir()
a = 1
#print(dir(a))
l = [1]
#print(dir(l))
print(dir(a) == dir(l))


# #### Introspection de l'affectation

# Dans les traitements suivants, retrouvons les comportements décrits précédemment.
# Etonné ?

# In[7]:


# affectation de non-mutables
a = 1
print("a:", a, type(a), id(a))
b = a
print("b:", b, type(b), id(b))
b = 2
print("b:", b, type(b), id(b), "\n")

# affectation de non-mutables
s = "aagskjhdsqgf qkdhqhq "
print('s:', s, type(s), id(s))
s2 = s
print('s2', s2, type(s2), id(s2))
s2 = "a"
print('s2', s2, type(s2), id(s2), "\n")

# affectation et modification de mutables
l = [0,0]
print(l, type(l), id(l))
t = l
print(t, type(t), id(t))
l = [1, 0]
print(l, type(l), id(l))
print(t, type(t), id(t))
t = [1,1]
print(t, type(t), id(t))
t[0] = 0
print(t, type(t), id(t), "\n")



# **Remarque.**
# Les premiers traitements (repris ici) :

# In[8]:


# affectation de non-mutables
a = 1
b = a

s = "aagskjhdsqgf qkdhqhq "
s2 = s

# affectation de mutables
l = [0,0]
t = l


# vérifient :

# In[9]:


print(
    id(a) == id(b), 
    id(s) == id(s2),
    id(l) == id(t)
     )


# Ah ?!! Ca ne correspond pas à ce qui avait été décrit : l'affectation de non-mutable `x = y` était supposée créer un nouvel espace mémoire pour stocker la valeur pour `x` ... ???? 

# Ici l'environnement _choisit d'économiser de la place en mémoire_ en ne dupliquant pas les valeurs non mutables : après affectation de l'une vers l'autre, elles ont la même valeur !  
# Une seule valeur est stockée et elle est référencée par 2 variables :  
# - la valeur non modifiée (à droite de l'affectation) est toujours référencée par "sa" variable  
# - la valeur modifiée (à gauche de l'affectation) référence aussi cette valeur.  
# 
# Cette optimisation, similaire au traitement du cas non mutable, est un peu piégeuse pour la compréhension.  
# Cependant, elle est sans effet sur les instructions suivantes, comme cet exemple l'illustre. 
# 

# In[10]:


# affectations de non-mutables -- épisode 2
a = 1
b = a
print("a=", a, id(a))
print("b=", b, id(b))
print("pas de nouvel espace mémoire suite à b = a. \n")

a = 2
print("a=", a, id(a))
print("b=", b, id(b))
print("a est modifié donc un nouvel espace mémoire est créé pour a. \n")

a = a + 1
print("a=", a, id(a))
print("a est encore modifié et un nouvel espace mémoire est encore créé.")
print("Un autre choix aurait été possible mais celui-ci est en cohérence avec le premier traitement observé.\n")

a = 5
print("a=", a, id(a))
a += 1
print("a=", a, id(a), "bizarre : a += 1 devrait être effectué en place : cf. plus loin")
print()

a = b + 2
print("a=", a, id(a))
print("b=", b, id(b))
print("pas de surprise")


# ### Affectation en python : compléments

# #### Modification partielle _vs._ modification complète d'un mutable
# 
# <div class="alert alert-block alert-info">
# 
# On retiendra que la modification totale d'un objet mutable conduit à la création d'un nouvel emplacement en mémoire. 
#     
# En revanche, <b>une modification partielle d'un objet mutable provoque un effet de bord</b>. 
# 
# </div>   

# Si l'objet est mutable alors sa modification **partielle** :
# * est effectuée "en place", c-a-d. à l'adresse mémoire occupée par l'objet.
# * Cette modification __est visible__ "depuis" les autres variables qui référencent (le cas échéant) cet objet. 
# * C'est un **effet de bord**. 

# In[11]:


# affectation de mutables
l = [0,0]
t = l

print("t = l")
print(l, id(l))
print(t, id(t))

print("modification partielle de l")
l[0] = 2
print(l, id(l))
print(t, id(t))

print("modification totale de l")
l = [4,3]
print(l, id(l))
print(t, id(t))

print("modifications de l par ses méthodes (aspects POO)")
t = l
l.sort()
print(l, id(l))
print(t, id(t))
l.reverse()
print(l, id(l))
print(t, id(t))
l.insert(1,11)
print(l, id(l))
print(t, id(t))




# #### Comment dupliquer (re-copier) un objet mutable et obtenir 2 objets différents en mémoire ?
# 
# Il faut :
# - réaliser une copie avec la fonction `copy()` du module `copy`
# - modifier _l'ensemble_ de l'objet :
#     - en créant des tranches complètes de listes : `m[:] = l` ou `m[0,len(l)] = l` 
#     
# La duplication est motivée pour distinguer des traitements différents de l'un ou de l'autre objet.  
# 
# 

# In[12]:


import copy
# affectations et modifications d'objets mutables
# une liste est mutable
l = [1, 2, 3]

# initialisation par référence -> pas de duplication
print("par référence")
m = l
print("l=",l, " == m=",m)

# la modification (partielle) de l impacte aussi m
l[0] = 5
print("l=",l, " == m=",m)

# la modification complète de l n'impacte pas m
# rmq: c'est une initialisation qui créé un nouvel emplacement mémoire
m = [5, 5, 5]
print("l=",l, " =/ m=",m)


# affectation avec copie explicite 
print("par copie")
# par tranches complètes
m = l[0:len(l)]
mm = l[:]

# par copy
m_copy = copy.copy(l)

print("l=",l,"== m=",m," == mm=",mm," == m_copy=",m_copy)

l[0]=0
print("l=", l,"=/ m=",m," == mm=",mm," == m_copy=",m_copy)
l = [0, 0, 0]
print("l=",l, "=/ m=",m," == mm=",mm," == m_copy=",m_copy)


# In[13]:


# les strings sont non-mutables
# les lists sont mutables

un_dalton = "Jo" #string
print(id(un_dalton), un_dalton)
print()

les_dalton = []    #list
les_dalton.append(un_dalton)
print(id(les_dalton), les_dalton)
print(id(les_dalton[0]), les_dalton[0])
print()

print("affectation par référence (pas de duplication)")
les_freres_dalton = les_dalton #affectation par reference (pas de duplication)
les_freres_dalton.append('Jack')
un_dalton = 'Averell'

print(id(les_dalton), les_dalton)
#print(id(les_dalton[0]), les_dalton[0])
print(id(les_freres_dalton), les_freres_dalton)
print(id(un_dalton), un_dalton)
print()

print (un_dalton, les_dalton, les_freres_dalton)


# In[14]:


un_dalton = "Jo" #string
print(id(un_dalton), un_dalton)
les_dalton = []    #list
les_dalton.append(un_dalton)  # rmq : modification SANS d'affectation
print(id(les_dalton), les_dalton)
print(id(les_dalton[0]), les_dalton[0])
print()

print("affectation avec duplication")
les_freres_dalton[:] = les_dalton # [:] permet de dupliquer !
print(id(les_dalton), les_dalton)
print(id(les_freres_dalton), les_freres_dalton)
print()

les_freres_dalton.append('Jack')
un_dalton = "Averell"
les_dalton.append(un_dalton) # rmq : modification SANS d'affectation
print(id(les_dalton), les_dalton)
print(id(les_freres_dalton), les_freres_dalton)

print (un_dalton, les_dalton, les_freres_dalton)


# #### Des subtilités pour `x += 1` _vs._ `x = x + 1` 
# 
# La composition d'une affectation et d'un opérateur binaire (ici celui associé au symbole '+')  est appelé une _affectation augmentée_.  
# 
# Le [manuel de référence du python3](https://docs.python.org/fr/3/reference/simple_stmts.html#index-6) indique en **section 7.2.1** : 
# > An augmented assignment expression like x += 1 can be rewritten as x = x + 1 to achieve a __similar, but not exactly equal effect__. In the augmented version, x is only evaluated once. Also, when possible, the actual operation is performed __in-place__, meaning that rather than creating a new object and assigning that to the target, the old object is modified instead.
# 
# Nous n'avons pourtant pas pu constater cette modification en place pour `a += 1`  dans l'exemple plus haut. 
# Mystère ? 
# 
# L'exemple suivant montre encore que le caractère mutable ou non d'une variable modifie tout ce qui comporte une affectation.

# In[15]:


# a et b non mutables
a = 0
b = 11
print(id(a), id(b))

a += 1
b = b + 1
print(id(a), id(b))

# a et b mutables
a = [0]
b = [11]
print(id(a), id(b))

a += [1]
b = b + [1]
print(id(a), id(b))


# L'affectation augmentée de la liste (mutable) `a` est bien effectuée en place.
# Le traitement sur la liste `b`, "similaire mais pas exactement égal" (!) utilise un nouvel espace de stockage pour la nouvelle valeur de `b`.
# 
# Ces traitements sont "exactement égaux" (!) lorsqu'ils sont appliqués à des entiers (non mutables) : création d'un nouvel espace de stockage. 
# 
# Et tout ceci est bien cohérent si on relit **bien** ce qu'indique le manuel : 
# > _Also, **when possible**, the actual operation is performed in-place, ..._
# 
# Comme nous l'avons rappelé en Section 1.3.2, la modification d'une variable _non mutable_ implique la création d'un nouvel emplacement mémoire, _i.e._ d'une nouvelle variable mais de même identifiant. Ce qui n'est pas le cas pour une modification partielle d'une variable mutable.

# **($\star)$ Rmq.** Il faudrait aller encore un peu plus loin dans l'analyse de l'affectation augmentée. 
# 
# En effet, que penser de `x += f(x)` où `f(x)` lui-même peut modifier `x`, voire même le modifier avec une affectation augmentée ?
# 
# Les exemples suivants illustrent différents cas de ce type. Attendre la section 1.4 suivante qui clarifie le passage de paramètres selon le caractère mutable ou non de l'argument avant de les regarder plus en détail. 
# 
# On retiendra surtout cet extrait de la documentation python (version française, section 1.7.2) :
# > Au contraire des assignations normales, les assignations augmentées **évaluent la partie gauche avant d'évaluer la partie droite**. Par exemple, a[i] += f(x) commence par s'intéresser à a[i], puis Python évalue f(x), effectue l'addition et, enfin, écrit le résultat dans a[i].

# In[16]:


def f(t : int or list) -> int or list:
    '''t en modifié localement mais pas "returné"'''
    u = t
    t = t + t
    print("id dans f -- t:", id(t), ", u: ", id(u) )
    return u

a = 2
print(a, id(a))
a += f(a)
print(a, id(a))

l = [10]
print(l, id(l))
l += f(l)
print(l, id(l))


# In[17]:


def f(t : int or list) -> int or list:
    '''t en modifié localement et renvoyé'''
    u = t
    t = t + t
    print("id dans f -- t:", id(t), ", u: ", id(u) )
    return t

a = 2
print(a, id(a))
a += f(a)
print(a, id(a))

l = [10]
print(l, id(l))
l += f(l)
print(l, id(l))


# In[ ]:





# ## ($\star$) Fonctions : aspects avancés

# <div class="alert alert-block alert-success">
#     Cette section relève de <b>l'objectif 20</b>
# </div>

# Nous allons étudier plus en détail le passage des paramètres de fonction en python.  
# 
# On a écrit :
# 
# >python : passage $\Leftrightarrow$ **affectation**
# 
# En effet, le passage de paramètre correspond à l'affectation :
# > `paramètre formel = paramètre effectif`  
# 
# On a détaillé que le mécanisme de ce type d'affectation (copie vs. référence) dépendait du caratère mutable (référence) ou non-mutable (copie) des objets. 

# **Rappel** 
# 
# Le [tutoriel python.org](https://docs.python.org/fr/3/tutorial/controlflow.html#id2) dit :
# > Les paramètres effectifs (arguments) d'une fonction sont introduits dans la table de symboles locale de la fonction appelée lorsqu'elle est appelée ; par conséquent, __les passages de paramètres__ se font par valeur, la valeur étant toujours une __référence à un objet__, et non la valeur de l'objet lui-même.
# 
# Ce traitement est similaire à celui de l'_affectation_ en python décrit
# [plus haut](#revisiter_les_variables_et_l_'_affectation).
# Ce qui donne les 2 cas suivants.

# ### Le paramètre est de type non-mutable
# 
#  * transmission de la _valeur_ de l'argument effectif 
#  * argument formel _similaire à_ une variable locale de la fonction
#  * à l'extérieur de la fonction : pas de modification de la variable passée en argument 

# In[18]:


# fonctions et paramètres de type non-mutable
def f(x : int) -> int:
    '''retourne une variable locale'''
    r = x + 1 
    return r

def g(x : float) -> float:
    '''retourne le paramètre formel modifié'''
    x = x + 1
    return x

u = 0
y = 0.0

print("avant les appels:", "u=",u, ", y=", y)
print()

print("f(u)=", f(u))
print("g(y)=", g(y))
print()

print("après les appels:", "u=",u, ", y=", y)
print()


# - Les valeurs de `u` et `y` sont bien inchangées dans l'appelant bien que `y` soit un paramètre d'entrée modifié et retourné dans `g`.  Il faut voir ces paramètres formels comme des variables locales.  
# 
# - Bien sûr, il manque dans l'appelant une affectation du retour de la fonction.

# In[19]:


y = 0.0
print(y)
y = g(y)
print(y)
print(y == g(y))


# - **Attention au `print(appel de f)` !** 
# 
# **Exercice**. Expliquer pourquoi c'est normal !

# ### Le paramètre de type mutable
# 
#  * transmission de _l'adresse_ de l'argument effectif 
#  * l'argument effectif est _ainsi_ la variable extérieure à la fonction
#      * il _peut_ donc y avoir modification de la valeur dans l'appelant de la variable passée en argument même si celle-ci n'est pas retournée par la fonction. C'est un _effet de bord._
# 

# In[20]:


# fonction et paramètres de type mutable
def f(x : list) -> list:
    '''extension d'une liste avec duplication de ses valeurs
    l'utilisation pythonique du symbole * est quand même maladroite pour ce type de traitement
    '''
    x = x * 2
    return x

l = [0,1]
ll = l   # même référence
#m = []  # création
m[:] = l # duplication 
mm = l[:] # création+duplication

print("avant appel:")
print("l=",l, "ll=",ll, ", m=", m,  "mm=", mm)
print("id : l=", id(l), ", ll=",id(ll), ", m=", id(m), ", mm=", id(mm))
print()

l = [0,1]
print("appel avec affectation l = f(l):")
l = f(l)
print("l=",l, "ll=",ll, ", m=", m)
print("id : l=",id(l), ", ll=",id(ll), ", m=", id(m))
print()


# **Exercice**
# 
# 1. Dans le premier appel (avec affectation vers `l`), pourquoi `ll` qui est (était) une référence vers `l` n'est pas modifiée ?
# 

# L'appel avec affectation (dans `l`) n'a pas eu d'effet (de bord) sur l'autre référence (`ll`), ni bien sûr sur les variables dupliquées.
# C'est pourtant bien la référence de l'argument effectif qui est connue de l'appel de la fonction. 
# 
# Ici, la fonction **modifie complètement** ce paramètre mutable. Une nouvelle variable locale est donc créée et renvoyée. L'affectation (même dans la variable fournie comme argument d'entrée) effectue la mise à jour de la variable affectée.   

# **Attention**
# 
# Les écritures approximatives de fonction (sans `return`) ou les appels sans affectation du résultat (à la procédure) peuvent être dangereux. 
# 
# **pythontutor.** [L'exécution suivante](http://pythontutor.com/visualize.html#code=%23%20fonctions%20sans%20annotation%20de%20type%20pour%20l'exemple%0Adef%20f%28x%29%20%3A%0A%20%20%20%20x%20%3D%20x%20*%202%0A%20%20%20%20return%20x%0A%0Adef%20g%28x%29%20%3A%0A%20%20%20%20x%20%3D%20x%20*%202%0A%0Adef%20h%28x%29%3A%0A%20%20%20%20x%5B0%5D%20%3D%20777%0A%20%20%20%20%20%20%20%20%0Au%20%3D%203%0At%20%3D%20%5B1,%202%5D%0A%0A%23%20appel%20f%20%28modification%20complete%20avec%20return%29%20sans%20affectation%0Af%28u%29%0Af%28t%29%0A%0A%23%20appel%20g%20%28sans%20return%20explicite%29%20et%20sans%20affectation%0Ag%28u%29%0Ag%28t%29%0A%0A%23%20appel%20h%20%28modification%20partielle%29%20sans%20affectation%0Ah%28t%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# est une fois de plus instructive. 

# Un comportement similaire est obtenu lorsque la fonction manipule un paramètre objet par ses méthodes. L'exemple suivant illustre ce cas.

# In[21]:


# procedure : methode et paramètres de type mutable
def g(x : list) -> None:
    '''appel d'une méthode sur un objet mutable'''
    x.append(1)
    #return None

l = [0,0]
ll = l   # même objet
m = l[:] # duplication

#observons
s = (l,ll,m)
print("l, ll, m")
for x in iter(s):
    print(x, type(x), id(x))
print()

print("appel sans affectation du retour: g(l)")
print("print g(l)=", g(l))
print("l=",l, "ll=",ll,", m=", m)
print("id=",id(l), "id=",id(ll), ", id=", id(m))
print()

print("appel avec affectation: l = g(l)")
l = g(l)
print("l=",l, "ll=",ll, ", m=", m)
print("id=",id(l), "id=",id(ll), ", id=", id(m))
print()


print("appel avec affectation m = g(l):")
l = [0,0]
m = g(l)
print("l=",l, "ll=",ll, ", m=", m)
print("id=",id(l), "id=",id(ll), ", id=", id(m))
print()


# ATTENTION : c'est bien piégeux ! 
#     
# Retenons pour l'instant, c-a-d. tant qu'on ne manipule pas d'objet.
#     
# - Le passage de paramètre s'effectue : 
#     - par valeur pour des non-mutables  
#     - par adresse  pour des mutables,    
# - et ce conformément aux mécanismes d'affectation :  
#     - copie pour des non-mutables  
#     - référence pour des mutables. 
# - Les paramètres formels sont équivalents à des variables locales.  
# - L'affectation avec `return` **doit** (devrait) être le seul effet dans l'appelant.

# <div class="alert alert-danger">
#     
# <b>Attention</b> aux modifications partielles de paramètres effectifs mutables.  
#     
# </div>

# **Rmq.** Sur ce point, on trouve de tout sur internet et même les ouvrages (dont certains sont dispos à la BU). J'ai lu :
# 
# - c'est du passage par référence  
# - c'est du passage par valeur
# - c'est un mélange des 2 
# - c'est aucun des deux ...  
# 
# 
# **Exemple.** Retour sur une fonction de permutation de 2 entiers ... ? 

# In[22]:


a = 1
b = 11

print("avant : a,b =", a, b)
t = a
a = b
b = t
print("après : a,b =", a, b)

def permuter(x, y: int) -> None:
    ''' attention : 
    les print dans cette fonction sont uniquement à but pédagogique
    '''
    print("dans permuter, avant x,y :", x, y)
    t = x
    x = y
    y = t
    print("dans permuter, après x,y :", x, y)
    #return x, y
    
# marche pas !
a = 1
b = 11
print("avant fonction : a,b =", a, b)
permuter(a, b)
print("après fonction : a,b =", a, b)


# ### (Optionnel) Avoir les `id ` claires !
# 
# Reprenons les observations précédentes effectuées grâce à pythontutor avec un focus particulier sur cette fonction `id()`. 
# Cette fonction peut être très utile pour _debugger_ un développement qui ne fonctionne pas correctement. 
# 
# #### Utilisons les `id()` avec les mutables

# In[23]:


# fonction et paramètres de type mutable
def f(x: int) -> int:
    print("  f avant : @=", id(x))
    x = x * 2
    print("  f après : @= ", id(x))
    return x

l = [0,0]
ll = l   # même référence
m = l[:] # duplication

print("avant les appels:")
print("l=",l, "ll=",ll, "m=", m)
print("@l=",id(l), "@ll=",id(ll), "@m=",id(m))
print()

print("appel sans affectation du retour:")
print("main: @l=", id(l))
print("print f(l)=", f(l), "@f(l)=", id(f(l)))
print("l=",l, "ll=",ll,", m=", m)
print("@l=",id(l), "@ll=",id(ll), "@m=",id(m))
print()

print("appel avec affectation l = f(l):")
l = f(l)
print("main: @l(après l=f(l))=", id(l))
print("l=",l, "ll=",ll, ", m=", m)
print("@l=",id(l), "@ll=",id(ll), "@m=",id(m))
print()


# #### Utilisons les `id()` avec les non mutables 

# In[24]:


# fonctions et paramètres de type non-mutable
# f avec variable intermédiaire explicite
u = 0

def f(x: int) -> int:
    print("  f_r: avant @=", id(x))
    r = x + 2
    print("  f_r: après @=", id(x))
    return r

def g(x: int) -> int:
    print("  f_x: avant @=", id(x))
    x = x + 2
    print("  f_x: après @=", id(x))
    return x

def h(x: int) -> int:
    print("  f_=: avant @=", id(x))
    x += 2
    print("  f_=: après @=", id(x))
    return x

print("avant les appels:")
print("u=",u, "@u=", id(u))
print()

print("appel sans affectation du retour:")
print("f(u)=", f(u), "@f(u)=", id(f(u)))
print("u=", u, "@u=", id(u))
print()

print("appel avec affectation du retour:")
u = f(u)
print("u après u=f(u)=", u, "@u=", id(u))


# In[25]:


# fonctions et paramètres de type non-mutable
# f sans variable locale explicite
u = 1

def f(x: int) -> int:
    print("  f_x: avant @=", id(x))
    x = x + 2
    print("  f_x: après @=", id(x))
    return x

print("avant les appels:")
print("u=",u, "@u=", id(u))
print()

print("appel sans affectation du retour:")
print("f(u)=", f(u), "@f(u)=", id(f(u)))
print("u=", u, "@u=", id(u))
print()

print("appel avec affectation du retour:")
u = f(u)
print("u après u=f(u)=", u, "@u=", id(u))


# In[26]:


# fonctions et paramètres de type non-mutable
# f avec affectation composée
u = 0

def f(x : int) -> int:
    print("  f_=: avant @=", id(x))
    x += 2
    print("  f_=: après @=", id(x))
    return x

print("avant les appels:")
print("u=",u, "@u=", id(u))
print()

print("appel sans affectation du retour:")
print("f(u)=", f(u), "@f(u)=", id(f(u)))
print("u=", u, "@u=", id(u))
print()

print("appel avec affectation du retour:")
u = f(u)
print("u après u=f(u)=", u, "@u=", id(u))


# ## Les fonctions en python : derniers compléments faciles
# 
# Deux compléments faciles (arguments nommés et argument avec valeur par défaut) ainsi qu'une courte liste de ce qu'il reste à découvrir ... pour les plus curieux.  

# ###  Arguments nommés
# 
# Lors de l'_appel_, nommer les paramètres _formels_ et la valeur correspondante de l'argument (effectif), permet un ordre quelconque de ceux-ci.

# In[27]:


def trois_mots(mot1, mot2, mot3 : str) -> str:
    return mot1 + mot2 + mot3

m1 = 'Bonjour '
m2 = 'étudiantes et '
m3 = 'étudiants !'

#appel par position
m_classique = trois_mots(m1,m2,m3)

# appel par nom
m = trois_mots(mot3=m3, mot1=m1, mot2=m2) 

print(m_classique)
print(m)


# ###  Argument avec valeur par défaut
# 
# Les _derniers_ paramètres formels peuvent bénéficier de valeurs par défaut  
# * derniers : tous à partir d'un rang arbitraire 
# * les précédents sont sans valeur par défaut  
# 
# Lors de l'_appel_, ces valeurs sont utilisées en cas d'absence des paramètres effectifs.
# 
# Syntaxe : 
# * Ces valeurs sont définies avec une affectation _après_ l'annotation de type.  
# * L'annotation raccourcie de types (une annotation commune à tous les paramètres)  ne peuvent être utilisées en cas d'argument avec valeur par défaut.
# 
# <div class="alert alert-block alert-warning">
#     
# En pratique, limiter les valeurs par défaut à des paramètres _non-mutables_ : `int`, `bool`, `float`, `str`,  `tuple`  
# 
# </div>

# In[28]:


def incrementer(x : int, y : int = 1) -> int:
    return x + y

def tournure_polie(mot1 : str, mot2 : str = " Madame, ", mot3 : str = "Monsieur." ) -> str:
    return mot1 + mot2 + mot3

a = 0
print("a=",a)
a = incrementer(a)
print("a=",a)

print(incrementer(a))
print(incrementer(a, 7))

print(tournure_polie('Bonjour'))
print(tournure_polie('Au revoir', ' très cher '))
print(tournure_polie('Au revoir', mot3 ='et très cher Monsieur'))
print(tournure_polie('Au revoir ', "les uns,", ' et les autres.'))


# ### Ce qu'il reste à voir sur les fonctions en python
# 
#  
# * Argument de type fonction  
# * Nombre variable d'arguments (tuple et dictionnaire)
# * Fonction comme valeur de première classe : `lambda` fonction
# 

# ## Synthèse
# 
# ### Avoir les idées claires 
# 
# - Les principes du passage de paramètres appelant <-> appelé   
#     * "matériel" : par valeur _vs._ par adresse
#     * logique : in _vs._ out _vs._ inout
#     * aide : différencier fonction _vs._ procédure 
# - L'effet de bord est néfaste 
#     - possible pour le passage par adresse, et les variables globales (à proscrire)
# - L'affectation et le passage de paramètres **en python**
#     - pas de surprise pour les non-mutables (= variables locales)  
#     - **attention aux mutables** : danger d'effet de bord _si modification partielle_ 
#     - ne pas prendre de risque : `return` dans la fonction et affectation dans l'appelant 
#  
# ### Savoir-faire en python 
#     
# * Fonctions avec arguments nommés, avec paramètres par défaut.
# 
# **Objectif 20**
# 
# * Affectation en python   
#     - non-mutables : (référence à) la valeur
#     - mutables : (référence à) l'adresse
#     - attention aux mutables  : 
#         modification partielles _vs._ duplication (par `copy.copy` ou par "tranches complètes") 
#     - penser "objet" aide pour le comportement des mutables
# * Fonction et passage d'argument appelant/appelé en python : 
#     - similaire à l'affectation : distinguer mutable _vs._ non mutable  
# * Savoir effectuer des introspections (fonction `id()`)
# 
jupyter nbconvert --to html_embed --template toc2 7-fonctions-avancees.ipynb