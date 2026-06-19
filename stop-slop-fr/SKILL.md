---
name: stop-slop-fr
description: Élimine les tics d'écriture de l'IA dans les textes en français. À utiliser lors de la rédaction, l'édition ou la relecture d'un texte français pour supprimer les marqueurs prévisibles de l'IA (amorces creuses, connecteurs scolaires, mots fétiches, jargon, anglicismes, gérondifs finaux, faux contrastes, voix passive, « on » impersonnel, énumérations ternaires, typographie).
metadata:
  trigger: Rédaction de prose, édition de brouillons, relecture pour repérer les marqueurs IA en français
  author: Adapté en français à partir de stop-slop de Hardik Pandya (https://hvpandya.com) — licence MIT
---

# Stop Slop (français)

Supprimer les marqueurs prévisibles de l'écriture IA dans un texte français.

Cette adaptation cible les tics propres au français, pas une traduction des règles anglaises. Le français a ses propres amorces, son jargon, ses anglicismes et ses structures (gérondif final, clivées « c'est… que », « on » impersonnel, énumérations ternaires, typographie).

## Règles de base

1. **Couper les expressions de remplissage.** Supprimer les amorces creuses (« il est important de noter que »), les béquilles d'emphase, les connecteurs scolaires en série et tous les adverbes en -ment. Voir [references/expressions.md](references/expressions.md).

2. **Casser les structures formulaïques.** Éviter les faux contrastes (« ce n'est pas X, c'est Y »), les énumérations par la négation, la fragmentation dramatique, les questions rhétoriques de relance, le gérondif final commentant l'action, l'agentivité factice. Voir [references/structures.md](references/structures.md).

3. **Voix active, acteur nommé.** Chaque phrase a un sujet humain qui agit. Pas de voix passive (« la décision a été prise »). Pas de « on » qui masque l'acteur (« on observe que »). Pas d'objet inanimé qui agit (« la donnée nous dit »).

4. **Être précis.** Pas de déclaration vague (« les enjeux sont considérables »). Nommer la chose précise. Pas d'extrêmes faciles (« tous », « toujours », « jamais ») qui font un travail vague.

5. **Mettre le lecteur dans la scène.** Pas de voix de narrateur surplombant. « Vous » vaut mieux que « les gens ». Le concret bat l'abstrait.

6. **Varier le rythme.** Mélanger les longueurs de phrases. Deux éléments valent mieux que trois (méfiance des énumérations ternaires). Varier les fins de paragraphe. Pas de tiret cadratin.

7. **Faire confiance au lecteur.** Énoncer les faits directement. Pas d'atténuation, pas de justification, pas de prise par la main.

8. **Couper les phrases « à citer ».** Si ça sonne comme une accroche LinkedIn, réécrire.

## Vérifications rapides

Avant de livrer un texte :

- Des adverbes en -ment ? Les supprimer.
- « véritable / véritablement » ? Couper.
- De la voix passive ? Trouver l'acteur, en faire le sujet.
- Un « on » qui cache l'acteur ? Nommer la personne ou utiliser « vous ».
- Un objet inanimé qui fait un verbe humain (« la technologie transforme ») ? Nommer la personne.
- Un connecteur scolaire en tête de phrase (« En outre », « Par ailleurs », « En effet », « Ainsi », « Force est de constater ») ? Couper ou fondre.
- Une amorce creuse (« il est important de noter que », « il convient de souligner ») ? Aller droit au but.
- Un faux contraste (« ce n'est pas X, c'est Y », « il ne s'agit pas de X mais de Y ») ? Énoncer Y directement.
- Un gérondif final qui commente (« …, ouvrant la voie à de nouvelles possibilités ») ? Le couper.
- Une clivée de remplissage (« Ce qu'il faut retenir, c'est… ») ? Énoncer le fait.
- Trois phrases d'affilée de même longueur ? En casser une.
- Une énumération ternaire (« X, Y et Z ») par réflexe ? Réduire à deux ou un.
- Un tiret cadratin (—) ? Le remplacer par une virgule, un point ou des parenthèses.
- Une formule de conclusion automatique (« En somme », « En définitive », « Au final », « Vous l'aurez compris ») ? Couper.
- Une déclaration vague (« les implications sont majeures ») ? Nommer l'implication précise.
- Typographie : guillemets français « » (pas `"`), espace insécable avant `: ; ! ?`, pas de virgule d'Oxford avant « et ».

## Notation

Noter de 1 à 10 chaque dimension :

| Dimension | Question |
|-----------|----------|
| Franchise | Affirmations ou annonces ? |
| Rythme | Varié ou métronomique ? |
| Confiance | Respecte l'intelligence du lecteur ? |
| Authenticité | Sonne humain et français (pas traduit) ? |
| Densité | Reste-t-il quelque chose à couper ? |

En dessous de 35/50 : réviser.

## Exemples

Voir [references/exemples.md](references/exemples.md) pour des transformations avant/après.

## Licence

MIT. Adapté de [stop-slop](https://github.com/hardikpandya/stop-slop) de Hardik Pandya.
