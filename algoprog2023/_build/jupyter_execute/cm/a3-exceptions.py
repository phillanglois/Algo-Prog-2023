#!/usr/bin/env python
# coding: utf-8

# # Exceptions
# 
# Programmation.
# 
# Version 2020 (PhL).
# 
# **NOTE 2022** Reprendre ce chapitre pour afficher les exceptions levées par le nb.
# Metadata de ce nb maj avec 
# `allow_errors: true`
# cf [doc](https://jupyterbook.org/content/execute.html#execution-configuration)

# <h1>Table des matieres<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Principes" data-toc-modified-id="Principes-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Principes</a></span></li><li><span><a href="#Les-exceptions-prédéfinies" data-toc-modified-id="Les-exceptions-prédéfinies-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Les exceptions prédéfinies</a></span></li><li><span><a href="#Traitement-des-exceptions-en-python" data-toc-modified-id="Traitement-des-exceptions-en-python-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Traitement des exceptions en python</a></span><ul class="toc-item"><li><span><a href="#Premier-exemple-gentil" data-toc-modified-id="Premier-exemple-gentil-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Premier exemple gentil</a></span></li><li><span><a href="#Remarques" data-toc-modified-id="Remarques-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Remarques</a></span></li><li><span><a href="#Exemples" data-toc-modified-id="Exemples-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exemples</a></span></li></ul></li><li><span><a href="#Exceptions-définies-par-l'utilisateur" data-toc-modified-id="Exceptions-définies-par-l'utilisateur-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Exceptions définies par l'utilisateur</a></span><ul class="toc-item"><li><span><a href="#Levée-d'exception-prédéfinie" data-toc-modified-id="Levée-d'exception-prédéfinie-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Levée d'exception prédéfinie</a></span></li><li><span><a href="#Définir-ses-propres-exceptions" data-toc-modified-id="Définir-ses-propres-exceptions-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Définir ses propres exceptions</a></span></li></ul></li><li><span><a href="#Précondition" data-toc-modified-id="Précondition-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Précondition</a></span></li><li><span><a href="#Synthèse" data-toc-modified-id="Synthèse-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Synthèse</a></span></li></ul></div>

# ## Principes
# 
# Motivation : certains traitements ne peuvent pas s'effectuer correctement. Comme par exemple l'évaluation d'une racine carrée négative, une division par zéro, la lecture au delà de la fin d'un fichier, l'écriture au delà de la zone mémoire accessible, ... 
# 
# Ces situations _exceptionnelles_ sont prises en compte par le mécanisme des _exceptions_. 
# 
# 3 étapes :
# 1. `raise`: l'apparition de la situation exceptionnelle _lève_ une exception
# 2. `except`: un _traitement de substitution_ (ou _traite exception_) défini pour gérer au mieux l'exception concernée est appliqué  
# 3. suite à ce traitement : _reprise_ ou _abandon_ du traitement initial.  

# En général, la levée d'une exception correspond à une situation _anormale_ du traitement. Ainsi le traitement normal est _interrompu_ et le _traite exception_ a pour objectif de "limiter la casse". 
# Il est rare, mais pas impossible, qu'un _traite exception_ permette de reprendre l'exécution normale du traitement principal.  
# 
# Il existe deux types d'exceptions.
# - les **exceptions prédéfinies** par le langage ou par des modules utilisés  
# - les exceptions définies par l'utilisateur  

# <div class="alert alert-block alert-info">
# Bien distinguer les _erreurs de syntaxe_ à l'interprétation/compilation des exceptions à _l'exécution_. 
# </div>

# ## Les exceptions prédéfinies
# 
# En python (et dans d'autres langages), ces exceptions sont nombreuses.
# Voir par exemple : [doc python](https://docs.python.org/fr/3.5/library/exceptions.html)
# 
# Elles sont organisées selon leur origine (système, calcul, mémoire, exécution, périphérique, ...) par groupe et/ou de façon hierarchisée : [hierarchie des exceptions python](https://docs.python.org/fr/3.5/library/exceptions.html#exception-hierarchy)

# Parmi les exceptions les plus souvent rencontrées :
# 
# ``` python
# - ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
# - EOFError
# - NameError
# - OSError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
# - RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       |    +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
# - TypeError
# - ValueError
#       |    +-- UnicodeError
# ```

# **Remarque** :
# - Expliquer pourquoi les exceptions `SyntaxError` ou `IndentationError` peuvent être levées à l'exécution ?

# ## Traitement des exceptions en python
# 
# La gestion des exceptions s'effectue avec la construction suivante qui __encadre les zones à risques__ : 
# 
# ```python
# try :
#     # la partie du traitement principal susceptible de mal se passer
# except UneException:
#     # traitement prévu si l'exception `UneException` est levée
# except (UneAutre, EtEncoreUneAutre):
#     # traitement prévu si les exceptions `UneAutre` ou `EncoreUneAutre` sont levées
# except:
#     # traitement prévu si toute autre exception est levée
# else:
#     # traitement si aucune exception n'a été levée dans le bloc 'try' 
# ```

# **Principe **
# - le bloc `try` est exécuté
# - si aucune exception est levée par cette exécution, les blocs `except` sont sautés et le traitement continue normalement après l'instruction `try` 
#     - dans le bloc `else` si il existe  
#     - sinon à l'instruction suivante de même niveau que le `try`
# - si une instruction du bloc `try` lève une exception :
#     - le bloc `try` est _immédiatement_ abandonné : il n'est donc pas exécuté en entier
#     - on recherche si un traite exception correspondant à l'exception levée est défini
#         - si oui : on l'exécute et on continue après l'instruction `try` 
#         - si non : l'exception est propagée au `try` de niveau englobant.  
#         

# ### Premier exemple gentil

# In[1]:


#x = float(input("Un float stp :"))
x = 3
print("Son inverse vaut", 1./x)
print("et on vérifie : x * 1/x =", x * 1/x)


# Le traitement précédent (qui mélange ES et traitements) comporte une situation exceptionnelle qui va lever l'exception arithmétique `ZeroDivisionError` dans le cas suivant.

# ```python
# x = 0.0
# print("Son inverse vaut",  1./x)
# ```
# ```shell
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-2-56b7ed41bd3d> in <module>
#       1 x = float(input("Un float stp :"))
# ----> 2 print("Son inverse vaut",  1./x)
# 
# ZeroDivisionError: float division by zero
# ```

# On encadre la zone dangereuse avec un bloc `try - except`.  

# In[2]:


try :
    x = float(input("Un float stp :"))
    print("Son inverse vaut", 1./x)
except ZeroDivisionError :
    x = float(input("Un float NON NUL stp :"))
    print("Son inverse vaut", 1./x)
except:
    print("Désolé : on ne peut rien pour toi")
    raise
print("et on vérifie : x * 1/x =", x * 1/x)


# In[3]:


try :
    x = float(input("Un float stp :"))
    print("Son inverse vaut", 1./x)
except ZeroDivisionError :
    x = float(input("Un float NON NUL stp :"))
    print("Son inverse vaut", 1./x)
except :
    print("Désolé : on ne peut rien pour toi")
    raise
print("et on vérifie : x * 1/x =", x * 1/x)


# In[4]:


try :
    x = float(input("Un float stp :"))
    print("Son inverse vaut", 1./x)
except ZeroDivisionError :
    x = float(input("Un float NON NUL stp :"))
except :
    print("Désolé : on ne peut rien pour toi")
    raise
print("et on vérifie : x * 1/x =", x * 1/x)


# **Analyse**
# - Le traitement d'entrée au clavier est risqué  :
# - levée de l'exception `ZeroDivisionError` si l'utisateur entre `0` 
# - dans ce cas, le traite-exception permet de récupérer _cette_ erreur en redemandant une autre entrée
#     - traitement sûr si la nouvelle entrée est correcte
#     - mais ....

# In[5]:


try :
    x = float(input("Un float stp :"))
    print("Son inverse vaut", 1./x)
except ZeroDivisionError :
    x = float(input("Un float NON NUL stp :"))
    print("Son inverse vaut", 1./x)
except :
    print("Désolé : on ne peut rien pour toi")
    raise
print("et on vérifie : x * 1/x =", x * 1/x)


# **Exercice**
# - Que faire ?

# ### Remarques
# 
# - __Un seul__ traite exception est exécuté lorsque le bloc `try` lève une exception  
# - Principe de **propagation ascendante d'une exception non traitée** : si aucun traite-exception est rencontré pour l'exception levée,
#     - cette exception est **propagée** au niveau supérieur, 
#     - et ce jusqu'à rencontrer le traite-exception qui va, 
#     - ou à défaut d'arrêter définitivement le traitement  
# - `raise` propage explicitement l'exception au niveau supérieur
# - __Interdire__ le "`except` sans `raise`" qui va absorber toutes les exceptions, même celles non prévues et donc significatives d'une anomalie profonde de l'exécution  

# ### Exemples
# 
# Les ES sont des zones à risque.
# 

# In[6]:


try :
    f = open("./fichier_qui_n_existe_pas.txt", "r")
except FileNotFoundError:
    print("Fichier pas trouvé")


# In[7]:


get_ipython().system('cat ./tmp/fichier_entrees2.txt')


# Le comportement suivant illustre la robustesse de python :
# - `readline()` ne lève pas d'exception EOF 
# - mais renvoit une chaine vide ;
# - ce qui n'est pas le cas de nombreux langages qui effectueraient le même traitement (incorrect)

# In[8]:


f = open("./tmp/fichier_entrees2.txt", "r")

x = [0]*7
for i in range(7):
    x[i] = f.readline()

print(x)
f.close()


# Peut quand-même avoir des problèmes :

# In[9]:


import numpy as np
f = open("./tmp/fichier_entrees2.txt", "r")

tab = np.zeros(3, dtype='int32')

n = int(input("Nbre de valeurs à lire : "))

for i in range(n):
    tab[i] = f.readline()

print(tab)
f.close()


# In[10]:


import numpy as np
f = open("./tmp/fichier_entrees2.txt", "r")

tab = np.zeros(3, dtype='int32')

n = int(input("Nbre de valeurs à lire : "))

for i in range(n):
    try:
        tab[i] = f.readline()
    except IndexError:
        print("Tab trop petit :", np.shape(tab))
        
print(tab)
f.close()


# ## Exceptions définies par l'utilisateur
# 
# Le développement de modules ou de traitements peut nécessiter de prévoir des cas exceptionnels qui seraient déclenchés par leur utilisation incorrecte.  
# 
# ### Levée d'exception prédéfinie
# 
# On peut souhaiter _lever une exception prédéfinie_ qui correspond au type d'erreur qu'elle couvre dans le cas général.
# 
# Il suffit d'exécuter :
# > `raise telle_exception("message d'accompagnement") `
# 
# **Exemple**  
# Un exemple est donné dans le paragraphe suivant avec l'exception `AssertionError` 

# In[11]:


'''On récupère des entrées au clavier pour initialiser un vecteur de taille fixée.
le traitement de la ligne 10 peut lever l'exception prédéfinie IndexError'''
v = [0, 0, 0]
cond = True
i = 0
while cond:      
    x = float(input("Une valeur stp :"))
    if i >= len(v):
        raise IndexError("v est de longueur", len(v), "et", i,"-ième entree.")
    v[i] = x
    i = i + 1    

    


# ### Définir ses propres exceptions
# 
# Il faut aussi pouvoir _définir ses propres exceptions_   
# - adaptées au traitement proposé par notre module   
# - et qui seront éventuellement traités par le contexte qui utilise notyre module.  
# 
# En python, la définition des exceptions passe par la définition de _classes_ (et de sous-classes d'exception) intégrées au module développé.  
# 
# N'ayant pas introduit la notion de classe, nous ne détaillerons donc pas (cette année) comment définir ses propres exceptions.   

# ## Précondition
# 
# Certaines fonctions (ou traitements) sont définies avec des hypothèses sur les arguments effectifs.  
# - Par exemple, la division `x/y` n'est pas définie pour `y == 0` et ce cas lève l'exception prédéfinie `ZeroDivisionError`.  
# 
# L'instruction **`assert`** permet de vérifier une précondition.  
# - Une _précondition_ est une expression à valeur booléenne  
#     - Exemple : `y != 0` est une précondition pour la division `x/y`  
# - Si la précondition est satisfaite (True), le traitement continue normalement  
# - sinon l'exception `AssertionError` est levée.  

# In[12]:


def diviser(x, y):
    assert y != 0
    return x/y

print(diviser(4., 2.))
print(diviser(4., 0.))


# L'assertion peut être accompagnée d'un message indicatif comme annoncé plus haut.  

# In[13]:


def mon_diviser(x, y):
    assert y != 0, "mon_diviser : division par 0"
    return x/y

print(mon_diviser(4., 2.))
print(mon_diviser(4., 0.))


# **Utilisation**
# - Vérifier les préconditions le plus tôt possible dans le cadre de la fonction pour éviter les modification d'états qui ne seront pas menées correctement jusqu'au bout  
# - Le traitement est similaire à un `if` associé à la levée de l'exception `AssertionError` mais la lecture d'une clause `assert` est plus informative qu'un `if` (parmi d'autres) sur les conditions d'utilisation du code concerné.  
# - Utile au debuggage  

# ## Synthèse
# 
# - Les exceptions qualifient des traitements incorrects _exceptionnels_ 
# - Les traites exception permettent de "récupérer la main" pour sortir au mieux du c as incorrect
# - Encadrer les zones à risque de la construction : `try: ... except: ...` 
# - Le mécanisme est "traitement `except` ou sinon propagation"  
# - `raise` pour lever ses exceptions  (prédéfinies ou personnelles) 
# - `assert` pour définir et vérifier des préconditions  
# 
