# Compétences 

Mis à jour : {sub-ref}`today`, lecture : {sub-ref}`wordcount-minutes`
minutes minimum, PhL.

Les compétences de cet enseignement sont rassemblées dans ce fichier pour vous aider à contrôler votre apprentissage au long du semestre.

Les aspects signalés avec une ($\star$) relèvent plutôt d'un objectif (d'apprentissage niveau) 20. 


## Savoir faire et pré-requis technique

Dans/avec un notebook jupyter :

- savoir mettre en oeuvre de la programmation simple en python (niveau semestre 1) dans un notebook jupyter 
- savoir documenter cette programmation (énoncés, descriptions, ...) avec markdown

## Fonctions

### Avoir les idées claires

- reconnaître et utiliser une fonction prédéfinie ou existante
- reconnaître et distinguer :
    - définition et paramètres formels _vs._ appel et paramètres effectifs
    - spécification, en-tête, signature : spécifier pour utiliser, pour vérifier  _vs._ corps : implémentation du traitement  
- comprendre que appel = changement de contexte  
    - trace de l'exécution _vs._ séquentialité des instructions écrites 
    - dynamique vs. statique  
- distinguer appelant _vs._ appelé : 
    - le rôle de l'appel, 
    - le rôle du `return` 
- identifier la portée des variables : 
    - variables locales _vs._ variables plus globales  
- se souvenir que l'effet de bord est indésirable  


### Ce qu'il faut savoir faire 

**Cadre** : en/pour python 

- utiliser une fonction prédéfinie ou existante
- définir et écrire la spécification d'une fonction qui réalise un traitement décrit en français, ou qui résoud un problème (simple) décrit en français  
- définir et écrire des appels simples (tests unitaires) 
- définir et écrire l'implémentation d'une fonction associée à une spécification 

## Boucles avancées

### Avoir les idées claires

- Structure de données : représentation d'un tableau multidimensionnel comme une liste de listes  
- Structure de contrôle de type boucles imbriquées indépendantes et dépendantes : 
    - intérêt et exemples simples, 
    - dénombrer les itérations de ces constructions.

### Ce qu'il faut savoir faire 

**Cadre** : en/pour python 

- Définir et écrire un traitement classique de tableau multidimensionnel  : parcours simple, parcours conditionnel 
- Ecrire une initialisation de tableau multidimensionnel en python (représenté par des listes)
- Définir et écrire une spécification de fonction avec des paramètres de type tableau  
- Identifier les cas particuliers liés à la structure de tableau : tableau de dimension 0, tableau vide

## Entrées-Sorties simples avec des fichiers

### Avoir les idées claires

- Distinguer fichier logique _vs._ physique, texte _vs._ binaire, mode lecture _vs._ écriture (_vs._ lecture-écriture) 
- Connaître les 4 étapes de manipulation d'un fichier : association/ouverture/lecture-écriture/fermeture
- Distinguer représentation textuelle et valeur (numérique)   


### Savoir-faire

- Savoir écrire les lectures-écritures simples de fichier texte avec `.readline()`, `.read()` et `.write()`
- Comprendre et gérer l'effet des caractères spéciaux 
- ($\star $) Savoir écrire les lectures-écritures de fichiers texte avec les instructions python adaptées   


## Complexité

### Avoir les idées claires

- Connaître le principes de l'analyse de la complexité en temps : modèle de calcul, mesure et paramètre de la complexité, meilleur et pire cas
- Savoir exprimer et exploiter une complexité asymptotique : notations de Landau, principales classes de complexité des algorithmes, interprétation pratique de ces classes
- Savoir établir la complexité d'algorithmes itératifs simples ou récursifs terminaux (algorithmes étudiés en cours)

### Savoir-faire

- Connaître des exemples significatifs d'algorithmes de complexité polynomiale et logarithmique (complexité, pires et meilleurs cas)  
- Savoir identifier (sans nécessairement le prouver) la complexité, les meilleur-pire cas d'un algorithme  


## Récursivité

### Avoir les idées claires

- Savoir conduire une approche diviser pour régner et en déduire une solution récursive : application à des exemples calculatoires simples (factorielles, exponentiation entière, exponentiation rapide)
- Savoir identifier la (ou les) terminaison, la récursion et l'initialisation d'un traitement avec un algorithme récursif : application à des exemples simples (factorielles, exponentiation entière, exponentiation rapide)


### Savoir-faire

- Savoir écrire sous la forme d'une fonction de même signature les versions itérative et récursive d'un traitement calculatoire simple
- Construire la pile des appels et son évolution lors d'un traitement récursif

## Rechercher

### Avoir les idées claires

- Connaître les principes des formes itératives et récursives des algorithmes de recherche fondamentaux : recherche séquentielle, recherche dichotomique.
- Savoir conduire une approche diviser pour régner et en déduire une solution récursive pour le problème de la recherche d'une valeur dans un ensemble ou des problèmes similaires.
- Savoir identifier la (ou les) terminaison, la récursion et l'initialisation d'une recherche de valeur (ou problème similaire) avec un algorithme récursif
 
### Savoir-faire

- Savoir écrire sous la forme d'une fonction de même signature les versions itérative et récursive d'un algorithme de recherche de valeur dans un ensemble
- Savoir écrire des tests unitaires pertinents pour ces traitements  

## Trier

### Avoir les idées claires

- Connaître, reconnaître et savoir classifier les algorithmes de tri selon leurs caractéristiques (tris en place, par comparaisons, quadratiques/rapides/linéaires) 
- Comprendre les algorithmes de tri insertion, _quicksort_ et fusion grâce à leur invariant
- Savoir identifier les pires et meilleurs cas des tris insertion, _quicksort_ et fusion

 
### Savoir-faire

- Savoir écrire des traitements récursifs en place de tableaux (indices \[g, d \[)
- Savoir écrire les tris insertion, quicksort et fusion sous une forme simple (itérative vs. récursive)
- Savoir écrire des tests unitaires pertinents pour ces traitements  

## Types composés

### Avoir les idées claires

Distinguer les  caractéristiques des structures de données (SD) _tuple_, _liste_, _dictionnaire_, _ensemble_ et _chaîne de caractères_ -- aussi appelés type composé ou conteneur en python
 
- pour représenter, stocker les données et effectuer les traitements adaptés au problème  
- pour effectuer l'accès aux valeurs, le parcours (séquences, itérateur), et la modification ou la copie (mutabilité) de ces SD.
- ($\star$) Connaître les complexités de ces traitements 


### Savoir faire

- Connaître la syntaxe python de définition et manipulation de ces SD
- Créer des listes et dictionnaires en compréhension
- Connaître les méthodes (prédéfinies) utiles au traitement, en particulier des chaînes de caractères 
- Définir des spécifications de fonctions avec un ou des paramètres de type composé

## Sous programmes et affectations : aspects avancés

### Avoir les idées claires 

- Les principes du passage de paramètres appelant <-> appelé   
    * "matériel" : par valeur _vs._ par adresse
    * logique : in _vs._ out _vs._ inout
    * aide : différencier fonction _vs._ procédure 
- L'effet de bord est néfaste 
    - possible pour le passage par adresse, et les variables globales (à proscrire)
- L'affectation et le passage de paramètres **en python**
    - pas de surprise pour les non-mutables (= variables locales)  
    - **attention aux mutables** : danger d'effet de bord _si modification partielle_ 
    - ne pas prendre de risque : `return` dans la fonction et affectation dans l'appelant 
    
 
### Savoir-faire en python 
    
- Fonctions avec arguments nommés, avec paramètres par défaut.
- ($\star$) Affectation en python   
    - non-mutables : (référence à) la valeur
    - mutables : (référence à) l'adresse
    - attention aux mutables  : 
        modification partielles _vs._ duplication (par `copy.copy` ou par "tranches complètes") 
    - penser "objet" aide pour le comportement des mutables
- ($\star$) Fonction et passage d'argument appelant/appelé en python : 
    - similaire à l'affectation : distinguer mutable _vs._ non mutable  
- ($\star$) Savoir effectuer des introspections (fonction `id()`)

## Entrées-Sorties : aspects avancés

### Avoir les idées claires

- Connaître les principes du formatage des données pour pouvoir retrouver rapidement dans la documentation (de cours ou de référence) les commandes pour effectuer ce traitement.

### Savoir-faire

- Utiliser les formatages de base des types `int` et `float` de python
- En s'appuyant sur les documents de cours ou de référence, définir et appliquer des formatages évolués et adaptés aux données manipulées avec python


## Modules utiles

### Avoir les idées claires

- Pouvoir définir une stratégie de tests avec un part d'aléatoire bien choisie
- Pouvoir définir une stratégie de mesure des temps de traitements, être conscient de la difficulté de la fiabilité de ce type de mesures 

### Savoir-faire

- Savoir générer de l'aléa avec le module `random`
- Savoir utiliser le module `matplotlib` pour créer des tracés graphiques pertinents
- Savoir mesurer des temps d'exécution à l'aide du module  `time` 
- Savoir rechercher et (re)trouver dans la documentation de ces modules


## Des QCM et autres sites à exploiter

Le net est riche de ressources à exploiter. 
En voici quelques-unes sélectionnées et à exploiter en plus de ceux proposés à chaque fin de chapitre.

- [Site](https://www.bernon.fr/index.php?page=exercice-banque-e3c-thème-a) de M. Bernon : QCMs interactifs issus de la banque de données des E3C  

- [Site](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python_function) de Fabrice Sincere (lien sur le qcm sur les fonctions) 

- Fonctions, Objectif 20 : [France IOI]
(http://www.france-ioi.org/algo/chapter.php?idChapter=509)

