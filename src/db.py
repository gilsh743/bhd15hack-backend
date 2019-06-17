from flaskext.mysql import MySQL
from conf import APP_MYSQL_CONF

ORIGINAL = "orig"
TRANSLATED = "translated"

def _set_app_mysql_conf(app, app_conf=None):
    if app_conf is None:
        for key, val in APP_MYSQL_CONF.iteritems():
            app.config[key] = val
    else:
        raise NotImplementedError

def _init_mysql(app):
    '''
    Func should be called after init_init_mysql_by_app
    '''
    mysql = MySQL()
    mysql.init_app(app)
    return mysql

def get_mysql_by_app(app):
    _set_app_mysql_conf(app)
    return _init_mysql(app)
