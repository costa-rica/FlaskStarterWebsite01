from flask import Flask
# from .._common.config import config
from ._common.config import config
import os
# import logging
# from logging.handlers import RotatingFileHandler
from pytz import timezone
from datetime import datetime
# from ws_models import Base, engine, login_manager
from fsw_models import Base, engine
from ._common.utilities import login_manager, custom_logger_init, teardown_appcontext
from flask_mail import Mail
import secure


if not os.path.exists(os.path.join(os.environ.get('WEB_ROOT'),'logs')):
    os.makedirs(os.path.join(os.environ.get('WEB_ROOT'), 'logs'))


logger_init = custom_logger_init()

logger_init.info(f'--- Starting Flask Starter Website 01 ---')
TEMPORARILY_DOWN = "ACTIVE" if os.environ.get('TEMPORARILY_DOWN') == "1" else "inactive"
logger_init.info(f"- TEMPORARILY_DOWN: {TEMPORARILY_DOWN}")
logger_init.info(f"- FSW_CONFIG_TYPE: {os.environ.get('FSW_CONFIG_TYPE')}")


if os.environ.get('FSW_CONFIG_TYPE')=='workstation':
    logger_init.info(f"- ! This should not print if not local ! -")
    logger_init.info(f"- MYSQL_DB_URI: {config.MYSQL_DB_URI}")
    logger_init.info(f"- ! This should not print if not local ! -")


mail = Mail()
secure_headers = secure.Secure()

def create_app(config_for_flask = config):
    app = Flask(__name__)
    app.teardown_appcontext(teardown_appcontext)
    app.config.from_object(config_for_flask)
    login_manager.init_app(app)
    mail.init_app(app)


    ############################################################################
    ## create folders for DB_AUXILIARY
    create_folder(config_for_flask.DB_AUXILIARY)
    create_folder(config_for_flask.DIR_LOGS)
    # website files
    create_folder(config_for_flask.WEBSITE_FILES)
    create_folder(config_for_flask.DIR_WEBSITE_IMAGES)
    create_folder(config_for_flask.DIR_WEBSITE_VIDEOS)
    # database
    create_folder(config_for_flask.DATABASE_HELPERS)
    create_folder(config_for_flask.DB_UPLOAD)
    ############################################################################
    # Build MySQL database
    # Base.metadata.create_all(engine)
    logger_init.info(f"- MYSQL_USER: {config_for_flask.MYSQL_USER}")
    logger_init.info(f"- MYSQL_DATABASE_NAME: {config_for_flask.MYSQL_DATABASE_NAME}")

    from app_package.bp_main.routes import bp_main
    from app_package.bp_users.routes import bp_users
    # from app_package.bp_error.routes import bp_error
    # from app_package.bp_admin.routes import bp_admin

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_users)
    # app.register_blueprint(bp_error)
    # app.register_blueprint(bp_admin)

    return app

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger_init.info(f"created: {folder_path}")