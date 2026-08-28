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
        cur.execute('SELECT id, name, created_at FROM urls ORDER BY id DESC')
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