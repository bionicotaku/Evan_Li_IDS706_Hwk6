[![CI](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk6/actions/workflows/cicd.yml/badge.svg)](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk6/actions/workflows/cicd.yml)
## Evan_Li_IDS706_Hwk6
### File Structure
```
Evan_Li_IDS706_Hwk6/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── data/
│   └── create.sql
│   └── load.sql
│   └── mydatabase.db   -> database
├── LICENSE
├── main.py
├── Makefile
├── mylib/
│   ├── gen.py          -> generate sample data
│   ├── setup.py        -> create database and load data
│   ├── CRUD.py         -> CRUD operations
├── README.md
├── requirements.txt
└── test_main.py
```
## Intrduction

This project will first create a database with 3 tables (users, products, orders), generate sample data and load. Then, it will test the create, read, update, delete operations.

## Preparation
1. Install all the packages `make install`
2. Format code `make format`
3. Lint code `make lint`
4. Test coce `make test`

## CRUD
1. Create database, generate sample data and load  `make database-setup`
2. Test CRUD operations `make run-crud`
