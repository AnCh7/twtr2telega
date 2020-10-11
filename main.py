import logging

import tweepy
from envparse import Env
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext.messagehandler import MessageHandler, Filters

from bot import TwitterForwarderBot
from commands import *
from job import FetchAndSendTweetsJob

env = Env(
    TELEGRAM_BOT_TOKEN=str,
    TELEGRAM_CHAT_ID=str,
    TWITTER_API_KEY=str,
    TWITTER_API_KEY_SECRET=str,
    TWITTER_ACCESS_TOKEN=str,
    TWITTER_ACCESS_TOKEN_SECRET=str,
)

if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

    logging.getLogger(TwitterForwarderBot.__name__).setLevel(logging.DEBUG)
    logging.getLogger(FetchAndSendTweetsJob.__name__).setLevel(logging.DEBUG)

    # initialize Twitter API
    auth = tweepy.OAuthHandler(env('TWITTER_API_KEY'), env('TWITTER_API_KEY_SECRET'))
    try:
        auth.set_access_token(env('TWITTER_ACCESS_TOKEN'), env('TWITTER_ACCESS_TOKEN_SECRET'))
    except KeyError:
        print("Either TWITTER_ACCESS_TOKEN or TWITTER_ACCESS_TOKEN_SECRET "
              "environment variables are missing. "
              "Tweepy will be initialized in 'app-only' mode")

    twapi = tweepy.API(auth)

    # initialize Telegram API
    token = env('TELEGRAM_BOT_TOKEN')
    chat_id = env('TELEGRAM_CHAT_ID')  # always using same chat
    updater = Updater(bot=TwitterForwarderBot(token, chat_id, twapi))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', cmd_start))
    dispatcher.add_handler(CommandHandler('help', cmd_help))
    dispatcher.add_handler(CommandHandler('sub', cmd_sub, pass_args=True))
    dispatcher.add_handler(CommandHandler('unsub', cmd_unsub, pass_args=True))
    dispatcher.add_handler(CommandHandler('list', cmd_list))
    dispatcher.add_handler(CommandHandler('export', cmd_export))
    dispatcher.add_handler(CommandHandler('all', cmd_all))
    dispatcher.add_handler(CommandHandler('wipe', cmd_wipe))
    dispatcher.add_handler(CommandHandler('auth', cmd_get_auth_url))
    dispatcher.add_handler(CommandHandler('verify', cmd_verify, pass_args=True))
    dispatcher.add_handler(CommandHandler('export_friends', cmd_export_friends))
    dispatcher.add_handler(CommandHandler('set_timezone', cmd_set_timezone, pass_args=True))
    dispatcher.add_handler(MessageHandler([Filters.text], handle_chat))

    queue = updater.job_queue
    queue.put(FetchAndSendTweetsJob(), next_t=0)

    updater.start_polling()
