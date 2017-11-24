# Explications 

Sur la homepage, il y a une photo de la NSA.
qui est chargé par un "viewer" d'image : ?page=media&src=
En realité on est sur une faille include qui genere une XSS.

Parce que le viewer se contente de mettre ce qu'il y a dans src pour le mettre dans l'attribut data.

Il suffit de lui passer une data en dur exemple : ?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=

----

# Cas d'usage ?

Il est possible faire une redirection avec une XSS d'un site a un autre, et de recuperer les cookies qui malheureusement parfois stock les id password en clair :(

----

# Comment l'eviter ?

En evitant d'inserer directement la data de l'url dans la page, et en passant des ids qui pointeraient sur des images (en db)