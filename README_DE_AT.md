# Stop Slop – Österreichische Anpassung

Ein Skill zum Entfernen von KI-typischen Sprachmustern **speziell optimiert für österreichisches Deutsch**.

## Was dieses Dokument ist

Der Original "Stop Slop" Skill ist auf englische KI-Tells ausgerichtet. Diese Anpassung übersetzt nicht nur, sondern **kennt die österreichischen Sprachmarker**, die in AT-Texten zu künstlicher Prosa führen:

- **"Im Prinzip"** – das österreichische Universalfüllwort
- **"halt", "eben", "irgendwie"** – österreichische Abschwächer
- **"Schauen Sie...", "Na ja..."** – österreichische Ausweichformeln
- **"Vereinfacht gesagt"** – typisch AT: Ankündigung statt Tat
- **Understatement-Phrasen** – die österreichische "ist halt so"-Mentalität

## Skill-Struktur (österreichisch)

```
stop-slop/
├── SKILL.md                    # Kernregeln (mit AT-Hinweis)
├── references/
│   ├── phrases.md              # Englisch (Original)
│   ├── phrases_de_at.md        # 🇦🇹 ÖSTERREICHISCH (NEU)
│   ├── structures.md           # Strukturelle Muster
│   └── examples.md             # Vorher/Nachher-Beispiele
├── README.md                   # Englisch (Original)
├── README_DE_AT.md             # 🇦🇹 Dieses Dokument
└── LICENSE
```

## Quick Start für Österreich

1. **Lies `phrases_de_at.md`** – alle österreichischen Sprachmuster, die zu entfernen sind
2. **Beim Schreiben/Redigieren** immer prüfen:
   - ✋ Gibt es "im Prinzip", "halt", "irgendwie"?
   - ✋ Startet ein Satz mit "Schauen Sie...", "Na ja..."?
   - ✋ Klingt es nach AT-Understatement ("ist irgendwie kompliziert")?
3. **Scoring anwenden** – die 5 Dimensionen bewerten (siehe `phrases_de_at.md`)

## Die österreichischen Klassiker

### 1. "Im Prinzip"
Das absolute Österreich-Lieblingskind. Bedeutet oft nichts:
- ❌ "Im Prinzip ist das ein Problem"
- ✅ "Das ist ein Problem"

### 2. "halt" / "eben"
Nur österreichisch, immer überflüssig:
- ❌ "Das ist halt so"
- ✅ "Das muss sich ändern"

### 3. "Schauen Sie..."
Österreichische Höflichkeitsfalle – wirkt ausweichend:
- ❌ "Schauen Sie, das ist irgendwie kompliziert"
- ✅ "Das erfordert folgende drei Schritte..."

### 4. "Vereinfacht gesagt"
Wenn du das brauchst, ist es nicht vereinfacht:
- ❌ "Vereinfacht gesagt, die Synergien entstehen durch..."
- ✅ "Die Teile funktionieren zusammen, weil..."

### 5. Understatement-Kultur
Österreicher schwächen ab. Das macht Texte schwächer:
- ❌ "Das ist eigentlich irgendwie interessant"
- ✅ "Das ist entscheidend, weil..."

## Scoring (österreichisch)

| Dimension | Frage | AT-Warnsignal |
|-----------|-------|---------------|
| **Direktheit** | Statements statt Ankündigungen? | "Schauen Sie...", "Na ja...", "Im Prinzip..." |
| **Rhythmus** | Variiert oder monoton? | "halt eben quasi"-Reihungen |
| **Vertrauen** | Respekt vor Leserin? | Zu viel Understatement |
| **Authentizität** | Klingt es menschlich? | Behörden-Deutsch, zu formal |
| **Dichte** | Schnittbares vorhanden? | "irgendwie", "quasi", "sozusagen" |

**Unter 35/50 → Überarbeiten.**

## Verwendung

### Mit Claude
```
Nutze den /stop-slop Skill, um meinen Text auf österreichische 
KI-Tells zu prüfen. Besonders wichtig: "im Prinzip", "halt", 
"irgendwie", "Schauen Sie...". Scoring danach.
```

### Manuell
1. Text schreiben
2. `phrases_de_at.md` durchgehen (5 Min)
3. Alles Markierte revidieren
4. Scoring anwenden → fertig

## Lizenz

MIT — Frei verwendbar. Österreichische Sprachmuster gerne erweitern!

---

**Autor der AT-Anpassung:** Roland Dunzendorfer (basierend auf Hardik Pandya's "Stop Slop")
