name=CONTRIBUTING.md
# How to contribute

1. Edite `species.json` mantendo a estrutura `cardId -> charaIndex -> { ... }`.
2. Incremente `version` em +1 e atualize `updatedAt`.
3. Rode `python scripts/validate.py` antes de abrir o PR.
4. **Não copie texto de wikis para `profile`.** Escreva 1-2 frases originais e curtas. Se não tiver certeza, deixe `profile: null`.
5. `cardId` deve ser o `dimId` do header do card (visível ao ler o card com o dumper), não um índice arbitrário.