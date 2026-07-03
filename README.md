# Bookmark Manager API

A REST API for saving, organizing, and revisiting links — built with
**FastAPI** as a hands-on project to learn how to design and build a backend
API from scratch (routing, request/response validation, databases, auth, and
async I/O).

## Why this project

Most "learn FastAPI" tutorials use a to-do list. This is a bookmark/read-later
manager instead, because it touches a wider range of real backend concepts:

- Standard CRUD (create, read, update, delete)
- Per-user data (auth-gated, not a public list)
- Filtering/searching (by tag, by read status)
- **Calling an external resource from the API itself** — when you save a
  bookmark without a title, the API fetches the page and pulls the `<title>`
  for you, which is a natural intro to async HTTP calls in a backend context

## Planned features

- [ ] User registration & login (JWT-based auth)
- [ ] Create / read / update / delete bookmarks
- [ ] Each bookmark: URL, title, notes, tags, read/unread status
- [ ] Auto-fetch page title when one isn't provided
- [ ] Filter bookmarks by tag and/or read status
- [ ] Auto-generated interactive API docs (`/docs`, built into FastAPI)
- [ ] *(open-ended from here — folders, sharing, import/export, etc. added as I go)*

## Tech stack

| Piece            | Choice                          |
|-------------------|----------------------------------|
| Framework         | FastAPI                          |
| Database          | SQLite (via SQLAlchemy)          |
| Auth              | JWT (`python-jose`) + `passlib` for password hashing |
| Async HTTP calls  | `httpx`                          |
| HTML parsing      | `BeautifulSoup4` (for title fetching) |
| Server            | `uvicorn`                        |

## Project structure

```
app/
  main.py          # app entrypoint, mounts routers
  config.py        # settings
  database.py      # SQLAlchemy engine/session
  models.py        # DB tables (User, Bookmark)
  schemas.py       # Pydantic request/response models
  auth.py          # password hashing + JWT helpers
  utils.py         # async page-title fetcher
  routers/
    auth.py        # /auth/register, /auth/login
    bookmarks.py   # /bookmarks CRUD
requirements.txt
.env.example
```

Each feature area lives in its own router/model, so new functionality can be
added later without reworking what's already there.

## Setup

```bash
git clone <your-repo-url>
cd bookmark-api
pip install -r requirements.txt
cp .env.example .env   # then set a real SECRET_KEY
```

## Run

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive API docs.

## API overview

| Method | Endpoint              | Description                        | Auth required |
|--------|------------------------|-------------------------------------|----------------|
| POST   | `/auth/register`      | Create a new user                  | No             |
| POST   | `/auth/login`         | Log in, get a JWT access token     | No             |
| POST   | `/bookmarks`           | Save a new bookmark                | Yes            |
| GET    | `/bookmarks`           | List your bookmarks (filterable)   | Yes            |
| GET    | `/bookmarks/{id}`      | Get a single bookmark              | Yes            |
| PATCH  | `/bookmarks/{id}`      | Update a bookmark                  | Yes            |
| DELETE | `/bookmarks/{id}`      | Delete a bookmark                  | Yes            |

## Status

🚧 Work in progress — learning project, building incrementally.

## License

MIT
