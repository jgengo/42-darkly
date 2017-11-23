# Explications

Dans la page de survey.

On est devant un tableau, avec pleins de formulaires, sans aucune validation (ni en front ni en back).
Il suffit de changer une des value d'un field par une valeur que l'on veut par exemple : 10000 ce qui donnera 10 000 points (de quoi fausser le survey)

----

# Cas d'usage ?

Tricher sur des sondages, admettons un site d'une radio amateur qui ferait un sondage pour determiner la prochaine musique qui passera.

Eh hop ! C'est toi qui chosit.

----

# Comment l'eviter ?

En Web, il est important d'avoir une protection en back efficace, et eventuellement une en front pour l'usage experience.

### en PHP

```php
function check_value($value)
{
	($value >= 1 && $value <= 10) ? true : false
}
```