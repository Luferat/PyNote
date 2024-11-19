from flask import g, render_template


def mod_404():
    page = {
        'pagetitle': 'Erro 404',
        'conf': g.conf,
    }
    return render_template('404.html', **page), 404