#!/usr/bin/env python
# coding: utf-8

# (ch:ES-fichiers)=
# # Entrées-sorties simples avec des fichiers

# Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.

# Chapitre où on étudie comment effectuer des entrées-sorties (E/S) simples à l'aide de fichiers.
# 
# Jusqu'à présent les entrées-sorties ont été générées à grands coups de `print()` et d'` input()` pour interagir avec l'écran ou le clavier.
# Les entrées-sorties ne sont pas limitées au couple écran-clavier.
# Bien au contraire, ces derniers ne sont que des cas particuliers d'une notion plus générale : celle de _fichier_. 

# ## Notions générales et vocabulaire important
# 
# ### Fichier, fichier texte et fichier binaire
# 
# A la différence de la mémoire de l'ordinateur, le fichier (_file_ en anglais) permet de stocker de l'information et la retrouver si l'alimentation électrique de l'ordinateur est interrompue.  
# Par information, on entend des données de tout type (nombres, sons, images,...), des programmes, des bibliothèques de composants du logiciel, ...  
# "Physiquement", les [supports matériels de ces fichiers](https://fr.wikipedia.org/wiki/Mémoire_de_masse) sont variés et évoluent selon les technologies disponibles : cartes perforées, bandes magnétiques, disques optiques, mémoires flash ... 

# En pratique, il faut distinguer les _fichiers_ dits **texte** (ou fichiers textuels) des _fichiers_ (dits) **binaires**. 
# 
# - Les fichiers texte  contiennent de l'information exploitable par l'humain 
# - Les fichiers binaire contiennent de l'information uniquement exploitable par l'ordinateur
# 
# Bien sûr, ces deux familles de fichiers sont au final une suite de bits stockés sur un support physique.   
# Dans ce chapitre, l'accent sera surtout mis sur les fichiers de texte utiles pour nos développements de taille modeste.

# ### Programmer avec des fichier : principes
# 
# La plupart des langages de programmation distinguent les fichiers (dits) logiques des fichiers (dits) physiques.
# 
# - Les __fichiers logiques__ sont des variables manipulées par le programme  
#     - Ce sont des variables d'un nouveau type : le type _fichier_
# - Les __fichiers physiques__ sont les supports effectifs du stockage de l'information (en mémoire, sur disque, sur clé, ...). 
#     - Ils sont identifiés par le "chemin" système de leur localisation (le _path_)(`/home/mon_user_id/work/le_fichier.txt`)   
#     - Ils ne sont manipulés qu'une seule fois : lors de l'association fichier logique $\to$ fichier physique

# __Utiliser un fichier__ (en lecture, écriture ou lecture-écriture) consiste en les 4 étapes suivantes.
# 1. __associer le fichier logique__ à __un fichier physique__
# 2. __ouvrir__ le fichier logique  
# 3. effectuer les __traitements__ désirés sur le fichier logique  
# 4. __fermer__ le fichier logique  
# 
# L'étape d'ouverture du fichier précise le __type des traitements__ qui seront effectués en distinguant :
# - la lecture : _read_
# - l'écriture : _write_
# - la lecture + l'écriture : _readwrite_  

# __Organisation :__ 
# 
# - Un fichier est décomposé en **lignes** et se termine par un symbole de fin de fichier : _EOF (end of file)_     
# - Une ligne est une **suite de caractères** et se termine par un symbole de fin de ligne : _EOL (end of line)_  
# - Les traitements correspondent à un _accès séquentiel_ du fichier, en commençant à ligne 1.   

# **Remarque.**
# 
# Le symbole de fin de ligne varie selon les systèmes d'exploitation [lien wikipedia](https://fr.wikipedia.org/wiki/Fin_de_ligne) ou, en mieux, la [version en anglais](https://en.wikipedia.org/wiki/Newline). 
# Il en est de même pour le [symbole de fin de fichier](https://en.wikipedia.org/wiki/End-of-file).
# 
# Dans ce qui suit, on identifiera le symbole de fin de ligne avec **le caractère spécial `\n`**.
# 

# :::{dropdown} Aspect historique
# 
# **Fichier à accès direct _vs._ à accès séquentiel.**
# 
# On distingue :
# -  les fichiers qui permettent d'accéder _directement_ à une ligne (et l'enregistrement) quelconque de leur contenu,   
# - les fichiers qui nécessitent un parcours systématique et _séquentiel_ à partir de la dernière ligne accédée (et donc depuis le début du fichier lors de la première opération).
# 
# Ces différents comportements sont essentiellement dues à des aspects matériels.
# Historiquement, les fichiers stockés sur des bandes magnétiques (!) étaient à accès séquentiel.
# 
# La plupart des fichiers utilisables aujourd'hui sont à accès direct -- ce qui sera le cas dans ce qui suit.
# 
# :::

# ## Trois exemples simples pour savoir faire

# <div class="alert alert-info">
# 
# Objectif 10 : On se limite à des manipulations simples (lecture ou écriture) de fichier de texte.
#     
# </div>

# Un premier objectif de ce chapitre est de faciliter les tests de vos développements en limitant la perte de temps liée à la saisie au clavier, perte de temps qui est d'autant plus élevée que le nombre de saisies est élevé (nombreuses valeurs ou nombreux essais).   
# 
# La forme des fichiers dépend des valeurs stockées mais aussi des facilités de lecture-écriture du langage.
# Un fichier structuré de façon simple, voire simpliste, fera l'objet de procédures d'entrée-sortie faciles à écrire.  
# Inversement, les traitements d'un fichier structuré de façon plus complexe seront vite plus techniques à écrire.
# En contre-partie, le fichier simple sera souvent moins commode à manipuler via l'éditeur de texte qu'un fichier dont la structure reflète déjà celle de l'information qu'il contient.
# 
# Face à ce compromis, nos premiers exemples visent des procédures d'entrées-sorties simples pour python. 
# - Le premier manipule _uniquement_ des chaînes de caractères et se limite à des lectures
# - Le deuxième effectue des lectures et traitements sur des entiers et des flottants
# - Le troisième effectue des écritures d'entiers et de flottants

# ### Premier exemple : lectures de `str` 
# 
# 
# #### Objectif
# 
# Je veux tester la fonction `nb_occ()` qui compte le nombre d'occurrences d'une lettre dans une chaîne de caractères. 

# In[1]:


def nb_occ (char: str, texte: str) -> int:
    '''calcule et retourne le nombre d'occurrences de char dans texte'''
    nb = 0
    for i in range(len(texte)):
        if texte[i] == char:
            nb = nb + 1
    return nb


# #### Deux fichiers de test
# 
# Je décide de compléter plusieurs fichiers texte composés de 2 lignes selon le modèle suivant :
# 
# > le caractère cherché  
# > la chaîne de caractères à explorer
# 
# Les fichiers `test_nb_occ0.txt` et `test_nb_occ1.txt` sont deux exemples de tels fichiers. 

# In[2]:


get_ipython().system('cat tmp/test_nb_occ0.txt')


# In[3]:


get_ipython().system('cat tmp/test_nb_occ1.txt')


# #### Lecture ligne à ligne avec `.readline()` qui fournit une `str` par ligne 
# 
# La fonction-méthode python `.readline()` permet :
# - de parcourir séquentiellement le fichier ligne après ligne,
# - et chaque ligne lue est fournie comme une `str`.

# Chaque ligne des fichiers de test contient une chaîne de caractères.
# Cette lecture avec `.readline()` est donc tout à fait adaptée.

# :::{important} 
# 
# La fonction-méthode `.readline()` est une fonction particulière. 
# Il s'agit en fait d'une _méthode_. 
# Une méthode est une fonction dont l'appel est préfixé par l'identifiant d'une variable (un objet en fait) suivi d'un `.` 
# On parlera donc de _fonction-méthode_.
# 
# Exemple. `mon_fichier.readline()` pour indiquer que `readline()` s'applique au fichier (logique) de nom `mon_fichier`.
# 
# On pourrait se demander pourquoi `mon_fichier` n'est pas un paramètre de l'appel de `readline()`, c-a-d. que `mon_fichier` pourrait apparaître entre `( )` lors de l'appel. Ce point sera clarifié ultérieurement. Ce n'est certainement pas la première fois que vous rencontrez cette **notation préfixée pointée**. Ce ne sera pas la dernière. Ce n'est pas le cas ici avec `.readline()` mais des paramètres autres que celui préfixé peuvent apparaître entre `( )` lors de l'appel. 
# :::

# In[4]:


# association et ouverture du fichier -- noter le mode "r" pour read
f = open("./tmp/test_nb_occ0.txt", "r", encoding="utf8")

# lecture séquentielle par ligne. 
c = f.readline() # lecture du caractère 
m = f.readline() # lecture du mot

# fermeture    
f.close()


# :::{note}
# Notez le préfixe `f` devant `.readline()` où `f` est le nom du fichier logique défini à l'association/ouverture.
# :::

# Les 4 étapes association/ouverture/lecture/fermeture de ce fichier sont effectuées. 
# 
# Le traitement des entrées n'est pourtant **pas terminé**. 

# #### Nettoyage des caractères spéciaux de fin de ligne
# 
# Observons plus en détail ce qui a été _effectivement_ lu.  
# Un focus sur le caractère `c` lu à la première ligne du fichier suffit à comprendre.

# In[5]:


print(c)
print(type(c))
print(len(c))


# Surprise : `c` est un caractère de longueur 2 !?
# 
# En effet, la première ligne du fichier est composé d'un caractère (ici `z`). Mais elle est aussi terminée par le caractère spécial d'EOL, ici `\n`. Ce qui fait 2 caractères au total lus par `.readline()`.
# 
# On peut le vérifier en convertissant `c` en `lst` :

# In[6]:


print(list(c))


# Il faut donc "nettoyer" chaque ligne lue de ce caractère spécial si le traitement à effectuer le nécessite.
# C'est très souvent le cas.
# 
# Les tranches de `str` ou de `lst`  python (_slice_) rendent ce nettoyage facile : on rappelle que le dernier élément d'un tableau est d'indice -1.

# In[7]:


c = c[:-1] # tranche de tableau qui "supprime" la dernière valeur de c 
print(c)


# Et de même pour le mot lu en seconde ligne du fichier :

# In[8]:


if m[-1] == '\n':
    m = m[:-1]
print(m)


# **Remarques.** 
# 
# - On a ajouté un test de la présence du _EOL_ car la dernière ligne d'un fichier ne se termine pas nécessairement ainsi.
# - Les caractères spéciaux et la notion d'_échappement_ (avec un `\`) sont traités dans cette [section](sec:echappement) sur les `str` du chapitre sur les type composés.

# #### Traitement : le premier test de `nb_occ()`
# 
# Passons enfin au traitement proprement dit, ici le test le la fonction `nb_occ()`.

# In[9]:


assert nb_occ(c, m) == 0


# On a donc lu le premier fichier de test de `nb_occ`. La fonction a passé avec succès le test défini par les paramètres lus dans ce fichier. L'exécution sans erreur de l'instruction `assert` permet de continuer.  

# **Rmq.** Les fichiers _physiques_ doivent exister pour être ouverts, lus, modifiés, fermés.  

# #### Exploitation du second fichier
# 
# On recommence lecture et test pour le second fichier de test où 5 occurrences de la lettre `n` sont attendus.

# In[10]:


get_ipython().system('cat tmp/test_nb_occ1.txt')


# On supprime directement le _EOL_ à chaque lecture à l'aide de la tranche `[:-1]`.

# In[11]:


# association et ouverture du fichier -- noter le mode "r" pour read
f = open("./tmp/test_nb_occ1.txt", "r", encoding="utf8")

# lecture séquentielle par ligne
c = f.readline()[:-1] # lecture du caractère 
m = f.readline()[:-1] # lecture du mot

# fermeture    
f.close()

# affichage par curiosité
#print(list(c), m, nb_occ(c, m))

# test
assert nb_occ(c, m) == 5


# Ce second test de `nb_occ()` est aussi validé.

# **Extensions possibles.**
# 
# Il vient naturellement à l'idée de rassembler dans un seul fichier plusieurs cas tests, voire même les résultats attendus de chacun de ces tests. Même dans ce cas simple, de telles extensions sont vite plus compliquées qu'il y parait. En effet, ajouter par exemple les résultats attendus revient à ajouter des valeurs entières (les nombres d'occurrences attendus) dans un traitement pour l'instant limité à de la manipulation de `str`.
# 
# L'exemple suivant permet d'illustrer un cas similaire.

# ### Deuxième exemple : lecture `.readline()` avec conversion de type et effets dynamiques
# 
# #### Objectif
# 
# Je veux tester la fonction de produit scalaire suivante.

# In[12]:


def prod_scal(u : list[float], v : list[float], n : int) -> float:
    '''calcule et retourne le produit scalaire u^t.v où u et v sont de taille n'''
    assert len(u) == len(v) == n
    res = 0.0
    for i in range(n):
        res = res + u[i]*v[i]
    return res


# #### La forme d'un fichier de test
# 
# Je décide de compléter un fichier texte selon le modèle suivant :
# 
# > $n$  
# > $u$   
# > $v$   
# > $u^t v$ 
# 
# Ainsi :
# 
# 1. la première donne la taille $n$ des vecteurs,  
# 2. les $n$ lignes suivantes donne les composantes de $u$,
# 3. les $n$ lignes suivantes celles de $v$,
# 3. enfin la dernière indique la valeur du produit scalaire (calculée "à la main").
# 
# Ainsi, je vais pouvoir comparer le résultat de `prod_scal()` et celui attendu, et ce sur des vecteurs de tailles arbitraire. Chaque choix ($n$, $u$, $v$, $u^t v$) est un _cas test_ pour `prod_scal()`.
# 
# `test_prod_scal.txt` est un exemple d'un premier cas test : 2 vecteurs de taille 4 de produit scalaire égal à 2.

# In[13]:


get_ipython().system('cat ./tmp/test_prod_scal.txt')


# #### Conversions et effets dynamiques
# 
# **Analyse préliminaire**
# 
# 1. Conversions `str` $\to$ valeurs numériques
#     - Le fichier de texte contient _uniquement_ des caractères, des `str` en python.
#     - Pourtant, ces `str` correspondent à un `int` ou des `float`
#     - Ainsi, des conversions adaptées devront être effectuées pendant (ou après) la lecture :
#         - conversion en `int` pour la ligne 1
#         - conversions en `float` pour les autres
# 
# 2. Conséquences dynamiques 
#     - La taille des vecteurs est connue _après_ avoir lu la valeur pour `n` (ligne 1) 
#     - Les vecteurs devront être créés une fois `n` connu
#     - La lecture de la suite du fichier (composantes des 2 vecteurs, résultat attendu) dépend aussi de la valeur lue pour $n$
#     
# 
# 3. Rappel : la gestion des fins de ligne
#     - Chaque ligne du fichier se termine par un caractère spécial _EOL_, ici `\n`
#     - Comme précédemment, ces caractères spéciaux seront lus aussi et un traitement adapté sera défini -- par exemple, les supprimer. 

# On va profiter de cet exemple pour donner **une autre construction** python des 4 étapes association/ouverture/lecture/fermeture de ce fichier.
# 
# - La lecture est toujours effectuée ligne après ligne avec `.readline()` 
# - mais la construction avec la clause de contexte `with` permet de se dégager de l'ouverture et la fermeture au préalable obligatoires.

# #### Lecture avec la clause `with` 
# 
# Cette lecture de la première ligne uniquement pour commencer en illustrant cette nouvelle construction très utile en pratique.

# In[14]:


# association/ouverture/lecture/fermeture avec clause with
with open("./tmp/test_prod_scal.txt", "r", encoding="utf8") as f:
    # la taille n : lecture et nettoyage du EOL
    n = f.readline()[:-1]


# In[15]:


print(n, len(n), type(n))


# On retrouve la configuration de l'exemple précédent sans à avoir à utiliser les instructions `open()`et `.close()`.
# 
# Occupons-nous maintenant du typage des valeurs lues.
# 

# #### Lecture `.readline()` avec `with` et typage 
# 
# Le nettoyage de chaque ligne étant effectué après la lecture et avant l'affectation, le typage est aisé : d'abord un `int` puis des `float`.

# In[16]:


# association/ouverture/fermeture avec clause with
with open("./tmp/test_prod_scal.txt", "r", encoding="utf8") as f:
    # la taille n : lecture
    n = int(f.readline()[:-1])
    
    # premier vecteur : création et lecture
    x = [0. for i in range(n)]
    for j in range(n):
        x[j] = float(f.readline()[:-1])
    # second vecteur : création et lecture
    y = [0. for i in range(n)]
    for j in range(n):
        y[j] = float(f.readline()[:-1])
    # produit scalaire : resultat attendu 
    ps_exact = float(f.readline()[:-1])  


# **Remarque.** Ne pas oublier le nettoyage de _EOL_ lors de chaque `readline()`. 
# 
# Il ne reste plus qu'à tester.

# #### Test unitaire de `prod_scal()`

# In[17]:


assert prod_scal(x, y, n) == ps_exact


# Le test ainsi validé nous rassure sur la correction de `prod_scal()`. 
# 
# Bien sûr, des extensions similaires à celles explicitées à l'exemple précédent sont tentantes. 
# On vous invite à continuer en ce sens en exercice.

# ### Troisième exemple : écritures simples avec `.write()`
# 
# 
# On termine en montrant comment l'écriture simple _dans_ des fichiers textes s'obtient de façon très similaire avec la fonction méthode `.write()`.
# 
# Toujours les 4 étapes mais :
# - l'ouverture du fichier s'effectue en mode `w` (_write_) ou `a` (_append_ : ajouter à la fin)
# - la fonction-méthode `.write()` permet l'écriture d'une `str` 
# - la conversion vers des `str` sera donc un préalable
# - ainsi que la gestion des _EOL_, ici `\n` pour effectuer les sauts de lignes souhaités dans le fichier
#     - en effet, `.write()` écrit la `str` à la suite de la dernière écriture effectuée.

# #### Construction d'un cas test de `nb_occ()`

# In[18]:


# Préparation des données à stocker
from random import randint

# une taille de vecteurs au hasard
n = randint(1, 10)

# un choix de composantes tel que ps_exact == n
x = [float(i) for i in range(1, n+1)]
y = [1./float(i) for i in range(1, n+1)]


# In[19]:


## vérifications
print(n, x, y, prod_scal(x, y, n))


# #### Enregistrement dans un fichier de test

# In[20]:


# association/ouverture/fermeture avec clause with
with open("./tmp/test_prod_scal_write.txt", "w", encoding="utf8") as f:
    f.write( str(n) + '\n' )
    for i in range(n):
        f.write( str(x[i]) + '\n' )
    for i in range(n):
        f.write( str(y[i]) + '\n' )
    f.write( str(float(n))  + '\n' )  # ==ps_exact        


# On vérifie que le fichier `
# ./tmp/test_prod_scal_write.txt` a bien été créé et son contenu.

# In[21]:


get_ipython().system('ls -l tmp/test_prod_scal*.txt')


# In[22]:


get_ipython().system('cat tmp/test_prod_scal_write.txt')


# :::{warning} 
# L'ouverture en écriture (mode `w`) écrase éventuellement un fichier physique existant et de même nom.  
# :::

# #### Exploitation du fichier de test
# 
# :::{dropdown}
# 
# Il suffit maintenant de lire ce fichier et d'effectuer le test.
# 
# ```python
# # association/ouverture/fermeture avec clause with
# with open("./tmp/test_prod_scal_write.txt", "r", encoding="utf8") as f:
#     # la taille n : lecture
#     n = int(f.readline()[:-1])
#     
#     # premier vecteur : création et lecture
#     x = [0. for i in range(n)]
#     for j in range(n):
#         x[j] = float(f.readline()[:-1])
#     # second vecteur : création et lecture
#     y = [0. for i in range(n)]
#     for j in range(n):
#         y[j] = float(f.readline()[:-1])
#     # produit scalaire : resultat attendu 
#     ps_exact = float(f.readline()[:-1])  
#     
# assert ps_exact == prod_scal(x, y, n)
# ```
# 
# On est rassuré.
# 
# :::

# ### Synthèse et minimum à savoir-faire
# 
# Pour ce qui concerne les entrées en se limitant à des fichiers où chaque valeur est stockée sur une ligne, on a vu :
# - les 4 étapes classiques association/ouverture/lecture/fermeture,
# - la construction simplifiée avec la clause `with`,
# - la lecture séquentielle ligne après ligne avec `.readline()`,
# - l'écriture simple avec `.write()`,
# - la gestion des caractères spéciaux _EOL_,
# - la conversion des lectures `str` vers des types adaptés aux traitements à effectuer,
# - et inversement pour les écritures.
# 
# On a naturellement complété cette présentation par l'écriture de tests unitaires à l'aide d'instructions `assert`.
# 
# Bien maîtriser le `print()` peut faire gagner du temps. Se reporter à [cette section](sec:print) si besoin. 

# (sec:EScomplements)
# 
# ## Compléments

# <div class="alert alert-warning">
# 
# A lire en seconde lecture    
# </div>

# Cette section pour introduire d'autres fonctions de lecture-écriture que `.readline()`et `.write()`.
# 
# * Des lectures complètes du fichier
#     - `.read()`: lit tout le fichier et retourne un `str`  
#     - `.readlines()`: lit tout le fichier et retourne une `list` de `str`  
#     
# * Une autre lecture partielle  
#     - `.read(oct)`: lit `oct` octets dans le fichier et retourne un `str`
# 
# * Ecriture ligne à ligne
#     - `.writelines()`: écrit une `list` de `str`, ligne après ligne dans le fichier 
#     
# Selon les besoins, ces fonctions facilitent l'écriture des entrées-sorties sur fichier.

# :::{note} Noter le `s` dans `.readlines()`, et de façon symétrique dans `.writelines()`.
# :::

# ### Lecture complète : `.read()` fournit une `str` 
# 
# Les fichiers de test précédents peuvent bien sûr être "lu d'une seule fois" : lecture complète _vs._ lecture ligne à ligne. 
# 
# #### Principe 
# 
# La fonction-méthode `.read()` effectue cette lecture complète et retourne une chaîne de caractères _unique_.
# 
# Un exemple sur un de nos précédents fichiers.

# In[23]:


# association et ouverture du fichier -- noter le mode "r" pour read
f = open("./tmp/test_prod_scal.txt", "r", encoding="utf8")

# lecture complète du fichier et maj d'un string
s = f.read()    

# fermeture    
f. close()


# :::{attention} **ATTENTION au `read()` !**  
# 
# Comme le dit le manuel (7.2.1):  
# > it’s your problem if the file is twice as large as your machine’s memory.

# In[24]:


print(len(s))


# In[25]:


print(s)


# :::{important}
# La lecture complète du fichier ne fait pas disparaître la structuration du fichier en lignes.
# Les caractères spéciaux _EOL_ sont toujours présents dans la chaîne de caractères issue du `.read()`.
# Un `print()` trop naïf peut être trompeur.
# :::
# 
# Se reporter à la [section](sec:print) pour re-visiter le `print` si besoin était.

# Bien sûr, nos précédents fichiers et traitements ne sont pas adaptés à cette lecture complète et la `str` unique qui en découle. En revanche, un exemple classique de l'intérêt de `.read()` est la lecture complète d'un fichier qui contient un texte (même long) enregistré dans un format brut : utf-8 par exemple, voir [cet article facile à lire](https://zestedesavoir.com/tutoriels/1114/comprendre-les-encodages/2-histoire/) pour plus de détails.
# 
# #### Exemple classique 
# 
# L'exemple suivant illustre l'utilisation classique du `.read().`
# 
# Le roman _La disparition_ de G. Perec (1968) est 
# [bien connu](https://fr.wikipedia.org/wiki/La_Disparition_(roman)) 
# pour l'absence de la lettre `e` dans ses 300 pages -- [entre autres](https://jazlebontemps.com/2016/12/15/la-disparition-roman-de-georges-perec-1968/) .
# 
# Hélas, je n'ai pas réussi à trouver un fichier texte contenant une version parfaite de ce roman (n'hésitez-pas à combler ce manque). `./tmp/ladisparition.txt` est un exemple d'un tel fichier "imparfait". 
# 
# Vérifions-le en utilisant la fonction-méthode [`.count`](https://docs.python.org/fr/3.9/library/stdtypes.html?highlight=str.count#str.count) qui s'applique à une `str` et retourne le nombre d'occurrences de son argument.

# In[26]:


with open("./tmp/ladisparition.txt", "r") as f:
    full_roman = f.read()
    
print(len(full_roman))
print( full_roman.count('e') )


# En effet, il y a 5 occurrences de trop de la lettre `e` dans ce roman (j'ai laissé le titre et le nom de l'auteur en début de fichier).

# In[27]:


get_ipython().system('head -3 ./tmp/ladisparition.txt')


# ### Lecture complète : `readlines()` fournit une `list` de  `str` 
# 
# #### Principe
# 
# De façon similaire, `.readlines()` (avec un 's' à la fin) effectue une lecture complète du fichier et retourne une liste de `str`, liste composée de chaque ligne du fichier.
# 
# L'exemple suivant nous aide à exhiber les caractère spéciaux `\n` non encore "nettoyés". 

# In[28]:


# association et ouverture du fichier -- noter le mode "r" pour read
f = open("./tmp/test_prod_scal.txt", "r", encoding="utf8")

# lecture complète et maj d'une liste de str
l = f.readlines()    

# fermeture    
f. close()


# In[29]:


print(len(l))


# In[30]:


print(l)


# **Exercice.**
# Expliquer les résultats obtenus par :
# > `len(s)` issu de `.read()`  
# 
# et  
# 
# > `len(l)` issu de `.readlines()`

# :::{dropdown} Réponse.
# 
# ```python
# for elem in l: 
#     print(elem[:-1], len(elem), sep="->")
# ```
# ```shell
# 4->2
# 1.->3
# 1.->3
# 1.->3
# 1.->3
# 1.->3
# 1.->3
# -1.->4
# 1.->3
# 2.->3
# ``` 
# :::

# #### ($\star$) Exemple classique
# 
# On peut maintenant traiter des fichiers plus commodes pour tester `prod_scal()`.
# 
# Plusieurs cas-tests sont regroupés dans le suivant de façon plus lisible :
# - comme précédemment, chaque cas test est défini par le quadruplet $(n, x, y, x^t y).$ 
# - chacun de ces paramètres est écrit sur une ligne
# - chaque cas test est terminé par une ligne vide.

# In[31]:


get_ipython().system('cat ./tmp/test_prod_scal3.txt')


# Cette procédure d'ES (un peu technique) nécessite des transformations de `str`, par exemple la fonction-méthode `.split()`, qui sont présentées au chapitre [_Types composés_](ch:typescomposes).

# In[32]:


# lecture du fichier de données cas-test
# et préparation des données pour tests

with open("./tmp/test_prod_scal3.txt", 'r') as f:
    l_data = f.readlines()

#print(l_data)

# nettoyage en place
l_data = [e[:-1] for e in l_data]
print("data nettoyées: ", l_data)

# décompte du nombre de cas-test
nbcastest = 0
for elem in l_data:
    if elem == '': # chaque cas-test se termine par une ligne vide
        nbcastest = nbcastest + 1
#print(nbcastest)

# tab_castest pour stocker les paramètres de chaque cas test
tab_castest = [0 for i in range(nbcastest) ]
# maj paramètres : n, x[n], y[n], x^t.y exact soit 4 valeurs dont 2 listes de float

i_elem = 0 # indice dans l_data
for numtest in range(nbcastest):
    n = int(l_data[i_elem])
    # les parametres sont rangés dans un vecteur de taille 4 (un objet/struct serait mieux)
    tab_castest[numtest] = [0 for i in range(4)]
    tab_castest[numtest][0] = n # n du cas test
    tab_castest[numtest][3] = float(l_data[i_elem + 3]) # prod scal exact du cas test
    tab_castest[numtest][1] = [float(val) for val in l_data[i_elem + 1].split(' ')] # x[n] du cas test
    tab_castest[numtest][2] = [float(val) for val in l_data[i_elem + 2].split(' ')] # y[n] du cas test
    i_elem = i_elem + 5 # +1 final pour ligne vide

print("les cas tests: ", tab_castest)


# In[33]:


# la vérification de `prod_scal()`
for nb in range(len(tab_castest)):
    castest = tab_castest[nb]
    assert prod_scal(castest[1], castest[2], castest[0]) == castest[3]


# Et voilà le travail ! 
# Il est maintenant facile d'étendre les cas tests de `prod_scal()` en complétant le fichier `./tmp/test_prod_scal3.txt` selon le format adopté`

# ### Origine classique des problèmes d'ES 
# 
# La gestion des caractères spéciaux, `\n` entre autres.
# 
# - `f.read()` peut lire et retourner le caractère `\n` ou  la chaîne vide `''`, ce qui est différent :
#     - `\n` = une ligne vide ... de caractères "classiques" : elle est réduite au caractère spécial qui désigne _EOL_
#     - `''` = pas de ligne : on a atteint la fin du fichier _EOF_  
# - `f.readlines()` (comme `f.readline()`) lit une ligne complète, caractère spécial (`\n`) compris.
#     - il retourne donc _aussi_ ce `\n` de _EOL_ 
#     - sauf dans le cas de la dernière ligne si celle-ci n'en comporte pas ! 
# 
# En pratique, on retiendra :
# - que la dernière ligne d'un fichier peut être source de problème,
# - entre autres car les éditeurs de texte (et les systèmes d'exploitation) peuvent ajouter certains caractères non entrés par l'utilisateur lors de l'enregistrement et de la fermeture du fichier.

# (sec:print)=
# ### Bien contrôler ses `print()`
# 
# Deux exemples pour :
# 1. rappeler comment utiliser `sep` et `end` 
# 2. expliciter l'effet du caractère spécial `\n` (nouvelle ligne) dans l'affichage d'une chaîne de caractères avec `print()`.

# In[34]:


#rappel : sep, end
s = "azertyuiop"
print(s, s, s, sep="*", end="--")
print("@@") # par defaut : end='\n'

s = "azertyuiop\n"
print(s, s, s, sep="*", end="--")


# In[35]:


# s est _une_ chaine de caractères
s = "azer\ntyuiop"
print(s)
print(s, sep="*")
print(s, end="--")


# Nous reviendrons sur les caractères spéciaux dans le chapitre sur les chaînes de caratères. 

# **Quiz**  
# 
# Quelle est la dernière ligne du fichier `./tmp/fichier_entrees.txt` ?
# 1. 188
# 2. 188\n
# 3. \n
# 4. '' (ligne vide) 

# In[36]:


get_ipython().system('cat ./tmp/fichier_entrees.txt')


# :::{dropdown}
# Réponse. `.readlines()` est votre ami. 
# 
# ```python
# with open("./tmp/fichier_entrees.txt", 'r') as f:
#     l_st = f.readlines()
#     
# print(l_st)
# ```
# ```shell
# ['6\n', '99\n', '21\n', '33\n', '44\n', '33\n', '188\n']
# ```
# :::

# In[ ]:





# ## Synthèse 

# ### Avoir les idées claires
# 
# - Distinguer fichier logique _vs._ physique, texte _vs._ binaire, mode lecture _vs._ écriture (_vs._ lecture-écriture) 
# - Connaître les 4 étapes de manipulation d'un fichier : association/ouverture/lecture-écriture/fermeture
# - Distinguer représentation textuelle et valeur (numérique)   
# 
# 
# ### Savoir-faire
# 
# - Savoir écrire les lectures-écritures simples de fichier texte avec `.readline()` et `.write()`
# - Comprendre et gérer l'effet des caractères spéciaux 
# - ($\star $) Savoir écrire les lectures-écritures de fichiers texte avec les instructions python adaptées   
# 

# ### Un dernier conseil
# 
# - Le risque d'erreur lors de la mise au point du traitement d'ES sur fichier est important.  
# - Il n'est pas rare de perdre tout ou partie d'un fichier à lire.
# - On ne peut donc que conseiller :
# 1. de **commencer par** effectuer une copie de sauvegarde des fichiers originaux avant tout développement de code d'ES
# 2. de vérifier pas à pas la mise au point de ces traitement avec des `print()` bien choisis -- qui seront bien sûr commentés une fois le traitement validé.

# ### Ce qu'il restera à voir
# 
# Ce chapitre s'est limité à la manipulation de fichiers texte.
# Lorsque les données à sauvegarder sont volumineuses et souvent accédées, il est classique d'avoir recours à des **fichiers binaires**. En python, ces fichiers sont définis en ajoutant la caractéristique `b`  au mode `r`, `w`, ou `a` lors de l'association/ouverture du fichier. Ensuite, les traitements décrits dans ce chapitre s'appliquent globalement. 
# 
# Le chapitre [ES avancées](ch:ES-avancees) complète celui-ci en présentant comment _formater_ les données lues ou écrites dans les fichiers.
# 
# On peut se déplacer dans un fichier pour accéder à un enregistrement quelconque (une ligne ou une fraction de ligne). Ce type de traitement nécessite de caractériser comment la position de ces enregistrements  est définie -- par le langage de programmation et en général en nombre d'octets depuis le début du fichier. Le lecteur intéressé se reportera à la documentation (de python) pour ces manipulations un peu techniques. 
# 
# Les traitements précédents permettent de créer et d'exploiter des fichiers, et ce indépendamment de leur stockage dans le _système de fichiers_ de l'environnement utilisé (Linux, w\*\*\* ou m\*\*\*).
# Il est utile de compléter ces traitements par de la _manipulation_ de fichiers de façon similaire à celle vue en cours de Système au semestre 1. Pour cela, python propose les modules suivants :  
# - `os` qui permet de se déplacer dans l'arborescence du système de fichiers  
# - `os.path`, sous-module du précédent, qui permet de lister des fichiers, des répertoires et certaines de leurs caractéristiques  
# - `shutil` qui permet de copier, déplacer et supprimer des fichiers ou des parties d'arborescence.  
# 

# In[ ]:




