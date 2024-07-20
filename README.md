### Hexlet tests and linter status:
[![Actions Status](https://github.com/remortalite/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/remortalite/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2295c08218d270007651/maintainability)](https://codeclimate.com/github/remortalite/python-project-83/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2295c08218d270007651/test_coverage)](https://codeclimate.com/github/remortalite/python-project-83/test_coverage)


# Анализатор страниц

Сайт: [Анализатор страниц](https://python-project-83-wnzl.onrender.com)

## Описание

Приложение предназначено для проверки сайтов на доступность, а также вывода основных параметров сайта (заголовки, код ответа, описание сайта если указано).
В проекте используется фреймворк Flask с базой postgresql (psycopg2 для Python).

## Установка и запуск

Для запуска сайта необходимо подготовить базу данных скриптом `build.sh` (можно использовать команду `make build`).
Далее запускается приложения, используя WSGI сервер gunicorn:

```bash
make install start
```

## Примеры работы

