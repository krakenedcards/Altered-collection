---
name: update-altered-collection
description: Update owned copy counts and French availability in data/collection.json from user-provided collection information.
---

# Update collection

Read `data/cards.json` and `data/collection.json`.

1. Resolve user card names to exact card references.
2. If multiple refs match, use set/faction/rarity/collector number; ask only if ambiguity remains.
3. Update only the affected entries in `data/collection.json`.
4. `count` means total copies in all languages.
5. Set `has_french=true` when at least one French copy is confirmed.
6. Never infer French from total count.
7. Never invent ownership or negative counts.
8. Preserve all existing catalog references.
9. After batch edits, validate that every ref in `data/cards.json` exists in `data/collection.json`.
