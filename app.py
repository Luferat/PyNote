from flask import Flask
from flask_mysqldb import MySQL

from config import Config
from modules.about import mod_about
from modules.index import mod_index
from modules.initialize import mod_init
from modules.new import mod_new
from modules.policies import mod_policies
from modules.view import mod_view
from modules.http_errors import mod_404

app = Flask(__name__)

app.config.from_object(Config)
mysql = MySQL(app)


@app.before_request
def start():
    return mod_init(mysql)


@app.route("/")
def index():
    return mod_index()


@app.route("/view/<int:id>")
def view(id: int):
    return mod_view(id)


@app.route("/new", methods=['GET', 'POST'])
def new():
    return mod_new(mysql)


@app.route('/about')
def about():
    return mod_about()


@app.route('/policies')
def policies():
    return mod_policies()


@app.errorhandler(404)
def page_not_found(e):
    return mod_404()


if __name__ == '__main__':
    app.run(debug=True)
