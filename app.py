from flask import Flask, g, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pynotepad'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = 'utf8mb4'

mysql = MySQL(app)


@app.before_request
def start():

    cur = mysql.connection.cursor()
    cur.execute("SET NAMES utf8mb4")
    cur.execute("SET character_set_connection=utf8mb4")
    cur.execute("SET character_set_client=utf8mb4")
    cur.execute("SET character_set_results=utf8mb4")
    cur.execute("SET lc_time_names = 'pt_BR'")

    sql = "SELECT var, val FROM config"
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()

    # print('\n\n\n ROW:', rows, '\n\n\n')

    g.conf = {}
    for row in rows:
        g.conf[row['var']] = row['val']

    # print('\n\n\n CONF:', g.conf, '\n\n\n')

    pass


@app.route("/")
def index():

    page = {
        'pagetitle': '',
        'conf': g.conf,
    }

    return render_template('index.html', **page)


@app.route("/view/<int:id>")
def view(id: int):
    # print('\n\n\n ID:', id, '\n\n\n')

    page = {
        'pagetitle': 'Título da Nota',
        'conf': g.conf,
    }
    return render_template('view.html', **page)


@app.route("/new", methods=['GET', 'POST'])
def new():

    toForm = {
        'id': 0,
        'title': 'Nova anotação',
        'content': '',
        'placeholder': 'Nova anotação',
        'action': '/new',
        'categories': []
    }

    sql = "SELECT * FROM category ORDER BY cat_name"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()

    # print('\n\n\n ROWS:', rows, '\n\n\n')

    page = {
        'pagetitle': 'Nova Anotação',
        'conf': g.conf,
        'css': 'new.css',
        'js': 'form.js',
        'toForm': toForm,
        'categories': rows,
    }

    if request.method == 'POST':

        form = dict(request.form)
        form['categories'] = request.form.getlist('categories')

        # print('\n\n\n FORM:', form, '\n\n\n')

    return render_template('new.html', **page)


@app.route('/about')
def about():

    page = {
        'pagetitle': 'Sobre...',
        'conf': g.conf,
    }
    return render_template('about.html', **page)


@app.route('/policies')
def policies():
    page = {
        'pagetitle': 'Sua Privacidade',
        'conf': g.conf,
    }
    return render_template('policies.html', **page)


@app.errorhandler(404)
def page_not_found(e):
    page = {
        'pagetitle': 'Erro 404',
        'conf': g.conf,
    }
    return render_template('404.html', **page), 404


if __name__ == '__main__':
    app.run(debug=True)
