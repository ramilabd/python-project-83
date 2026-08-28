import os

from flask import Flask, abort, flash, redirect, render_template, request, url_for

from page_analyzer import repository, url_utils

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls', methods=['POST'])
def add_url():
    raw_url = request.form.get('url', '')
    errors = url_utils.validate_url(raw_url)

    if errors:
        return render_template('index.html', errors=errors, url=raw_url), 422

    name = url_utils.normalize_url(raw_url)
    existing_url = repository.find_url_by_name(name)

    if existing_url:
        flash('Страница уже существует', 'info')
        return redirect(url_for('show_url', id=existing_url['id']))

    new_id = repository.save_url(name)
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('show_url', id=new_id))


@app.route('/urls')
def urls():
    all_urls = repository.get_all_urls()
    return render_template('urls.html', urls=all_urls)


@app.route('/urls/<int:id>')
def show_url(id):
    url = repository.find_url_by_id(id)
    if url is None:
        abort(404)
    return render_template('url.html', url=url)