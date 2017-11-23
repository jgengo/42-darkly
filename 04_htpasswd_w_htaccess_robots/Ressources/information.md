# Explications

Dans robots.txt, on voit qu'il y a un dossier en disallow /whatever si on rentre dedans on trouve un htpasswd qui store un login:password.

le password est enchiffré en md5, il suffit de prendre un site avec une grosse db de hash pour trouver le mot de passe : dragon

Si on re-utilise le login:password sur la route /admin on peut acceder au flag.

----

# Cas d'usage ?

Il est possible de mettre a la racine de ses sites un robots.txt, c'est une convention (tres peu respecté) qui permet de dire aux bots / crawler qui font de l'indexisation de page de ne pas "indexer" certaines routes qu'on prefere ne pas voir etre afficher sur le site.

Jusque là tout va bien, sauf que dans ce cas precis, le .htpasswd etait pas protegé par un htaccess qui aurait evité que la route soit accessible.

----

# Comment l'eviter ?

Bah justement, en protegeant son dossier par un htaccess.
Et en evitant de croire que la convention de robots.txt :D