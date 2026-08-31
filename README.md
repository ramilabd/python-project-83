# Анализатор страниц (Python Flask)

[![hexlet-check](https://github.com/ramilabd/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ramilabd/python-project-83/actions)

Веб-приложение, которое проверяет сайты на SEO-пригодность: добавляет URL, делает по нему HTTP-запрос и извлекает `status_code`, `h1`, `title` и `meta description`.

**Демо:** https://page-analyzer-hx3e.onrender.com/

Курс Хекслета: [Python-разработчик](https://ru.hexlet.io/programs/python)

## Стек

Python, Flask, PostgreSQL (psycopg3), Gunicorn, Tailwind CSS, requests, BeautifulSoup4

## Установка

Понадобятся: Python 3.14+, PostgreSQL, `uv` и `npm`.

```bash
git clone https://github.com/ramilabd/python-project-83.git
cd python-project-83

# Установка Python- и JS-зависимостей (uv sync + npm install)
make install
```

Создайте файл `.env` в корне проекта:

```SECRET_KEY=любая_случайная_строка```

```python
python3 -c "import secrets; print(secrets.token_hex(16))"
```

Создайте таблицы в базе данных:

```DATABASE_URL=postgresql://user:password@localhost:5432/page_analyzer```

```bash
psql -a -d $DATABASE_URL -f database.sql
```

## Использование

```bash
# Запуск в режиме разработки (Flask debug-сервер)
make dev

# Сборка CSS + запуск через gunicorn (как в production)
make build
make start
```

Приложение будет доступно на http://localhost:8000 (или на порту из `PORT`).

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме.

Этот репозиторий третий проект курса Хекслета: [Python-разработчик](https://ru.hexlet.io/programs/python).