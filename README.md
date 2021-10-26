# Twitter 2 Telegram forwarder bot
Bot that forwards messages from Twitter to Telegram users, groups or channels.
> Based on https://github.com/franciscod/telegram-twitter-forwarder-bot

## Setup
#### 1. Telegram
1. Create a public channel.
1. Copy channel id: @xxxxxxxxxx.
1. Create a Telegram bot via BotFather (https://t.me/botfather).
1. Copy bot API token.
1. Add bot as administrator to your channel.

#### 2. Twitter
1. Open https://developer.twitter.com/en/apps and create a new app.
1. Copy `Access token`, `Access token secret`, `API key`, `API secret key`.

#### 3. Secrets.env
Fill secrets.env file.

#### 4. Python and virtualenv
Install pyenv and python 3.6.12:
```bash
brew install openssl readline sqlite3 xz zlib
curl https://pyenv.run | bash
pyenv install 3.6.12
```
Create virtual environment and install packages:
```bash
pyenv virtualenv 3.6.12 twtr2telega
pyenv local twtr2telega
pip install -r requirements.txt
```

#### 5. Run bot
```bash
python main.py
```

#### 6. Configure bot
1. Set timezone.
1. Add subs.

### Deployment to AWS EC2
1. Update AWS_ACCOUNT_ID in build.sh and run.sh files.
1. Create ECR repo.
1. Run `build.sh`.
1. Copy files to EC2:
```
sudo scp -i \
    "~/.ssh/xxxxxxxx.pem" \
    ./secrets.env ./peewee.db ./run.sh \
    xxxxxxxx@yyyyyyyyy.compute-1.amazonaws.com:/home/ec2-user/twtr2telega
```
1. Ssh to your EC2:
```bash
ssh -i "xxxxxxxx.pem" xxxxxxxx@yyyyyyyyy.compute-1.amazonaws.com
```
1. Stop and remove container:
```bash
docker stop twtr2telega
docker rm twtr2telega
``` 
1. Run `run.sh`

### Docker commands
```bash
docker build --pull --rm -f "Dockerfile" -t twtr2telega:2 "."
docker run -it --rm \
    --env-file secrets.env \
    --mount type=bind,source=$(pwd)/peewee.db,target=/usr/app/twtr2telega/peewee.db \
    twtr2telega:2
```
