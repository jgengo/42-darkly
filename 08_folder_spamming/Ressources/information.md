# Explications

Dans le robots.txt expliqué dans la faille htpasswd
Il y avait aussi un dossier .hidden de Disallow.

On tombe face a des dossiers, qui contiennent des dossiers qui contiennent des dossiers.
Il y a qu'une seule solution la, c'est de scripter un crawler pour lire tous les fichiers.

./script.rb http://192.168.2.128/ .hidden/ > result.txt

Apres avoir bien tourné faire des coups de : grep -v ' ' du fichier result.txt

----

# Cas d'usage ?

Encore une fois la mise a part pour cacher du contenu et le perdre dans un tas de dossier bien sale, je vois pas trop l'utilité.

Surtout que si tu veux proteger de la data, autant faire un htaccess correct.

Curieux...

----

# Comment l'eviter ?

En utilisant plutot un htaccess pour proteger un dossier avec des fichiers qu'on ne veut pas montrer.