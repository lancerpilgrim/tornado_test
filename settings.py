import os
import logging
import logging.config
from werkzeug.local import LocalProxy


class Log:
    conf = {
        'version': 1,
        'formatters': {
            'basic': {
                'format': '%(asctime)s %(name)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'basic',
            },
            'rotate_mp': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'level': 'DEBUG',
                'formatter': 'basic',
                'when': 'D',
                'interval': 1,
                'filename': os.getenv('LOG', './api.log'),
            }
        },
        'loggers': {
            'root': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },

            'api': {
                'level': 'DEBUG',
                'handlers': ['console', 'rotate_mp'],
                'datefmt': '%Y-%m-%d %H:%M:%S',
                'propagate': 0,
            }
        },
    }

    logging.config.dictConfig(conf)


logger = logging.getLogger('api')


class MySQL:
    host = os.getenv('MYSQL_BD_HOST', '127.0.0.1')
    port = int(os.getenv('MYSQL_BD_PORT', 3306))
    user = os.getenv('MYSQL_BD_USER', 'root')
    database = os.getenv('MYSQL_BD_DATABASE', 'bidong')
    password = os.getenv('MYSQL_BD_PASSWORD', '123456')
    charset = 'utf8'
    url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'.format(
        user, password, host, port, database, charset)
