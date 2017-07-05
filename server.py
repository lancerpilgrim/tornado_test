__author__ = "Lancer"
__email__ = "lancerpilgrim@outlook.com"
__date__ = "$2017-5-20 00:00:00$"
import os
import yaml

from tornado import ioloop
from tornado.web import Application
from tornado.options import define, options, parse_command_line

from config.config import logger, WebServerConfig
from routes import ROUTES

define('port', default=8888, type=int)
define('host', default='0.0.0.0', type=str)
define('env', default='/etc/env.yaml', type=str)


def setup_env(env):
    """
    初始化环境变量
    """

    def _(prefix, conf):
        if not isinstance(conf, dict) and prefix:
            os.environ[prefix.upper()] = str(conf)
        else:
            for k, v in conf.items():
                if prefix:
                    _('{}_{}'.format(prefix, k).upper(), v)
                else:
                    _(k.upper(), v)

    with open(env) as f:
        _conf = yaml.load(f)
        _('', _conf)


def setup_app():
    application = Application(ROUTES, **WebServerConfig)
    return application


if __name__ == '__main__':
    parse_command_line()
    setup_env(options.env)
    app = setup_app()
    app.listen(options.port, options.host)
    ioloop.IOLoop.current().start()
    logger.info('Run server on port {}'.format(options.port))
