# Stop Slop — version française 🇫🇷

Un skill qui **nettoie les textes français des marqueurs de l'IA**. Il repère et supprime les tournures prévisibles qui trahissent un texte généré par un LLM, pour obtenir une prose qui sonne humaine et naturellement française.

> ⚠️ Ce skill est **spécifique au français**. Ce n'est pas la traduction des règles anglaises : l'IA écrit le français avec ses propres tics, que les règles anglaises ne couvrent pas (et certaines règles anglaises ne sont pas des problèmes en français). Pour l'anglais, voir le projet original [stop-slop](https://github.com/hardikpandya/stop-slop).

## À quoi ça sert

Quand vous rédigez, éditez ou relisez un texte en français — article, e-mail, doc, post — le skill applique une discipline anti-« slop » : couper le remplissage, casser les structures formulaïques, nommer les acteurs, varier le rythme, faire confiance au lecteur. Le résultat est plus court, plus direct et moins reconnaissable comme « écrit par une IA ».

## Ce que ça fait concrètement

Il traque et corrige les marqueurs IA **propres au français** :

- **Amorces creuses** — « Il est important de noter que », « Force est de constater que », « Soyons clairs ».
- **Connecteurs scolaires en série** — « En outre », « Par ailleurs », « Néanmoins », « Ainsi ».
- **Mots fétiches** — « crucial », « essentiel », « incontournable », et surtout « véritable ».
- **Adverbes en -ment** — « véritablement », « profondément », « simplement », « fondamentalement ».
- **Anglicismes et calques** — « impacter », « adresser un problème », « faire du sens », « au final ».
- **Gérondif final** — la queue en « -ant » qui commente l'action (« …, ouvrant la voie à de nouvelles possibilités »). Tic IA français majeur, sans équivalent anglais.
- **Le « on » impersonnel** — masque l'acteur comme la voix passive (« on observe que »).
- **Phrases clivées** — « Ce qu'il faut retenir, c'est… », « C'est là que tout se joue. »
- **Voix passive** — « la décision a été prise » → nommer qui décide.
- **Agentivité factice** — « la donnée nous dit », « le marché récompense ».
- **Faux contrastes** — « ce n'est pas X, c'est Y », « il ne s'agit pas de X mais de Y ».
- **Énumérations ternaires** par réflexe et **fragmentation dramatique**.
- **Formules de conclusion** automatiques — « En somme », « En définitive », « Vous l'aurez compris ».
- **Typographie française** — guillemets « », espace insécable avant `: ; ! ?`, pas de tiret cadratin, pas de virgule d'Oxford.

## Exemple

**Avant :**
> « À l'ère du tout-numérique, il est important de noter que l'IA est un véritable game-changer. En outre, force est de constater qu'elle impacte profondément tous les secteurs. La donnée nous le dit, transformant ainsi notre façon de travailler. En somme, l'avenir nous le dira. »

**Après :**
> « L'IA change le travail dans la santé, la finance et le droit. Les radiologues lisent leurs clichés avec un modèle de détection ; les analystes laissent un agent trier les transactions suspectes. »

## Structure

```
stop-slop-fr/
├── SKILL.md                  # Règles de base, checklist, notation (en français)
├── references/
│   ├── expressions.md        # Expressions à supprimer
│   ├── structures.md         # Motifs structurels à éviter
│   └── exemples.md           # Transformations avant/après, pensées en français
├── README.md
└── LICENSE
```

## Installation et utilisation

**Claude Code :** placer ce dossier dans `~/.claude/skills/`.

```bash
git clone https://github.com/amdiakhate/stop-slop.git
cp -R stop-slop/stop-slop-fr ~/.claude/skills/
```

Le skill se déclenche automatiquement quand vous rédigez, éditez ou relisez un texte français. Vous pouvez aussi l'invoquer explicitement avec `/stop-slop-fr`.

**Projets Claude :** téléverser `SKILL.md` et les fichiers de `references/` dans la base de connaissances.

**Instructions personnalisées :** copier les règles de base de `SKILL.md`.

**Appels API :** inclure `SKILL.md` dans le prompt système ; les fichiers de référence se chargent à la demande.

## Notation

Avant de livrer un texte, le noter de 1 à 10 sur cinq dimensions : franchise, rythme, confiance, authenticité, densité. En dessous de 35/50 : réviser.

## Crédits et licence

Adapté en français à partir de [stop-slop](https://github.com/hardikpandya/stop-slop) de [Hardik Pandya](https://hvpandya.com). Licence MIT — utilisez et partagez librement.
