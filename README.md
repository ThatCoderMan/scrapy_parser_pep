# Парсер Python.org

![workflows](https://github.com/ThatCoderMan/scrapy_parser_pep/actions/workflows/workflow.yml/badge.svg)

<details>
<summary>Project stack</summary>

- Python 3.10
- Scrapy
- GitHub Actions

</details>

### Описание
Данный код представляет собой асинхронный парсер документации Python 
при помощи библиотеки **scrapy**. Он предоставляет возможность получить 
информацию о PEP (Python Enhancement Proposal) и их статусах.


### Инструкция по запуску:
Клонируйте репозиторий:
```commandline
git clone git@github.com:ThatCoderMan/scrapy_parser_pep.git
```
Установите и активируйте виртуальное окружение:

- *для MacOS:*
    ```commandline
    python3 -m venv venv
    ```
- *для Windows:*
    ```commandline
    python -m venv venv
    source venv/bin/activate
    source venv/Scripts/activate
    ```
Установите зависимости из файла requirements.txt:
```commandline
pip install -r requirements.txt
```

### Использование:
Для запуска парсера необходимо перейти в папку pep_parse:
```commandline
cd pep_parse
```
И выполнить команду:
```commandline
scrapy crawl pep 
```
Результаты будут сохранены в папке results
- в файле pep_<date>.csv находится информация по всем PEP (их номер, название и статус)
- в файле status_summary_<date>.csv находится информация о колличестве статусов PEP


### Автор проекта:

[Artemii Berezin](https://github.com/ThatCoderMan)
