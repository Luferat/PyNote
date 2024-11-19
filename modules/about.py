from flask import g, render_template


def mod_about():

    page = {
        'pagetitle': 'Sobre...',
        'conf': g.conf,
    }
    return render_template('about.html', **page)
