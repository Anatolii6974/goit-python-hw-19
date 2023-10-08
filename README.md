HomeWork 09
__________________________________

poetry new hw9scr
cd hw9scr
poetry install
poetry add bs4
poetry add requests

-- Run main.py and create quotes.json and authors.json --
poetry run py main.py

-- Run load_json.py (models.py) from homework 08
poetry add pymongo mongoengine
poetry run py load_json.py
