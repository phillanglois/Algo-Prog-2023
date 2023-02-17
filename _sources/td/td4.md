(td:td4)=
# Feuille 4

- Le symbole $\blacksquare$ indique les exercices ou questions obligatoires. Commencez pas ceux-là.
- Les symboles $\star$ et $\star \star$ indiquent les exercices ou questions de difficulté relative plus importante.


**Focus**

-   complexité : analyses et approches expérimentales

**Compétences**

- Connaître le principes de l'analyse de la complexité en temps : modèle de calcul, mesure et paramètre de la complexité, meilleur et pire cas
- Connaître des exemples significatifs d'algorithmes de complexité polynomiale et logarithmique (complexité, pires et meilleurs cas)  
- Savoir établir la complexité d'algorithmes itératifs simples ou récursifs terminaux (algorithmes étudiés en cours)
- Savoir exprimer et exploiter une complexité asymptotique : notations de Landau, principales classes de complexité des algorithmes, interprétation pratique de ces classes
- Savoir identifier (sans nécessairement le prouver) la complexité, les meilleur-pire cas d'un algorithme 

## Objectif 10

### $\blacksquare$ QCM (Extrait de CC)
  
  Dans les questions de cet exercice, le terme ''complexité''
  (seul) désigne la complexité en temps. On précise ''complexité en
  espace'' si on s'intéresse à cette notion.    

1. Une analyse de complexité en temps  mesure le temps d'exécution 
d'un programme sur les ordinateurs des salles info. (Vrai/Faux)
2. Dans une analyse de complexité en temps, le coût d'une
    multiplication de 2 entiers codés sur 32 bits est de 1 unité tandis que celui
    de la multiplication de 2 nombres flottants codés sur 64 bits
    est de 2 unités. (Vrai/Faux) 
3. Lors d'une analyse de complexité en temps, le coût d'une
    répétition \t{while} est égal à trois fois celui du \t{for} à cause
    du compteur géré de manière explicite : incrémentation et comparaison. (Vrai/Faux) 
4. Citer un exemple d'algorithme avec une complexité
    constante dans le meilleur cas et linéaire dans le pire cas. 
5. Citer un exemple d'algorithme avec une complexité
    quadratique  dans le pire cas. 
6. Quel est le meilleur cas dans une recherche séquentielle itérative ? 
7. Quel est le meilleur cas dans une recherche dichotomique dans $n$ valeurs triées ? 
8. Un algorithme a une complexité temporelle cubique en la
    taille de son entrée, que peut-on dire de son temps
    d'exécution si l'on double la taille de l'entrée ?   
9. La fonction de complexité $C(n) = 4n^3 + 25n^2 + 10^2$ est
    asymptotiquement linéaire? quadratique ? ou cubique ?
    Pourquoi? 
9. Les complexités asymptotiques des programmes $P1$ et $P2$ sont
    égales à $\theta(n)$ donc leurs fonctions de complexité $C_1(n)$
    et $C_2(n)$ sont égales.
    (Vrai/Faux)
9. Un algorithme a une complexité en espace quadratique en son
    paramètre $n$. Pour $n = 100$, il requiert 1Mo d'espace mémoire pour
    pouvoir s'exécuter.
    De quelle quantité de mémoire aura-t-il {\it approximativement} besoin
    pour s'exécuter avec $n = 1000$ ? 


(exo:doubleboucle)=
### $\blacksquare$ Exercice

1.  Dérouler l'algorithme suivant en explicitant les valeurs de
    l'ensemble de ses variables.

    ```{code-block} python
    ---
    linenos: true
    ---
    for i in range (4): 
        for j in range(i,4): 
            k = i + j
    ```
2.  Même question en remplaçant la ligne 2 par :

    ```{code-block} python
     for j in range(i+1,4):
    ```
3.  Compter le nombre d'additions dans chacun des deux cas.
4.  Coder une vérification de ces deux questions.



### $\blacksquare $ Exercice

On reprend [l'exercice précédent](exo:doubleboucle) en introduisant un nombre arbitraire  $n$ d'itérations de chaque boucle.

1.  Quelle est une mesure naturelle de la complexité de cet algorithme ?
    Quel est le paramètre de cette complexité ?

2.  Pour chacun des cas suivants : compter le nombre d'additions
    effectuées à chaque itération de la boucle intérieure. En déduire le
    nombre total d'additions. Quelle est la complexité asymptotique de
    cet algorithme ?

	a.  On modifie la ligne 1 :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(n): 
		for j in range(i,4):
	```

	b.  on modifie maintenant la ligne 2 :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(4): 
		for j in range(n):
	```

	c.  ou aussi :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(4): 
		for j in range(i,n):
	```

	d.  Avec les lignes 1 et 2 suivantes :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(n): 
		for j in range(n):
	```

	e.  ou aussi les lignes 1 et 2 suivantes :

	```{code-block} python
	---
	linenos: true
	---
	for i in range(n): 
		for j in range(i,n):
	```


Rappel. Il est utile de connaître la valeur de la somme des $n$ premiers
entiers et son équivalent asymptotique :

$$1+2 +  \dots + n =  \sum_{k=1}^n k = n(n+1)/2  \approx n^2/2 =  \theta(n^2) et donc = \cal{O}(n^2).$$


### $\blacksquare $ Exercice 

Effectuer l'analyse de la complexité des fonctions
suivantes (déjà étudiées dans la feuille 2).

1.  La fonction `est_egal()` qui réalise la comparaison entre deux
    tableaux et retourne le booléen correspondant.

2.  La fonction `nb_communs()` qui retourne le nombre de valeurs
    communes entre deux tableaux.


### Exercice

Effectuer une analyse expérimentale de la
complexité pour comparer l'efficacité des algorithmes de recherche
itérative et dichotomique (cas de l'entrée triée). Dégager les
comportements dans le meilleur cas, dans le pire cas de chacun d'entre eux.

### Exercice

_Note :_ La question 2 fait appel à la récursivité.

1.  Rappeler l'algorithme (classique) du produit de deux matrices carrés
    de taille $n$ et sa complexité asymptotique

2.  ($\star$) Sur wikipedia chercher *algorithme de Strassen*, le comprendre et
    noter sa complexité asymptotique

3.  Coder ces deux algorithmes et effectuer une analyse
    expérimentale de leurs complexités pour $n$ variant raisonnablement.

4.   ($\star$) Qu'en conclure ?


### Exercice -- qui commence en Objectif 10 et finit en Objectif 20

_Note :_ Cet exercice fait appel à la fonction python `append()` qui ajoute une valeur à une liste.

1.  Premier algorithme.

    1.  Quel traitement effectue l'algorithme suivant ?

        ```{code-block} python
        ---
        linenos: true
        ---
        n = int(input()) 
        l1 =  [ ] 
        for i in range(n+1): 
            ok = False 
            for j in range(n+1): 
                for k in range(n+1): 
                    if i == j ** 2 + k ** 2: 
                        ok = True 
            if ok == True: 
                l1.append(i)
        ```        

    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.
    3.  En déduire la complexité asymptotique de cet algorithme.
2.  Deuxième algorithme.
    1.  Justifier que l'algorithme suivant résout le même problème que
        l'algorithme précédent.

        ```{code-block} python
        ---
        linenos: true
        ---
        n = int(input()) 
        l2 =  [ ] 
        for i in range(n+1): 
            ok = False 
            j = 0
            while j  < n+1 and (ok == False): 
                k = 0 
                while k  < n+1 and ok == False: 
                    if i == j ** 2 + k ** 2: 
                        l2.append(i) 
                        ok = True 
                    else: 
                        k = k + 1 
                j = j + 1 
        ```
    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.
    3.  En déduire la complexité asymptotique de cet algorithme.
    4.  Que conclure ?

## Objectif 20

3.  ($\star \star$)Troisième algorithme.

    1.  Justifier que l'algorithme suivant résout le même problème que
        les algorithmes précédents.

        ```{code-block} python
        ---
        linenos: true
        ---
        from math import sqrt 
        
        n = int(input()) 
        l3 =  [ ] 
        for i in range(n+1): 
            ok = False 
            j = 0 
            while j<= int(sqrt(i)) and ok == False: 
                k = 0 
                while k<= int(sqrt(i - j ** 2)) and (ok == False):
                    if i == j ** 2 + k ** 2: 
                        l3.append(i) 
                        ok = True 
                    else: 
                        k = k + 1 
                j = j + 1 
        ```
    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.
    3.  En utilisant les indications suivantes, déduire la complexité asymptotique de
        cet algorithme.
        
        Indications : Il n'est pas difficile de montrer la majoration
        asymptotique suivante :

        1.  $ \sum_{i=0}^{n}  \sqrt{i} =  \mathcal{O}( n  \sqrt{n})$.

        On peut obtenir les équivalents asymptotiques suivants :

        -   $\sum_{i=0}^{n} \sqrt{i} \sim \frac{2}{3} n \sqrt{n} = \theta(n \sqrt{n})$;

        -   $\sum_{i=0}^{n} [1+ \sum_{j=0}^{\sqrt{i}} (1+\sqrt{i-j^2})]
                  \sim \frac{\pi}{8} n^2 = \theta(n^2)$.
    4.  Que conclure ?
4.  ($\star$) Quatrième algorithme.
    1.  Justifier que l'algorithme suivant résout le même problème que
        les algorithmes précédents.

        ```{code-block} python
        ---
        linenos: true
        ---
        from math import sqrt 
        
        n = int(input()) 
        l4 =  [ ] 
        for i in range(n+1): 
            ok = False 
            j = 0 
            while j <= int(sqrt(i)) and (ok == False): 
                c = i - j ** 2 
                s = int(sqrt(c)) 
                if s * s == c:
                    l4.append(i) 
                    ok = True 
                j = j + 1 .
        ```

    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.
    3.  En utilisant un logiciel de calcul formel ou les relations
        précédentes, en déduire la complexité asymptotique de cet
        algorithme.
    4.  Que conclure ?
5.  ($\star$) Cinquième algorithme.
    1.  Justifier que i) l'algorithme suivant résolve le même problème
        que les algorithmes précédents, mais ii) effectue un traitement
        différent de ces derniers.

        ```{code-block} python
        ---
        linenos: true
        ---
        from math import sqrt, floor 
        
        n = int(input()) 
        l5 =  [ ] 
        for i in range(floor(sqrt(n))+1): 
            for j in range(i, floor(sqrt(n - i ** 2))+1): 
                r = i ** 2 + j ** 2 
                l5.append(r) 
        ```
    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.
    3.  ($\star \star$) En utilisant le logiciel [`SageMath`](https://www.sagemath.org/fr/), en déduire la complexité asymptotique de cet algorithme.
    4.  Que conclure ?

### Exercice 

Effectuer une analyse expérimentale de la
complexité des cinq algorithmes précédents pour des valeurs de $n$
	choisies de façon adaptée entre 10 et 10 000.
