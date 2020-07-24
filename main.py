from pathlib import Path

import time, datetime
import os
import random
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import logging
import configparser

logs = Path('logs')
log_name = 'logs ' + str(datetime.datetime.strftime(datetime.datetime.now(), '%d_%m_%Y %H.%M.%S')) + '.log'
logging.basicConfig(format=u'[LINE:%(lineno)d]# %(levelname)-9s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=logs/log_name)


class Config:
    config = configparser.ConfigParser()
    config.read('settings.ini')
    access_token = config.get('Config', 'access_token')
    owner_id = config.get('Config', 'owner_id')
    API_version = config.get('Config', 'API_version')


vk = vk_api.VkApi(token=Config.access_token)
logging.info("Everythin' is a'ight")

