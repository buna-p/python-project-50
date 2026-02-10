# Gendiff

 —  утилита для поиска различий между двумя файлами формата YAML/JSON.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/buna-p/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/buna-p/python-project-50/actions)

## Возможности

- Сравнение файлов в формате YAML/JSON.
- Вывод различий в трех форматах:
  - json — выводит результат в формате JSON;
  - stylish — выводит результат в легкочитаемом формате;
  - plain — выводит разницу в виде текста.

## Работа

Установка:
1. Клонируйте репозиторий командой git clone.
2. Установите пакет командой make install.

Запуск по команде:
    gendiff [-h] [-f FORMAT] first_file second_file

Опции:
    -h, --help — показать справку;
    -f, --format — задать формат вывода (stylish, plain, json).


## Примеры работы