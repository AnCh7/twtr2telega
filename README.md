# Twitter 2 Telegram forwarder bot
Bot that forwards messages from Twitter to Telegram users, groups or channels.
> Based on https://github.com/franciscod/telegram-twitter-forwarder-bot

## Setup

#### Telegram
1. Create public channel.
1. Create a Telegram bot: https://t.me/botfather.
1. Set the bot as administrator in your channel.
1. Set timezone.

#### Twitter
1. Open https://developer.twitter.com/en/apps and create a new app.
1. Copy `Access token`, `Access token secret`, `API key`, `API secret key`.

#### Secrets.env
Fill secrets.env file.

#### Python 3.5
Install pyenv and python 3.5.9:
```bash
brew install openssl readline sqlite3 xz zlib
curl https://pyenv.run | bash
pyenv install 3.5.9
```

#### Virtualenv
Create virtual environment and install packages:
```bash
pyenv virtualenv 3.5.9 twtr2telega
pyenv local twtr2telega
pip install -r requirements.txt
```

#### Docker
```bash
docker build --pull --rm -f "Dockerfile" -t twtr2telega:latest "."
docker run --env-file secrets.env --rm -it  twtr2telega:latest
```