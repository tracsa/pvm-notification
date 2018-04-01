from lib.logger import log
from lib.loop import Loop
from itacate import Config
import time
import os

if __name__ == '__main__':
    # Load the config
    config = Config(os.path.dirname(os.path.realpath(__file__)))
    config.from_pyfile('settings.py')
    config.from_envvar('PVM_NOTIFICATOIN_SETTINGS', silent=False)

    # Set the timezone
    os.environ['TZ'] = config['TIMEZONE']
    time.tzset()

    # Logging stuff
    import logging

    logging.basicConfig(
        format = '[%(levelname)s] %(message)s - %(filename)s:%(lineno)s',
        level  = config['LOG_LEVEL'],
    )

    # Run the event loop
    loop = Loop(config)
    loop.run()
