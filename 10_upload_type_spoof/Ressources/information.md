# Explications

Dans la page d'upload d'image.

On peut POST sur le formulaire d'envoit un fichier .php en le faisant passer par une image.

Il y a dans ce dossier un fichier pour exploit cette faille (10.sh), mais on pourrait aussi imaginer utiliser Tamper Data sur Firefox pour editer a la voler le nom du fichier qu'on veut envoyer lors du POST.

----

# Cas d'usage ?

Imaginez pouvoir mettre du code .php sur un site ? Ca vous ouvre les portes a tout.

----

# Comment l'eviter ?

Avant tout il vaut mieux eviter toutes redirections vers des images uploadez pour eviter de dire le dossier ou il est stocké.

Utilisez plutot un id de db qui pointerait dessus exemple : 

image.php?id=XXX

et ce image.php aurait un header avec le content-type de l'extension de l'image attendu

un htaccess sur le dossier ou sont uploadé les images avec une regle qui autorise que les fichiers de type images

### le htaccess

```
deny from all
    <Files ~ "^\w+\.(gif|jpe?g|png)$">
    order deny,allow
    allow from all
    </Files>
```