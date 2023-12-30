from flask import Flask, render_template, session
from routes.start import start_page

app = Flask(__name__)
app.register_blueprint(start_page)
