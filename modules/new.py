from flask import g, render_template, request


def mod_new(mysql):

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

        print('\n\n\n FORM:', form, '\n\n\n')

    return render_template('new.html', **page)
