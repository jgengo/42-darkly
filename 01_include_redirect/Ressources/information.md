# Explications

Dans le footer
Il y a les 3 liens pour les reseaux sociaux (facebook, twitter et instagram)
Le site utilise une page redirect qui prend en params un "site"
On peut y passer un autre site comme par exemple : http://www.google.fr/

----

# Cas d'usage ?

On peut se servir cette faille pour rediriger des utilisateurs vers un faux site pour faire du phising.
Imaginez une seconde que votre banque avait une faille de la sorte, des petits malins s'amuseraient a envoyer des mass-mails
et le lien semblerait legit vu qu'il contiendrait l'adresse de votre banque, de peu que cela tombe sur une personne pas tres
regardante, ou pas tres technophile, il pensera etre sur le site de sa banque et entrera ses identifiants.

---- 

# Comment l'eviter ?

Par exemple ils auraient pu faire un array de params possibles, et interdire les autres.

### en PHP

```php
function check_site($site)
{ 
	$allowed_redirect = array ("facebook", "twitter", "intagram");

	if (in_array($_GET['site'], $allowed_redirect)
	{
		function_qui_redirige($_GET['site']);
	} else {
		return false;
	}
}

if (isset($_GET['site'])
	check_site($_GET['site'])
```