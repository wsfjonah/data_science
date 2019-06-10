import logging
from logging import handlers
import time
import os
import reporting.common.config4me as config


LOG_DIR_DEFAULT = 'c:/var/log/reporting/'
LOG_FORMAT = '%(asctime)15s - %(name)8s - %(levelname)8s: %(message)s'


def info(message):
    log_dir = config.get_config("Logging", "log.dir")
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    # if not os.path.exists(log_dir):
    os.makedirs(log_dir, 0o777, True)

    logger = logging.getLogger()
    filename = "bxru_info_"+time.strftime('%Y-%m-%d', time.localtime(time.time()))

    handler = handlers.RotatingFileHandler(os.path.join(log_dir, filename + ".log"))
    logger.addHandler(handler)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.info(message)
    logger.removeHandler(handler)


if __name__ == "__main__":
    info('test')

