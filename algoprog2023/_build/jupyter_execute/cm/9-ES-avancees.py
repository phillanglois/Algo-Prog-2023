#!/usr/bin/env python
# coding: utf-8

# (ch:ES-avancees)=
# # Les entrées-sorties (E/S) : aspects avancés
# 
# **Partie Programmation**    
# version 2021, v1 PhL.

# Chapitre où on étudie comment peaufiner le format ses entrées-sorties à l'écran ou dans des fichiers de texte.
# 
# Ce chapitre complète le chapitre "Entrées-sorties avec des fichiers".  
# 

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Les-entrées-sorties-(E/S)-:-aspects-avancés" data-toc-modified-id="Les-entrées-sorties-(E/S)-:-aspects-avancés-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Les entrées-sorties (E/S) : aspects avancés</a></span><ul class="toc-item"><li><span><a href="#Les-formats-d'écriture,-de-lecture-et-d'affichage" data-toc-modified-id="Les-formats-d'écriture,-de-lecture-et-d'affichage-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Les formats d'écriture, de lecture et d'affichage</a></span><ul class="toc-item"><li><span><a href="#Spécifier-le-format-de-nombres-et-des-chaînes-de-caractères" data-toc-modified-id="Spécifier-le-format-de-nombres-et-des-chaînes-de-caractères-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Spécifier le format de nombres et des chaînes de caractères</a></span><ul class="toc-item"><li><span><a href="#Formatage-de-nombres-int" data-toc-modified-id="Formatage-de-nombres-int-1.1.1.1"><span class="toc-item-num">1.1.1.1&nbsp;&nbsp;</span>Formatage de nombres <code>int</code></a></span></li><li><span><a href="#Formatage-de-nombres-float" data-toc-modified-id="Formatage-de-nombres-float-1.1.1.2"><span class="toc-item-num">1.1.1.2&nbsp;&nbsp;</span>Formatage de nombres <code>float</code></a></span></li><li><span><a href="#Formatages-de-chaînes-de-caractères" data-toc-modified-id="Formatages-de-chaînes-de-caractères-1.1.1.3"><span class="toc-item-num">1.1.1.3&nbsp;&nbsp;</span>Formatages de chaînes de caractères</a></span></li><li><span><a href="#Les-caractères-spéciaux-\..." data-toc-modified-id="Les-caractères-spéciaux-\...-1.1.1.4"><span class="toc-item-num">1.1.1.4&nbsp;&nbsp;</span>Les caractères spéciaux <code>\...</code></a></span></li></ul></li><li><span><a href="#Les--expressions-ou-chaînes--formatées" data-toc-modified-id="Les--expressions-ou-chaînes--formatées-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Les  <em>expressions</em> ou <em>chaînes  formatées</em></a></span></li><li><span><a href="#La-méthode-.format()." data-toc-modified-id="La-méthode-.format().-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>La méthode <code>.format()</code>.</a></span></li><li><span><a href="#($\star$)-Compléments" data-toc-modified-id="($\star$)-Compléments-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>($\star$) Compléments</a></span><ul class="toc-item"><li><span><a href="#str()-et-repr()" data-toc-modified-id="str()-et-repr()-1.1.4.1"><span class="toc-item-num">1.1.4.1&nbsp;&nbsp;</span><code>str()</code> et <code>repr()</code></a></span></li><li><span><a href="#Souplesses-de-l'arg-de-.format()." data-toc-modified-id="Souplesses-de-l'arg-de-.format().-1.1.4.2"><span class="toc-item-num">1.1.4.2&nbsp;&nbsp;</span>Souplesses de l'<code>arg</code> de <code>.format()</code>.</a></span></li><li><span><a href="#Méthodes-spécifiques-(sans-.format())" data-toc-modified-id="Méthodes-spécifiques-(sans-.format())-1.1.4.3"><span class="toc-item-num">1.1.4.3&nbsp;&nbsp;</span>Méthodes spécifiques (sans <code>.format()</code>)</a></span></li></ul></li></ul></li><li><span><a href="#Synthèse" data-toc-modified-id="Synthèse-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Synthèse</a></span><ul class="toc-item"><li><span><a href="#Avoir-les-idées-claires" data-toc-modified-id="Avoir-les-idées-claires-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Avoir les idées claires</a></span></li><li><span><a href="#Savoir-faire" data-toc-modified-id="Savoir-faire-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Savoir-faire</a></span></li></ul></li></ul></li></ul></div>

# ## Les formats d'écriture, de lecture et d'affichage
# 
# Il s'agit de _définir la façon dont s'écrivent, se lisent ou s'affichent à l'écran_ les informations textuelles, _i.e._ les chaînes de caractères.  
# Exemple : combien de chiffres après la virgule d'un `float`, utiliser une notation scientifique ($\pm 1.xxxx \cdot 10^E$), insérer ou non des caractères avant la `str` à afficher, ...  
# 
# On commence par la syntaxe qui permet d'exprimer le formatage voulu (syntaxe un peu lourde au début), puis on montre deux moyens d'appliquer l'opération de formatage : les _chaînes formatées_ (ou _f-string_ en python) puis la méthode plus générale `.format` (méthode définie pour les `str`).   
# 
# <div class="alert alert-danger">
# 
# Ces __formats__ d'affichage s'appliquent aux **chaînes de caractères** utiles aux entrées-sorties **textuelles** (avec `print()` pour l'écran, mais aussi `write()` et `read()` pour les fichiers de texte).
#     
# </div>

# ### Spécifier le format de nombres et des chaînes de caractères 
# 
# La syntaxe générale d'un __format__ (d'écriture ou d'affichage) est :
# 
# > `:[drapeau][largeur][.precision][type]`
# 
# Après le symbole `:`, chacun des 4 champs est optionnel.
# - `[drapeau]` contrôle la justification de la valeur par :
#     - un caractère de remplissage  (optionnel) : `.`,`*`,`-`, ... 
#     - et sa position : centré :`^`, aligné à gauche : `<`, à droite : `>`
# - `[largeur]` : la largeur de l'écriture (en nombre de caractères)
# - `[.precision]` : le nombre de chiffres après la virgule `.` pour les nombres flottants
# - `[type]`: le paramètre le plus important qui dépend du type de la valeur et décrit un mode général de représentation.
# 
# Une valeur de format est aussi appelée **code** de format par la littérature python. 

# **Rmq. importante** 
# Les exemples qui suivent pour illustrer l'effet de ces codes sont donnés :
# - sur l'affichage à l'écran par `print()`, 
#     - un effet identique est obtenu par des `read()` ou des `write()` dans les fichiers;
# - d'une _chaîne formatée_ ou aussi  _f-string_) : c'est une forme de chaine de caractères 
#     - reconnaissable par le `f`ou `F` qui précède le `"`ou le `'` d'ouverture de chaîne,
#     - et qui sera détaillée dans la section suivante.
#     
# 
# On a indiqué que `[type]`est le paramètre de format le plus important en pratique. C'est donc lui qui guide la présentation.

# #### Formatage de nombres `int` 
# 
# Le champs `[type]`peut prendre les valeurs `d` (par défaut), `x`, `X`, `o`, et `b` dont le sens est illustré par les 5 codes suivants.
# 
# type | code (`str`) | format  
# -----|--------|------
# int | `{0:d}` | **entier en base 10 (décimal)** (par défaut)
# int | `{0:x}` | entier en base 16 (hexa-décimal) en minuscules 
# int | `{0:X}` | entier en base 16 (hexa-décimal) en majuscules 
# int | `{0:o}` | entier en base 8 (octal)
# int | `{0:b}` | entier en base 2 (binaire)
# 
# **Rmq.** Ne pas se soucier du '0' avant le ':'  qui débute le format.  

# In[1]:


print("22")
print(f"{22:d}")
print(f"{22:x}")
print(f"{22:X}")
print(f"{22:o}") 
print(f"{22:b}")


# On verra avec la présentation des chaînes formatée qu'on peut formater des expressions évaluées à l'exécution -- mais toujours comme des chaînes de caractères.
# 
# Le traitement suivant est similaire au précédent en introduisant une variable `var` à (la valeur de) laquelle s'applique le formatage.

# In[2]:


var = 22
print(var)
print(f"{var:d}")
print(f"{var:x}")
print(f"{var:X}")
print(f"{var:o}")
print(f"{var:b}")


# On illustre brièvement l'effet des champs `[position]` et `[largeur]` sur des décimaux.

# In[3]:


var = 22
print(var, ": format par défaut du print")
print(f"{var:10d}", ": sur 10 caractères, alignement à droite par défaut pour 'int'")
print(f"{var:-^10d}", ": centré sur 10 caractères")
print(f"{var:.<10d}", ": aligné à gauche, 10 caractères complétés par des .")


# Les écritures classiques des entiers sont aussi obtenues à l'aide des codes suivants.
# 
# type | code (`str`) | format  
# -----|--------|------
# int | `{0:+d}` | entier en base 10 avec signe `+` explicite 
# int | `{0:0=nb}` | entier en base 10 écrit avec `nb` chiffres, complétés de `0` si besoin
# int | `{0:#x}` | entier en base 16 avec `#`
# int | `{0:#o}` | entier en base 8 avec `o`
# int | `{0:#b}` | entier en base 2 avec `b`

# In[4]:


var = 22
print(f"{var:+d}")
print(f"{var:0=4}")
print(f"{var:#X}")
print(f"{var:#o}")
print(f"{var:#b}")


# #### Formatage de nombres `float`   
# 
# Le champs `[type]` peut prendre les valeurs `f`, `e`, `g` et `%`.
# 
# Avec les champs `[drapeau]`, `[largeur]` et `[précision]`, on obtient des formats adaptés aux `float`.
# 
# type | code (`str`) | format  
# -----|--------|------
# float | `{0:2.4f}`|  2 chiffres avant la virgule et 4 après
# float | `{0:.5e}`| notation scientifique avec 5 chiffres après la virgule
# float | `{0:g}`|  un format générique "qui va bien"
# float | `{0:.2%}`| pourcentage avec 2 décimales

# In[5]:


from math import pi as pi
print("pi=", pi)
print(f"{pi:2.3f}")
print(f"{pi:+.5e}")
print(f"{pi:g}")
print(f"{pi:*^+15.5e}")


# **Rmq.** Ces formatages d'`int` et de `float` apparaissent aussi dans d'autres langages de programmation, _e.g._ C.  

# #### Formatages de chaînes de caractères
# 
# Dans ce cas, on défini les champs `drapeau` et `largeur` comme déjà indiqué.
# 
# type | code (`str`) | format  
# -----|--------|------
#   str | `{:nb}`| chaîne justifiée à gauche sur `nb` caractères (complétée d'espaces _à droite_ si besoin)
#   str | `{:>nb}`| chaîne justifiée à droite sur `nb` caractères (complétée d'espaces _à gauche_ si besoin)
#   str | `{:^nb}`| chaîne _centrée_ sur `nb` caractères (complétée d'espaces si besoin)
#   str | `{:-^nb}`| chaîne _centrée_ sur `nb` caractères, complétée de `-` si besoin
# str | `{:.<nb}`| chaîne justifiée à gauche  sur `nb` caractères, complétée de `.` _à droite_ si besoin

# In[6]:


s = "un texte formaté"
print(len(s))
print(f"{s:35}")
print(f"{s:>35}")
print(f"{s:^35}")
print(f"{s:+^35}")


# #### Les caractères spéciaux `\... `
# 
# On rappelle que les _caractères spéciaux_ ou _séquences d'échappement_ sont l'association du "backslash" `\` et de certains symboles (ou  suite de symboles).
# Cette suite de caractères (qui commence par `\`) est interprétée de façon particulière.
# 
# Caractères spéciaux "de contrôle":  
# - `\b` : _backspace_ 
# - `\t` `\v`: tabulation horizontale ou verticale
# - `\n` : _new line_ saut de ligne  
# - `\f` : _form feed_  saut de page  
# - `\r` : retour en début de ligne 
# 
# On a vu que  le `\` évite d'évaluer "normalement" le symbole qui le suit.
# 
# Donc :
# 
# - `\\` s'évalue comme le caractère `\`, 
# - `\'` ou `\"` ou `\/` comme les symboles `'` ou `"` ou `/`   
# - et `\\n` comme la chaîne de **2** caractères **non évalués** `\n`.
# 
# Retenons que `\` permet de ne pas _interpréter avec le sens réservé par les choix du langage de programmation_ le caractère qui le suit. 
# Il ramène au caractère ou à la chaîne de caractère écrites -- et non son interprétation.
# Cette notion se retrouve dans d'autres langages de programmation : C, ...
# 
# 
# Des fonctions plus générales qui résolvent ce type de problème sont présentées comme compléments en fin de chapitre.

# print("a\\nb")

# ### Les  _expressions_ ou _chaînes  formatées_ 
# 
# **Principe**
# 
# 1. On définit un _format d'affichage_ pour une chaîne de caractères qui dépend de la valeur de certains _champs_ à formater 
# 2. On applique ce format à un nombre arbitraire de valeurs
# 3. On obtient un nombre arbitraire de valeurs affichées de la même manière.
# 
# Syntaxe :
# > `f"une chaine de caractères qui contient au moins un {champs à formater}"` 

# In[7]:


quantieme = 12
mois = "mars"
annee = 2021
temp = 18.2
s = f"La température du {quantieme} {mois} {annee} est {temp}oC."
print(s)


# L'intérêt de ces expressions (ou chaînes) formatées est mis en valeur en introduisant les formats d'affichage vus précédemment pour chaque champs et le type de valeur attendu.
# 
# Ces formats d'affichage commencent ici après le `:` de chaque champs de l'expression formatée.

# In[8]:


quantieme = 4
mois = 'mars'
annee = 2021
temp = 18.2
s1 = f"La température du {quantieme:2d} {mois:^10} {annee} est {temp:2.1f}oC."
# un entier sur 2 chiffres décimaux, 
# une chaine centrée sur 10 caractères,
# un nombre flottant avec au plus 2 chiffres significatifs et une décimale

quantieme = 12
mois = 'janvier'
annee = 2021
temp = 5.58
s2 = f"La température du {quantieme:2d} {mois:^10} {annee} est {temp:2.1f}oC." 

print(s1)
print(s2)


# ### La méthode `.format()`.
# 
# L'exemple précédent donne envie de pouvoir définir _une fois pour toute_ l'expression formatée et de pouvoir _l'appliquer_  à un nombre arbitraire de valeurs pour obtenir l'affichage formatée de ces valeurs.
# 
# C'est l'objet de la méthode `.format()` qui s'applique à des `str`.

# La syntaxe de `.format()` est un peu déroutante au début.
# > `st_format.format(arg)` retourne une chaîne de caractères `str` formatée
# 
# - `st_format` est une chaine de caractères qui définit **le format d'affichage** voulu : similaire à l'_expression formatée_, elle contient les champs délimitées par des `{ }` qui  intégrent éventuellement des spécifications de format.  
# - `arg` est un _conteneur_ `tuple` ou `dict` ou `str` de _valeurs à formater_.
# 
# Ainsi `st_format.format(arg)` applique à `arg`, les traitements définies entre **`{ }`** de la chaîne de _définition du format_ `st_format`. 

# **Rmq.**
# - Cette construction permet de définir "une fois pour toute" la chaîne `st_format` puis de l'appliquer à un nombre arbitraire d'`arg` -- ce qui n'est pas possible avec les expressions formatées _f-strings_.
# - On rappelle que le type `str` est **non-mutable** -- ce qui nous fait souvent préférer la dénomination _expression formatée_ plutôt que chaîne formatée, traduction rapide du jargon python _f-string_.

# **Exemple.** Une météo hasardeuse.

# In[9]:


import random

le_format = "La température du {:2d} {:^10} {} est {:+5.1f} oC."

a = 2021
for m in ('janvier','février','mars'):
    for q in range(1,28,4):
        t = random.uniform(-2.0,15.9)
        s = le_format.format(q, m, a, t)
        print(s)
        


# Le formatage de données textuelles s'applique aussi aux E-S sur fichiers.

# Il est classique de mentionner que la méthode `.format()` permet aussi d'effectuer des substitutions (des remplacements) de  certaines parties de chaînes de caractères. 

# In[10]:


# formatage avec remplacement par st
le_format =  "Le {} mot est {} {}"
st_formatee = le_format.format("premier", "très important", "....")

# affichage
print(st_formatee)
print(le_format)

# ecriture fichier
st1 = "capital, "
st2 = "assurément"
with open("./tmp/format1.txt", "w", encoding="utf8") as f:
    f.write(st_formatee)
    f.write("\n")    
    f.write(le_format.format("dernier", st1 + st2, "!"))
    f.close()


# In[11]:


get_ipython().system('cat tmp/format1.txt')


# **Rmq.** Il est commode de voir la chaîne `st_format` comme un masque de mise en forme qui va s'appliquer aux valeurs de l'argument `arg`. 
# Cette utilisation par remplacement peut faire penser (à tort) à un rôle inversé de l'argument à formater `arg` et de la chaîne `st_format` qui définit le formatage. 
# Ce risque de confusion sera levée avec l'étude de la programmation objet (en python) -- hors du programme de ce semestre.  

# ### ($\star$) Compléments
# 
# <div class="alert alert-warning">
# 
# Objectif 20 et en seconde lecture 
#     
# </div>

# ####  `str()` et `repr()`
# 
# Vous avez utilisé --de façon explicite ou "à votre insu"-- la fonction `str()` pour convertir une valeur de type quelconque en sa représentation comme une chaîne de caractères.
# - Citez un exemple d'utilisation implicite de `str()`
# 
# La fonction `str()` donne accès à la chaîne de caractères argument _interprétée_.
# 
# La fonction `repr()` donne accès à la chaîne de caractères argument sans l'interpréter. 

# In[12]:


val = 22
s = str(val)
r = repr(val)
print(val, s, r, sep="*")
print(type(val), type(s), type(r))
print()

val = "\n"
s = str(val)
r = repr(val)
print(val, s, r, sep="*")
print(type(val), type(s), type(r))
print()

val = "\\n"
s = str(val)
r = repr(val)
print(val, s, r, sep="*")
print(type(val), type(s), type(r))


# Lorsqu'aucun formatage particulier n'est souhaité, ces fonctions peuvent être utilisées avec les raccourcis suivants qui complètent les champs `{}` des _f-strings_ ou du formatage de `.format()`.
# - `!s` pour u `str()`
# - `!r` pour `repr()`
# - `!a` pour `ascii()`

# In[13]:


mr_ou_mme = "Madame, \n Monsieur."
hello_s = f"Bonjour {mr_ou_mme!s}"
hello_r = f"Bonjour {mr_ou_mme!r}"
hello_a = f"Bonjour {mr_ou_mme!a}"
print(hello_s, hello_r, hello_a, sep="**")


# In[14]:


st = "Bonjour, \n bonjour !"
print(st)
print("{!s}".format(st))
print("{!r}".format(st))
print("{!a}".format(st))


# #### Souplesses de l'`arg` de `.format()`.
# 
# Avec `.format()`, les arguments à formater peuvent être indiqués par position implicite (par défaut comme jusqu'à présent) ou _explicite_ mais aussi par _nommage_ ou par _liste/dictionnaire_ -- dans la définition et dans l'appel pour les deux derniers.
# 
# La position des valeurs du conteneur `arg` argument de `.format(arg)` est précisée dans les `{ }` de `st_format` :    
# - de façon **explicite** avec **`{pos}`**  
# - de façon **nommée** avec **`{nom}`**   
# - en correspondance avec l'item `i` d'un _argument `lst`_ avec **`{0[i]}`**  
# - en correspondance avec la valeur de `clé`  d'un un _argument `dict`_  avec **`{0[clé]}`**  
# 
# Ces positions peuvent être complétées d'une _spécification de formatage_.  

# In[15]:


st_pos =  "{1} {0} est {2}"
st_nom =  "{article} {sujet} est {complement}"
st_lst = "{0[0]} {0[1]} est {0[2]}"
st_dict = "{0[article]} {0[sujet]} est {0[complement]}"


print(st_pos.format("ciel", "le", "bleu"))
print(st_nom.format(article="la", sujet="mer", complement="calme"))
print(st_lst.format( ["la", "montagne", "violette"] ))
d = dict(complement="chaud", article="le", sujet="soleil") # syntaxe dictionnaire param. nommés
print(st_dict.format(d))


# #### Méthodes spécifiques (sans `.format()`)
# 
# On verra que certains traitements peuvent être obtenus avec des méthodes spécifiques aux `str`.
# 
# méthode | effet
# --------|------
# `str.center(nb)` | centre `str`sur `nb`caractères
# `str.rjust(nb)` | justifie `str` _à droite_ sur `nb` caractères 
# `str.ljust(nb)` | justifie `str` _à gauche_ sur `nb` caractères 
# `str.zfill(nb)` | ajoute des zéros à gauche de `str` pour obtenir `nb` caractères 
# 

# ## Synthèse 
# 
# ### Avoir les idées claires
# 
# - Connaitre les principes du formatage des données pour pouvoir retrouver rapidement dans la documentation (de cours ou de référence) les commandes pour effectuer ce traitement.
# 
# ### Savoir-faire
# 
# - Utiliser les formatages de base des types `int` et `float` de python
# - En s'appuyant sur les documents de cours ou de référence, définir et appliquer des formatages évolués et adaptés aux données manipulées avec python
jupyter nbconvert --to html_embed --template toc2 6-ES-avanceesjupyter nbconvert 5p-ES.ipynb --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --SlidesExporter.reveal_theme=solarized