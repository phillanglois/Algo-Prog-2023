#!/usr/bin/env python
# coding: utf-8

# # Compétences 
# 
# version 2022, PhL.
# 
# Les compétences de cet enseignement sont rassemblées dans ce fichier pour vous aider à contrôler votre apprentissage tout au long du semestre.
# 

# In[1]:


# -*- coding : utf8 -*-
from typing import List


# ## Savoir faire et pré-requis technique
# 
# Dans/avec un notebook jupyter :
# 
# - savoir mettre en oeuvre de la programmation simple en python (niveau semestre 1) dans un notebook jupyter 
# - savoir documenter cette programmation (énoncés, descriptions, ...) avec markdown

# ## Fonctions
# 
# ### Avoir les idées claires
# 
# - reconnaître et utiliser une fonction prédéfinie ou existante
# - reconnaître et distinguer :
#     - définition et paramètres formels _vs._ appel et paramètres effectifs
#     - spécification, en-tête, signature : spécifier pour utiliser, pour vérifier  _vs._ corps : implémentation du traitement  
# - comprendre que appel = changement de contexte  
#     - trace de l'exécution _vs._ séquentialité des instructions écrites 
#     - dynamique vs. statique  
# - distinguer appelant _vs._ appelé : 
#     - le rôle de l'appel, 
#     - le rôle du `return` 
# - identifier la portée des variables : 
#     - variables locales _vs._ variables plus globales  
# - se souvenir que l'effet de bord est indésirable  
# 
# 
# ### Ce qu'il faut savoir faire 
# 
# **Cadre** : en/pour python 
# 
# - utiliser une fonction prédéfinie ou existante
# - définir et écrire la spécification d'une fonction qui réalise un traitement décrit en français, ou qui résoud un problème (simple) décrit en français  
# - définir et écrire des appels simples (tests unitaires) 
# - définir et écrire l'implémentation d'une fonction associée à une spécification 

# ## Boucles avancées
# 
# ### Avoir les idées claires
# 
# - Structure de données : représentation d'un tableau multidimensionnel comme une liste de listes  
# - Structure de contrôle de type boucles imbriquées indépendantes et dépendantes : 
#     - intérêt et exemples simples, 
#     - dénombrer les itérations de ces constructions.
# 
# ### Ce qu'il faut savoir faire 
# 
# **Cadre** : en/pour python 
# 
# - Définir et écrire un traitement classique de tableau multidimensionnel  : parcours simple, parcours conditionnel 
# - Ecrire une initialisation de tableau multidimensionnel en python (représenté par des listes)
# - Définir et écrire une spécification de fonction avec des paramètres de type tableau  
# - Identifier les cas particuliers liés à la structure de tableau : tableau de dimension 0, tableau vide

# ## Entrées-Sorties : fichiers
# 
# ### Avoir les idées claires
# 
# - Distinguer fichier logique _vs._ physique, texte _vs._ binaire, mode lecture _vs._ écriture (_vs._ lecture-écriture) 
# - Connaître les étapes de manipulation d'un fichier : association/ouverture/lecture-écriture/fermeture
# - Distinguer valeur (numérique) et sa représentation textuelle 
# 
# ### Savoir-faire
# 
# - Savoir écrire les lectures-écritures simples de fichier texte avec les instructions python adaptées  
# - Comprendre et gérer l'effet des caractères spéciaux 

# ## Complexité
# 
# ### Avoir les idées claires
# 
# - Principes de l'analyse de la complexité en temps : modèle de calcul RAM, paramètres de complexité, meilleur et pire cas
# - Complexité asymptotique : notations de Landau, principales classes de complexité des algorithmes, interprétation pratique de ces classes
# - Complexité, pires et meilleurs cas des algorithmes vus ce semestre
# - Savoir établir la complexité d'algorithmes itératifs simples ou récursifs terminaux.
# 
# 
# ### Savoir-faire
# 
# - Exemples d'algorithme des principales classes de complexité 
# - Savoir identifier (sans nécessairement le prouver) la complexité, les meilleur-pire cas d'un algorithme  

# ## Types composés
# 
# ### Avoir les idées claires
# 
# voir cours 
# 
# ### Savoir-faire
# 
# voir cours

# ## Récursivité
# 
# ### Avoir les idées claires
# 
# - Savoir conduire une approche diviser pour régner et en déduire une solution récursive : application à des exemples calculatoires simples (factorielles, exponentiation entière, exponentiation rapide)
# - Savoir identifier la (ou les) terminaison, la récursions et l'initialisation d'un traitement avec un algorithme récursif : application à des exemples simples (factorielles, exponentiation entière, exponentiation rapide)
# - 
# 
# ### Savoir-faire
# 
# - Savoir écrire sous la forme d'une fonction de même signature les versions itérative et récursive d'un traitement calculatoire simple
# - Construire la pile des appels et son évolution lors d'un traitement récursif
# 
# 

# ## Entrées-Sorties : aspects avancés
# 
# ### Avoir les idées claires
# 
# - Connaitre les principes du formatage des données pour pouvoir retrouver rapidement dans la documentation (de cours ou de référence) les commandes pour effectuer ce traitement.
# 
# ### Savoir-faire
# 
# - Utiliser les formatages de base des types `int` et `float` de python
# - En s'appuyant sur les documents de cours ou de référence, définir et appliquer des formatages évolués et adaptés aux données manipulées avec python

# ## Rechercher
# 
# ### Avoir les idées claires
# 
# - Connaître les principes des formes itératives et récursives des algorithmes de recherche fondamentaux (recherche séquentielle, recherche dichotomique) 
# - Savoir conduire une approche diviser pour régner et en déduire une solution récursive pour le problème de la recherche d'une valeur dans un ensemble ou des problèmes similaires.
# - Savoir identifier la (ou les) terminaison, la récursions et l'initialisation d'une recherche de valeur (ou problème similaire) avec un algorithme récursif
# - 
# 
# ### Savoir-faire
# 
# - Savoir écrire sous la forme d'une fonction de même signature les versions itérative et récursive d'un algorithme de recherche de valeur dans un ensemble
# - Savoir écrire des tests unitaires pertinents pour ces traitements  

# ## Des QCM et autres sites à exploiter
# 
# Le net est riche de ressources à exploiter. 
# En voici quelques-unes sélectionnées et à exploiter en plus de ceux proposés à chaque fin de chapitre.
# 
# - [Site](https://www.bernon.fr/index.php?page=exercice-banque-e3c-thème-a) de M. Bernon : QCMs interactifs issus de la banque de données des E3C  
# 
# - [Site](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python_function) de Fabrice Sincere (lien sur le qcm sur les fonctions) 
# 
# - Fonctions, Objectif 20 : [France IOI]
# (http://www.france-ioi.org/algo/chapter.php?idChapter=509)
# 

# In[ ]:




