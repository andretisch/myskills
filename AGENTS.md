# AGENTS.md

## Repository overview

This repository (`andretisch/myskills`) is a **résumé portfolio** — it contains two PDF résumés and no application source code.

| File | Description |
|------|-------------|
| `Резюме AI ML engineer LLM МЛ-инженер Андрей Владимирович Тишкин от 03-05-2026 18-30.pdf` | AI/ML engineer résumé (5 pages) |
| `Резюме Главный системный администратор Руководитель ИТ-отдела Андрей Владимирович Тишкин от 21-04-2026 17-50.pdf` | Sysadmin / IT lead résumé (5 pages) |

There are no services to start, no dependencies to install, and no lint/test/build commands.

## Cursor Cloud specific instructions

- **No dev server**: Nothing listens on a port. Do not look for `package.json`, `docker-compose.yml`, or similar.
- **No update dependencies**: The VM update script is a no-op (`true`). There is nothing to refresh on startup.
- **Verification**: Confirm the two PDFs exist and are valid with `file *.pdf`. Both should report `PDF document, version 1.5, 5 page(s)`.
- **Optional tooling**: `pdftotext` / `pdfinfo` (from `poppler-utils`) are not installed by default. Install only if you need to extract résumé text for analysis.
- **Branches**: Only `main` exists. No feature branches or application code elsewhere in this repo.
