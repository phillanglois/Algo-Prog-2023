(td:td4)=
# Feuille 4

- Le symbole $\blacksquare $ indique les exercices ou questions obligatoires. Commencez pas ceux-là.
- Les symboles $\star$ et $\star \star$ indiquent les exercices ou questions de difficulté relative plus importante.


**Focus**

-   complexité : analyses et approches expérimentales

## Objectif 10

(exo:doubleboucle)=
### $\blacksquare $ Exercice

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

On reprend [l'exercice précédent](exo:doubleboucle) en introduisant un nombre arbitraire $n$
d'itérations de chaque boucle.

1.  Quelle est une mesure naturelle de la complexité de cet algorithme ?
    Quel est le paramètre de cette complexité ?

2.  Pour chacun des cas suivants : compter le nombre d'additions
    effectuées à chaque itération de la boucle intérieure. En déduire le
    nombre totale d'additions. Quelle est la complexité asymptotique de
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

$$1+2 +  \dots + n =  \sum_{k=1}^n k = n(n+1)/2  \approx n^2/2 =  \theta(n^2).$$


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
comportements dans le meilleur cas, dans le\pire cas et en moyenne.

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

        _Correction_
        
        Trouve tous les entiers entre 0 et $n$ qui s'écrivent comme la
        somme de 2 carrés.
        

    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.

        _Correction_
        
        - Paramètre de complexité : $n$. 
        - On peut compter le nombre de
        comparaisons : il est égal au nombre d'additions et à la moitié
        du nombre de mises au carré ou multiplications. On a 3 boucles
        imbriquées : 
            - la boucle extérieure en i est effectuée exactement $n+1$ fois 
            - à chaque itération de i, la boucle médiane en j est effectuée exactement $n+1$ fois, donc $(n+1)^2$
        au total 
            - et à chaque itération de j, la boucle intérieure est
        effectuée exactement $n+1$ fois, soit au total $(n+1)^3$ fois
        exactement.

        Conclusion : on effectue exactement : $(n+1)^3$ additions et
        comparaisons, et $3(n+1)^3$ additions. Soit donc de façon
        équivalente pour $n$ grand, $n^3$ opérations.
        

    3.  En déduire la complexité asymptotique de cet algorithme.

        _Correction_

        Elle est cubique en $n$.

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

         _Correction_

        On arrête les boucles en k et j dès qu'une somme de deux carrés
        valant i est trouvée.

    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.

        _Correction_

        Seules des majorations sont possibles ici. De la même façon que
        précédemment : 
        
        - au plus $(n+1)^3$ additions et comparaisons 
        - au plus $2(n+1)^3$ multiplications

    3.  En déduire la complexité asymptotique de cet algorithme.

        _Correction_

        Elle est au plus cubique en $n$, cad. en $O(n^3)$.

    4.  Que conclure ?

        _Correction_

        Asymptotiquement équivalent à l'algo précédent.

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


        _Correction_

        On arrête l'itération en j dès que j  >\sqrt(i), et de même on
        arrête l'itération en k dès que k  >\sqrt(i - j ^2).

    2.  Estimer la complexité de cet algorithme : préciser le paramètre
        de complexité et estimer de la façon la plus précise possible le
        nombre de chaque opération arithmétique exécutée, estimation qui
        sera exprimée comme une fonction de ce paramètre.

        _Correction_

        On ajoute aux décomptes précédent le nombre de racine carrées.
        On a encore des majorations : - nbre de + :


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

    3.  ($\star \star$) En utilisant le logiciel [`SageMath`](https://www.sagemath.org/fr/), en déduire la complexité asymptotique de<=  cet algorithme.

    4.  Que conclure ?

### Exercice 

Effectuer une analyse expérimentale de la
complexité des cinq algorithmes précédents pour des valeurs de $n$
	choisies de façon adaptée entre 10 et 10 000.
