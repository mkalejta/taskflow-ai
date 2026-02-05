# taskflow-ai
Platforma do automatyzacji codziennych zadan i przeplywow pracy (workflow) z wykorzystaniem AI, np. podzial zadan na etapy, sugerowanie terminow, analizowanie priorytetow oraz integracja z popularnymi narzedziami (e-mail, kalendarz, Slack, Trello, JIRA).

## Stack
- Frontend: Next.js 15, React 19
- Backend: FastAPI, SQLAlchemy, Alembic
- Baza danych: PostgreSQL 16

## Uruchomienie (Docker)
Najprostsza metoda to uruchomienie skryptu, ktory czysci kontenery i wolumeny (resetuje baze danych), a nastepnie startuje aplikacje:

```bash
bash scripts/run.sh
```

Po starcie:
- Frontend: http://localhost:3000
- API: http://localhost:8000

Alternatywnie bez skryptu:

```bash
docker compose up -d --build
```

## Zmienne srodowiskowe
Mozesz ustawic je w shellu lub w pliku `.env` w katalogu glowym:

- `PG_USER` (domyslnie `taskflow`)
- `PG_PASSWD` (domyslnie `taskflow`)
- `PG_DB` (domyslnie `taskflow`)
- `PG_PORT` (domyslnie `5432`)
- `OPENAI_API_KEY` (opcjonalne, dla funkcji AI)
- `NEXT_PUBLIC_API_URL` (domyslnie `http://localhost:8000`)

## Zatrzymanie
```bash
docker compose down
```
