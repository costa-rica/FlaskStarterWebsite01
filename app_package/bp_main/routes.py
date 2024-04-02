from flask import Blueprint
from flask import render_template, current_app, send_from_directory
import os
from app_package._common.utilities import custom_logger
import datetime
from flask_login import login_required, login_user, logout_user, current_user


logger_bp_main = custom_logger('bp_main.log')
bp_main = Blueprint('bp_main', __name__)


@bp_main.route("/", methods=["GET","POST"])
def home():
    logger_bp_main.info(f"-- in home page route --")
    # Get today's date
    today = datetime.date.today()

    # Format the date as a string with the full month name, date, and year
    formatted_date = today.strftime("%B %d, %Y")

    return render_template('main/home.html', formatted_date = formatted_date)

@bp_main.route("/page2", methods=["GET","POST"])
@login_required
def page2():
    logger_bp_main.info(f"-- in page2 route --")
    # Get today's date
    today = datetime.date.today()

    # Format the date as a string with the full month name, date, and year
    formatted_date = today.strftime("%B %d, %Y")

    return render_template('main/page2.html', formatted_date = formatted_date)
