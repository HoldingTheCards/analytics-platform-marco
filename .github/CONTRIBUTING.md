# Contributing Guidelines

## 1 Issues
Nutze die Issue-Forms:
- Feature: `.github/ISSUE_TEMPLATE/feature_request.yml`
- Bug: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Task: `.github/ISSUE_TEMPLATE/task.yml`

Direktlinks:
- Feature → https://github.com/<USER>/<REPO>/issues/new?template=feature_request.yml
- Bug     → https://github.com/<USER>/<REPO>/issues/new?template=bug_report.yml
- Task    → https://github.com/<USER>/<REPO>/issues/new?template=task.yml

## 2 Branching
- `main` = stabil  
- Feature-Branches: `feat/<kurzbeschreibung>`  
- Fix-Branches: `fix/<kurzbeschreibung>`

## 3 Conventional Commits
Format: `<type>(optional scope): <summary>`
Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

**Beispiele**
- `feat(sql): add window function examples`
- `fix(notebooks): correct data path in EDA notebook`
- `docs: add visual roadmap to README`

## 4 Pull Requests
- Ein PR pro Thema, kleiner Scope.
- Nutze das PR-Template: `.github/PULL_REQUEST_TEMPLATE.md`
- Verlinke Issues: `Closes #<id>`
- Checklist vollständig abhaken (Tests/Lint falls vorhanden, Docs aktualisiert).

## 5 Reviews & CODEOWNERS
- CODEOWNERS triggert automatisch Review-Requests an @marco-knieling.

## 6 Versionierung mit Git-Tags
- `v1.0` – Fundament & Setup  
- `v1.1` – ...  
- `v2.0` – ...

Befehle:
```bash
git tag -a v1.0 -m "Version 1.0 – Fundament & Setup"
git push origin v1.0