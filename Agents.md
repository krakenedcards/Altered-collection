# Altered Collection — Agent Instructions

## Role
This repository is the source of truth for a personal Altered TCG collection. Track **Common** and **Rare** cards only.

Each distinct card reference is a separate entry. If a Common has two Rare variants, the Common and each Rare reference are tracked independently.

## Ownership model
For every card reference:
- `count`: total physical copies owned, all languages combined.
- `has_french`: true if at least one owned copy is French.

Target for every card:
- at least 4 total copies;
- at least 1 French copy.

Do not store individual copies.

## Source files
- `data/cards.json`: normalized French catalog of all Common/Rare cards loaded at initialization.
- `data/collection.json`: personal ownership state.
- `scripts/missing_cards.py`: local missing-card report.
- `.agents/skills/`: agent workflows.

## Updating the collection
When the user supplies ownership:
1. Resolve the card to an exact `ref` using `data/cards.json`.
2. Ask for clarification if a name is ambiguous.
3. Modify only `data/collection.json`.
4. Counts are total copies, not French copies.
5. Set `has_french=true` only when the user confirms a French copy.
6. Never invent counts or language.
7. Never make a count negative.
8. Preserve every catalog reference in `collection.json`.

## Missing cards
A card is incomplete when `count < 4` OR `has_french=false`.
- `missing_total=max(0,4-count)`
- `missing_french=1` when `has_french=false`, otherwise 0.
If total copies are already 4 but French is absent, the report must still flag the need for a French copy/replacement.

## Catalog refresh
Use the community Altered card database as the upstream catalog. Refreshing must preserve existing collection values by reference, initialize new refs to zero, and never silently delete an old collection entry.
