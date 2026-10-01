---
name: missing-altered-cards
description: Report Common/Rare Altered cards still needed to reach 4 copies total and at least one French copy.
---

# Missing cards

Read `data/cards.json` and `data/collection.json`.

A card is complete only if `count >= 4` and `has_french == true`.

For every incomplete card:
- `missing_total = max(0, 4-count)`
- `missing_french = 0` if French is present, otherwise `1`.

Default report fields:
Set · collector number · French name · rarity · faction · current count · French present · total copies needed · French copy needed.

Sort by set, collector number, rarity. Finish with aggregate totals.
