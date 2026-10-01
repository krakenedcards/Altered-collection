# Altered Collection

Personal tracker for an Altered TCG collection.

**Scope:** Common and Rare cards only. Unique cards are intentionally excluded.

## Collection target

Every distinct card reference should reach:
- **4 copies total**, regardless of language
- **at least 1 French copy**

Ownership is compact:

```json
"ALT_CORE_A_AX_22_C": {
  "count": 3,
  "has_french": true
}
```

## Agent workflows

- **Record/update ownership:** `.agents/skills/update-altered-collection/SKILL.md`
- **List missing cards:** `.agents/skills/missing-altered-cards/SKILL.md`
- **Refresh the catalog:** `.agents/skills/sync-altered-catalog/SKILL.md`

## Catalog source

The initial catalog was built from French JSON set data in the community-maintained Altered TCG card database, which describes itself as a database of Common/Rare non-Unique cards in supported languages.

Upstream: https://github.com/PolluxTroy0/Altered-TCG-Card-Database
