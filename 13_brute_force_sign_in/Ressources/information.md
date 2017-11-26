# Explications

Grace a la faille d'injection SQL sur search member et search image, j'ai vu une base de donnée qui s'appelait : "Member Brute Force".

J'aurais pu directement depuis les injections SQL trouvé le login/mot de passe. Mais allons vers le brute force dans ce cas...

On peut trouver sur ce site une liste des 25 mots de passe les plus utilisés.

`http://datanews.levif.be/ict/actualite/le-top-25-des-mots-de-passe-les-plus-courants-et-les-plus-faibles/article-normal-292823.html`

(voir le script shell pour brute force)

On obtient le flag.

----

# Cas d'usage ?

Le Brute force est une des methodes les plus simples, mais surement l'une des plus longue.

Elle permet d'obtenir le mot de passe d'un admin, et d'avoir le controle sur le site.

----

# Comment l'eviter ?

En se protegeant des brutes forces, avec des limites de call par minutes sur une page, ou sur un login.

