from flask import Flask, render_template

from app.api.group import Group
from .io_handlers.flask_handler import FlaskIOHandler
from .models.leader import Leader
from .models.student import Student
from .storage.pickle_storage import PickleStorage

app = Flask(__name__)

from app.api import bp as api_bp

groups = [["group", api_bp, "/group1"]]

for title, bp, url in groups:
	app.register_blueprint(bp, url_prefix=url)

@app.template_test('instanceof')
def is_instanceof(value, type_name):
    return value.__class__.__name__ == type_name

@app.route("/")
def index():
	r = ""
	for title, bp, url in groups:
		r += f'<a href="{url}">{title}</a><br>'
	return render_template("index.tpl", groups=r)
