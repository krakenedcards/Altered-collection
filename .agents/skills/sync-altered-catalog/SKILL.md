---
name: sync-altered-catalog
description: Refresh the Common/Rare French card catalog from the upstream community database while preserving personal ownership data.
---

# Sync catalog

Upstream: `PolluxTroy0/Altered-TCG-Card-Database`.

1. Discover all directories under `SETS/`.
2. For each set, read `<SET>_FR.json` when present.
3. Keep only rarity references `COMMON` and `RARE`.
4. Normalize to `ref`, `name_fr`, `set`, `faction`, `rarity`, `collector_number`.
5. Replace `data/cards.json` with the refreshed catalog.
6. Merge refs into `data/collection.json`: preserve existing `count` and `has_french`; initialize new refs to 0/false.
7. Never silently erase a collection entry that disappears upstream; flag it for review.
8. Run the missing-card report after syncing.
