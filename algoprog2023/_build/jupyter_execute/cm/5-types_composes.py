#!/usr/bin/env python
# coding: utf-8

# (ch:typescomposes)=
# # Les types composés
# 
# Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes`
# minutes minimum, PhL.

# Les types composés ou _conteneurs_ de python sont  introduits  dans ce chapitre :  
# - les types _non mutables_ de python : `tuple` et `str`
# - les types _mutables_ de python : `list`, `set` et `dict`
# 
# **Rmq de vocabulaire :** 
# 
# J'utilise les termes _mutable_ et _non mutable_.  
# La version française de la documentation de python préfère les termes _muable_ et _immuable_.

# ## Les types composés ou _conteneurs_ en python
# 
# Les types scalaires permettent de manipuler des _valeurs scalaires_ comme les :  
# - `bool` 
# - `int`  
# - `float`  
# - `complex` 
# - les caractères (souvent dénotés de type _char_ mais absent en python)  
# 
# Un type composé permet de **regrouper plusieurs valeurs**, de même type ou non, scalaire ou non, **dans une seule variable** (ou un seul objet).  
# 
# **Vocabulaire.**
# Ces types composés sont appelés des _conteneurs_ en python.
# Ce sont aussi des premiers exemples de _structures de données_ en algorithmique.
# 
# **Exercice.** Vous en connaissaissez déjà au moins un. Lequel ?

# ### Les questions abordées dans ce chapitre
# 
# - Comment créer un conteneur ?
# - Comment accéder à une valeur dans un conteneur ?
# - Comment modifier un conteneur ?
#     - Comment modifier une de ses valeurs ?
#     - Comment ajouter ou supprimer une valeur ?
# - Comment parcourir (toutes) les valeurs d'un conteneur ?
# 
# Les réponses à ces questions dépendent :
# - du type de conteneur, 
# - de son caratère mutable ou non, 
# - de son caractère itérable ou non, 
# - de son caractère séquençable ou non.
# 
# ($\star$) Les deux dernières caractéristiques (itérable, séquençable) seront abordées en seconde lecture. 
# 
# ($\star$) On analysera aussi la complexité des ces différents traitements selon les principaux types composés.
# 

# ### La vision classique  
# 
# Dans la plupart des langages de programmation, les types composés _classiques_ sont les suivants.
# 
# **Les tableaux**, déjà revus dans ce [chapitre](ch:boucles), sont définis comme des ensembles de valeurs _de même type_ et de nombre _connu et fixé_ "une fois pour toute" lors de leur définition (ce nombre est la _taille_ ou la _dimension_ du tableau) et dont les valeurs sont _ainsi stockées de façon contigüe en mémoire_.   
#     - les valeurs sont accédées par un ou des _indice_ indiqué entre un ou plusieurs `[]`   
# 
# **Les enregistrements** ou **structures** sont définis comme un ensemble de valeurs de _types quelconques_. Le nombre de valeurs est défini "une fois pour toutes" mais sans hypothèse  sur le mode de stockage.   
#     - les enregistrements sont composés de _champs nommés_ aussi appelés _attributs_  
#     - la valeur stockée dans le champ d'un enregistrement est accessible en _notation pointée_ : `id_de_variable.nom_du_champ`.  
#     

# Aucun type composé natif de python ne correspond exactement aux 2 types composés classiques tableau et enregistrement. 
# Le module `numpy` définit  "de vrais" tableaux, les `ndarray`, que nous abordons dans cette [annexe](ann:ndarray).

# Exemple : Une structure `etudiant` pourrait être définie à partir des 4 champs suivants :
# - `etudiant.numero_etud`, 
# - `etudiant.nom`, 
# - `etudiant.prenom` et 
# - `etudiant.diplome`.  

# ### Les conteneurs python 
# 
# **Vocabulaire python :**  un _conteneur_ est une variable (un objet) de type composé 
# 
# Les conteneurs python sont répartis en 2 familles. 
# 
# 1. Les conteneurs **non mutables** dont _la forme et les valeurs_ sont _fixées_ une fois pour toute lors de leur définition :
#     - les chaines de caractères : `str` écrits avec des `" ... "` ou des ` ... ` 
#     - les t-uplets ou `tuple` : des valeurs écrites entre `(  )` et séparées par des `,` 
#     - les ensembles ou `set` : des valeurs écrites avec des `{   }` et séparées par des `,`    
#     
# 2. Les conteneurs **mutables** qui peuvent changer de forme et de valeurs.
#     - des listes ou `list` : des valeurs écrits entre `[  ]` et séparées par des `,`  
#     - des dictionnaires (tableaux associatifs) ou `dict` : des couples de valeurs écrits entre `{ }` et séparées par des `,`  
#     - les fichiers de texte 

# Les fichiers (le type `file`) sont aussi des conteneurs. 
# Ils ne sont pas abordés ici et font l'objet de ce [chapitre](ch:ES-fichiers).    

# ## Ce qui est commun aux conteneurs python
# 
# ### Opérations communes aux conteneurs python 
# 
# **Accès à l'élément** par indexation :
# 
# > `v[1]`,`m[3][2]`, `st[-1]`, `tuple[-len(tuple)]`, `d[clé]`  
# 
# - L'"indice" est indiqué entre `[ ]`
# - Un conteneur _ordonné par des indices entiers_ est appelé une **séquence**.
# 
# **Tranche** d'un conteneur (_slice_): 
# 
# > `conteneur[i:j]` est composé des valeurs de l'indice `i` à `j-1` 
# 
# Des fonctions de base qui s'appliquent à une variable conteneur:
# * `len()` qui renvoie le nombre de valeurs du conteneur
# * `min()`, `max()`, `sorted()` si une relation d'ordre s'applique _aux éléments_
#     - Rmq: `sorted()` modifie l'état du conteneur.
# * **itération sur les _valeurs_** d'un conteneur :
#     > `for val in conteneur:`  
#     - pythonerie utile en pratique pour parcourir les valeurs d'un conteneur sans se soucier de son "indice" 
#     - cette itération s'effectue indépendamment de l'existence ou non d'un ordre sur les _valeurs_ du conteneur, ie. séquence ou non séquence. 
#     - tous les conteneurs sont ainsi des **itérables**.
# 
#      

# **Exercice.** Que pensez-vous de la variable `v` définie par `v = range(10)` par exemple ?

# In[1]:


v = range(10)
print(v)

for val in v:
    print(val, end=",")
print()

print(type(v), type(val))


# _Réponse :_ `v` peut être vue comme un ensemble ordonné itérable de valeurs entières. Ici le terme _ensemble_ est à comprendre au sens mathématique ; il ne s'agit pas des ensembles `set` de python présentés plus loin.
# 
# L'exemple suivant illustre la différence entre un tableau et un conteneur de type `list`.

# In[2]:


from math import exp

en_vrac = ['a','z','e','r','t', 1, 2, 3, 3.14159, exp(1.0)]
print(type(en_vrac), len(en_vrac))


# Et maintenant quelques manipulations avec les opérations de base sur ces conteneurs.

# In[3]:


print(en_vrac)

# conversion de type : list -> tuple
des_float = tuple(en_vrac[-2:]) 

# len, min, max
print(des_float, len(des_float), min(des_float), max(des_float), end="\n")


# In[4]:


# accès par indexation et tranche
print(en_vrac, des_float)
print(type(en_vrac[0]), type(en_vrac[-3]), type(des_float[1]), type(des_float[1:3]))


# In[5]:


# les tranches de conteneurs sont souvent très utiles.
print(en_vrac[1:-1])
print(des_float[1:3])


# In[6]:


# conversion en `str` et concaténations
print(en_vrac)
st = ''
for c in en_vrac[0:-2]:
    #st = st + c     # non : normal !
    st = st + str(c)  # concatenation de chaines de caractères
print(st, type(st))


# Le caractère non mutable d'une `str` explique le comportement suivant.

# In[7]:


# sorted sur `str` retourne une `list` 
print(sorted(st), type(sorted(st)))

st2 = str(sorted(st))
print(st2, type (st2))

print( len(sorted(st)), len(st2) )


#     
# ### Conteneurs itérables et séquences 
# 
# Tous les conteneurs sont (des) _itérables_.
# 
# - la construction suivante a du sens et permet le parcours des _valeurs_ du conteneur
# > `for val in cont:`  
# >  `   ...`
# 
# Mais tous les conteneurs ne sont pas des _séquences_.
# 
# Une **séquence** est un conteneur indexé par des entiers 
# - types python : `tuple`, `list` et `str`
# - les valeurs sont ainsi _ordonnées_ dans le conteneur
# 
# Les dictionnaires `dict` et les ensembles `set` sont itérables mais pas des séquences.

# **Fonctions supplémentaires**  
# 
# `cont` est un conteneur.
# 
# * concaténation : `cont1 + cont2`
# * duplication : `cont * cst`
# * `reversed(cont)` renvoie le conteneur _itérable_ en ordre inverse
# 
# Et aussi les 2 fonctions-méthodes suivantes dont on n'oubliera pas qu'elle peuvent "coûter très cher" : 
# * correspondance valeur -> indice  : 
# `cont.index(val)` 
# retourne le plus petit (ou premier) indice d'une valeur argument présente dans le conteneur `cont`, génère une exception si la valeur est absente  
# 
# * décompte :
# `cont.count(val)` 
# retourne le nombre d'occurrences de `val` dans le conteneur `cont` 

# In[8]:


print(en_vrac[0:-2]) 


# In[9]:


st = ''
for c in reversed(en_vrac[0:-2]):
    st = st + str(c)  # concatenation de chaines de caractères
print(st, sorted(st))


# In[10]:


st1 = st + st
st2 = st * 2
print(st, st1, st1 == st2)

print(st.count('a'))
print(st.index('a'))


# ## Les `tuple` 
# 
# **`tuple`** ( ou t-uplets) : _conteneur_ _non mutable_ de valeurs _écrites entre `(  )`_ ,  séparées par des `,`, et _indexées de 0 à `len(tuple)-1`_.
# 
# > (3, "bonjour", 7, 1.32)
# 
# - Bien identifier les 4 aspects qui définissent un tuple  
# - En pratique, les parenthèses sont facultatives  
#     * donc un tuple singleton peut être noté : `a,`  
#     * __Ne pas oublier la `,`!!__ 
#     

# In[11]:


t = (3,)
print(type(t))

# ATTENTION !
t = (3)
print(type(t))
t = 3,  
print(type(t))


# <div class="alert alert-block alert-info">
#     
# On préférera donc écrire les tuples systématiquement entre parenthèses. 
#     
# </div>

# In[12]:


# premières manipulations de tuple
c = (1,2,3)
c2 = c + c
print(c2)
d1 = c * 3
c = c + (4,)
print(c, d1)


# **Attention.** 
# 
# - Les `tuple` sont non mutables donc modifier `c` (ici par concaténation à l'avant-dernière ligne) créé en fait une _nouvelle_ variable `c`.  
# - L'exécution [pythontutor](https://pythontutor.com/visualize.html#code=c%20%3D%20%281,2,3%29%0Ac2%20%3D%20c%20%2B%20c%0Ad1%20%3D%20c%20*%203%0Ac%20%3D%20c%20%2B%20%284,%29&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# illustre bien ce point important.

# **Exercice.** Que penser de la fonction à la spécification incomplète suivante ?

# In[13]:


def permuter(a : int, b : int) :
    '''il manque la spécification de la sortie'''
    return b, a

x, y = 3, 7
print(x, y, type(x), type(y))
x, y = permuter(x, y)
print(x, y, type(x), type(y))
(u, v) = permuter(x, y)
print(u, v, type(u), type( (u, v) ), type( (u, v)[0] ) )


# In[14]:


#d1[2] = 7 lève TypeError: 'tuple' object does not support item assignment


# In[15]:


# manipulations de tuple avec les fonctions de base
print(c, d1)
print(d1[1], d1.index(3))
print(d1.count(3))
d1 = c * 2
print(c, d1)
print(d1[1], d1.index(3))
print(d1.count(3))


# Le code suivant :
# 
# ```python
# print("on a dit _non_ mutable !")
# c[1] = 11
# ```
# 
# déclenche l'erreur suivante:
# 
# ```python
# TypeError                                 Traceback (most recent call last)
# <ipython-input-10-b869b5ab11d8> in <module>
#       1 print("on a dit _non_ mutable !")
# ----> 2 c[1] = 11
# 
# TypeError: 'tuple' object does not support item assignment
# ```    

# ## Les listes `list`
# 
# **`list`** : _conteneur_ __mutable__ de valeurs _écrites entre `[  ]`_,  séparées par des `,`, et _indexées de 0 à `len(lst)-1`_
# 
# > [3, "bonjour", 7, 1.32]
# 
# * Les valeurs sont de type quelconque -- non nécessairement unique.
# 
# En pratique, les listes python sont des structures de données sophistiquées, très souples d'utilisation.  

# ### Créer une liste
# 
# Une liste peut être construite comme suit : 
# * à partir d'une liste vide notée : `[]`  
# * explicitement (ou aussi dit _en extension_) avec des valeurs séparées par des `,` et entre `[ ]`: `[a]`, `[a, b, c]`
# * **en compréhension** : `[x for x in iterable]`
# * avec le constructeur de type : `list()` ou `list(iterable)`

# In[16]:


# une liste explicite
liste = [1, 2, 3, 4, 5, 6, 7]
sous_liste = liste[:3]
un_a_trois = (1, 2, 3)
autre = list(un_a_trois)

print(liste, sous_liste, autre)
print(un_a_trois == autre, autre == sous_liste)

# les carres des elements
les_carres = [x ** 2 for x in liste]
print(les_carres)

# Afficher les nombres pairs
print([x for x in liste if x % 2 == 0])
# Plus simple que filtrer, egalement :)

#Affiche les carres pairs (combinaison des deux)
print([x**2 for x in liste if x ** 2 % 2 == 0])
# ou print([x for x in [a ** 2 for a in liste] if x % 2 == 0])
  


# ### Méthodes sur des listes
# 
# **Rappel :** Une _méthode_ est une fonction qui s'applique à _une_ variable (un objet) avec une notation pointée -- et non des parenthèses.   
# 
# **Compléments :** 
# 
# - Une méthode peut être une fonction de plusieurs paramètres. 
# - Le paramètre indispensable est celui mis devant le `.` de _la notation pointée obligatoire_. 
# - Les paramètres supplémentaires sont des arguments entre parenthèses en plus de la notation pointée.   
# - Remarquer que les méthodes suivantes modifient la liste à laquelle elles s'appliquent.
# 
# Syntaxe | Effet
# --------|------
# `une_lst.append(val)` | ajoute la valeur `val` à la fin de `une_lst`  
# `une_lst.extend(seq)` | ajoute la séquence `seq` à la fin de `une_lst`  
# `une_lst.insert(idx,val)` | _insère_ la valeur `val` en position `idx` dans `une_lst`  
# `une_lst.remove(val)` | supprime la valeur `val` de `une_lst`  
# `une_lst.pop()` | supprime la __dernière valeur__ de `une_lst` (s'utilise comme procédure)
# `une_lst.pop(idx)` | supprime la valeur d'indice `idx` de `une_lst`     
# `une_lst.sort()` | trie `une_lst` __en place__ (s'utilise comme procédure) 
# `une_lst.reverse()` | inverse `une_lst` __en place__ (s'utilise comme procédure) 
# 
# **Rmq.**
# 
# - Les accès, modifications (ajout/suppression de valeur) et parcours d'une liste sont des opérations simples (et optimisées) grâce à ces méthodes.
# - Ainsi comme déjà indiqué, les listes en python sont des structures de données qui cachent une importante sophistication. 
# 

# In[17]:


les_daltons = ["Jo", "Jack", "William", "Averell"]
print(les_daltons)
les_daltons[0] = "le méchant"
print(les_daltons)
les_daltons.append("Ma Dalton")
print(les_daltons)
print()


# In[18]:


# Voir les différences de comportement des 2 cas suivants
#chien_stupide = ("rantanplan",)   # c'est un tuple
chien_stupide = ("rantanplan")    # c'est une str

print(type(chien_stupide))
les_daltons.append(chien_stupide)
print(les_daltons)
print("on comprend :")
lst = list(chien_stupide)
print("lst:",lst)
print()


# In[19]:


print("on corrige :", les_daltons)
while les_daltons[-1] != "Averell":
    les_daltons.pop()
print(les_daltons)
les_daltons.pop(0)
print(les_daltons)


# In[20]:


les_daltons.reverse()
print(les_daltons)
les_daltons.sort() 
print(les_daltons)


# ### Affectation entre listes
# 
# <div class="alert alert-block alert-danger">
#     
# **ATTENTION** : l'affectation `liste_destination = liste_source` __ne crée pas une nouvelle__ `liste_destination`.
# 
# </div> 
# 
# * L'effet de cette affectation est la création d'un nouveau _nom de liste_ qui désigne _le même ensemble de valeurs en mémoire_ que celui désignés par l'autre nom `liste_source`.  
# 
# * Ainsi la modification de ces valeurs, qui est possible ici car les listes sont _mutables_, en utilisant un des deux noms (identifiant) _source_ ou _destination_, agira _indifféremment_ de l'identifiant utilisé : il n'y a qu'un seul ensemble de valeurs stockées en mémoire.
# 
# * Il est bien sûr possible de _dupliquer_ ces valeurs et les désigner effectivement avec deux identificateurs différents. Plusieurs solutions existent en python dont :
#     * la fonction `copy`du module `copy`
#     * l'affectation de tranches complètes.
# 
# Ce comportement, commun aux _types composés mutables_ et qui peut surprendre, sera étudié en détail dans le chapitre _"Fonctions : aspects avancés"_.  
# 
# Si besoin, l'utilisation de `copy.copy` (importé du module `copy`) sera la solution.  

# Cette particularité permet d'introduire les deux notions importantes suivantes qui sont classiques en programmation -- au delà de python.
# 
# * Notion d'**effet de bord** : la modification par un identifiant agit sur les valeurs "de" l'autre identifiant.  
# * Notion de **référence** : l'identifiant d'une variable (mutable) est une _référence_ vers un espace de mémoire. 

# [Illustration avec python tutor](https://goo.gl/GK6Gc7)

# In[21]:


import copy 

liste1 = [1, 1, 2]
liste2 = liste1
liste2[0] = 3
print(liste1 == liste2)
print(liste1, liste2)
print(id(liste1), id(liste2))
print()

print("duplication avec copy.copy : ")
new_liste = copy.copy(liste1)
new_liste[0] = 999
print(new_liste == liste1)
print(liste1, new_liste)

print("duplication par affectation de tranche complète : ")
liste3 = liste1[:]
liste1[0] = -5
print(liste3 == liste1, liste1==liste2)
print(id(liste3), id(liste1))


# ## Les dictionnaires  `dict`
# 
# Les dictionnaires python sont des _tableaux associatifs_.
# 
# ### Tableau associatif 
# 
# Structure de données classique (hors python)
# 
# * type de donnée _composé_ 
# * formé par les _couples_ `clé -> valeur`
# * la `clé` est unique dans le tableau associatif : 
#     * `clé` permet de désigner (d'atteindre) `valeur` dans le dictionnaire
#     * Dans un tableau associatif, la clé joue même rôle que l'indice dans un tableau. 
# * cette `clé` n'induit pas un ordre sur les valeurs du tableau associatif -- même si la clé est un entier !

# ### Dictionnaire `dict` en python
# 
# **Syntaxe.** 
# * des couples `clé : valeur` -- bien noter la séparation avec `:`  
# * écrits entre `{  }` et 
# * séparées par des `,` 
# > `{clé1: val1, clé2: val2, ...}`  
# 
# * _Mutable_, itérable mais non séquençable  
# 
# * **Accès** à la valeur : `un_dict[clé]` 
#     - similaire à l'accès à la valeur dans une liste, dans une chaîne de caractères, ...  
# 

# In[22]:


h_lever_WE = {'samedi': 8, 'dimanche': 9 }
print(h_lever_WE['samedi'] > h_lever_WE['dimanche'])


# **Rmq.**
# * Un dictionnaire n'est pas "ordonné par ses indices" : 
#     * Cette absence d'ordre justifie le caractère _non séquençable_ de cette structure.
#     * Différent des `str`, `tuple` et `list` qui sont des conteneurs _séquençables_.  
# * Les valeurs peuvent être de _type quelconque_  
#     * voir exemple suivant
# * L'**accès `clé -> valeur`** s'effectue en temps constant (très court en pratique : technique de _hachage_ ) 

# In[23]:


jour = 2
res = "toto"
message = ''

# ce dictionnaire utilise comme clés les valeurs des 3 variables précédentes
d = {jour:3, message:"bonjour", "nombre":7, res:1.32}

print(d)


# **Opérateurs, fonctions et méthodes.**
# * `len()` : retourne le nombre de valeurs de l'argument

# In[24]:


les_daltons = { "le_mechant": "Jo", '2': "Jack",  3: "William", "le_cretin": "Averell"}
print(len(les_daltons), les_daltons)
non = (les_daltons["le_mechant"] == les_daltons[3])
print("non:", non)


# **Rmq.**
# - Les clés d'un dictionnaire sont de type quelconque et non constant.  
# - En pratique, préférer des clés qui donnent un sens à la valeur correspondante et au dictionnaire.  

# **Méthodes introspectives**
# * `.keys()` : fonction-méthode qui retourne la liste des `clé`  de l'argument  
# * `.values()` : fonction-méthode qui retourne la liste des `val` de l'argument  
# * `.items()` : fonction-méthode qui retourne la liste des couples `clé:val` de l'argument  

# In[25]:


print(les_daltons)

les_cles = les_daltons.keys()
print(les_cles)
print(type(les_cles))
# type(les_cles[0]) produit TypeError: 'dict_keys' object is not subscriptable

les_noms = les_daltons.values()
print(les_noms, type(les_noms))

tout = les_daltons.items()
print(tout, type(tout))
print()


# **Parcourir** un dictionnaire
# 
# * `cle in un_dict`: appartenance d'une clé 
#     * utilisable dans `for ...` et produit un parcours _sur les clés_.
# * On peut itérer sur les`_valeurs_ du dictionnaire mais selon un ordre aléatoire.  
#     * `iter(un_dict)` retourne un tuple (séquence) qui sert d'itérateur     

# In[26]:


print("Attention : l'itération simple suivante parcourt les clés")
for c in les_daltons:
    print(c)


# In[27]:


for c in iter(les_daltons.keys()):
    print(c)
print("--")
for v in iter(les_daltons.values()):
    print(v)
print("--")
for v in iter(les_daltons.items()):
    print(v, type(v)) 


# **Modifier un dictionnaire**
# 
# * `.pop(cle)` : _efface_ `(cle:val)` et retourne `val`
# * `del un_dic[cle]` détruit l'entrée `cle : val` du dictionnaire `un_dic` 
# * `.update(autre_dict)` :  ajout ou maj avec un `autre_dict` (et écrasement si clé commune)    
# * `.clear()` : efface le dictionnaire

# In[28]:


print("mutable : ajout, retrait, modification")
les_daltons["la_maman"] = "Ma Dalton" #ajout
print(les_daltons)
del les_daltons["le_mechant"] #retrait
print(les_daltons)
print("le_mechant" in les_daltons, len(les_daltons))
print() 

animaux_fideles = {"le_cretin":"Rantanplan", "la_classe": "Jolly Jumper"}
animaux_fideles.pop("la_classe") #retrait
print(animaux_fideles)
les_daltons.update(animaux_fideles) # ajout-réduction de dictionnaires
print("changement de cretin : ", les_daltons)


# ## Les chaînes de caractères `str`
# 
# Leur importance pratique mériterait presque un chapitre dédié.
# Bien relire cette section plusieurs fois.
# 
# **`str` (string) ou chaîne de caractères :** type de donnée _non mutable_ composé d'une suite ordonnée de caractères  (_séquence_) 
# * syntaxe : s'écrit indifféremment avec `' '` et `" "` 

# ### Opérations 
# * `len()`, concaténation, répétition
# 
# **Accès** 
# * par indexation : `s[i]`, `s[0]`, `s[-1]`
# * par extraction de sous-chaînes ou tranches de `str` : `s[i:j]`, `s[:]`, `s[i:]`, `s[-2:]`, `s[1:10:2]`      

# In[29]:


hello = 'bonjour !'
print(hello[-1], len(hello))
s = hello[0:len(hello):2]
print(s, len(s))


# **Modification**
# 
# * Une `str` est _**non** mutable_
# * Toute modification de sa valeur 
#     * créé une nouvelle `str` 
#     * et détruit la précédente ;
#     * ce qui justifie que la nouvelle `str` puisse être désignée par le même identifiant.
#     * Se souvenir des illustrations pythontutor déjà vues (copie de `list`, concaténation de `str`).

# In[30]:


s = 'abc'
print(s, id(s))

t = s
print(t, id(t))

s = s + 'def'
print(s, id(s))


# ### Fonctions-méthodes 
# 
# Ces fonctions-méthodes spécifiques aux `str` sont utiles en pratique.  
# Savoir qu'elles existent est suffisant dans le cadre de ce cours.  
# Les identifiants sont en général bien explicites.  
# 
# On distingue surtout deux types de fonctions-méthodes. 
#      
# Celles qui retournent un `bool`: 
# 
# - `.isupper()`, `.istitle()`,  
# - `.isalnum()` (comprendre _is alpha and num_),  `.isalpha()`, `.isdigit()`, `.isspace()`,  
# - `.startswith()`, `.endswith()`  
# 
# 
# Celles qui modifient l'argument `arg` :
# 
# - la casse des caractères : `.upper()`, `.lower()`, `.capitalize()`, `.swapcase()`  
# - la justification : `.expantabs(nb)`, `.center(width)`, `.ljust()`, `.rjust()`, `.zfill(width)` (comprendre _zero fill_),  
# 
# ou aussi : 
# 
# - `.replace(old, new, count)` où `count` est le nombre de remplacements à effectuer, 
# - `.join(cont)` concatène les chaînes du conteneur `cont` en intercalant `arg`,  
# - `.split(seps)` partage la chaîne `arg` selons `seps` et retourne le tout sous forme de `list` de `str` ; 
#      - **très utile en pratique** pour manipuler les mots d'un texte par exemple.  
# 
# On finit en mentionnant cette dernière méthode de recherche :
# 
# - `.find(substr, deb, fin)` qui retourne l'indice de `substr` dans `arg[deb,fin]`.    
# 
# 
# 

# In[31]:


hello = 'bonjour !'

t = hello.split('o')
print('z' in t, 'b' in t)
print(t)

plus_fort = hello.upper()
print(hello, hello.isupper())
print(plus_fort, plus_fort.isupper(), plus_fort.isalpha(), '\n')

liste_de_deux = plus_fort.split()
print(".split:", liste_de_deux, type(liste_de_deux), type(liste_de_deux[0]), '\n')

liste_de_deux = 'zz!zz'.join(liste_de_deux)
print(".join:", liste_de_deux, type(liste_de_deux), '\n')

deux_fois_plus_fort = liste_de_deux.replace('!', '@'+str(liste_de_deux)+'@', 1)
print(".replace:", deux_fois_plus_fort)

deux_fois_plus_fort = liste_de_deux.replace('!', '@'+str(liste_de_deux)+'@', 2)
print(".replace:", deux_fois_plus_fort)


# **Rappel sur les fonctions-méthodes qui "modifient" une `str`**
# 
# - Le caractère _non mutable_ des `str` n'est pas mis en défaut par les méthodes de _modification_
# - Celles-ci créent de _nouvelles_ `str` 

# In[32]:


hello = 'bonjour !'
print(id(hello))

bjr = hello
print(id(bjr))

plus_fort = hello.upper()
print(id(plus_fort))

hello = plus_fort
print(id(hello))


# (sec:echappement)=
# ### Les caractères spéciaux ou caractères/séquences d'échappement
# 
# **Caractère d'échappement :** "backslash" `\`
# 
# **Caractères spéciaux ou séquences d'échappement :** l'association du "backslash" `\` et de certains symboles (ou  suite de symboles) a un sens particulier dans une chaîne de caractères.   
# Cela permet par exemple d'interpréter différemment les symboles `'` ou `"` ou ` `.  
# 
# **Quelques exemples ($\star$) à connaitre :**
# - `\'` ou `\"` ou `\\` ou `\/` : les symboles `'` ou `"` ou `\` ou `/`   
# - `\b` : _backspace_ 
# - `\t` `\v`: tabulation horizontale ou verticale
# - `\n` : _new line_ saut de ligne  
# - `\f` : _form feed_  saut de page  
# - `\r` : retour en début de ligne 
# 
# **Remarques.**
# - Cette notion se retrouve dans d'autres langages de programmation : C, ...   
# - On parle aussi de _séquence d'échappement_ mais retenons que l'association _`\` suivie d'un caractère_ est "comptée" comme un seul caractère : un caractère spécial.    
# 
# **Exemples.**

# In[33]:


s1 = 'bonjour'
s2 = '\tbonjour'

print(s1)
print(s2)
print('s1:', len(s1))
print('s2:', len(s2))
print('[', s1[0], ']')
print('[', s2[0], ']')


# **Comment utiliser le symbole `\` sans qu'il s'évalue comme l'annonce d'une séquence d'échappement ?**
# - avec lui même !
# - ainsi `\\` s'évalue comme le caractère `\` 
# - et `\\n` comme la chaîne de **2** caractères non évalués `\n` (piégeux !).

# In[34]:


print("\\ texte avec '\\' au début et à la fin \\")
print()

print("Bo\njour")
print("Bo\\njour")
print("Bo\\n\b\bnjour")


# Ainsi le `\` évite d'évaluer "normalement" le symbole qui le suit.  
# 
# **Rmq.**  
# Dans l'exemple suivant, expliquer pourquoi `va` (aux lignes affichées 2 et 4) n'est pas à la même colonne entre le premier et le second `print` ?  

# In[35]:


print('Bonjour \"mon ami\" ! \n \t \t  Ca va ?')
print('Bonjour \"mon ami\" ! \n \t \t  Ca va ? \r Comment')


# _Réponse :_
# 1. **Analyse du premier `print()`** : on s'intéresse à l'_interprétation_ par le `print()` de la chaîne de caractère argument.   
#     - `\n` et `\t` sont resp. les symboles du _saut à la ligne_ et de la _tabulation_    
#     - la tabulation est interprétée _dans mon environnement_ comme 7 (caractères) espaces  
#     - __lors de l'affichage__, la chaîne à afficher à partir du `\n` est donc _interprétée_ comme :
#         - 1 espace
#         - 7 espaces (1 tabulation)
#         - 1 espace
#         - 7 espaces (1 tabulation)
#         - 2 espaces
#         - les 7 caractères `Ca va ?`.  
#     - Soit donc au total 25 caractères affichés sur la seconde ligne (après le `\n`).      

# 2. **Analyse de second `print()`** : on va expliciter la valeur de la chaîne de caractères sans se soucier dans un premier temps de son interprétation à l'affichage, cad. lors de l'exécution du `print()`.  
#     - `\t` est une chaîne de caractères de longueur 1, cad. un caractère : 
#         - essayer `type('\t')` et `len('\t')` 
#     - à partir du `\n`, la chaîne de caractères ` \t \t  Ca va ?`  est de longueur 13
#         - essayer `len(' \t \t  Ca va ?')` 
#     - `\r` revient en début de ligne dans _cette chaîne de caractères_
#         - cad. juste après le `\n` 
#         - et donc "recule" (la position d'entrée) de 13 caractères sur cette ligne  
#     - ` Comment` est un chaîne de caractères de longueur 8 
#         - elle est placée aux 8 premiers caractères à partir de la position du curseur, cad. du début de la ligne
#         - et ainsi _écrase_ les 8 premiers caractères de la chaîne ` \t \t  Ca va ?`
#         - ces 8 premiers caractères sont : ` \t \t  Ca`  
#     - donc la chaîne de caractètes à afficher devient, à partir du `\n`: ` Comment va ?`
#         - on peut vérifier que `len(" Comment va ?")` retourne 13. 
#     - L'affichage obtenu est conforme à l'analyse.  

# In[36]:


print('[\t]')
tab = '[' + 'x'*7 + ']'  # sept x entre crochets
print(tab)
print()
print('Bonjour \"collègue\" ! \n \t \t  Ca va ?')
s = '.'*25
print(s)
print('Bonjour \"collègue\" ! \n \t \t  Ca va ? \r Comment')
s = '.'*13
print(s)


# In[37]:


print(len(' Comment va ?'))


# ## Les ensembles   `set` et `frozenset`
# 
# **`set`** (ensemble) : type composé de valeurs **uniques** écrites entre `{ }` et séparées par des `,`. 
# 
# > {3, "bonjour", 7, 1.32}
# 
# * `set`: ensemble _mutable_  
# * ($\star$) `frozenset` : ensemble _non mutable_ 
# 
# La fonction `set()` permet de créer un ensemble à partir d'un tuple ou d'une chaîne de caractères.  
# 
# **Opérations :**
# - opérations ensemblistes (des maths) : 
#     * `in` et `not in` :  appartenance ou non 
#     * `|` : union
#     * `&` : intersection
#     * `-`: différence
#     * `^`: différence symétrique  (complémentaire de l'intersection)
#     * `<=` ou `<` : inclusion ensembliste, resp. _est un sous-ensemble de_ vs. _est inclus strictement dans_; `A < B` == `A <= B` and `A != B` (et de même : `>=` `>`)

# In[38]:


bof = {'b', 'o', 'f'}
voyelles = set('aeiouy')
aie = set('aie')

print(voyelles, len(voyelles))

print('a' in voyelles)
print('a' in bof)

print("aie :", aie)
print("voyelles :", voyelles)

print("union :", voyelles | aie)
print("autre union :", voyelles | bof)
print("intersection :", voyelles & aie)
print("difference : ", aie - voyelles, bof - voyelles)
print("difference symétrique: ", aie ^ voyelles)
print("inclusions :", aie < voyelles, aie <= voyelles, aie >= voyelles, bof < voyelles)
 
#print(aie[1])  # déclenche une erreur : l'accès indexé n'est pas possible dans un ensemble


# ## Spécifier des fonctions avec des types composés
# 
# 
# Les fonctions peuvent manipuler des arguments de type composé.
# 
# On a déjà vu beaucoup d'exemples avec les tableaux.
# Ces derniers ayant été représentés en python par le type (composé) _liste_, on sait expliciter le _type_ de tels paramètres à l'aide de `List` (avec une majuscule) du module `typing`.
# 
# On va étendre cette approche aux type composés vus dans ce chapitre.

# <div class="alert alert-block alert-info">
# 
# Depuis python **3.9**, il est possible de paramètrer les types prédéfinis avec des `[ ]` de façon similaire à celle décrite dans la section 2 de cette partie.
# 
# Il n'est donc plus nécessaire de passer par les types "avec majuscule" de `typing`.
# 
# </div>

# ### Paramètres de type composé prédéfini
# 
# Les types composés prédéfinis de python sont renvoyés par la fonction `type()` (appliquée à une variable). 
# 
# - `list`
# - `dict`
# - `tuple`
# - `set`
# - `str`

# In[39]:


unTuple = (1,2,3)
uneListe = [1, 'a', 1.3]
unDictionnaire = { "le_mechant":"Jo", '2':"Jack",  3:"William", "le_cretin": "Averell"}
unEnsemble = {'b', 'o', 'f'}
uneChaineDeCaracteres = "bof"

for v in (unTuple, uneListe, unDictionnaire, unEnsemble, uneChaineDeCaracteres):
    print(type(v))


# **Solution minimale.** On peut donc **utiliser ces types prédéfinis** pour spécifier le type des paramètres d'une fonction.
# 
# 
# <div class="alert alert-block alert-info">
#     
# Par la suite, on utilisera au moins cette solution minimale pour toutes les spécifications de fonction avec des paramètres de type composé.
# 
# </div>
# 

# In[40]:


def nb_caracteres(s : str) -> int:
    return len(s)

def nb_entrees(d : dict) -> int:
    return len(d)

def card(s : set) -> int:
    return len(s)

# exemple de 2 fonctions d'identifiant identiques 
# mais de signature différentes grâce au typage de
# ses paramètres formels
# On appelle aussi cette homonymie de la "surcharge de fonctions"
def nb_val(l : list) -> int:
    return len(s)

def nb_val(t : tuple) -> int:
    return len(s)
  
print(nb_caracteres(uneChaineDeCaracteres))
print(nb_entrees(unDictionnaire))
print(card(unEnsemble))
for v in (uneListe, unTuple):
    print(nb_val(v))    


# **Rmq.** Dans l'exemple précédent, on a 2 fonctions d'identifiant identique `nb_val()` mais de signatures différentes grâce au typage de leurs paramètres formels.
# 
# On a par exemple déjà signalé cette caractéristique avec les différents sens du symbole `+` selon qu'il s'applique à des entiers, des flottants, des chaînes de caractères, ...
# 
# 
# On appelle aussi cette homonymie de la _surcharge de fonctions_.

# ### ($\star$) Mieux expliciter le type composé 
# 
# Comme on l'a fait pour _mieux_ expliciter les tableaux, on peut utiliser le module `typing` pour aussi expliciter "l'intérieur" d'un type composé, cad. le type de ses composants.
# 
# Par exemple, le type d'un tableau 2D de valeurs entières (type composé qui regroupe des valeurs de même type)  a été spécifié par :
# > `List[List[int]]`
# 
# 
# On a ainsi explicité :
# - la dimension du tableau : ici 2 et la représentation comme une liste de listes
# - le type de ses valeurs  : ici des entiers, _ie._ des `int` 
# 
# Ce qui n'était pas possible avec le seul type prédéfini `list` (avec un `l`).

# In[41]:


from typing import List

def maxTab2D( t : List[List[int]], d1 : int, d2 : int) -> int:
    m = t[0][0]
    for i in range(d1):
        for j in range(d2):
            if t[i][j] > m:
                m = t[i][j] 
    return m

print(maxTab2D([[1,0],[1,2]], 2, 2))


# **Une solution satisfaisante.**
# Le module `typing` introduit les types prédéfinis "avec majuscule" suivants  :
# 
# >  `List` , `Dict`, `Tuple`, `Set`
# 
# et
# 
# > `Union`
# 
# Ces types permettent d'expliciter "l'intérieur" des arguments de type composé. La syntaxe s'appuie sur les crochets `[ ]` déjà rencontrés pour les tableaux-listes.
# 
# **Exemples.**
# 
# - `Tuple[int, float, str]` est un _tuple_ triplet composé d'un entier, d'un flottant et d'une chaîne de caractères.
# 
# - `Dict[str, int]` est un dictionnaire de couples _clés:valeur_ de types  `str:int`  
# 
# - `Union`
#     - `Union[int, float]` est un paramètre de type `int` ou `float`.
#     - Il convient par exemple pour écrire une seule version de la fonction `nb_val()`. 

# Ces types paramètrables pourront être utiles pour  spécifier au mieux des paramètres de fonctions de type composé.
# 
# On y accède après l'importation suivante.
# 
# **Rmq.** Depuis python 3.9, une approche similaire est possible avec les types prédéfinis python (sans majuscule). 
# 

# In[42]:


from typing import List, Dict, Tuple, Set, Union


# In[43]:


def nb_entrees(d : Dict[str, str]) -> int:
    return len(d)

def card(s : Set[str]) -> int:
    return len(s)

# exemple d'Union pour la surcharge
def nb_val(cont : Union[List[int], Tuple[int]]) -> int:
    return len(cont)

unTuple = (1,2,3)
uneListe = [1, 'a', 1.3]
unDictionnaire = { "le_mechant":"Jo", '2':"Jack",  3:"William", "le_cretin": "Averell"}
unEnsemble = {'b', 'o', 'f'}
uneChaineDeCaracteres = "bof"

print(nb_entrees(unDictionnaire))
print(card(unEnsemble))
for v in (uneListe, unTuple):
    print(nb_val(v))    


# In[44]:


# autre exmple avec Union
def maxListe( l : List[Union[int, float]]) -> int:
    m = l[0]
    for i in range(len(l)):
        if l[i]> m:
            m = l[i] 
    return m

resI = maxListe([1, 0, 1, 2, 2, 2])
resF = maxListe([1.0, 1.2, 2.2])

print(resI, resF)


# Consulter la [documentation](https://docs.python.org/fr/3/library/typing.html?highlight=typing#typing.Union)
# pour d'autres constructions plus avancées et très utiles.

# ## Synthèse 
# 
# * Conteneurs non mutables : `str`, `tuple` (et `frozenset`)
# * Conteneurs  mutables : `list`, `dict`, `set`
# * Création, accès aux valeurs, parcours et modification
# * Des fonctions (pour les non mutables) et des fonction-méthodes
# * **Attention** : la modification de non mutable cache une recopie en mémoire 
# * **Attention** : bien que très simples à utiliser, certaines fonctions-méthodes sont d'un coût algorithmique élevé (complexité non constante)
# * Quels mutables choisir ?
#     - les `list` pour des tableaux 1D de valeurs de type qcq et où le traitement demande de la souplesse 
#     - les `dict` pour des clés `str` 
#     - ($\star$) mais aussi les `ndarray` pour du calcul numérique type algèbre linéaire ou les tableaux multi-dimensionnels de valeurs numériques -- voir [cette annexe](ann:ndarray).
# * La spécification d'arguments de type composé avec le module `typing` ou plus directement en python>=3.9

# ### Avoir les idées claires
# 
# 
# Distinguer les  caractéristiques des structures de données :
# tuple, liste, dictionnaire, ensemble, et chaîne de caractères
# -- aussi appelés type composé ou conteneur en python :
# 
# - pour une représentation,un stockage des données et des traitements adaptés au problème  
# - pour effectuer l'accès aux valeurs, le parcours (séquences, itérateur), et la modification ou la copie (mutabilité) de ces SD
# - ($\star$) Connaître les complexités de ces traitements 
# 
# 
# 
# ### Savoir faire
# 
# - Connaitre la syntaxe python de définition et manipulation de ces SD
# - Créer des listes et dictionnaires en compréhension
# - Connaître les méthodes (prédéfinies) utiles au traitement, en particulier des chaînes de caractères 
# - Définir des spécifications de fonctions avec un ou des paramètres de type composé
# 
