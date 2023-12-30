from flask import Blueprint

start_page = Blueprint('start_page', __name__, template_folder='templates')


@start_page.route("/")
def show():
    return "<p>Japão!</p>"
