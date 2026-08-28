import os

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def get_connection():
    return psycopg.connect(DATABASE_URL)


def get_all_urls():
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
        cur.execute('''
            SELECT urls.id,
                   urls.name,
                   last_checks.created_at AS last_check_created_at,
                   last_checks.status_code AS last_check_status_code
            FROM urls
            LEFT JOIN (
                SELECT DISTINCT ON (url_id) url_id, created_at, status_code
                FROM url_checks
                ORDER BY url_id, id DESC
            ) AS last_checks ON last_checks.url_id = urls.id
            ORDER BY urls.id DESC
        ''')
        return cur.fetchall()


def find_url_by_id(url_id):
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
        cur.execute('SELECT id, name, created_at FROM urls WHERE id = %(id)s', {'id': url_id})
        return cur.fetchone()


def find_url_by_name(name):
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
        cur.execute('SELECT id, name, created_at FROM urls WHERE name = %(name)s', {'name': name})
        return cur.fetchone()


def save_url(name):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            'INSERT INTO urls (name) VALUES (%(name)s) RETURNING id',
            {'name': name}
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id


def create_check(url_id):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            'INSERT INTO url_checks (url_id) VALUES (%(url_id)s) RETURNING id',
            {'url_id': url_id}
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id


def get_checks(url_id):
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            'SELECT * FROM url_checks WHERE url_id = %(url_id)s ORDER BY id DESC',
            {'url_id': url_id}
        )
        return cur.fetchall()