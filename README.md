# Bitly URL shortener

Project has 2 features:
- generates bitlink from typed URL.
- shows count of clicks from typed bitlink.


### How to install

You need to set BITLY_TOKEN in `.env` file. The syntax of `.env` file supported by python-dotenv:
```
# a comment and that will be ignored.
REDIS_ADDRESS=localhost:6379
MEANING_OF_LIFE=42
MULTILINE_VAR="hello\nworld"
```
Then adds them to environment variable using [python-dotenv](https://pypi.org/project/python-dotenv/0.9.1/):
```
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BITLY_TOKEN')
```
A CLI interface dotenv is also included, which helps you manipulate the `.env` file without manually opening it:
```
$ pip install "python-dotenv[cli]"
$ dotenv set USER=foo
$ dotenv set EMAIL=foo@example.org
$ dotenv list
USER=foo
EMAIL=foo@example.org
$ dotenv run -- python foo.py
```

This token provides access to API [bil.ty](https://app.bitly.com/). 

You can get token from [tokens generator](https://bitly.com/a/oauth_apps). You need `GENERIC ACCESS TOKEN`.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for learning API web-services [dvmn.org](https://dvmn.org/).