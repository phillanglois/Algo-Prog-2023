#!/usr/bin/env python
# coding: utf-8

# (td:td2)=
# # Feuille 2
# 
# :::{note}
# 
# Feuille téléchargeable au format jupyter notebook (`.ipynb`) 
# 
# :::
# - Le symbole $\blacksquare$ indique les exercices ou questions obligatoires. Commencez pas ceux-là.
# - Les symboles $\star$ et $\star\star$ indiquent les exercices ou questions de difficulté relative plus importante.

# **Focus**
# 
# -   tableaux 1D et chaînes de caractères
# -   Fonctions avec arguments de ces types
# 
# 
# **Compétences**
# 
# - utiliser une fonction prédéfinie ou existante
# - définir et écrire la spécification d'une fonction qui réalise un traitement décrit en français, ou qui résout un problème (simple) décrit en français  
# - définir et écrire des appels simples (tests unitaires) 
# - définir et écrire l'implémentation d'une fonction associée à une spécification 
# 
# **Rappel de quelques consignes**
# 
# - Relire celles de la [feuille 1](td:td1)
# - Les fonctions avec un ou plusieurs arguments de type tableau (`lst`,
# `str`) doivent expliciter la (ou les) _dimensions_ de chacun de ces
# arguments tableaux à l'aide des arguments supplémentaires nécessaires.
# 
# Exemple.
# ```python
# def sommer(t : List[float], n : int) -> float: 
#     '''retourne la somme les valeurs du tableau t 
#     de valeurs flottantes et de dimension n'''
# ```

# ## Objectif 10

# (exo:tablst)=
# ### $\blacksquare$ Exercice
# 
# Soit `t` un tableau 1D
# d'entiers de taille `n` arbitraire. Voici quelques traitements
# classiques de ces tableaux et les fonctions associées.
# 
# 1.  `max()` qui calcule et retourne la valeur maximale d'un tableau 1D.
# 
# 2.  `max_ind_max()` qui calcule et retourne le plus grand indice de la
#     valeur maximale d'un tableau 1D.
# 
# 3.  `min_ind_max()` : une modification de la fonction précédente qui
#     calcule et retourne le plus petit indice de la valeur maximale d'un
#     tableau 1D.
# 
# 4.  `est_dans()` qui retourne un booléen indiquant si une valeur fournie
#     en argument est présente ou non dans le tableau.
# 
# 5.  `nb_occ()` qui calcule et retourne le nombre d'occurrences d'une
#     valeur donnée à partir d'un indice donné.
# 
#     -   Proposer une fonction unique telle que le nombre d'occurrences
#         d'une valeur donnée dans le tableau complet soit calculé et
#         retourné par un appel au nombre minimal de paramètres.
# 
# 6.  `nb_occ_max()` qui calcule et retourne le nombre d'occurrences de la
#     valeur maximale d'un tableau.
# 
# Pour chacune de ces fonctions, deux questions.
# 
# 1.   Proposer des solutions itératives alternatives (`for` vs.
#     `while`) lorsque qu'elles conduisent à des traitements différents.
# 
# 2.  Tests unitaires : expliciter différents tableaux `t` qui
#     correspondent, le cas échéant, à des cas particuliers de traitement.
#     Les tester pour valider vos solutions.

# ### Exercice
# 
# Ecrire un programme qui effectue les traitements
# successifs suivants :
# 
# 1.  définir les vecteurs de base ($i,j,k$) de taille 2 et 3 ainsi que
#     les vecteurs unités de même taille ;
# 
# 2.  coder la vérification l'orthogonalité ou non de vecteurs ;
#     l'appliquer aux vecteurs précédents ;
# 
# 3.  définir un vecteur de taille 5 dont les composantes sont des valeurs
#     entières aléatoires de l'intervalle $[-10,10]$ (on rappelle que
#     `import random` permet d'accéder à la fonction `random.randint` et
#     que la fonction `help` est notre amie);
# 
# 4.  définir les matrices identité en dimension 2 et 3;
# 
# 5.  pour la dimension 3, coder le produit matrice carrée $\times$
#     vecteur appliqué aux matrices et vecteurs précédents ;
# 
#     -   proposer une version où les vecteurs (entrée et résultat) sont
#         des vecteurs en ligne, puis une version où ces vecteurs sont des
#         vecteurs en colonne (conformément à la définition mathématique).
# 
# 6.  définir 2 matrices non carrées et compatibles avec leur produit
#     matriciel ; coder ce produit matriciel et le tester.
# 
# Prendre soin à écrire des traitements les plus indépendants possibles
# des dimensions choisies dans l'énoncé.

# ### Exercice
# 
# On reprend le contrôle de la validité du numéro de
# sécurité social de l'exercice 3, feuille de TP2, semestre 1.
# 
# 1.  Ecrire la vérification de la clé sous la forme d'une fonction
#     adaptée.
# 
# 2.  Appliquer cette fonction au traitement d'un nombre arbitraire de
#     numéros entrés au clavier.

# ### $\blacksquare$ Exercice (extrait d'examen 2017 sans machine)
# 
# 1.  Que calcule la fonction `m` suivante ?
# 
# ```python
#     def m(s : str, n : int, c : str ) -> int: 
#         ''' role : à vous de deviner :) '''
#         res = 0
#         for i in range(n): 
#             if s[i] == c: 
#                 res = res + 1 
#         return res
# ```
#        
# 
# 2.  Quel résultat produit l'exécution du code suivant ?
# 
# ```python
#     t = "anticonstitutionnellement" 
#     nba = m(t, len(t), 'a') 
#     nbe = m(t, len(t), 'e') 
#     nbl = m(t, len(t), 'l') 
#     print(len(t), nba, nbe, nbl)
# ```
#        
# (que:mmavecm)=
# 3.  Utiliser la fonction `m` pour écrire une fonction `mm` qui identifie
#     et retourne la lettre ayant le maximum d'occurrences dans une chaîne
#     de caractères de longueur `n`. Si plusieurs lettres conviennent,
#     l'algorithme identifiera celle dont l'occurrence est la plus tardive
#     dans `s`. Par exemple `'o'` dans `'toto'`.
# 
# 4.  Écrire le code qui utilise `mm` et fournit l'affichage suivant.
# 
# ```python
#     t est la lettre qui apparaît le plus ( 5 fois) dans anticonstitutionnellement 
#     o est la lettre qui apparaît le plus ( 2 fois) dans toto
# ```
#        
# 
# 5.  Modifier `mm` pour que dans le cas d'une occurrence maximale
#     multiple, l'algorithme identifie la lettre de première occurrence.
#     Par exemple, `'t'` dans `'toto'`.
# 
# 6.  Réécrire la fonction `mm` de la
#     [question](que:mmavecm)
#     sans utiliser la fonction `m`.

# ### $\blacksquare$ Exercice
# 
# Un palindrome est un mot, ou un groupe de mots, dont l'ordre des lettres
# reste le même qu'on le lise de la droite vers la gauche ou inversement.
# Des exemples bien connus sont "été", "kayak", "mon nom", "élu par cette
# crapule". Ce dernier permet d'illustrer qu'on ne tient pas compte en
# général des accents, trémas, cédilles, ni des espaces. Dans cet exercice
# :
# 
# -   un mot ou un groupe de mots est représenté par une chaîne de
#     caractères (`str`),
# 
# -   ces caractères sont sans accent, tréma, ni cédille : "ete"
# 
# -   les espaces sont considérés comme des caractères : ainsi "elu par
#     cette crapule" n'est pas un palindrome ici.
# 
# 1.  Ecrire une fonction qui teste si un argument est ou non un
#     palindrome et retourne le booléen correspondant.
# 
# 2.  Utiiser cette fonction pour tester un nombre arbitraire de mots
#     entrés au clavier.

# ### Exercice (Codage ASCII) 
# 
# L'ASCII est un codage de caractères qui
# définit 128 codes sur 7 bits. Chaque code correspond à un caractère :
# chiffres, lettres, symboles mathématiques et de ponctuation. En Python,
# la fonction `ord()` retourne le code ASCII d'un caractère fourni en
# argument. La fonction `chr()` retourne le caractère associé à un code
# donné.
# 
# Ecrire un programme qui affiche la table des 128 codes ASCII.

# ### Exercice 
# 
# Ecrire une fonction qui transforme un tableau de 0 et de
# 1 de longueur arbitraire, en l'entier de base 10 qui est codé par ce
# tableau en représentation de position en base 2 :
# 
# $$
# (b_n b_{n-1} \cdots b_1 b_0)_2 = (\sum_{i=0}^n b_i \times
#   2^i)_{10} \text{ avec } b_i \in \{0, 1\}.
# $$

# ## Objectif 20
# 
# ### Exercice
# 
# Les fonctions suivantes seront définies et utilisées dans
# un programme (principal) qui définit des tableaux que vous choisirez
# pour vérifier la validité de vos traitements. Vous choisirez la
# structure de donnée la plus adaptée à ces traitements.
# 
# 1.  Ecrire une fonction `est_egal()` qui réalise la comparaison entre
#     deux tableaux de dimension 1 et retourne le booléen correspondant.
#     On convient que deux tableaux sont égaux si leurs tailles sont
#     égales et si leurs valeurs sont égales deux à deux.
# 
# 2.  Ecrire une fonction `nb_communs()` qui retourne le nombre de valeurs
#     communes entre deux tableaux de dimension 1.
# 
# 3.  Reprendre les 2 questions précédentes pour des tableaux 2D.
#     L'égalité entre tableaux multi-dimensionnels suppose l'égalité des
#     dimensions, des tailles deux à deux dans chaque dimension, et des
#     valeurs deux à deux pour toutes les valeurs du tableau.

# ### Exercice (Algorithme de type Monte-Carlo)
# 
# On va calculer une approximation de $\pi$ de façon probabiliste.
# 
# 1.  Ecrire une fonction qui vérifie si un point du plan défini par ses
#     coordonnées $(x,y)$ appartient à un disque de centre $(a,b)$ et de
#     rayon $r$.  
#     Rappel. L'équation du cercle de mêmes caractéristiques est :
#     $(x-a)^2 + (y-b)^2 = r^2$.
# 
# 2.  Identifier dans la documentation du module python `random` la
#     fonction adaptée à la génération d'un point aléatoire dans le carré
#     $[-1, 1] \times [-1, 1]$.
# 
# 3.  Soit $\mathcal{C}$ le cercle de centre 0 et de rayon 1. Ecrire une
#     programme qui génère $n$ points aléatoires situés dans le carré
#     précédent et calcule le ratio entre les points situés dans le cercle
#     $\mathcal{C}$ et $n$.
# 
# 4.  Faire varier $n$ et observer l'évolution de ce ratio.
# 
# 5.  ($\star$) En déduire une approximation de $\pi$.

# ### Exercice (Une première cryptanalyse)
# 
# *L'analyse fréquentielle, découverte au IXe siècle par Al-Kindi, examine
# les répétitions des lettres d'un message chiffré afin de trouver la clé.
# Elle est inefficace contre les chiffrements modernes tels que DES, RSA.
# Elle est principalement utilisée contre les chiffrements
# mono-alphabétiques qui substituent chaque lettre par une autre et qui
# présentent un biais statistique.* (wikipedia).  
# 
# L'analyse de la fréquence d'apparition des lettres dans les écrits d'une
# langue donnée permet donc de déchiffrer les messages cryptés par
# certains chiffrements simples. En se limitant aux textes en francais et
# écrits en minuscules, nous allons effectuer les deux dernières étapes du
# processus suivant.
# 
# -   Etape 1 : Estimer la fréquence moyenne d'apparition en français des
#     lettres de l'alphabet. Ici nous utiliserons des résultats existants.
# 
# -   Etape 2 : Appliquer un chiffrement de César pour crypter un message
#     arbitraire.
# 
# -   Etape 3 : Effectuer l'analyse fréquentielle du message ainsi chiffré
#     pour (tenter de) retrouver le message d'origine.
# 
# 1.  Etape 2. Le chiffrement de César est une technique simple de
#     décalage régulier (permutation circulaire) de chaque lettre de
#     l'alphabet. La longueur de ce décalage – distance entre la position
#     d'une lettre décalée et sa position d'origine ($\le$ 26) – est la
#     *clé* de ce chiffrement.
# 
#     1.  Ecrire une fonction `cesar()` qui retourne le chiffré d'un
#         message arbitraire (chaine de caractères) pour une clé
#         arbitraire.
# 
#     2.  Ecrire une fonction `decesar()` qui retourne le message
#         d'origine connaissant la clé de chiffrement.
# 
#     (que:cesar)=
#     3.  Valider vos fonctions avec le chiffrement suivant de clé 5.
#         Faire d'autres essais et utiliser aussi les ressources
#         disponibles sur le web.  
# 
#         |                 |     |                                       |
#         |:----------------|:---:|:--------------------------------------|
#         | message clair   |  :  | `UNIVERSITE DE PERPIGNAN VIA DOMITIA` |
#         | message chiffré |  :  | `ZSNAJWXNYJ IJ UJWUNLSFS ANF ITRNYNF` |
# 
# 2.  Etape 3. Déchiffrement d'un texte chiffré de clé inconnue. La
#     fréquence moyenne d'apparition des lettres de l'alphabet dans un
#     texte en français est [par exemple donné dans](https://fr.wikipedia.org/wiki/Analyse_fréquentielle#Fréquence_d'apparition)
# 
#     1.  Proposer une solution pour déchiffrer un message que l'on sait
#         crypté par un chiffrement de César mais de clé inconnue.
# 
#     2.  Coder cette solution et l'appliquer aux messages de [la
#         question](que:cesar).
# 
#     3.  Evaluer comment votre solution "passe à l'échelle", c'est-à-dire
#         comment son efficacité évolue pour des textes de tailles qui
#         augmentent. Proposer des optimisations.

# ### Exercice ($\star$) 
# 
# Ecrire un programme qui trouve le plus petit
# entier non nul tel que les chiffres de ce nombre s'inversent quand on le
# multiplie par 9.
