# AI-DMC application workspace

## Scope

This checkout implements Person 2: Application Engineer and the authorized shared project setup. Do not implement Person 1's OCR, extraction, LLM classification, evaluation, or authoritative taxonomy. Temporary fixtures belong under backend/app/integrations, clearly labeled demo.

## Sources

- Approved design: docs/superpowers/specs/2026-10-31-application-engineer-design.md.
- Frontend design: .agents/skills/ai-dmc-apple-glass-ui/SKILL.md.
- Implementation checklist: docs/superpowers/plans/2026-10-31-application-engineer.md.

The source team guide names five database tables. Its mention of six in P2-03 was clarified by the user: implement five.

## Working rules

Preserve the pipeline output and API contracts. Document proposed interface changes before implementing them. Respect lecturer access rules on every file and document operation. Never commit real documents, data/, storage/, .env, credentials, or local databases. Keep mock results visibly distinct from real processing.

Check backend tests and frontend production build for relevant changes. Validate PostgreSQL migrations against PostgreSQL when Docker or a database is available; SQLite tests do not replace that check. Report checks that could not be run. Partner review, real pipeline integration, server deployment, and lecturer trials are external gates, not local completion claims.
