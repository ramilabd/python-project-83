from urllib.parse import urlparse

import validators


def normalize_url(url):
    parsed = urlparse(url)
    return f'{parsed.scheme}://{parsed.netloc}'


def validate_url(url):
    errors = {}
    if not url:
        errors['url'] = 'URL обязателен'
    elif len(url) > 255:
        errors['url'] = 'URL превышает 255 символов'
    elif not validators.url(url):
        errors['url'] = 'Некорректный URL'
    return errors