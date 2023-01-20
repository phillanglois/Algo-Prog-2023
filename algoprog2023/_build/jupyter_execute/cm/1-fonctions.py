#!/usr/bin/env python
# coding: utf-8

# (ch:fonctions)=
# # Fonctions

# Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.

# Dans ce premier chapitre, nous abordons une notion importante qui fait l'objet de différentes appellations : fonction, procédure ou sous-programme. (Le titre de ce chapitre à longtemps été "Fonctions, procédures, sous-programmes"). 
# Vous connaissez les fonctions en mathématiques depuis le collège. 
# La notion de sous-programme à une consonance très "programmation". 
# Ces notions partagent beaucoup de points communs.
# 
# Ce chapitre est le plus générique possible : les différents aspects et le vocabulaire associés à la notion de fonction existent dans la très grande majorité des langages de _programmation impérative_. 
# Nous nous efforcerons de compléter ces notions classiques avec celles plus spécifiques de python qui sont importantes pour votre pratique de la programmation.
# La syntaxe python3 est bien sûr utilisée -- dès le titre  ! 
# 
# Un chapitre ultérieur complète cet présentation avec des aspects plus techniques, plus informatique, et leurs traitements en python. 

# ## Introduction
# 
# ### Généralités et vocabulaire (début)
# 
# De façon imagée, une fonction en mathématiques est _un traitement_ un peu compliqué que l'on décrit de façon synthétique par un symbole ou un nom, souvent réduit à la seule lettre $f$ -- pas que bien sûr : on se souvient des fonctions $\cos, \sin$, ... Ce traitement peut _dépendre d'un ou plusieurs paramètres_, souvent aussi notés avec les lettres $x, y$, ... 
# 
# On peut ainsi appliquer ce traitement facilement à des valeurs arbitraires, en notant par exemple $f(3.2)$ ou $\cos(\pi/4)$ l'application de ces fonctions et en identifiant ces écritures aux valeurs numériques correspondantes, par exemple $\sqrt 2/2$ pour la seconde écriture. 
# 
# La notion de sous-programme, qui englobe les notions de fonction et de procédure, reprend cette démarche _de notation synthétique et paramétrable d'un traitement compliqué_ dans le contexte d'un traitement informatique.

# - Le terme **sous-programme** est un (sous-)ensemble de lignes de code, souvent paramétrable, que l'on désigne d'un nom pour ré-utiliser "directement" ces lignes de codes à l'aide de ce nom. 
# - On **appelle** ce nom pour exécuter ces lignes de codes. 
# - Cet appel contient aussi **la valeur des paramètres traités** par cette exécution.
# 
# De façon imagée encore, un sous-programme peut-être vu comme une boîte opaque qui "prends des choses" en entrée (les paramètres), effectue des traitements qui dépendent de ces paramètres et fourni un "résultat" en sortie -- dans le cas d'une fonction. 
# La boîte porte le nom du sous-programme est en général accompagné d'une description de ce qu'elle fait. La boîte est opaque : je peux m'en servir, je connais **ce qu'elle fait** mais pour ça, je n'ai pas besoin de savoir **comment** elle le fait.
# 
# Une analogie facile : je peux me servir d'une voiture sans savoir comment la mécanique ou l'électronique fonctionnent.

# Une **fonction** est un sous-programme qui **calcule et renvoie** une (ou des) valeur(s).  On dit aussi "retourner" à la place de "renvoyer".
# - exemple : _je_ calcule le double d'une valeur donnée en entrée et _je_ retourne (ou _je_ renvoie) ce résultat comme sortie.
# 
# Une **procédure** est un sous-programme qui **réalise une action** -- sans sans renvoyer quoi que ce soit.
# - exemple : _j_'affiche l'heure du moment. 
# Oui : "afficher" n'est pas "renvoyer".  
# 
# Différencier fonction et procédure aide à la compréhension du traitement réalisé par le sous-programme en question.

# <div class="alert alert-block alert-info">
#     
# **Spécificité python** : il n'y a que des fonctions (pas de procédure).  
# 
# </div>
# 
# Donc par la suite, on utilisera surtout le terme _fonction_ mais on ne manquera pas d'indiquer lorsqu'une fonction python est une procédure au sens défini ci-dessus.

# Vous avez déjà rencontré _et utilisé_ des fonctions python "sans le savoir" -- par exemples la fonction mathématique `sqrt()` ou la procédure d'écriture à l'écran `print()`.
# 
# Il est important de distinguer :
# 
# - l'utilisation de fonctions "existantes"
# - la définition de nouvelles fonctions
# 
# C'est un peu "la poule et l'oeuf" car une fonction dite existante a du être définie avant d'exister :)

# ### Utiliser une fonction existante
# 
# Prenons l'exemple **des fonctions mathématiques** (dites) **prédéfinies.**
# 
# Les fonctions mathématiques connues comme les fonctions trigonométriques, logarithmes, exponentielles, puissances ... sont "fournies avec le langage de programmation". 
# Elle sont définies et regroupées sous la forme de _bibliothèques_ de fonctions aussi appelées _modules_ en python.  
#   
# #### Appeler pour utiliser

# In[1]:


from math import cos, pi
# pour utiliser la fonction cos et la valeur pi définis dans le module math

c = cos(pi/3)
# calcul qui utilise cos et pi, puis affectation du résultat dans la variable c

print(c)
# affichage de la valeur de la variable c


# Humm ... ce calcul n'est pas très précis ... Voir la digression proposée en fin de cette section pour les curieuses et les curieux.

# **Commentaires**  
# 
# * Ligne 1 : fonction `cos` et valeur `pi` sont disponibles   
# 
# * Ligne 2 : _à droite_ de l'affectation (=) : _appel_ de la fonction `cos(...)` pour l'_argument_ `pi/3`.  
# 
# * Ligne 2 : _à gauche_ de l'affectation  : valeur-résultat affectée dans la variable `c`
# 
# * Ligne 3 : affichage de la valeur _retournée_  

# #### Vocabulaire (suite)
# 
# L'**appel** de la fonction est caractérisé par :
# 
# * le **nom** de la fonction :  ici `cos(...)`
# * ses **arguments d'entrée** : ici la valeur $\pi$/3
# * une valeur de **retour** (résultat, destination) : 
#     - ici une variable résultat : `c`, 
#     - ou aussi un terme d'une expression : `cos(pi/3)**2 + sin(pi/3)**2`
# * vocabulaire : _argument_ ou _paramètre effectif_
# 
# L'exemple précédent contient uniquement un _appel de fonction_ -- et aucune définition des fonctions utilisées.
# 
# * ici, on _utilise_ le nom `cos` de la fonction trigonométrique _cosinus_ pour obtenir la valeur de cette fonction pour l'argument d'entrée fourni.    
# * on voit bien que cet appel ne nécessite pas de connaître _comment_ cette fonction calcule le résultat qu'elle renvoie (ou retourne).  Cette fonction est bien vue comme une boîte opaque (une _boîte noire_).

# <div class="alert alert-block alert-info">
#     
# **A retenir** : Les **parenthèses `(...)`** derrière le nom de la fonction : c'est à ça qu'on reconnait une fonction !  
# 
# </div>
# 
# 
# <div class="alert alert-block alert-info">
# 
# **A retenir** : la construction 
#         `from module import fonction1, fonction2` 
#         permet d'utiliser les fonctions `fonction1` et `fonction2` définies dans la bibliothèque `module`
# 
# </div>

# ### Définir une nouvelle fonction et l'utiliser
# 
# Donnons maintenant un exemple où **nous** définissons une fonction pour l'utiliser ensuite.
# 
# #### Ecriture mathématique habituelle
# 
# Un exemple de fonctions numériques du collège-lycée : la fonction affine $f(x) = 2x + 1$ 
# 
# - vous savez calculer (de tête) $f(0)$, $f(1)$, $f(-1)$, ... 
# - vous connaissez sa représentation graphique : une droite de pente 2 et d'ordonnée à l'origine 1.

# #### En python
# 
# 1. Définition
# 
# - On commence par _définir_ `f` et ses paramètres : ici un seul paramètre `x` de type `float`.
# - La fonction `f` _retourne_ une valeur de type `float`.
# - La partie indentée par rapport à `def` définit le traitement -- on reconnaît le calcul de $f(x)$ -- et la valeur retournée par la fonction -- ici la valeur de la variable _locale à la fonction_ `res`.  

# In[2]:


def f(x : float) -> float:
    res = 2 * x + 1
    return res


# 2. Utilisation : appels
# 
# On utilise `f` : on _appelle_ `f` pour différentes valeurs de son paramètre `x`.  
# Ces valeurs sont appelées des _arguments_ de l'appel. 
# Il peuvent être des valeurs numériques, des variables, des expressions, des appels à des fonctions ... 
# Bref tout ce qui peut être _évalué_ (_ie._, calculé) et qui _le sera **avant**_ l'exécution de l'appel de la fonction.

# In[3]:


# 3 appels pour des valeurs numériques
a = f(0)
b = f(1.0)
c = f(-1)
d = f(3.0)

print(a, b, c, d)


# In[4]:


# 2 appels pour des variables
zero = 0
un = f(zero)
trois = f(un)

print(zero, un, trois)


# In[5]:


# 2 appels dans une expression 
combien = f(zero) + f(un) 

# 2 appels : 1 d'une expression et 1 dans un argument qui est une expression 
et_celui_la = f(zero + f(un)) 

print(combien, et_celui_la)


# In[6]:


# un joli tracé vaut mieux qu'un long discours
import matplotlib.pyplot as plt

x = [i for i in range(-5,5)] # une liste de 10 arguments
y = [f(i) for i in x] # la liste des 10 valeurs de la fonction correspondante

plt.plot(x, y)
plt.title("f(x)=2x+1")
#plt.close()


# #### Premiers commentaires et vocabulaire (encore) important
# 
# 1. 
#     - On a **défini** (`def`) la fonction $f$ une fois, au début. 
#     - Puis on l'a utilisée, i.e. **appelée**, plusieurs fois : 
#         - pour calculer les valeurs ponctuelles :
#             - de valeurs numériques,
#             - de l'évaluation d'expressions,
#             - de l'évaluation de (l'appel) de fonction,
#         - pour effectuer des tracés, ...

# 2. 
#     - La définition a une forme très semblable à l'expression mathématique avec un  (ou des) **paramètre**  ou aussi **paramètre _formel_** $x$, et **des parenthèses** : $f(x)$. 
#     - Elle contient (au moins) un `return` qui correspond à un résultat fourni par la fonction. 
#     - C'est ainsi que ce résultat est **retourné** (ou renvoyé) par la fonction.   

# 3.  - Les appels, comme en math, correspondent à "remplacer" `x` par une valeur numérique donnée
#     - cette valeur d'appel est appelée **argument** ou aussi **paramètre _effectif_** (de l'appel).    

# 4. **Important.** 
# 
#     - Les **seuls** `print` de ces exemples s'appliquent à des _valeurs retournées_ par la fonction f
#     - **Aucun `print` dans la définition de `f`**.

# ### Pourquoi des sous-programmes ? (des fonctions ?)
# 
# * Eviter de ré-écrire, de dupliquer, du code -- souvent le code qui correspond au _comment_ du traitement.      
# * Simplifier la lecture donc la compréhension : le _quoi_ suffit pour cela. 
# * Ré-utiliser l'existant
# 
# Les fonctions sont une nouvelle _structure_ en programmation et en algorithmique. 
# Une fonction permet d'écrire les algorithmes/codes de façon plus _modulaire_.
# * _Modularité_ : découper un traitement compliqué en une suite d'étapes plus simples
# * Ce découpage peut être appliqué _récursivement_ : _cad_ appliqué au sein de chaque étape, et ce de façon répétée, jusqu'à que le traitement de l'étape soit assez simple pour être écrit !

# ### Distinguer le _Quoi_ du _Comment_ 
# 
# Ces deux exemples permettent d'introduire deux notions complémentaires **et différentes**.
# 
# * **La spécification**  = ce que ça fait : le QUOI 
# * **Une implémentation** = comment ça le fait : le COMMENT  
# 
# Avec l'exemple des fonctions mathématiques prédéfinies :
# - nous savons _ce que calculent_ ces fonctions : le **quoi** ;
# - et pourtant (la plupart d'entre) nous ne sait pas **comment** elles sont calculées. 
# 
# Dans l'exemple de la fonction affine, l'expression mathématique $f(x) = 2 x + 1$ mélange le _quoi_ et le _comment_.  Notre définition de fonction python, elle, explicite les 2 : le quoi et le comment.
# 

# **Question** : Quelles sont les 4 notions définies par le paragraphe précédent ?
# 
# **Question** : Y-a-t'il d'autres façon de calculer la fonction $f$ précédente ? Qu'en déduire ?
# 

# ### ($\star$) Digression de fin de section
# 
# Revenons sur le premier exemple pour tenter de se rassurer.

# In[7]:


cos(pi/3)


# In[8]:


cos(pi)


# In[9]:


from math import *
# on importe "tout" math

c = cos(pi/3.0)
s = sin(pi/3)

un = c*c + s*s

print("cos, sin, cos*cos + sin*sin = ", c, s, un)


# Profitons-en pour indiquer que ce genre d'appels est un premier exemple de _test unitaire_. On teste la correction du traitement des fonctions `cos` et `sin` en vérifiant une propriété mathématique caractéristique.
# 
# 
# **Un premier exemple de test unitaire**
# 
# On montre comment effectuer la même vérification avec l'instruction `assert` adaptée à ces tests unitaires.

# In[10]:


c = cos(pi/3.0)
s = sin(pi/3)

assert c*c + s*s == 1


# Il ne se passe rien. L'assertion est vraie.
# Morale : "Pas de nouvelle, bonne nouvelle !"
# 
# On peut donc être un peu plus exhaustif.

# In[11]:


# des valeurs caractéristiques 
assert cos(0) == 1.0
assert cos(pi) == -1.0
assert sin(0) == 0.0
assert sin(pi/2.) == 1.0

# dont mais certaines difficiles à obtenir
#assert cos(pi/2.) == 0.0
#assert cos(3. * pi/2.) == 0.0
#assert sin(pi) == 0.0
#assert sin(3. * pi/2.) == 0.0


# In[12]:


# une propriété qui ne rassure pas comlètement ...
import random

for _ in range(20):
    v = random.uniform(-10,10)
    #assert cos(v)**2 + sin(v)**2 == 1
    print(cos(v)**2 + sin(v)**2)


# ## Les grands principes : définition, signature, corps et appels de fonction  
# 
# 
# <div class='alert alert-block alert-danger'>
#     
# NE PAS CONFONDRE :  **LA** définition  vs. **LES** appels    
# 
# </div>
# 
# <div class="alert alert-success">
# 
# La définition d'une fonction est constituée de sa _signature_ et de son _corps_.
# 
# </div>
# 
# <div class="alert alert-success">
# 
# La signature "ne fait rien". Elle _décrit_ les paramètres formels, cad. comment utiliser la fonction (par l'appel) et ce qu'elle fait.
# 
# </div>
# 
# <div class="alert alert-success">
# 
# Le corps est _le traitement qui sera exécuté par l'appel_ de la fonction.
# 
# </div>
# 
# <div class="alert alert-success">
# 
# L'appel définit les _arguments_ (ou _paramètres effectifs_) et _réalise le traitement_ (l'exécution) du corps de la fonction pour ces arguments .
# 
# </div>

# ### Définition d'une fonction
# 
# De façon générale, la définition d'une fonction contient :
# 
# * le _nom_ de la fonction
# * les **paramètres formels** des _entrées_ : leurs nombres, leurs types, l'identificateur de chacun  
# * les _sorties_ : leurs nombres, leurs types, l'identificateur de chacune    
# * le _traitement_ défini avec ces paramètres formels (d'entrée et de sortie) et, souvent, des _variables locales_ (à la fonction)
# 
# signature _vs._ corps pour distinguer le _quoi_ du _comment_ :
# 
# - Le traitement correspond au _comment_. Il est défini dans le _corps_ (ou l'implémentation) de la fonction  
# - Le _quoi_ est décrit par la signature de la fonction
# 

# #### Syntaxe(s) python de la définition de fonction
# 
# On commence avec la syntaxe historique des fonctions en python. 
# Puis on profite des versions plus récentes du langages ($\ge 3.9$) qui permettent de définir facilement le _type_ des paramètres d'entrée et de retour de la fonction. 

# <div class='alert alert-block alert-info'>
# 
# **RETENIR** : Le mot clé `def`, les `()` et le `:`
#     
# </div>    
# 
# Syntaxe Python "historique" :   
# ```python
# def nom(liste de paramètres formels séparés par des virgules):
#     ... # le corps de la fonction : ce qu'elle fait 
#     return 'sortie'
# ```

# Soyons plus précis **en explicitant le _type_ des paramètres** d'entrée et de sortie.
# 
# https://fr.wikiversity.org/wiki/Python/Les_types_de_base
# 

# Cette syntaxe Python **améliorée** est **A UTILISER SYSTEMATIQUEMENT** :   
# ```python
# def nom('1er paramètre formel': son type, '2ème paramètre formel': son type, ...) -> type du retour:
#     ... # le corps de la fonction : ce qu'elle fait 
#     return 'sortie'
# ```

# Exemples de définition complète (signature et corps) : 

# In[13]:


def f(x : float) -> float:
    '''Une fonction affine déjà rencontrée'''
    y = 2 * x + 1
    return y

def qui_suis_je(n : int) -> int:
    '''?'''
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


# ### La signature d'une fonction
# 
# La _signature_ d'une fonction permet de connaître le minimum nécessaire et suffisant pour utiliser (appeler) cette fonction, ie. le _quoi_ (que fait la fonction et de quoi a-t-elle besoin pour ça ?)
# 
# On ne garde que le nécessaire de la syntaxe améliorée :

# In[14]:


def f(x : float) -> float:
    '''Fonction affine de coeff directeur 2 et d'ordonnée à l'origine 1'''

def qui_suis_je(n : int) -> int:
    '''Calcule et retourne la factorielle de l'entier positif n''' 


# La lecture de la première signature dit que la fonction `f`  prend en entré un paramètre de type numérique à virgule flottante (on dira _un flottant_) noté `x` et fourni en retour une valeur flottante. Le commentaire, appelé _docstring_ décrit ce que fait la fonction `f`.   

# <div class='alert alert-block alert-warning'>
# 
# Vocabulaire -- selon les langages de programmation : 
# <ul>
#     <li> signature = spécification = en-tête (= prototype)  </li>
#     <li> corps = implémentation  </li>
# </ul>
#     
# </div>    

# <div class='alert alert-block alert-danger'>
# 
# ATTENTION  : une telle signature n'est pas reconnue telle quelle par python
#   
# EN PRATIQUE : il faudra compléter la signature par le corps pour que la fonction soit correctement définie et reconnue (à suivre) 
# 
# </div>

# **$\star$ Rmq : statique _vs._ dynamique.** 
# Selon les langages de programmation, la signature peut-être séparée (voire compilée) indépendamment de l'implémentation de la fonction. Ainsi (re)connue du compilateur, cette signature peut lui servir pour _vérifier automatiquement la correction_ de l'implémentation de la fonction et aussi des appels à cette fonction : nombre de paramètres effectifs, type de ces paramètres, type du résultat retourné, ... Ces vérifications sont possibles lors de la _compilation_ , cad. avant toute exécution du programme. Ce type de vérification diminue le risque d'erreur lors de l'exécution. 
# 
# On parle d'analyse _statique_ (ou de vérification statique) pour ces _traitements effectués lors de la compilation_. Oui : un compilateur est un programme qui s'exécute ! Il "prend en entrée" un code (dit) source et produit en sortie un code (dit) exécutable. Ce traitement comporte plusieurs étapes dont celle de vérification mentionnée qui s'effectue lors de l'étape (dite) d'analyse syntaxique -- ne pas confondre les termes "syntaxique" et "statique".
# 
# De façon complémentaire, on parle d'analyse _dynamique_ (ou de vérification dynamique) pour les traitements effectués lors de l'exécution du programme.
# 

# ### L'appel d'une fonction
# 
# L'appel de la fonction consiste à exécuter la fonction pour des valeurs fixées des arguments d'entrée.  
# 
# Syntaxiquement : 
# * le _nom_ de la fonction (sans le `def` mais avec les `( )`)
# * les **paramètres effectifs** : les _valeurs_ des arguments d'entrée
# * les _identifiants_ des variables de sortie

# In[15]:


# appel de f pour la valeur 0
ordonnee_a_l_origine =  f(0) 
 
print(ordonnee_a_l_origine)  


# In[16]:


t = 1
r = f(t)
print(r)


# In[17]:


print("n, f(n), n!")
# plusieurs appels de f et de qui_suis_je
for  val in range(3):
    print(val, f(val), qui_suis_je(val))


# On a vu en début de présentation que les paramètres effectifs peuvent être plus généralement la valeur d'une variable, d'une expression (évaluée), d'une fonction (appelée).    

# ### Le corps et le retour de valeur avec `return` 
# 
# Le corps définit le traitement de la fonction.  
# Il complète la signature.  
# Ce traitement s'effectue avec les paramètres formels et des variables locales à la fonction.  
# A l'issue du traitement, la fonction renvoie (ou retourne) une valeur de sortie.
# 
# **En python** : 
# 
# - le corps est _indenté_ d'un niveau par rapport à celui du `def` (qui finit par un `:`).
# - mot-clé `return`
#     * `return` une valeur, une variable, une expression
#      * `return None` : ne retourne rien ... mais le dit !  
#     * l'exécution d'un `return` **termine l'_exécution_ du corps de la fonction**
#         * à la fin de l'écriture du corps, en général ...
#         * mais pas toujours : le `return` n'est pas nécessairement unique (cf. paragraphe suivant)  

# :::{note}
# Spécificité python : comme il n'y a que des fonctions en python, une procédure sera écrite comme une fonction qui retourne `None` 
# :::
# 

# In[18]:


# définition de 3 fonctions
def doubler(u : int) -> int:
    """ retourne le double de u """
    return 2 * u

def tripler(u : int) -> int:
    """ retourne le triple de u    """
    v = 3 * u
    return v

# des appels

d = doubler(2)
t = tripler(2)

print(d, t)


# In[19]:


# un appel -- qui passe en python mais qui "gratte un peu" d'après l'en-tête de doubler ...
doubler(5.5)


# <div class='alert alert-block alert-warning'>
# 
# **NE PAS CONFONDRE** :  **paramètre formel** _vs._ **paramètre effectif** ou argument
# 
# </div>    
# 
# <div class='alert alert-block alert-danger'>
#     
# **CONSIGNE PEDAGOGIQUE** : il est interdit d'utiliser l'identifiant du paramètre formel comme paramètre effectif d'un appel.     
# </div>

# In[20]:


x = 3
# L'appel suivant est interdit pour la fonction affine f(x) définie précédemment
y = f(x)

y = f(3) # ok


val = 3
y = f(val) # ok


# <div class="alert alert-block alert-info">
# 
# **A retenir :** l'appel est situé _après_ la définition  
# 
# </div>  
# 
# - logique : il faut connaître la fonction pour l'utiliser ! 
# - `python` : se souvenir que `from module import f` permet de connaître, donc d'utiliser, `f` qui a été définie (par moi ou par un.e autre) dans la bibliothèque `module`

# ## L'appel de fonction rompt le séquencement des instructions exécutées 
# 
# Nous illustrons avec [pythontutor](http://pythontutor.com/visualize.html#mode=edit) l'exécution d'un appel de fonction. 

# - Fonction affine :
# [visualisation pythontutor](http://pythontutor.com/visualize.html#code=def%20f%28x%20%3A%20float%29%20-%3E%20float%3A%0A%20%20%20%20'''Une%20fonction%20affine%20d%C3%A9j%C3%A0%20rencontr%C3%A9e'''%0A%20%20%20%20y%20%3D%202%20*%20x%20%2B%201%0A%20%20%20%20return%20y%0A%20%20%20%20%0Aordonnee_a_l_origine%20%3D%20f%280%29%0A%0Aprint%28ordonnee_a_l_origine%29%0A%0Aprint%28%22n,%20f%28n%29%22%29%0A%23%20plusieurs%20appels%20de%20f%0Afor%20val%20in%20range%283%29%3A%0A%20%20%20%20print%28val,%20f%28val%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# 

# On observe :
# 
# - l'appel de fonction provoque une rupture de l'exécution séquentielle, un débranchement de l'appelant vers l'appelé ;
# - le `return` provoque le retour au cadre appelant pour continuer l'exécution séquentielle.
# - Plusieurs `return` ? Oui mais 1 seul exécuté par appel.

# ### Appel = appelant -> appelé ; return = appelé -> appelant 
# 
# Distinguer _appelant_ et _appelé_ :
# 
# - _l'appelant_ : le cadre (ie. la zone logique de code) où l'appel est effectué  
# - _l'appelé_ : le traitement de la définition de la fonction avec les paramètres effectifs de l'appel
# 
# **L'appel provoque une rupture de l'exécution séquentielle de l'appelant** : un débranchement de l'appelant vers l'appelé.
# 
# - L'appel "passe la main" à l'appelé en même temps qu'il transmet les paramètres effectifs et une information pour que l'appelé puisse, plus tard, revenir dans l'appelant (pour fournir le résultat, ie. retourner le résultat).  
# - L'exécution revient dans la zone de l'appelant une fois achevée l'exécution de l'appelé  -- en pratique, après l'exécution d'un `return`.
# - Ce `return` déclenche le retour dans l'appelant à l'instruction de l'appel -- car c'est souvent une affectation si l'appelé est une (vraie) fonction -- ou à l'instruction suivante -- si c'est une procédure qui ne renvoie aucun résultat, cad. un appel sans affectation. 

# <div class="alert alert-block alert-info">
# 
# **A retenir :**   Appel = appelant -> appelé ; return = appelé -> appelant 
# 
# </div> 

# ### `return` = terminaison du traitement de l'appel de fonction et retour au cadre appelant
# 
# L'exécution d'un `return`, quel qu'il soit, _termine l'exécution de la fonction_ et provoque le retour dans le cadre appelant.
# 
# Plusieurs instructions `return` sont possibles dans une même fonction. 
# Donc pas uniquement comme dernière instruction du corps de la fonction. 
# 
# - Le premier `return` exécuté arrête l'exécution
# - les instructions suivantes du corps de la fonction ne sont pas traitées -- comme dans une branche conditionnelle non prise, _eg._ dans une structure `if: ... elif: ... else: ...`. 

# [visualisation pythontutor](http://pythontutor.com/visualize.html#code=def%20aa%28u%20%3A%20float%29%20-%3E%20float%3A%0A%20%20%20%20'''La%20m%C3%AAme%20avec%202%20return%20'''%0A%20%20%20%20if%20u%20%3E%200%3A%0A%20%20%20%20%20%20%20%20res1%20%3D%20u%0A%20%20%20%20%20%20%20%20return%20res1%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20res2%20%3D%20-u%0A%20%20%20%20%20%20%20%20return%20res2%0A%20%20%20%20%20%20%20%20%0Aun%20%3D%20aa%281.0%29%0Aencore_un%20%3D%20aa%28-1.0%29%0A%0A%23%20Profitons-en%20pour%20montrer%20un%20%60assert%60%20%0Aassert%20un%20%3D%3D%20encore_un&cumulative=false&curInstr=14&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# de plusieurs `return` et 1 seul exécuté par appel. 

# In[21]:


def a(u : float) -> float:
    '''calcule la valeur absolue de u'''
    if u > 0:
        res = u
    else:
        res = -u
    return res


# **Rmq**.
# Nous expliquerons bientôt que `res` est une _variable locale_ à la fonction qui est définie pour retourner le résultat du traitement de la fonction. 

# In[22]:


def aa(u : float) -> float:
    '''La même avec 2 return '''
    if u > 0:
        res = u
        return res
    else:
        res = -u
        return res
    
def aaa(u : float) -> float:
    '''La même avec 2 return sans variable locale'''
    if u > 0:
        return u
    else:
        return -u


# In[23]:


# 2 appels
a_x = a(2)
a_y = a(-5)

# affichage
print(a_x, a_y)
#print(a(3))

# intérêt du doc-string
help(a)
help(aa)


# Nous verrons que les fonctions récursives sont friandes de `return` très tôt écrit dans le corps. 

# ### Exercice
# 
# * Reprendre les fonctions `a`, `aa` et `aaa` précédentes et bien identifier le séquencement des instructions exécutées dans l'appelant et l'appelé.  

# :::{note}
# Toute fonction python retourne un résultat. Si aucun `return` est exécuté, la valeur `None` est systématiquement retournée.
# :::
# 
# **Exemple**
# 

# In[24]:


def mal_ecrite(x : int) -> int:
    '''Je ne suis pas un bon exemple'''
    if x > 0:
        return x


# In[25]:


a = mal_ecrite(1)
b = mal_ecrite(0)
print(a, b)


# ## Variable locale _vs._ variable globale, portée des variables
# 
# Les notions de variable locale (à une fonction) ou de variable globale sont classiques en programmation.  
# 
# > **Variable locale** à une fonction : variable définie dans le _corps_ de la fonction pour permettre le traitement réalisé par la fonction.  
# 
# Par extension, les **paramètres formels** de la fonction **sont** aussi **des variables locales**.  

# > Une **variable** est dite  **globale** par rapport à une fonction si elle est définie à l'extérieur de la fonction, et plus particulièrement dans l'appelant de la fonction.  
# 
# Il faut donc introduire la notion de portée d'une variable.  

# > **Portée** : zone où une variable est _accessible_, ou autrement dit : zone où une variable est (re)connue à l'aide de son identifiant.  
# 
# **La portée d'une variable locale est** ... locale, cad. **limitée au corps de la fonction** qui contient sa définition.  
# Une variable locale _n'existe pas à l'extérieur_ de la définition ou du traitement de la fonction.  

# **Exemple.**
# 
# - Reprendre le pythontutor précédent et observer comment `res1` ou `res2` naissent, vivent et meurent.

# Une variable globale est définie dans le cadre _appelant_.  
# Une fois définie, sa portée est globale à ce cadre : cette variable est accessible sur l'ensemble de la zone qui contient sa définition et à partir de cette dernière. 
# 
# Ainsi :
# - la portée d'une variable globale inclut les fonctions, (et leurs corps) définies dans cette zone  
# - les portées d'une variable globale et d'une variable locale (à une fonction) se recouvrent (dans cette fonction); 
# - ce qui nécessitera de clarifier la situation dans le cas où _ces 2 variables ont le même identifiant_.
# 
# Ces trois dernières remarques justifient à l'interdit (à vocation pédagogique) suivant. 

# <div class="alert alert-block alert-danger">
#     
# CONTRAINTE PEDAGOGIQUE :  Dans la définition d'une fonction, il est interdit d'introduire ou d'utiliser des variables globales, excepté si ce sont des **constantes**.
#        
# </div>
# 
# Ainsi, vous ne devez limiter le corps de fonction au traitement de ses paramètres formels et de variables locales.
# 
# <div class="alert alert-block alert-info">
# 
# CONVENTION PYTHON : les identifiants de constantes s'écrivent en MAJUSCULES   
#     
# `ANNEE_EN_COURS = 2020`
# 
# </div>

# Au delà de certaines spécificités de python qui la rendent assez délicate, l'utilisation de variables globale  est à l'origine de la notion _d'effet de bord_ souvent à l'origine de longues phases de debugging. Nous reviendrons sur cet aspect au chapitre suivant.
# 
# Le besoin d'utiliser des variables globales dans des fonctions internes peut être satisfait en ajoutant ces variables comme paramètres de ces fonctions.  
# 

# ### Exercice
# 
# * Reprendre les fonctions `a`, `aa` et `aaa` précédentes et identifier leurs variables locales et leur portée, dans la définition, dans les appels, dans les appelants.   

# ## Compléments

# ### Erreur fréquente
# 
# <div class="alert alert-danger">
# 
# NE PAS CONFONDRE :  `return` _vs._ `print`
# 
# </div>
# 
# La relecture de paragraphe sur le rôle du `return` permet de bien se convaincre qu'un `return` fait des choses bien différentes d'un `print`.

# <div class="alert alert-info">
#     
# CONSEIL DÉJÀ SOUVENT RAPPELÉ : séparer les E/S des traitements
# 
# </div>
# 
# En pratique, les E/S (`print` et `input`) doivent être limitées :
# - aux programme principal (le `main`) 
# - aux sous-programmes d'entrées-sorties spécifiques à votre application, si il y en a.  
#     - Voir `afficher_pref_dpt()` en fin de chapitre.
#     

# ### Méthodologie d'écriture des fonctions  
# 
# En pratique, vous introduirez des fonctions en respectant **l'ordre d'écriture** suivant :
# 
# 1. écriture de la signature de la fonction  
# 2. écriture d'appels simples : notion de _test unitaire_
#     - appels simples = appels sur des valeurs de tests, cad. dont on connaît le résultat attendu de la fonction  
# 3. écriture du corps
# 4. exécution des test unitaires (et correction de l'étape précédente si besoin) 
# 5. écriture des appels voulus  
# 6. exécution des appels voulus
# 
# 
# <div class='alert alert-block alert-danger'>
# 
# CONSIGNE PEDAGOGIQUE : L'écriture de l'appel (simple) est effectuée avant celle du corps, _ie._ en se basant uniquement sur la signature.
# </div>
# 
# Ainsi, il n'est pas possible d'exécuter cet appel avant d'avoir fini l'étape suivante (écriture du corps).

# ### De l'intérêt de distinguer _fonction_ et _procédure_
# 
# <div class="alert alert-block alert-warning">
# 
# CONSEIL : Distinguer les fonctions des procédures oblige à se poser la question du besoin de modifier ou non les arguments du sous-programme.  
# 
# </div>
# 
# Une **fonction** :
# - calcule et retourne un résultat
# - à partir de la __valeur__ de ses paramètres effectifs.  
# - Ce résultat est connu de l'appelant par une affectation (au retour de l'appel).  
# - L'appel de la fonction ne modifie pas les paramètres effectifs. 
# 
# Une **procédure** :
# - effectue une action ou des traitements (dont des lectures et des écritures)
# - avec ses paramètres effectifs
# - et ne retourne pas de résultat.
# - L'appel d'une procédure peut modifier ses paramètres effectifs.
# 
# **Rmq.**
# Ainsi l'appel d'une procédure ne nécessite pas d'affectation dans l'appelant.
# 
# > A la différence d'autres langages, python n'introduit qu'un type de sous-programme : la fonction.  
# > Rappellons qu'une fonction python retourne _toujours_ une valeur, même si cette dernière est `None`.  
# 
# **Exercice.**  Donner un exemple de fonction python (utilisée depuis le début de l'année) qui est en fait une procédure.

# ### `help()` et _docstring_
# 
# `help()` est une fonction python prédéfinie qui affiche l'en-tête (la signature) complet de la fonction passée en paramètre.  
# 
# Elle fournit les informations nécessaires à l'utilisation correcte de la fonction, ainsi que des détails sur son objet et son implémentation -- si le ces aspects ont été décrits par le programmeur dans le `docstring` : la zone de commentaires entre ` ``` ``` ` et indentée sous le `def`.
# 
# Cette fonction est similaire à l'option de commande `--help` sous Unix.

# In[26]:


help(doubler)


# In[27]:


help(f)


# **Exercice**. A quoi reconnait-on que `help` est une fonction ?

# ### Plusieurs paramètres

# In[28]:


def puissance(x : float, n : int) -> float:
    '''calcule x**n de façon itérative pour'''
    # (un) corps de la fonction puissance
    r = 1.0
    for i in range(1, n+1):
        r = r * x
    return r

# appels avec des valeurs  
mille = puissance(10.0, 3)
print("mille =", mille)

vrai_ou_faux = (puissance(3.1,2) == 3.1 * 3.1)
print(vrai_ou_faux)


# In[29]:


# appels avec une variable

#n = int(input("n premières puissances de 2.0 pour n = "))
n = 5
for i in range(n+1):
    print("2 **", i, "=", puissance(2, i))

print("cas particulier")
print(puissance(2.0, 0))

# appels avec des variables

#p = float(input("n premières puissances de p pour p = "))
#n = int(input("et n = "))
p = 3
n = 4

for i in range(n+1):
    print(puissance(p,i))


# ### Plusieurs `return` (rappel)  
# 
# 1. Une fonction qui calcule et renvoie (retourne) la valeur absolue d'un entier
#     * Vue plus haut
# 2. Une fonction `puissance` qui calcule et renvoie $x^n$ pour $n>0$ et $x$ entier
#     * $x^n = x \times x \times x \times x \times \dots \times x$ avec $n-1$ multiplications
#     * $x^0 = 1$ pour $x \neq 0$
#     * pas la peine de perdre trop de temps pour calculer $0^n = 0$ 
#     * faire attention si $n < 0$ : ne rien calculer pour l'instant   

# In[30]:


def puissance2(x : float, n : int) -> float:
    '''calcule x**n de façon itérative : autre version'''
    if x == 0.0:
        return 0.0
    if n == 0:
        return 1
    else:
        r = x
        for i in range(2, n+1):
            print('on est dans la boucle')
            r = r * x
        return r


# appels avec des valeurs 
xx = 10.0
for n in range(0,4):
    val = puissance2(xx, n)
    print(xx, "**", n, "=", val)

#vrai_ou_faux = (puissance(3.1,2) == 3.1 * 3.1)
#print(vrai_ou_faux)


# **Exercice**
# 
# - Simplifier la branche `else` de `puissance2()`.

# ### Fonction sans paramètre 
# 
# Une fonction peut ne pas avoir de paramètre formel. Et donc être appelée sans argument (sans paramètre effectif).

# In[31]:


def tetu() :
    return 1

res = tetu() # appel et affectation du résultat
print('res = ', res)   # affichage

# boucle d'appels à tetu() dans un print()  
for i in range(5):
    print('appel tetu', tetu())
        
# appel sans affectation, ni print. 
# L'interpréteur python affiche sa valeur en Out[..] 
#doubler(1)

tetu()


# ### Fonction locale
# 
# A la manière d'une variable locale, une _fonction locale_ (à une fonction) est :
# 
# - définie dans le corps d'une fonction,
# - puis utilisable par cette fonction (englobante)
# - mais _uniquement par elle_ : elle est inconnue de l'extérieur de la fonction englobante,
# - et ce récursivement.

# In[32]:


def max3(x : int, y : int, z : int) -> int:
    '''
    autre version (1 return) sans fonction locale
    role : calcule et retourne le max de 3 valeurs
    '''
    if x < y:
        if y < z:
            res = z
        else:
            res = y
    else:
        if x < z:
            res = z
        else:
            res = x
    return res


# test exhaustif pour 3 valeurs différentes    
print(max3(1, 4, 2), max3(1, 2, 4), max3(2, 1, 4), max3(2, 4, 1), max3(4, 1, 2), max3(4, 2, 1))


# In[33]:


def max3_f_loc(x : int, y : int, z : int) -> int:
    '''
    role : calcule et retourne le max de 3 valeurs
    avec fonction locale
    '''
    def max2(u, v : int) -> int:
        '''
        fontion locale : 
        calcule et retourne le max de 2 valeurs'''
        if u > v:
            res = u
        else: 
            res = v
        return res
    
    if x < y:
        res = max2(y, z)
    else:
        res = max2(x, z)    
    return res


# In[34]:


m1 = max3(1, 4, 2)
m2 = max3_f_loc(1, 4, 2)

print(m1 == m2)


# ### Exercice
# 
# - Compléter le test unitaire de `max3`.
# - ($\star$) Ecrire une version de `max3` sans variable locale, ni fonction locale.    
# - ($\star$) Ecrire une version de `max3` avec une fonction locale et réduite à _une seule ligne d'instruction_ (pour le traitement de `max3`). 

# **Solution**

# In[35]:


def max3_v2(x : int, y : int, z : int) -> int:
    '''
    role : calcule et retourne le max de 3 valeurs
    version 4 return : sans variable, ni fonction locale 
    '''
    if x < y:
        if y < z:
            return z
        else:
            return y
    if x < z:
        return z
    else:
        return x
    


# In[36]:


def max3_fonctionnelle(x : int, y : int, z : int) -> int:
    '''
    role : calcule et retourne le max de 3 valeurs
    '''
    def max2(u, v : int) -> int:
        '''
        fonction locale : 
        calcule et retourne le max de 2 valeurs'''
        if u > v:
            res = u
        else: 
            res = v
        return res
    
    return max2(x, max2(y, z))

m = max3_fonctionnelle(1, 4, 2)
print(m)


# ### Pas d'effet de bord ! Pas de `global` !
# 
# Une fonction réalise un _effet de bord_ si son traitement modifie (au moins) une variable de l'appelant qui n'est pas la variable d'affectation de son retour, ni un paramètre effectif de l'appel (comme nous le verrons dans un prochain chapitre).

# En pratique (en python), l'éventuel effet de bord peut concerner n'importe qu'elle variable de l'appelant qui existe avant l'appel de la fonction, ie. hors du cadre de la fonction, dès lors que cette variable est caractérisée comme  (pour variable globale). 
# 
# :::{important}
# Pas d'effet de bord implique donc en python  pas d'utilisation du mot-clé `global`.  
# :::

# **Exemple.**
# 
# Dans l'exemple suivant, le second appel modifie aussi la valeur de `a`. Ce qui est impossible à deviner sans connaître le corps de la fonction. On ne peut donc plus l'utiliser comme une "boîte noire".

# In[37]:


a = 0
b = 0
un = 1

def incremente(u : int) -> int:
    return u + 1

def incremente_avec_effet_de_bord(u : int) -> int:
    global a  
    a = a + 10 # mais pourquoi faire ça ici ...
    return u + 1

a = incremente(un) # seul `a` est modifié par la fonction
print(a, b)

b = incremente_avec_effet_de_bord(un) # `a` et `b` sont modifiés 
print(a, b)


# ## Synthèse
# 
# ### Retenir 
# 
# - __Modularité__ : fonction pour factoriser le traitement, structurer le déroulement d'un algo, faciliter la compréhension du traitement et la maintenance des codes
#     - Tests unitaires de fonction, `assert`  
# - Une fonction se reconnaît à :
#     - `def` dans sa définition,
#     - ses parenthèses dans les appels.  
# - Sa _définition_ 
#     - commence par `def`, suivi de près par un `:`, et contient au moins un `return`;
#     - contient entre les parenthèses qui suivent son nom :
#         - la définition des paramètres formels, 
#         - et leur type : annotations `:` et `->`;
#     - contient une _documentation_ entre ` ''' ` qui détaille son rôle (`docstring`). 
# - La _signature_ (ou l'_en-tête_) de la fonction est l'ensemble de ces éléments, `return` excepté.  
#     - `help(nom_de_la_fonction)` affiche la signature de la fonction, cad sa définition, paramètres compris et le `docstring`. 
# - Le _corps_ d'une fonction est la zone indentée par rapport au `def` qui contient le traitement effectué par la fonction, et au moins un `return`.   

# Se souvenir que :
# 
# - l'appel à une fonction génère un _débranchement_ de la séquence d'instructions de l'_appelant_ pour exécuter les instructions de _l'appelé_
# - que le premier `return` exécuté dans l'appelé permet de _revenir_ à l'appelant pour continuer à exécuter la séquence d'instructions qui suit l'appel (dans l'appelant) -- souvent une affectation du résultat de l'appel. 

# ### Ne pas confondre 
# 
# > * __définition__ _vs._ __appel__  
# > * __signature__ _vs._ __corps__  
# > * paramètre __formel__ _vs._ argument ou paramètre __effectif__  
# > * appelé _vs._ appelant  
# > * __return__ _vs._ __print__  

# ### A venir
# 
# Un point important a été passé sous silence dans ce chapitre : 
# - comment s'effectue le passage de paramètres lors de l'appel ?  
# 
# Autrement dit : 
# - comment les paramètres formels de la définition d'une fonction "deviennent" des paramètres effectifs, cad. des valeurs effectivement traités (ou des objets effectivement manipulés) par les instructions du corps de la fonction ? 
# 
# Cette importante question sera traitée dans le chapitre suivant car les réponses diffèrent selon les langages de programmation -- car plus techniques qu'algorithmiques.    

# ## Exercices en démonstration

# ### Lister les notions vues jusqu'ici
# 
# - définition, paramètres formels, sortie  
# - appel, paramètres effectifs  
# - spécification (ce que ça fait) vs. implémentation (comment ça le fait)  
# - `def`, `()`, `return`,  
# - variables locales  
# - fonction, procédure  

# ### Différentes écritures de fonctions min
# 
# - Ecrire la fonction min(a,b) : signature, appels, puis corps ; test unitaires.
# - Proposer plusieurs écritures du corps : avec un seul return, avec deux, ...
# - S'en servir pour écrire la fonction min(x, y, z) : signature, appels, puis corps
# - Proposer plusieurs écritures du corps

# In[38]:


def min(a : int, b : int) -> int:
    '''retourne min(a,b)
    -> version un seul return
    '''
    if a < b:
        m = a
    else:
        m = b
    return m


# In[39]:


def min2(a : int, b : int) -> int:
    '''retourne min(a,b)
    -> version deux return
    '''
    if a < b:
        return a
    else:
        return b


# In[40]:


def min3a(a : int, b : int, c : int) -> int:
    '''retourne min(a,b,c)
    -> version 1 return, 2 appels à min(a,b)
    '''
    if min(a, b) < c:
        m = min(a, b)
    else:
        m = c
    return m


# In[41]:


def min3b(a : int, b : int, c : int) -> int :
    '''retourne min(a,b,c)
    -> version 1 return, 1 appel à min(a,b)
    '''
    m_ab = min(a, b)
    if m_ab < c:
        m = m_ab
    else:
        m = c
    return m


# In[42]:


def min3(a : int, b : int, c : int) -> int:
    '''retourne min(a,b,c)
    -> version fonctionnelle : 2 appels imbriqués 
    '''
    return min(min(a, b), c)


# In[43]:


# des appels
x = 23
y = 44
z = 27
m_xyz = min3a(x, y, z)
print(m_xyz)
m_xyz = min3b(x, y, z)
print(m_xyz)
m_xyz = min3(x, y, z)
print(m_xyz)


# ### Une procédure d'affichage (E/S) 
# 
# Ecrire une fonction qui réalise efficacement l'affichage suivant :
# 
# ```
# Carcassonne est la préfecture du département 11
# ------------------------------------------------
# Perpignan est la préfecture du département 66
# ------------------------------------------------
# Montpellier est la préfecture du département 34
# ------------------------------------------------
# Foix est la préfecture du département 09
# ------------------------------------------------  
# ```

# In[44]:


# Bourrin et pas satisfaisant
print("Carcassonne est la préfecture du département 11")
print("------------------------------------------------")
print("Perpignan est la préfecture du département 66")
print("------------------------------------------------")
print("Montpellier est la préfecture du département 34")
print("------------------------------------------------")
print("Foix est la préfecture du département 09")
print("------------------------------------------------")

# On pourrait bien sûr mettre tout dans un seul print (avec des `\n`)
# ce qui n'est pas satisfaisant non plus ...


# In[45]:


# Synthétique mais un peu pythonesque : une boucle sur des "couples" (tuple) 
for v,d in ("Carca", "11"), ("Perpi","66"), ("Montpel", "34"), ("Foix", "09"):
    print(v, "est la préfecture du département", d)
    print("------------------------------------------------")


# - Le couple entre parenthèses `("Carca", "11")` est un **tuple** python, notion sur laquelle nous reviendrons très vite  
# - En attendant, considérer ce tuple comme une constante composée de 2 valeurs de type string

# In[46]:


# définition d'une fonction qui affiche ce qu'on veut comme on veut
def afficher_pref_dpt(ville : str, num_dpt : str):
    print(ville, "est la préfecture du département", num_dpt)
    print("------------------------------------------------")


 # 4 appels de cette fonction
afficher_pref_dpt("Carca", "11")
afficher_pref_dpt("Perpi", "66")
afficher_pref_dpt("Montpell", "34")
afficher_pref_dpt("Foix", "09")

print()

# 4 appels synthétiques de façon pythonesque  
for (v,d) in ("Carca", "11"), ("Perpi","66"), ("Montpell", "34"), ("Foix", "09"):
    afficher_pref_dpt(v,d)



# **Rmq.** 
# 
# - Pourquoi `afficher_pref_dept()` n'est pas une fonction excepté pour python ?
# 
