---
name: missing-altered-cards
description: Report Common/Rare Altered cards still needed to reach 4 copies total and indicate when the French version is missing.
---

# Missing cards

Read `data/cards.json` and `data/collection.json`.

For each card:
- `missing_total = max(0, 4-count)`.
- Show the 🇫🇷 marker only when `has_french == false`.
- A card is considered missing from the collection report when `missing_total > 0` or when the French copy is missing.
- Only process Common and Rare cards.

## Default response format

Return the result as a Markdown table with exactly these columns, in this order:

| Set | N° | Nom français | Manquantes | 🇫🇷 |
|---|---:|---|---:|:---:|

Rules:
- **Set** must contain the set/program code (for example `CORE`, `ALIZE`, `BISE`, `CYCLONE`, `DUSTER`), not the full set name.
- **N°** is the collector number.
- **Nom français** is the French card name.
- **Manquantes** is the number of additional copies needed to reach 4.
- **🇫🇷** is shown only when the French version is not present; otherwise leave the cell empty.
- Do not add rarity, faction, current count, or other columns unless explicitly requested.
- Sort by set, then collector number.
- Keep the response concise and do not add aggregate totals unless explicitly requested.
