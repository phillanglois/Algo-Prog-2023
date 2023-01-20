#!/usr/bin/env python
# coding: utf-8

# # Annexe : les booléens en python (>3.6)
# 
# Une mise au point sur les booléens en python
# 
# - synthétique    
# - basée sur la documentation python 3.8 et
# - avec **ce qui est important à retenir** écrit en **gras**.
# 

# ## Synthèse qui suffit en L1  
# 
# Python définit :
# * deux valeurs booléennes `False` et `True`  
# * la fonction de conversion `bool()` qui retourne `True` la plupart du temps,   
# sauf : 
#     *  pour les arguments numériques **nuls** : `0`, `0.0`, `0 + 0j`, 
#     * la valeur spéciale `None` 
#     * et toute **valeur vide** -- cad de longueur `len()` égale à 0-- d'un type composé  `str`, `set`, `lst`, `dict`      
#     
#     
# où elle retourne `False`. 

# ## Valeurs booléennes
# > Les [valeurs booléennes](https://docs.python.org/fr/3.7/library/stdtypes.html#truth) sont les deux objets constants **False** et **True**.   
# 
# > Ils sont utilisés pour représenter les valeurs de vérité _bien que d'autres valeurs peuvent être considérées vraies ou fausses_.   
# 
# > Dans des contextes numériques (par exemple en argument d'un opérateur arithmétique), ils **se comportent comme les nombres entiers 0 et 1**, respectivement.   
# 
# ## Conversion en une valeur booléenne
# 
# > La fonction native **`bool()`** peut être utilisée pour convertir n'importe quelle valeur en booléen **tant que la valeur peut être interprétée en une valeur de vérité**.

# **($\star$)**
# Voilà la [description](https://docs.python.org/fr/3.7/library/functions.html#bool) de la fonction native `bool()`:
# 
# > `class bool([x])`  
# >
# > Donne une valeur booléenne, c'est à dire soit True, soit False.  
# > x est converti en utilisant la procédure standard d'évaluation de valeur de vérité.  
# > **Si x est faux, ou omis**, elle donne **False**, **sinon, elle donne True**. 
# > La classe bool hérite de la classe int (voir Types numériques — int, float, complex). 
# > Il n'est pas possible d'en hériter.  
# > Ses seules instances sont False et True (voir Valeurs booléennes).
# 
# > Modifié dans la version 3.7: x est désormais un argument exclusivement optionnel.

# **($\star$)**
# Et la [description](https://docs.python.org/fr/3.7/reference/datamodel.html?highlight=__bool#object.__bool__) de la méthode `.bool()`:
# 
# > `object.__bool__(self)`
# >
# > Appelée pour implémenter les tests booléens et l'opération native bool() ; elle doit renvoyer False ou True. 
# > Quand cette méthode n'est pas définie, **__len__() est appelée**, si elle est définie, et l'objet est considéré **vrai si** le résultat est **non nul**. 
# >  
# > Si une classe ne définit ni __len__() ni __bool__(), **toutes** ses instances sont considérées comme **vraies**.

# ## Objets et booléens  
# 
# Tout objet peut être comparé à une valeur booléenne, typiquement dans une condition if ou while ou comme opérande des opérations booléennes ci-dessous.
# 
# > Par défaut, **tout objet est considéré vrai**  
# > **à moins que** sa classe définisse :
# >- soit une méthode **__bool__() renvoyant False**  
# >- soit une méthode **__len__() renvoyant zéro**   
# >
# >lorsqu'elle est appelée avec l'objet. 
# 
# On va regarder plus en détail la méthode `bool()`dans la cellule suivante.
# 
# ```{Note}
# Voici la majorité des **objets** natifs considérés comme étant **faux** :
# 
# - les **constantes** définies comme étant fausses : **None** et **False**.
# - les **zéros de tout type numérique** : 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# - **les chaînes et collections vides** : '', (), [], {}, set(), range(0)
# ```
# 
# **Rmq.** Ainsi, tous les autres cas sont considérés comme étant **true** !  
# 
# > Les opérations et fonctions natives dont le résultat est booléen donnent toujours :
# - **0 ou False** pour faux 
# - **1 ou True** pour vrai, sauf indication contraire. 
# 
# (Exception importante : les opérations booléennes or et and renvoient toujours l'une de leurs opérandes.)

# In[1]:


# Sauter cette cellule à regarder à la fin si besoin :
help(bool)


# qui définit la méthode `bool()` suivante, héritée d'`int` :
# ```python
# __bool__(self, /)
#     self != 0
# ```
# On rappelle que :
# > par défaut, **tout objet est** considéré **vrai** **à moins que** sa classe définisse soit une méthode  **__bool__() renvoyant False** soit une méthode **__len__() renvoyant zéro** lorsqu'elle est appelée avec  l'objet;
# 
# et que l'on peut donc ré-écrire sous la forme de la fonction `mon_bool()` suivante :
# 

# In[2]:


def mon_bool(x = None):
    try: # si len() existe pour x
        res = len(x) != 0
        return res
    except: # sinon en s'inspirant de la méthode bool()
        res = (x != 0) and (x != None) and (x != False)
        return res


# Quelques test unitaires de notre fonction `mon_bool()` et de la méthode de référence `bool()`.

# In[3]:


print("False, None, 0, () : que du faux tout ça Madame !")
print("- avec bool(): ", bool(False), bool(None), bool(0), bool())
print("- avec mon_bool(): ", mon_bool(False), mon_bool(None), mon_bool(0), mon_bool())
print("- avec int():", int(False), int(0), int())

# le bloc suivant va déclencher une erreur qu'on va rattraper
try:
    print(int(None))
except:
    print("pb : int() ne s'applique pas à None")

print("\nint->booléen:")
for i in range(-3,4):
    print(i, "->", bool(i), mon_bool(i))

print("\nbool->booléen:")
for b in (False, None, True):
    print(b, "->", bool(b), mon_bool(b))
    
print("\nchar->booléen:")
for c in "azertyuiop=:;,?./+1234567890":
    print(c, "->", bool(c), mon_bool(c))
    
print("\nstring->booléen:")
for s in ('', "0"):
    print(s, "->", bool(s), mon_bool(s))


# In[4]:


help(str)


# Quizz: On regarde bien les dernières lignes des deux dernières catégories et on explique pourquoi on n'est pas surpris.
# 
# 
# ## Opérations booléennes --- `and`, `or`, `not`
# 
# Ce sont les opérations booléennes, classées par priorité ascendante :
# 
# > **x or y** : si x est faux, alors y, sinon x  
# > **x and y** : si x est faux, alors x, sinon y  
# > **not x** : si x est faux, alors True, sinon False
# 
# ```{warning}
# `or` et `and` sont des opérateurs "dits fénéants" : ils retournent le résultat dès que celui-ci est connu.  
# En pratique, dès que l'opérande de gauche a été évalué (à `false` pour `and` et à `true`pour `or`) et **sans évaluer** l'opérande de droite.  
# ```
# 
# ````{note}
# **Intérêt pratique très très commode !** : éviter le débordement d'un tableau dans un test.
# 
# ```python
#     if i < len(t) and t[i] == 0:
#     ...
# ```
# ````
# 
# Quizz : A votre avis, permuter les opérandes de la condition précédente est sans conséquence ? (True/False :)   

# ## Comparaisons 
# 
# Il y a huit opérations de comparaison en Python. 
# * `==` : égal  
# * `!=` : différent  
# * `<` : strictement inférieur  
# * `<=` : inférieur ou égal  
# * `>` : strictement supérieur  
# * `>=` : supérieur ou égal  
# * `is` : identité d'objet  
# * `is not` : contraire de l'identité d'objet  
# 
# Elles ont toutes la même priorité (qui est supérieure à celle des opérations booléennes). 
# 
# > **Attention.** Les comparaisons **peuvent être enchaînées arbitrairement**
# 
# Par exemple, x < y <= z est équivalent à x < y and y <= z, sauf que y n'est évalué qu'une seule fois (mais dans les deux cas z n'est pas évalué du tout quand x < y est faux).
# 
# 
