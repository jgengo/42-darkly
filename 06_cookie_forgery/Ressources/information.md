# Explications

En regardant du coté des cookies creaient par le site, on peut voir une relation key-value, avec un cookie qui a pour clé : i_am_admin, et une valeur qui veut dire : false en md5.

Il suffit d'edit par la valeur md5 de true et voila !

----

# Cas d'usage ?

J'ai du mal à imaginer qu'un site garderait en clair dans les cookies la protection "suis je admin".

Mais admettons! Il suffirait d'edit cette value pour obtenir les droits admin sur un site protegé.

----

# Comment l'eviter ?

Quitte a faire une protection sale, pour savoir si tu es admin d'un site, autant le mettre dans une session enchiffrée plutot que les cookies.

Apres le mieux c'est de plutot utiliser un system de droit par reconnaissance du user.