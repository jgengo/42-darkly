# Explications

Sur la page de recover password ( ?page=recover )

Il y a un bouton "submit" sans rien de plus, ce qui déja parait bizarre, quand on a oublié son mot de passe on est censé mettre son mail quelques part.

En inspectant la page, on peut voir dans la form que il y a un input field "mail" qui permet d'editer le mail de l'admin qui recoit les demandes de reset de password.

On peut edit le mail en question.

----

# Cas d'usage

On pourrait s'en servir pour flood / mail bomb des adresses emails en utilisant ce form ( ou la route du form ) pour faire un petit script qui tournerait en boucle.

un script shell d'example d'exploit / flood dans ce dossier (00.sh)

----

# Comment l'eviter ?

Alors là, tout simplement en evitant de mettre ce genre d'infos dans les params d'un formulaire !

et de le gerer en back !

### PHP

```php
function request_password($email)
{
	mail(
		"admin@mail.fr",
		"request password",
		"Hey! {$email} would like to get back a new password!",
		);
}
```
