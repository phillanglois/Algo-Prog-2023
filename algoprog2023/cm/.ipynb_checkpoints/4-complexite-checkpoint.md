(ch:complexite)=
# Complexités

Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes` minutes minimum, PhL.

# Complexités en temps, en espace
Complexité asymptotique

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexités : plan

[Motivations\, principes\, notions importantes et exemples introductifs](slide3.xml)

[Complexité en temps](slide11.xml)

[Complexité en espace](slide19.xml)

[Un autre exemple de complexité polynomiale](slide22.xml)

[Complexité et log](slide30.xml)[2](slide30.xml)

[\(\*\) Un complément](slide35.xml)

[Complexité asymptotique](slide41.xml)

[Exprimer les complexités asymptotiques des itérations et ](slide48.xml)[récursions](slide48.xml)

[Synthèse](slide55.xml)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Motivations

* Contexte
  * un problème à résoudre
    * \- une question et \(au moins\) une réponse qui dépend de paramètres : données "en entrée"
  * une instance de ce problème qui admet au moins une solution
    * \- un choix des paramètres\, des données d'entrée
  * un algorithme qui calcule cette solution
    * \- un algorithme\, ou même plusieurs algorithmes
* Questions du jour
  * De  __combien de temps __ a besoin l'algorithme pour calculer cette solution ?
  * De  __combien d'espace\-mémoire __ a besoin l'algorithme pour calculer cette solution ?
* Motivations
  * \- Appuyer sur la touche \<enter> ou non ?
  * \- Appliquer mon algorithme à toute instance de ce problème ?
  * \- Comment quantifier  _l’efficacité_  d’un algorithme ? Mesurer la difficulté de la résolution d’un problème ?
    * \- Objectif : choisir\, adapter\, améliorer\, …

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Je calcule la somme de n valeurs entières

Une instance : un choix de n et des n valeurs du tableau t

Principe d'un algorithme : je parcours le tableau\, "du début à la fin"\, je lis chaque valeur\, je l'accumule dans une variable \(initialement mise à zéro\)\, je retourne cette variable\.

def sommer\(t : List\[int\]\, dim\_t : int\) \-> int:

‘’’ somme itérative de n=dim\_t valeurs entières stockées dans un tableau t	entrées\. t tab d’int de longueur dim\_t\. Retourne res\.’’’

res = 0  	 \# j’'accumule dans res

for i in range\(dim\_t\):

res = res \+ t\[i\]

return res

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Je recherche l’indice d’une valeur parmi n valeurs stockées dans un tableau

Une instance : un choix de la valeur cherchée\, de n et des n valeurs du tableau t

Principe d'un algorithme : je parcours le tableau à partir de son premier indice\, je compare chaque valeur du tableau à la valeur cherchée\, si égalité je retourne l’indice de cette valeur\, sinon je répète ce traitement sur la valeur suivante\. Je renvoie un indice significatif de l’absence si aucune égalité n’a été satisfaite après le dernier indice du tableau\.

def rechercheIterative\(val : float\, t : List\[float\]\, dim\_t: int\) \-> int:

‘’’ recherche itérative de val dans t tableau de taille dim\_t	retourne l’indice de la première occurrence de val ou \-1 si absence’’’

i = 0  	 \# j’'accumule dans res

while i < dim\_t:

if val == t\[i\]:

return i

i = i\+1

return \-1

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité en temps, complexité en espace

Quel est le temps nécessaire à la résolution du problème avec un algorithme ?

Quel est l'espace\-mémoire nécessaire à la résolution du problème avec un algorithme ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité ? en temps ? en espace-mémoire ?

* 1\. On a  __un problème __ à résoudre :
  * calculer la somme de n valeurs entières stockées dans un tableau t
  * rechercher \(l’indice d’\)une valeur dans n valeurs stockées dans un tableau t
* 2\. On a \(au moins\)  __un algorithme __ qui résout ce problème
  * sommer\( \) dans sa version itérative codée avec une boucle for
  * rechercheIterative\( \) codée avec une boucle while
* 3\. Combien de  __temps__  pour calculer la réponse ?  Quel est le  _coût en temps _ de l'algorithme ?
  * sommer\( \)
  * \- ça  __dépend de n __ : le nombre de valeurs à sommer
  * \- a priori\, le temps de calcul est une fonction croissante de n
  * \- OK mais croissante comment ? linéaire ? quadratique ?  logarithmique ?
  * rechercheIterative\( \)
  * ça  __dépend __ de n\, de t  __et de val __ : le nombre de valeurs\, de leur ordre et de la valeur à trouver
  * _meilleur cas _ : val est à l’indice 0 et coût indépendant de n
  * _pire cas _ : val est absente de t et coût fonction croissante de n
* 4\. Combien  __d'espace\-mémoire __ pour calculer la réponse ? Quel est le  _coût en espace _ de l'algorithme ?
  * ça  __dépend __ aussi  __de n__  : faut déjà réussir à stocker les n valeurs \!
  * OK mais quel est  <span style="color:#ED7D31">l'espace mémoire supplémentaire </span> pour résoudre le problème ?
  * Dépendant ou indépendant de n ?  dépendant comment ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Paramètres de la complexité

* On a un problème à résoudre :
  * calculer la somme de n valeurs entières stockées dans un tableau t
* Quels sont les  <span style="color:#FF0000">paramètres du coût</span>  de sa résolution ?
* _La taille du problème _
  * \- ce qui caractérise la taille dépend du problème
  * \- sommer n valeurs entières\, rechercher dans n valeurs\, trier n valeurs :
    * taille = n = le nombre de valeurs
  * \- je calcule l'addition de 2 nombres entiers :
    * la taille =  le nombre de chiffres de chaque opérande\, ou le max des 2
* <span style="color:#4472C4">Certaines données/entrées du problème : instance du </span>  <span style="color:#4472C4">pb</span>
  * je recherche l’indice d’une valeur dans un tableau donné
  * je trie une liste déjà triée  _vs_ \. je trie une liste « bien mélangée »

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# complexité = f(taille) La question : ordre de grandeur pour des très grandes tailles ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Comment mesurer ce coût ?

* On a \(au moins\) un algorithme qui résout ce problème
  * sommer dans sa version itérative boucle for
  * rechercheIterative avec sa boucle while
* On veut mesurer les coûts en temps d'exécution et en espace\-mémoire\.
* Mesurer => exécuter l’algorithme pour une  __analyse de complexité__
* On exécute l'algorithme sur  _un modèle de machine_
  * _simple_  : beaucoup de détails d'une véritable exécution sont ignorés
  * mais  _pas trop simpliste _ : les résultats et les observations réelles sont raisonnablement corrélées
  * l'exécution continue a dépendre des données d'entrées : pire cas\, meilleur cas
  * l’objectif :  __dégager des tendances\, des ordres de grandeur __

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Mener une analyse de la complexité en temps

Un modèle d’exécution

Analyse du pire temps d'exécution avec le modèle RAM

Modèle vs\. pratique ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Un modèle de complexité pour mesurer le coût en temps d'un algorithme

* _Toutes les instructions importantes comptent 1 unité _ de temps :
  * 1 = affectation = comparaison = opération arithmétique = opération logique
  * = accès mémoire = entrées/sorties
* _Les instructions s’exécutent séquentiellement _ :
  * si l'instruction p coûte c1 et l'instruction q coûte c2\,
  * alors la suite d'instructions p\, q coûte c1\+c2
* _Coût du branchement conditionnel :  if\.\.\. _  _elif_  _ \.\.\. _  _else_  _ _  _…_
  * inférieur ou égal au coût maximum de chaque branche d'instructions
* _Coût de la répétition : for i in range\(n\): _  _corps\_de\_boucle_
  * si le coût de p ne dépend pas de i : n x coût\(corps\_de\_boucle\)
  * sinon : la somme des coûts de chacune des n répétitions
* _Coût de la répétition _  _while_  _\(condition\): _  _corps\_de\_boucle_
  * dépend du nombre de répétitions\, inconnu a priori
  * on peut cependant  <span style="color:#FF0000">majorer</span>  ce nombre de répétitions

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Je calcule la somme de n valeurs entières

Somme itérative avec accumulation

\- une boucle for

\- pas de test if …

\- additions entières\, affectations d’entiers\, accès \(lecture\) éléments 	d’un tableau\, retour\, contrôle de boucle for

<span style="color:#FF0000">1</span> 	def sommer\(t : List\[int\]\,  <span style="color:#FF0000">n </span> : int <span style="color:#FF0000"> </span> \) \-> int:

‘’’ somme itérative de  <span style="color:#FF0000">n</span>  valeurs entières stockées dans un 			tableau t\. entrées\. t tab d’int de longueur  <span style="color:#FF0000">n</span> \, retourne res’’’

<span style="color:#FF0000">2</span> 		res = 0  	 \# j’'accumule dans res

<span style="color:#FF0000">3</span> 		for i in range\( <span style="color:#FF0000">n</span> \):

<span style="color:#FF0000">4</span> 	     	 res = res \+ t\[i\]

<span style="color:#FF0000">5</span> 		return res

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Mesurer le coût de sommer(t, n) ?

  * sommer dans sa version itérative avec "boucle for"
* On a un modèle de complexité basé sur :
* chaque instruction compte 1 unité \(de temps\)
  * 1 = affectation = comparaison = opération arithmétique = op\. logique = \.\.\.
* donc on pourrait/devrait  _tout_  __ compter __ \.\.\.
* Simplification de  _la mesure _ :
* on  _identifie_  <span style="color:#4472C4"> </span>  _certaines instructions s_  _ignificatives_  _ du temps de traitement_
* Ici on compte "seulement" les additions de la ligne 4 dans sommer
  * on a autant d'affectations dans res que d'additions
  * on ne compte pas ces affectations\,
  * ni les additions cachées dans la mise à jour des indices de la boucle for
  * écart : facteur multiplicatif du nombre d’additions comptées
* conclusion :  _complexité\(_  <span style="color:#ED7D31"> __sommer__ </span>  _\) = f\(nombre d'additions du corps de boucle\)_

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# C(sommer) = f(nombre d'additions des lignes L3-4)

<span style="color:#000000">for in in range\(n\):</span>

<span style="color:#000000">      </span>  <span style="color:#000000">res</span>  <span style="color:#000000"> = </span>  <span style="color:#000000">res</span>  <span style="color:#000000"> \+ </span>  <span style="color:#000000">t</span>  <span style="color:#000000">\[i\] </span>

<span style="color:#000000">\- Mesure : comptons les additions </span>

<span style="color:#000000">\- </span>  <span style="color:#000000">Paramètre : n est la taille du problème "sommer n valeurs"</span>

L'algorithme sommer effectue 1 addition \(L4\)

à chacune des n répétitions de la boucle pour  \(L3\-4\)

La complexité de la sommation séquentielle sommer  _: _  _C\(n\) = n_

<span style="color:#000000">L'algorithme itératif  </span> sommer

a une  _complexité linéaire _  _en la taille du problème à résoudre_

<span style="color:#FF0000">IMPORTANT</span>  <span style="color:#000000"> : Quelle interprétation ? Quelle conséquence ? </span>

_\- si on double le nombre de valeurs à sommer\, on double le temps de calcul_

C'est d'autant plus vrai que n est assez grand pour que le temps de ces opérations \(les additions\) constitue  _la part significative _ du temps total de l'exécution de sommer\.

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Du modèle pour l'algorithme à la mesure d'un « vrai » programme

* Et en vrai\, sur l’ordinateur ?
  * Des différences importantes entre le modèle d'analyse de complexité de l'algorithme et la chaîne actuelle de calcul : processeur\, mémoires hiérarchiques\, options du compilateur\, parallélisme\, prédiction \.\.\.
  * La mesure des performances d'un code est un processus expérimental assez difficile et qui « ment facilement »
  * Expérience dans le cours de programmation
* L'analyse de complexité est cependant  _significative de la tendance _ des mesures
  * _En pratique _ : un problème donné de  _grande taille _ est résolu plus rapidement par un algorithme en n\,  que par un algorithme en n2 \, et encore plus que par un algorithme en n3 \.\.\.
* Exemple pour des algorithmes très calculatoires
  * on compte le nombre d'opérations arithmétiques
  * on mesure les temps d'exécution d'un programme \(python sur mac\-intel\)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Des mesures réelles de sommer

Mesures sur ma machine de la somme codée en C :

sommer est bien  _linéaire_  en nombre d'additions

Quel sur\-coût observe\-t\-on quand la taille du problème est multipliée par 10 ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Recherche itérative

Le coût de cette recherche dépend aussi de la valeur cherchée val

meilleur cas  _vs\._  pire cas ?

on s’intéresse au  _coût dans le pire cas : majoration_  du coût de  _toute exécution_

mesure de complexité en temps : nombre de comparaisons

paramètre de complexité : le nombre de valeurs _ _ n

ce nombre de comparaisons _ est majoré par_  le nombre de valeurs _ n _

Conclusion :  _complexité au pire linéaire _ en le nombre de valeurs

def rechercheIterative\(val : float\, t : List\[float\]\, dim\_t: int\) \-> int:

‘’’ recherche itérative de val dans t tableau de taille dim\_t	retourne l’indice de la première occurrence de val ou \-1 si absence’’’

i = 0  	 \# j’'accumule dans res

while i < dim\_t:

if val == t\[i\]:

return i

i = i\+1

return \-1

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité en espace

Combien de place mémoire pour que l’ago résolve le pb de taille n ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité en espace-mémoire

* Quelle quantité d'espace\-mémoire est nécessaire pour que l'algorithme trouve la solution du problème ?
* _Quel espace\-mémoire mesurer ?_
  * on ne compte pas la place des données d'entrée\, ni des résultats : incompressible quelque soit l'algorithme
  * on compte "juste"  _la place mémoire supplémentaire_
* Cas facile / moyen / un peu difficile  :
  * facile = statique : toutes les variables utilisées sont connues "dans l'algo"
    * on compte leurs places selon leurs types : scalaire\, tableau 1D\, 2D \.\.\.
  * moyen = dynamique
    * on utilise de l'allocation dynamique de mémoire \(les \`list\` python\)
  * un peu difficile = appels récursifs
    * l'algorithme est récursif \.\.\. à venir très bientôt \!\!
    * la complexité en espace\-mémoire peut alors être très\, voire trop importante

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité en espace-mémoire de sommer

def sommer\(t : List\[int\]\, n : int\) \-> int :

‘’’ somme itérative de n valeurs entières stockées dans un tableau t	de longueur n\. Retourne res’’’

res = 0

for i in range\(n\):

res = res \+ t\[i\]

return res

Analyse

on ne compte pas les n places\-mémoire pour l'entrée : le tableau d'entiers t

on ne compte pas res qui est le résultat retourné

il suffit de pouvoir stocker l'accumulation des t\[i\] : ici dans res

remarque : c'est toujours la même ligne qui compte \!

<span style="color:#ED7D31">un seul entier suffit et ce quelque soit la taille du problème \!</span>

Conclusion :

\. la complexité en espace\-mémoire de sommer est  <span style="color:#ED7D31">constante</span>   \(et égale à 1\)\.

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Un autre exemple de complexité polynomiale

Complexité quadratique du produit matrice x vecteur

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Je calcule le produit matrice x vecteurDéfinition et analyse de l’expression mathématique

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Je calcule le produit matrice x vecteur

<span style="color:#FF0000">1 </span> def Au\(A : List\[List\[float\]\]\,  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000"> </span> : int <span style="color:#FF0000">\, </span>  <span style="color:#FF0000">nb\_cols</span>  : int <span style="color:#FF0000">\, </span> u : List\[float\] <span style="color:#FF0000">\, </span>  <span style="color:#FF0000">nb\_cols</span>  : int\) \-> List\[float\]:

‘’’ calcule produit mat\-vec pour :

A matrice carrée de taille  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000"> \* </span>  <span style="color:#FF0000">nb\_cols</span>  <span style="color:#FF0000">			</span> u : vecteur de taille <span style="color:#FF0000"> </span>  <span style="color:#FF0000">nb\_cols</span>  <span style="color:#FF0000">\, </span> 		retourne v: vecteur de taille <span style="color:#FF0000"> </span>  <span style="color:#FF0000">nb\_lignes</span>  ’’’

for i in range\( <span style="color:#FF0000">nb\_lignes</span> \):

v\[i\] = 0  	 \# j’'accumule dans v\[i\]

<span style="color:#FF0000">4</span> 		for j in range\( <span style="color:#FF0000">nb\_cols</span> \):

<span style="color:#FF0000">5</span> 	     	v\[i\] = v\[i\] \+ A\[i\]\[j\] \* u\[j\]

<span style="color:#FF0000">6</span> 	 return  <span style="color:#FF0000">v</span>

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Algo de calcul du produit matrice x vecteur

1 def Au\(A : List\[List\[float\]\]\,  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000"> </span> : int <span style="color:#FF0000">\, </span>  <span style="color:#FF0000">nb\_cols</span>  : int <span style="color:#FF0000">\, </span> u : List\[float\] <span style="color:#FF0000">\, </span>  <span style="color:#FF0000">nb\_cols</span>  : int\) \-> List\[float\]:

‘’’ calcule produit mat\-vec pour :

A matrice carrée de taille  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000"> \* </span>  <span style="color:#FF0000">nbcols</span>  <span style="color:#FF0000">			</span> x : vecteur de taille <span style="color:#FF0000"> </span>  <span style="color:#FF0000">nb\_cols</span>  <span style="color:#FF0000">\, </span> 		retourne v: vecteur de taille <span style="color:#FF0000"> </span>  <span style="color:#FF0000">nb\_lignes</span>  ’’’

<span style="color:#FF0000">2</span> 	for i in range\( <span style="color:#FF0000">nb\_lignes</span> \):

3	    	v\[i\] = 0  	 \# j’'accumule dans v\[i\]

<span style="color:#FF0000">4</span> 		for j in range\( <span style="color:#FF0000">nb\_cols</span> \):

5	     	v\[i\] = v\[i\] \+ A\[i\]\[j\] \* u\[j\]

6	 return  <span style="color:#FF0000">v</span>

Appel pour : A\[n\]\[n\]\, u\[n\] \-> v\[n\]:  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000"> </span> =  <span style="color:#FF0000">nb\_cols</span>  <span style="color:#FF0000"> </span> =  _n_

Deux boucles for imbriquées de taille n chacune

_boucle extérieure _ :   _n_  __  __  _itérations_  __ __ de

\- ligne 3 : total = n affectations

\- ligne 4 : la boucle for  _intérieure_  _ _

_			\- _  _boucle intérieure _ :  _n_  __ __  _itérations_  __ __ de

\- ligne 5 :  1 \*\, 1 \+\, 1 =

\- total intérieur = 2n opérations\, n affectations

Total extérieur\-intérieur :  __2n__  __2 __  __opérations__ \, n2 \+ n affectations

__Asymptotiquement__  _ : _  _C\(_  _Ax_  _\) ~ n_  _2 _  _ _  _: _ complexité _ _  _quadratique_  _ _ en temps

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Des mesures réelles de A uLe produit matrice-vecteur A x est quadratique en nombre d'opérations arithmétiques

Attention : échelle log10 sur les axes

des x et des y \!

La pente vaut 2\, ce qui représente :

101 sur x  102 sur y

soit donc x  x2

Autre illustration :

le temps de calcul représenté en échelle log\-log est une droite parallèle à celle de n2

Conseil : être à l'aise pour choisir le tracé le plus parlant \!

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité en mémoire du produit matrice x vecteur

1 def Au\( _A_ \,  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000">\, </span>  <span style="color:#FF0000">nb\_cols</span>  <span style="color:#FF0000">\, </span>  _u_  <span style="color:#FF0000">\, </span>  <span style="color:#FF0000">n\_nb\_cols</span> \):

‘’’ calcule produit mat\-vec pour :

A matrice carrée de taille  <span style="color:#FF0000">nb\_lignes</span>  <span style="color:#FF0000"> x </span>  <span style="color:#FF0000">nbcols</span>  <span style="color:#FF0000">			</span> u : vecteur de taille <span style="color:#FF0000"> </span>  <span style="color:#FF0000">nb\_cols</span>  <span style="color:#FF0000">\, </span> 		retourne v: vecteur de taille <span style="color:#FF0000"> </span>  <span style="color:#FF0000">nb\_cols</span>  ’’’

<span style="color:#FF0000">2</span> 	for i in range\( <span style="color:#FF0000">nb\_lignes</span> \):

3	    	v\[i\] = 0  	 \# j’'accumule dans v\[i\]

<span style="color:#FF0000">4</span> 		for j in range\( <span style="color:#FF0000">nb\_cols</span> \):

5	     	v\[i\] = v\[i\] \+ A\[i\, j\] \* x\[j\]

6	 return  _v_

_Complexité en espace mémoire_

_1\. données \- résultats_

entrée : A\[n\]\[n\]\, u\[n\] 	  n2 \+ n

résultat : v\[n\] 		 n

l’espace mémoire de n2 \+ n est minimal \(sauf matrice ou vecteur particulier\)

_2\. algorithme _

mise à jour de chaque composante : traitement  _en place_

espace mémoire supplémentaire  __constant quelque soit n : O\(1\)__

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Le produit matrice x vecteur : synthèse

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Des mesures réelles de A u

Le produit matrice\-vecteur A u est  <span style="color:#4472C4"> __quadratique__ </span>  en nombre d'opérations arithmétiques

Mesures du temps t\(Au\) de l'exécution du produit matrice\-vecteur codé en python sur ma machine

Attention :  <span style="color:#FF0000">échelles logarithmiques </span> sur les 2 axes \!

\- se convaincre que la pente de t\(Au\) vaut 2\, ce qui représente k \. n2

\- la droite t\(Au \)/ n2 est horizontale : ce ratio est constant

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité et log2

Complexité et log

Réduire la complexité

Multiplier 2 entiers\, épisode 1

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Pas que des puissances entières de la taille du pbExemple : algorithmes de recherche

* Le problème : rechercher si une valeur est présente au non dans un tableau de n valeurs
* \- mesure de complexité :  _nombre de comparaisons_
* \- paramètre de cette complexité :   _n_  le nombre de valeurs dans le tabelau
* Un algorithme de  __complexité linéaire __ : recherche itérative \(ou séquentielle\)
  * \- je parcours le tableau du début à la fin et je compare chaque valeur du tableau à la valeur cherchée
  * je m’arrête quand j’ai trouvé ou à la fin du tabelau
  * j'effectue entre 1 et n comparaisons\, au plus n\, jamais plus que n
  * C recherche itérative \(n\) =   n    ou k x n   ou plus tard O\(n\)
  * __Nombre __  _maximal_  _ _  __de comparaisons = nombre d’itérations __  _du pire cas_

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

* Le problème : rechercher si une valeur est présente au non dans un tableau de n valeurs  _triées_  _ _
* La mesure de complexité :  _nombre de comparaisons_
* Un algorithme de  _complexité logarithmique _ :  <span style="color:#ED7D31">la </span>  <span style="color:#ED7D31"> __recherche dichotomique__ </span>
  * <span style="color:#000000">\- je partage le tableau en 2 et je compare la valeur du milieu\,</span>
  * <span style="color:#000000">\- selon le résultat de la comparaison je jette la moitié droite \(ou gauche\) du tableau\,</span>
  * <span style="color:#000000">\- je </span>  _recommence_  <span style="color:#000000"> sur ce tableau de taille moitié : partage en 2\, comparaison milieu\, abandon d'une moitié</span>
  * <span style="color:#000000">\- </span>  _et_  _ _  _ainsi de suite _  <span style="color:#000000">jusqu'à </span>
  * <span style="color:#000000">	avoir trouvé la valeur et là\, je m'arrête</span>
  * <span style="color:#000000">	OU obtenir un \(sous\-\)tableau réduit à 0 ou 1 élément et là\, je m'arrête \.\.\. peut\-être sans l'avoir trouvé</span>
  * <span style="color:#000000"> __Nombre de comparaisons = nombre de découpages en 2__ </span>
  * <span style="color:#000000">Nombre </span>  _maximal_  <span style="color:#000000"> de comparaisons = nombre de découpages en 2 jusqu'à l'arrêt "avec absence" \(pire cas\)</span>

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Combien de découpages par 2 de n valeurs jusqu'à en obtenir 1 seule ?

* La réponse : log2\(n\)
* Le principe : partons de  _n = 2_  _p_
  * \- division  _1_   2p / 2 = 2 <span style="color:#ED7D31">p\-1</span>
  * \- division  <span style="color:#ED7D31">2</span>   2p\-1 / 2 = 2 <span style="color:#ED7D31">p\-2</span>
  * \- \.\.\.
  * \- division  <span style="color:#ED7D31">k</span>   2p\-k\+1 / 2 = 2 <span style="color:#ED7D31">p\-k          </span>  <span style="color:#000000">\(la propriété à prouver par récurrence\)</span>
  * \- \.\.\.
  * \- division  <span style="color:#ED7D31">p</span>   2p\-p\+1 / 2 = 2p\-p = 2 <span style="color:#ED7D31">0 </span>  <span style="color:#000000">= 1</span>
* <span style="color:#000000">Il faut </span>  _p_  <span style="color:#000000"> divisions par 2 pour passer de 2</span>  <span style="color:#000000">p</span>  <span style="color:#000000"> à 1 </span>
* <span style="color:#000000">et </span>  <span style="color:#70AD47"> __p__ </span>  _ = log_  _2_  _\(2_  _p_  _\) = _  <span style="color:#70AD47"> __log__ </span>  <span style="color:#70AD47"> __2__ </span>  <span style="color:#70AD47"> __\(n\)__ </span>
  * C rech\. dichotomique\(n\) =   log2\(n\)    ou : k x log2\(n\) = k' x log10\(n\) = k" x ln\(n\)\,  ou plus tard O\(log\(n\)\)
* La recherche dichotomique : exemple de  _complexité logarithmique_
* <span style="color:#000000">Les algorithmes issus de stratégie </span>  _"diviser pour régner" _  _\(_  _divide_  _ and _  _conquer_  _\)_   <span style="color:#000000">introduisent des complexités en log : log\(n\) ou </span>  <span style="color:#000000">n\.log</span>  <span style="color:#000000">\(n\) ou \.\.\.  </span>

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Réduire la complexité ?

  * _Diviser pour régner _ ou  _divide_  _ and _  _conquer_
    * \- principe général basé sur la  _récursivité_
    * \- réduire le problème en un problème  _similaire_  ET de  _taille réduite _ \.\.\.
    * \.\.\. recommencer cette réduction \.\.\.\.
    * \.\.\. jusqu'à obtenir un problème suffisamment petit pour pouvoir trouver sa 		solution 	"immédiatement"\,
    * à partir de cette solution\, construire la solution du problème plus grand \.\.\.
    * \.\.\. et ainsi de suite jusqu'à obtenir la solution du problème de départ
    * \- principe présent dans la recherche dichotomique \!

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# (*) Compléments

Produit de deux entiers

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Un petit zoom sur le produit de 2 entiers

* Problème : multiplier 2 entiers de n chiffres \(en base 10\)
* Mesure : nombre de multiplications "chiffre à chiffre"
* Algorithme \(dit\) naïf de multiplication :
  * A la main \.\.\. pour sentir la réponse
  * chaque chiffre d'un opérande \(y'en a n\) est multiplié par chaque chiffre de l'autre opérande \(y'en a aussi n\) donc au total : n x n =  <span style="color:#ED7D31">n</span>  <span style="color:#ED7D31">2 </span>  <span style="color:#ED7D31">multiplications "chiffre à chiffre"</span>

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# La multiplication naïve est quadratique

* Décompte des opérations :
  * \- une multiplication 1 chiffre x 3 chiffres = 3 multiplications \(\+ 2 additions\)
  * \- on en fait 3\,  soit 9 multiplications \(\+ 6 additions\)
  * \- et on somme les 3\, soit 9 multiplications \(et 8 additions\)
* et ce pour la multiplication de 2 nombres à 3 chiffres :
* _on a bien effectué 3_  _2_  _ = 9 multiplications _
* Remarque : on ne compte pas les multiplications par les puissances de la base : 1\, 10\, 100\, \.\.\.
* ni les additions des produits partiels

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité quadratique du produit de 2 entiers

* <span style="color:#ED7D31">Analyse :</span>  <span style="color:#000000"> </span> formalisons le produit a x b  _en base 10_     ICI :  _n\+1_  chiffres

Comptons les produits partiels \(les x\) :  _\(n\+1\)_  _2_

\- formule développée :

1 \+ 2 \+ 3 \+ \.\.\. \+ \(k\+1\) \+ \.\.\.\+ n \+  _n\+1_  \+ n \+ \(n\-1\) \+ \(n\-2\) \+ \.\.\. \+ 2 \+ 1  = \(n\(n\+1\)/2\)x2 \+\( _n\+1_ \)

\- algorithme :  a et b ont n\+1 chiffres\, chaque chiffre de b est multiplié par les \(n\+1\) chiffres de a

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Réduire la complexité ?

* Problème : multiplier 2 entiers de n chiffres \(en base 10\)
* Mesure : nombre de multiplications "chiffre à chiffre"
* Algorithme naïf de multiplication :  <span style="color:#ED7D31">complexité quadratique</span>
  * n2 multiplications "chiffre à chiffre"
* _Existe\-t\-il un algorithme d'une complexité inférieure à n_  _2 _  _qui calcule le produit de 2 entiers ?_
* _Algorithme de _  _Karatsuba_  _ _  <span style="color:#000000">\(1960\) : complexité en </span>
  * si n = 1000 :
  * \- multiplication naïve = 1 000 000 produits
  * \- multiplication de Karatsuba =  50 000 produits\, soit  _20 fois plus rapide \!\!\!_
  *  Sera présenté en exercice sur la récursivité \!

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Un petit zoom sur le produit de 2 entiers

* _Remarques pour finir _
* \- Démarche similaire en base 2 :
* \- Algorithme naïf de multiplication :
* produit par la base = décalage d'un chiffre/bit vers la gauche
* produit axb : suite d'additions \(de prod\. ch\. à ch\.\) et de décalages
  * <span style="color:#ED7D31">	</span>  <span style="color:#000000">similaire</span>  <span style="color:#ED7D31"> </span>  <span style="color:#000000">au</span>  <span style="color:#ED7D31"> </span> produit de polynômes
* <span style="color:#000000">\- Algorithmes rapide \(</span>  <span style="color:#000000">Karatsuba</span>  <span style="color:#000000">\)</span>
  * <span style="color:#000000">entier sur machine = 64 bits et produit effectué "en" matériel </span>
  * <span style="color:#000000">intérêt de </span>  <span style="color:#000000">Karatsuba</span>  <span style="color:#000000"> : multiplier des grands entiers : N = n0 \+ n1 \+ \.\.\.</span>
  * <span style="color:#000000">GMP :</span>
  * <span style="color:#000000">[https://gmplib\.org/](https://gmplib.org/)</span>
  * <span style="color:#000000">sage \(python\)</span>
  * <span style="color:#000000">http://</span>  <span style="color:#000000">www\.sagemath\.org</span>  <span style="color:#000000">/</span>  <span style="color:#000000">fr</span>  <span style="color:#000000">/</span>

![](img/4-complexite5.tiff)

![](img/4-complexite6.png)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité asymptotique

Notations de Landau :

![](img/4-complexite7.tiff)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité en temps

* Ce qui importe : c'est  _l'ordre de grandeur _ du coût mesuré comme une fonction de la taille du problème\, quelque soit l'instance du pb\.
* Ce qui parle :  c'est le  _surcoût de temps pour résoudre un problème deux fois plus gros\, dix fois plus gros \! _
  * 10 fois plus gros avec une complexité :
  * cubique = 1000 fois plus long
  * quadratique = 100 fois plus long
  * linéaire = 10 fois plus long \.\.\. à la rigueur
  * racine carrée = environ 3 fois plus long  \.\.\. oui \!
  * logarithmique = 2 fois plus long  \.\.\. oui : je veux \!
  * exponentiel = 1010 fois plus long  \.\.\. aie aie aie : trop cher pour moi  \!\!\!\!

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité asymptotique

* Formaliser pour pour dégager les tendances asymptotiques
  * \-  <span style="color:#ED7D31">au pire </span>  <span style="color:#ED7D31"> __aussi __ </span> rapide <span style="color:#ED7D31"> __ __ </span> qu'un algorithme quadratique ?
  * \-  <span style="color:#ED7D31">au pire </span>  <span style="color:#ED7D31"> __au moins __ </span>  _aussi_  rapide qu'un algorithme quadratique ?
  * \-  <span style="color:#ED7D31">au pire </span>  <span style="color:#ED7D31"> __au plus __ </span>  _aussi_  rapide qu'un algorithme quadratique ?
* Comparaison asymptotique de fonctions et  _notations de Landau_
  * \-  _équivalent_  asymptotique :
  * \-  _minorant_  asymptotique :
  * \-  _majorant asymptotique_  __ __ :

![](img/4-complexite8.tiff)

![](img/4-complexite9.tiff)

![](img/4-complexite10.jpg)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Notations de Landau

![](img/4-complexite11.jpg)

![](img/4-complexite12.tiff)

![](img/4-complexite13.tiff)

![](img/4-complexite14.tiff)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Analyse asymptotique

Vocabulaire

f = O\(g\) :   _f est dominée asymptotiquement par g_

_Propriétés_

transitivité : f = O\(g\) et g = O\(h\) alors f = O\(h\)

invariance par multiplication : si f=O\(g\) alors k\.f = O\(g\) pour k>0

addition : f1 = O\(g1\) et f2 = O\(g2\)  alors f1\+ f2 = O\(g1\+g2\)

multiplication : f1 = O\(g1\) et f2 = O\(g2\)  alors f1x f2 = O\(g1xg2\)

_Majoration asymptotique O\( \.\) _ est  _la plus utile _ en pratique

l’analyse de complexité \(décompte\) conduit généralement à des majorations

majoration pertinente pour le pire cas

_Attention aux constantes cachées_

ces bornes asymptotiques cachent des constantes multiplicatives qui peuvent « faire la différence » entre 2 algorithmes de même complexité asymptotique

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexités asymptotiques

| Notation | Dénomination | Temps <br />pour n = 106 et 1GHz | Commentaires |
| :-: | :-: | :-: | :-: |
| O(1) | temps constant | 1 ns | rare |
| O(log n) | logarithmique | 10 ns | instantané ou presque.<br />il y a une constante cachée et du log2 en pratique |
| O(n) | linéaire | 1000 ns = 1 ms | sera supérieur à 1 min pour des tailles de pb comparables aux taille de RAM actuelles. Donc pb prédominant = gestion de la mémoire |
| O(n2) | quadratique | ¼ h  | ne pas dépasser n = 106 |
| O(nk) | polynomiale | k= 3  30 ans  | et pourtant on en rencontre souvent |
| O(2n) | exponentielle | plus de 10300 000 milliards d’années | algorithme inutilisable en pratique sauf pour des tout petits problèmes : n < 50 <br /> |

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Graphiquement

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Exprimer les complexités asymptotiques des itérations et récursions

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité d’algorithme itératif

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Itérations classiques

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Complexité d’algorithme récursif

* Fonction de complexité = relation de récurrence
* __Exemples__
* factorielle :  _C\(n\) = C\(n\-1\) \+ 1 _
  * l’appel récursif à fact\(n\-1\) :   _C\(n\-1\) _
  * 1 multiplication : 1
  * \(la comparaison : 1\)
* _et C\(0\) = 1_
* exponentiation classique :  _C\(n\) = C\(n\-1\) \+ 1_  et  _C\(0\) = 1_
* Exprimer  __C\(n\) sous forme non récursive __ par éliminations successives :
* _C\(n\) 	= 	C\(n\-1\) \+ 1 _
* _C\(n\-1\) 	= 	C\(n\-2\) \+ 1 _
* _C\(n\-2\) 	= 	_  _…_
* _…_  _\._
* _C\(2\) 	= 	C\(1\) \+ 1_
* _C\(1\) 	= 	C\(0\) \+ 1_
* _C\(0\) 	= 	1_
* _\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-_
* _C\(n\) 	= 	1 \+ 1 \+ _  _…_  _ \+ 1 = n \+ 1_
* __Conclusion __
* \- récurrence :  _C\(n\) = C\(n\-1\) \+ 1 _ et  _C\(0\) = 1  _  _ C\(n\) = n\+1_
* \- complexité asymptotique : complexité linéaire \(déjà vue\)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

* Récursions dichotomiques :  _C\(n\) fonction de C\(n/2\) _ et apparition de log2
* _C\(n\) = C\(_  <span style="color:#FF0000"> _n/2_ </span>  _\) \+ b _
  * exemples : exponentiation rapide\, élimination de la moitié des valeurs en temps constant\, recherche dichotomique
  * cas _ logarithmique _  _: C\(n\) = C\(1\) \+ b _  _x_  _ log_  _2_  _\(n\) = _  _O\(log\(n\)\)_
* _C\(n\) = C\(n/2\) _  <span style="color:#FF0000"> _\+ n_ </span>  _ _
  * exemples : traitement linéaire avant appel récursif dichotomique
  * cas  _linéaire_   _: C\(n\) = _  _O\(n\)_
* _C\(n\) = _  <span style="color:#FF0000"> _2_ </span>  _ C\(n/2\) _  <span style="color:#FF0000"> _\+ a _ </span>  <span style="color:#FF0000"> _x _ </span>  <span style="color:#FF0000"> _n _ </span>  _\+ b\, a ≠ 1 _
  * exemples : traitement linéaire avant 2 appels récursifs dichotomiques\, tri fusion
  * cas _ semi\-logarithmique _  _: _  _C\(n\) = _  _O\(_  _n\.log_  _\(n\)\)_
* _C\(n\) = _  <span style="color:#FF0000"> _a _ </span>  <span style="color:#FF0000"> _x_ </span>  <span style="color:#FF0000"> _ _ </span>  _C\(n/2\) \+ b\, a ≠ 1 _
  * exemples : répéter  _a_  fois l’appel récursif dichotomique
  * cas  _polynomial_   _: C\(n\) = _  _O\(n_  _log_  _2_  _ a_  _\)_

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Synthèse

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Analyse de complexité : avoir les idées claires

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Analyse de complexité : compléments

* _Pourquoi vouloir réduire la complexité ?_
  * \- pour résoudre des gros problèmes
  * \- mais aussi des problèmes pas nécessairement gros mais compliqués
  * __\- Il existe de nombreux problèmes qu'on se sait pas résoudre exactement en un temps réaliste\, souvent des problèmes d’optimisation : min\, max\, le plus court\, \.\.\.__
    * complexité exponentielle : 2n  problème du sac à dos \(force brute\)
    * complexité factorielle : n\!   problème du voyageur de commerce \(naïf\)
    * en pratique \(source wikipedia\, temps de base = 10 nanosec\)
      * exponentielle : pour n = 50\, temps T = 130 jours\,
      * pour n= 250 =  _10_  _59_  _ ans_
      * factorielle :	 pour n = 50\, temps T =  <span style="color:#ED7D31">10</span>  <span style="color:#ED7D31">48</span>  <span style="color:#ED7D31"> ans</span>
  * _P_  _ertinence pratique du modèle utilisé et de l’analyse menée ?_
  * \- modèle simple  _vs\._  exécution machine complexe
  * \- lecture\-écriture mémoire : tout sauf du temps constant\, compliqué
  * \- opération arithmétique : addition  _vs\._  division\, entier  _vs\._  flottant
  * \- exécution séquentielle des instructions : ça n'existe plus \-\- ou presque plus
    * les machines actuelles exécutent plusieurs instructions en parallèle\, dans un ordre différent du programme\, elles spéculent sur le résultats de tests ou d'accès mémoire \.\.\.
  * __les estimations asymptotiques \(grande taille du __  __pb__  __\) masquent ces effets__
  * demain : calcul quantique ?

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Analyse de complexité

* Une sensibilisation à une première notion d’informatique théorique
  * nos « petits » objectifs :
    * mieux comprendre l’efficacité d’un algorithme
    * estimer les effets de la taille d'un problème sur le temps de résolution
  * \- théorie de la complexité : une branche de l'informatique
  * \- objectif : classer les problèmes selon leurs difficultés de résolution\, \(cad\. le coût de leur résolution  _quelque soit l'algorithme _ utilisé\) et les relations entre ces classes de problèmes
  * \- modèles d'exécution : RAM \(ici\, Random Access Memory\)\, machines de Turing \("dites" déterministes ou non déterministes\)\, automates\, \.\.\.
* Autres aspects théoriques à voir ce semestre :
  * \- terminaison\, correction et preuves

Algo 2\. L1 math\-info\. UPVD\. \(PhL\)

# Tableau 1D :exemples de traitement et de complexités

# Des algorithmes d'évaluation polynomiale

# Plan et objectifs

* L'évaluation polynomiale
  * des additions et des multiplications répétées
  * des coefficients à stocker dans un tableau 1D
* Deux algorithmes d'évaluation
  * évaluation classique
  * évaluation de Horner
* Analyse de la complexité des deux algorithmes
  * l'évaluation classique peut\-être quadratique
  * l'évaluation de Horner est linéaire



Algo 2\. L1 math\-info\. PhL \(2020\)

# Rappels : les vecteurs de nombres

* Les vecteurs de nombres
  * nombres : entier\, flottants\, \(booléens ou bits\)
  * vecteurs : ensemble de ces valeurs
  * opérations arithmétiques ou logiques : \+\, \-\, x\, /\, ÷\, %\, AND\, OR\, XOR
  * une relation d'ordre : > ou >=



Algo 2\. L1 math\-info\. PhL \(2020\)

# Rappels : parcourir tout le tableau

* Exemples
  * \- les calculs arithmétiques ou statistiques des valeurs stockées dans le tableau : max/min\, somme/norme\, moyenne/écart type\, médiane\, \.\.\.
  * \- évaluation polynomiale : les coefficients sont stockés dans le tableau
  * \- bientôt : le tri des valeurs\, par ordre\, par signe\, \.\.\.
* Mise en œuvre d'un parcours complet
  * \- la boucle  _for _ sur les indices du tableau
  * écriture équivalente avec boucle :
  * _while_  _ _  _\+ initialisation indice \+ incrément indice \+ condition d'arrêt_



Algo 2\. L1 math\-info\. PhL \(2020\)

# Evaluation d'un polynôme

* Données
  * un degré :  <span style="color:#ED7D31">n </span> ou  <span style="color:#ED7D31">deg</span>  <span style="color:#ED7D31"> </span>
  * un polynôme  _a _ défini par ses n\+1 coefficients numériques
  * stockés dans un tableau de  _longueur n\+1_  :  _a=\[a_  _0_  _\, a_  _1_  _\, \.\.\.\, a_  _n\-1_  _\, a_  _n_  _\]_  _ _
  * une valeur d'évaluation :  <span style="color:#ED7D31">x</span>
* Sortie : on veut calculer
  * y =  _a\(x\) = a_  _0_  _ \+ a_  _1_  _\*x \+ a_  _2_  _\*x_  _2_  _ \+ \.\.\. \+ a_  _n\-1_  _\*x_  _n\-1_  _ \+ a_  _n_  _\*_  _x_  _n_
* Traitement
  * algorithme classique :  on calcule l'expression précédente
      * \. \(\.\.\.\(\( a0 \+ a1\*x\) \+ a2\*x2\) \+ \.\.\. \) \+ an\-1\*xn\-1 \) \+ an\*xn\)
      * \. on répète : le calcul de xi\, le produit avec a\[i\] et accumulation dans l'ordre croissant des puissances de x
  * \- algorithme de Horner :
      * \.  <span style="color:#ED7D31">y = \(\(\(\(\( a</span>  <span style="color:#ED7D31">n</span>  <span style="color:#ED7D31">\*x  \+ a</span>  <span style="color:#ED7D31">n\-1</span>  <span style="color:#ED7D31">\) \*x \+ a</span>  <span style="color:#ED7D31">n\-2</span>  <span style="color:#ED7D31">\) \* x \+ \.\.\.\+ \(a</span>  <span style="color:#ED7D31">2</span>  <span style="color:#ED7D31">\*x \+ a</span>  <span style="color:#ED7D31">1</span>  <span style="color:#ED7D31">\) \*x \+ a</span>  <span style="color:#ED7D31">0</span>  <span style="color:#ED7D31"> </span>
      * \. écriture plus compliquée mais algorithme plus simple et plus efficace



Algo 2\. L1 math\-info\. PhL \(2020\)

# Deux algorithmes d'évaluation polynomiale

Algorithme classique

Algorithme de Horner



Algo 2\. L1 math\-info\. PhL \(2020\)

# Algorithme classique : étape 1

* On veut calculer xi = x\*x\*x\* \.\.\. \*x pour i = 0\, 1\, \.\.\.\, deg\.
  * si i=0\, x0 = 1		\- si i=3\, x3=x\*x\*x 	ou  _x_  _3_  _=x_  _2_  _\*x_
  * si i=1\, x1=x		\- pour i\, xi = x\*x\*\.\.\.\*x 	ou  <span style="color:#70AD47">x</span>  <span style="color:#70AD47">i</span>  <span style="color:#70AD47">=x</span>  <span style="color:#70AD47">i\-1</span>  <span style="color:#70AD47"> \* x</span>
  * si i=2\, x2=x\*x		\- et ainsi jusqu'à i=deg\.
* Solution 1 : on calcule x1\, x2\, x3 \.\.\. xi à chaque fois
* _xi= 1\.0_
* _	for j in range\(i\): 	_
* _		xi = xi \* x	_ \#  <span style="color:#A5A5A5">ici j==i et xi==x\*x\*\.\.\.\*x pour i=1\, 2\, 3 \.\.\.\.</span>
* Remarque : on ne calcule pas x0\, xi vaut directement 1\.0  quand i==0\.



Algo 2\. L1 math\-info\. PhL \(2020\)

Ensuite\, pour chaque i de 0 à deg :

on multiplie xi par a\[i\] et on accumule dans la valeur calculée à l'itération 	précédente\, dans l'ordre croissant des puissances de x \(xi\)

Avant la première itération\, la variable\-résultat est initialisée à 0 car on effectue une accumulation dans cette variable

_res_  _ = 0\.0_

_for i in range\(deg\+1\): 	_ \#  _on note _  _deg_  _ le degré du polynôme = taille du tableau \+1 _

\#  <span style="color:#ED7D31">l'étape 1 donne xi pour chaque i</span>

<span style="color:#4472C4">res</span>  <span style="color:#4472C4"> =  </span>  <span style="color:#4472C4">res</span>  <span style="color:#4472C4"> \+ a\[i\] \* xi	</span> \#  <span style="color:#A5A5A5">ici xi=x\*x\*\.\.\.\*x pour i=0\,1\, \.\.\.</span>

En supposant que "l'étape 1 fait bien son travail"\, on vérifie que cette boucle calcule bien :

a\[0\]  pour deg==0			 a\[0\] \+ a\[1\]\*x \+ a\[2\]\*x2  pour deg==2\, \.\.\.

a\[0\] \+ a\[1\]\*x pour deg==1		 a\[0\] \+ a\[1\]\*x \+ a\[2\]\*x2 \+ \.\.\. \+ a\[deg\]\*xdeg  pour deg



Algo 2\. L1 math\-info\. PhL \(2020\)

# Algorithme classique

def evalPoly\(a\, deg\, x\):

_\# Rôle : évalue le polynôme a de _  _degre_  _ _  _deg_  _ en x\._

_\# Les _  _coeff_  _ sont stockés dans le tableau a avec indice==degré_

res = 0\.0	 <span style="color:#A5A5A5">\# valeur de p\(x\) initialisée à 0</span>

xi  = 1\.0		 <span style="color:#A5A5A5">\# pour x\*x\*\.\.\.\*x = x</span>  <span style="color:#A5A5A5">i</span>

_	for i in range\(deg\+1\):_ 		 <span style="color:#70AD47">xi = 1\.0</span>

<span style="color:#70AD47">		for j in range\(</span>  _1_  <span style="color:#70AD47">\, </span>  <span style="color:#ED7D31"> __i\+1__ </span>  <span style="color:#70AD47">\):	</span>  <span style="color:#ED7D31">\# cette boucle n'est pas effectuée si i==0</span>

<span style="color:#70AD47">			xi = xi \* x		\# ici on a xi==x\*x\*\.\.\.\*x==x\*\*i</span>

<span style="color:#5B9BD5">res</span>  <span style="color:#5B9BD5"> = </span>  <span style="color:#5B9BD5">res</span>  <span style="color:#5B9BD5"> \+ a\[i\]\*xi	\# accumulation du terme de degré i \(a\[i\]\*xi\) 							\# pour i=0\, 1\, \.\.\.\, </span>  <span style="color:#5B9BD5">deg</span>

return res



Algo 2\. L1 math\-info\. PhL \(2020\)

# Remarques

* Version 1 :
  * deux boucles for imbriquées
  * imbriquée = l'indice de la boucle intérieure dépend de l'indice de la boucle extérieure
  * ici : la valeur d'arrêt de la boucle intérieure est modifiée à chaque itération de la boucle extérieure
  * ce genre d'imbrication est très classique mais piégeux au début
  * attention aussi aux initialisations
    * ici : xi est remis à  1\.0 à chaque nouvelle itération de la boucle extérieure
* Version 2 :
  * on peut éviter de recalculer "tout xi" à chaque fois\,  ce qui supprime la boucle for intérieure
  * à faire en exercice\. Quelles conséquences ? \(correction en fin de présentation\)



Algo 2\. L1 math\-info\. PhL \(2020\)

# Algorithme de Horner

* On va calculer :
* <span style="color:#ED7D31">	</span>  _y = \(\(\(\(\( a_  _n_  _\*x  \+ a_  _n\-1_  _\) \*x \+ a_  _n\-2_  _\) \* x \+ \.\.\.\+ \(a_  _2_  _\*x \+ a_  _1_  _\) \*x \+ a_  _0_  _ _
* <span style="color:#000000">Principe :</span>
    * On multiplie le résultat précédent par x\, on ajoute a\[i\] et on accumule dans une variable résultat\.
    * Cette accumulation s'effectue dans  _l'ordre des indices décroissants_
    * Comme on accumule\, la variable\-résultat est initialisée avec précaution :
      * elle vaut soit 1\.0 \(on fait un produit\)\, soit an au départ \(attention aux calculs qui suivent\)
* <span style="color:#000000">Remarques :</span>
  * écriture plus compliquée mais algorithme plus simple et plus efficace
  * on commence par les indices de degré élevé\, puis on décrémente
*  boucle for avec  _un pas négatif_
  * for i in range\(n\, \-1\, \-1\): 	\# n\, n\-1\, n\-2\, \.\.\.\, 2\, 1\,  <span style="color:#FF0000"> __0 __ </span>  <span style="color:#FF0000">\(d’où borne droite = \-1\) </span>
  * \.\.\.\.



Algo 2\. L1 math\-info\. PhL \(2020\)

def Horner\(a\, deg\, x\):

<span style="color:#A5A5A5">\# rôle : évalue le polynôme a en x par l'algorithme de </span>  <span style="color:#A5A5A5">Horner</span>  <span style="color:#A5A5A5">\. </span>

<span style="color:#A5A5A5">\# Les </span>  <span style="color:#A5A5A5">coeff</span>  <span style="color:#A5A5A5"> de a sont stockés dans le tableau a avec indice==degré</span>

res = a\[deg\]		 <span style="color:#A5A5A5">\# coefficient de plus haut degré</span>

for i in range\(deg \- 1\, \-1\, \-1\):

res = res \* x \+ a\[i\]	 <span style="color:#A5A5A5">\# accumulation de </span>  <span style="color:#A5A5A5">Horner</span>

return res



Algo 2\. L1 math\-info\. PhL \(2020\)

* On vérifie que sont successivement calculés
* \-  a\[0\] 							si deg==0
* a\[1\]\*x \+ a\[0\] 					si deg==1
* <span style="color:#ED7D31">\(</span> a\[2\]\*x \+ a\[1\] <span style="color:#ED7D31">\)</span>  \*x \+ a\[0\] 				si deg==2
* <span style="color:#ED7D31">\(</span>  _\(_ a\[3\]\*x \+a\[2\] <span style="color:#5B9BD5">\)</span>  \*x \+ a\[1\] <span style="color:#ED7D31">\)</span>  \*x \+ a\[0\] 		si deg==3
* \.\.\.
* _\(_ \( <span style="color:#5B9BD5">\(</span>  a\[n\] \*x \+a\[n\-1\] <span style="color:#5B9BD5">\)</span>  \*x \+ \.\.\. \) \* x \+ a\[1\] <span style="color:#ED7D31">\)</span>  \*x \+ a\[0\] si deg==n
* Remarque
  * \- noter l'initialisation de res par le coefficient de plus haut degré



Algo 2\. L1 math\-info\. PhL \(2020\)

# Application : appel

_\# rôle : évalue le polynôme \(x\+1\)_  _4_  _ par l'algorithme de _  _Horner_ \.

n = 4 						 <span style="color:#A5A5A5">\# degré</span>

pascal4\[ <span style="color:#ED7D31"> __5__ </span> \] = \[1\.\, 4\.\, 6\.\, 4\.\, 1\.\] 		 <span style="color:#A5A5A5">\# </span>  <span style="color:#A5A5A5">coeff</span>  <span style="color:#A5A5A5"> du poly </span>  _pascal4_

x = float\(input\("entrer valeur d'évaluation"\)\)	 <span style="color:#A5A5A5">\# entrée x</span>

y = Horner\(pascal4\,  _4_ \, x\)			\# appel : calcul

print\("\(x\+1\)\*\*4 en "\, x\, " vaut "\, y\)		 <span style="color:#A5A5A5">\# sortie</span>



Algo 2\. L1 math\-info\. PhL \(2020\)

# Analyse de la complexité

Comptons\, comptons \!



Algo 2\. L1 math\-info\. PhL \(2020\)

# Complexité de l'évaluation polynomiale

* Complexité en temps
  * est une fonction du degré n
  * est mesurée par le nombre d'opérations arithmétiques : \+\, \*
  * ces opérations apparaissent dans la/les boucles pour
  * on se concentre sur ces boucles
  * l'ordre de grandeur pour des grandes valeurs de n nous intéresse
* Rappel utile
  * 1\+2\+ \.\.\.\+ n = ?
  * somme des n premiers termes d'une suite arithmétique de raison 1 et de premier terme 1
  * 1\+2\+ \.\.\.\+ n = n\(n\+1\)/2
  * ordre de grandeur pour les grandes valeurs de n :  n\(n\+1\)/2 = n2/2 \+ \.\.\.
  * cette somme est croissante "comme x2" :
  * elle a une croissance \(asymptotique\)  <span style="color:#ED7D31">quadratique</span>



Algo 2\. L1 math\-info\. PhL \(2020\)

# Complexité de l'évaluation classique

* _for i in range\(deg\+1\):		// n == _  _deg_
* <span style="color:#70AD47">xi = 1\.0</span>
* <span style="color:#70AD47">	for j in range\(</span>  _1\, _  <span style="color:#ED7D31"> __i\+1__ </span>  <span style="color:#70AD47">\): 		// cette boucle n'est pas effectuée si i==0</span>
* <span style="color:#70AD47">		xi = xi \* x		</span>
* <span style="color:#5B9BD5">	</span>  <span style="color:#5B9BD5">res</span>  <span style="color:#5B9BD5"> = </span>  <span style="color:#5B9BD5">res</span>  <span style="color:#5B9BD5"> \+ a\[i\]\*xi			</span>
* Comptons \!
  * à  _chaque itération en i _ :  1 addition\, 1 multiplication par xi=xi
  * calcul naïf de  _x_  _i _  _ = x\*x\* \.\.\.\* x _
    * <span style="color:#70AD47"> i multiplications </span>  <span style="color:#70AD47"> __à chaque fois \.\.\. __ </span>
    * <span style="color:#70AD47"> __\-__ </span>  __ __ cad\. 0 puis 1 puis 2 \.\.\. puis n
  * total sur  <span style="color:#5B9BD5">n</span>  _\+1 itérations en i _ :
    * n\+1 additions
    * 1\+2\+ \.\.\. \+ n multiplications = n\(n\+1\)/2
  * total = \(n\+1\)\(n\+2\)/2 = n2/2 \+ \.\.\.
  * ordre de grandeur quadratique
    * évaluation quadratique en le nombre d'opérations arithmétiques
  * <span style="color:#ED7D31">deux boucles </span>  <span style="color:#ED7D31">for </span>  <span style="color:#ED7D31">imbriquées </span>  <span style="color:#ED7D31"> quadratique</span>



Algo 2\. L1 math\-info\. PhL \(2020\)

# Complexité de l'évaluation de Horner

* res = a\[deg\]
* _for i in range\(\(_  _deg_  _ \- 1\)\, \-1\, \-1\) : 	// si n==_  _deg_  _ alors n itérations_
* _	_  _res_  _ = _  _res_  _ \* x \+ a\[i\]_  _	_
* Comptons \!
  * \- à  _chaque itération _ : 	1 addition et 1 multiplication
  * total sur  _n_  _ itérations _ : 	n additions et n multiplications
  * total évaluation : 	2n opérations arithmétiques
  * évaluation linéaire en le nombre d'opérations arithmétiques
    * \. il a été montré que  _cet algorithme est optimal _ pour l'évaluation des polynômes à valeurs scalaire \(1D\) : Ostrowsky \(54\)\, Pan \(66\)
    * \. optimal = il n'existe pas d'algorithme moins coûteux
  * <span style="color:#ED7D31">une seule boucle </span>  <span style="color:#ED7D31">for </span>  <span style="color:#ED7D31"> complexité \(asymptotique\) linéaire</span>



Algo 2\. L1 math\-info\. PhL \(2020\)

# Conclusion



Algo 2\. L1 math\-info\. PhL \(2020\)

# Sur les algorithmes d'évaluation polynomiale

* L'évaluation polynomiale
  * des additions et des multiplications répétées
  * des coefficients à stocker dans un tableau 1D
* Deux \(trois\) algorithmes d'évaluation
  * évaluation classique : deux versions dont une naïve
  * évaluation de Horner : plus simple en fait \!
* Analyse de la complexité des deux algorithmes
  * l'évaluation de Horner est linéaire
  * l'évaluation classique naïve est quadratique donc plus coûteuse
* Morale
  * deux boucles pour imbriquées : coût quadratique
  * une seule boucle pour : coût linéaire



Algo 2\. L1 math\-info\. PhL \(2020\)

# Exercices

* Coder ces algorithmes :
* pour obtenir des jolis tracés d'évaluation de vos polynômes préférés
* pour mesurer leurs performances réelles
  * \. prendre des polynômes type \(x\-1\)n sous forme développée \(triangle de Pascal\, coefficients binomiaux\) pour faire varier facilement le degré des polynômes;
  * \. pour chaque degré n\, évaluer en un nombre important de points et faire la moyenne
  * \. rassembler ces mesures dans des courbes et comparer avec les résultats théoriques



Algo 2\. L1 math\-info\. PhL \(2020\)

# Supplément

On peut aussi écrire l'évaluation classique avec un algorithme linéaire



Algo 2\. L1 math\-info\. PhL \(2020\)

# Algorithme classique : version 2

On peut éviter de recalculer "tout xi" à chaque fois\,  ce qui supprime la boucle pour intérieure

def evalPolyEco\(a\, deg\, x\) :

_	\# rôle : évalue le polynôme a de _  _degre_  _ _  _deg_  _ en x\. _

_	\#Les _  _coeff_  _ sont stockés dans le tableau a avec indice = degré_

res =  _a\[0\]_ 		//  <span style="color:#A5A5A5">valeur de p\(x\) initialisée à a\[0\]</span>

xi =  __1\.0__ 		//  <span style="color:#A5A5A5">pour x\*x\*\.\.\.\*x = x</span>  <span style="color:#A5A5A5">i</span>

_	for i in range\(1\, deg\+1\): 	// _  _boucle non effectuée si i==0_

<span style="color:#70AD47">xi = xi \* x		// mise à jour de xi</span>

<span style="color:#70AD47">		</span>  <span style="color:#5B9BD5">res</span>  <span style="color:#5B9BD5"> = </span>  <span style="color:#5B9BD5">res</span>  <span style="color:#5B9BD5"> \+ a\[i\]\*xi	//accumulation du terme de degré i</span>

return res



Algo 2\. L1 math\-info\. PhL \(2020\)

On peut éviter de recalculer "tout xi" à chaque fois\,  ce qui supprime la boucle pour intérieure

Quid de sa complexité ?



Algo 2\. L1 math\-info\. PhL \(2020\)

