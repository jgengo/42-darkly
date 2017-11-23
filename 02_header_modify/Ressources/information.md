# Explications

Dans le footer
il y a un lien bornToSec qui amene sur une page avec une musique de la mort qui tue !
Dans les commentaires de la page on peut voir des tits tips qui invite a changer ses headers pour passer un Referer pour faire croire qu'on vient de la page : https://www.nsa.gov/
et un User-Agent pour faire croire qu'on utilise un navigateur custom nommé : "ft_bornToSec"

---

# Cas d'usage ?

Je ne vois pas vraiment l'interet.
On pourrait imaginer ca comme une "protection" supplementaire sur un webservice.

Pour l'exploiter j'ai mis un script shell (02.sh) dans ce dossier qui va curl la page avec des options pour specifier un user-agent custom et un referer.

Sinon il y a aussi la possibilité de prendre des extensions Chrome ou Firefox pour ca.

----

# Comment l'eviter ?

en favorisant plutot une bonne page de connection admin avec une creation de session correct.

Si c'est pour un webservice, eventuellement le laisser, mais il faut ajouter un token, passcode en plus dans ces params.