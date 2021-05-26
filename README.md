# Bitly url shorterer

Project has 2 features:
- generates bitlink from typed url
- shows count of clicks from typed bitlink


### How to install

To correct script works you need set BITLY_TOKEN in yours enviroment variable `.env`. 

This token provides access to API [bil.ty](https://app.bitly.com/). You can get token from [tokens generator](https://bitly.com/a/oauth_apps). You need `GENERIC ACCESS TOKEN`

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for learing API web-services [dvmn.org](https://dvmn.org/).