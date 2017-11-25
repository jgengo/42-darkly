# Explications

On peut se servir de l'include de page pour faire du transversal directoring, pour remonter jusqu'a /etc/passwd

il suffit de remonter directory apres directory en passant : ../../../etc/passwd

lien: ?page=../../../../../../../etc/passwd

Pour obtenir le flag

----

# Cas d'usage ?

reussir a afficher une page qui n'est pas censé l'etre ?
Par exemple un fichier de config avec les mots de passe de la db, ou tout ce qu'on veut :)

----

# Comment l'eviter ?

En protegeant le param page en autorisant seulement les noms de fichiers dans le dossier page.

### en PHP

```php
function get_content_from($folder)
{
	return array_map( 
		function($str) { 
			return str_replace('.php', '', $str); },
		array_slice(scandir(ROOT.'/'.$folder), 2)
	);
}

$authorized_pages = get_content_from('pages');

if (isset($_GET['p']) && in_array($_GET['p'], $authorized_pages))
{
	include_once('pages/'.$_GET['p'].'.php');
}
```