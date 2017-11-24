# Explications

Sur la page feedback.

Si tu entre dans le commentaire "script" il te pete un flag
On est sur une faille XSS

---

# Cas d'usage ?

On est sur un cas un peu tiré par les cheveux parce que le fait d'ecrire juste "script" n'est pas censé etre une XSS, il faut reussir a poser les balises script eventuellement.

une faille XSS peut permettre de rediriger vers un site / page pour grab les cookies d'un admin ou autres utilisateurs.

Et certains, site (encore ajd), malheureusement stock les datas en clair dans les cookies.

----

# Comment l'eviter ?

Il faut a tout pris sanitize, .html_safe, strip_tags ou filter_var les retour de formulaire.

Il y a des tas de libs qui font ca pour vous maintenant.

### en PHP

```php
$cleaned_comment = htmlspecialchars($_GET['comment']);
```
