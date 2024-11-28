# Simple checker AI bot

## Installation
1) Clone this repo:
```shell
$ git clone https://github.com/omadli/checker_aibot
```

2) Open folder:
```shell
$ cd checker_aibot
```

3) Create virtual environment for python:
```shell
$ python3 -m pip install virtualenv
$ python3 -m venv venv
```

4) Activate virtual environment
- In windows:
```shell
$ .\venv\Scripts\activate
```
- In Linux (like Ubuntu, Kali, Debian):
```shell
$ source venv/bin/activate
```

5) Install requirements, python libraries:
```shell
$ pip install -r requirements.txt
```

6) Configurate `.env` values. Copy from `.env.example` file and create `.env` file.
```shell
$ cp .env.dist .env
```

7) Open `.env` file and edit your environment variables - **BOT_TOKEN**, **** and others.
Values:
 - **BOT_TOKEN** - Bot token from [@botfather](https://t.me/botfather)
 - **OPENAI_API_KEY** - OPENAI_API_KEY from [OpenAI Platform](https://platform.openai.com/settings/organization/api-keys)
 - **DEBUG** - boolean True or False for debugging
 - **ADMINS** - list[int] bot admins's telegram id number
 - **DB_URL** - Database connection URL like postgresql, mysql or sqlite3 (sqlite3 has problems with async)
 - **USE_REDIS** - boolean: True or False if True use `redis` for caching
 - **REDIS_DB** - `redis` database number (if USE_REDIS is True)
 - **REDIS_PASSWORD** - `redis` database password (if USE_REDIS is True)

8) Create `google_credentials.json` like `google_credentials_example.json` file with your datas for google sheet API.

9) Configure Database
Install and configure database (PostgreSQL, MySQL or others). Create schemas using these commands:
```shell
$ aerich init -t settings.TORTOISE_ORM
$ aerich init-db
```
Migrations:
```shell
$ aerich migrate
$ aerich upgrade
```

10) Installation done. Now you can run bot:
```shell
python main.py
```
<hr>
<br>

## Enable google sheets API and download credentials
### Enable API Access for a Project
1) Head to [Google Developers Console](https://console.developers.google.com/) and create a new project (or select the one you already have).

2) In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.

3) In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.

### For Bots: Using Service Account
A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs [sic].

Since it’s a separate account, by default it does not have access to any spreadsheet until you share it with this account. Just like any other Google account.

Here’s how to get one:

1) Enable API Access for a Project if you haven’t done it yet.

2) Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.

3) Fill out the form

4) Click “Create” and “Done”.

5) Press “Manage service accounts” above Service Accounts.

6) Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.

7) Select JSON key type and press “Create”.

You will automatically download a JSON file with credentials. It may look like `google_credentials_example.json`
