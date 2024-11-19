from flask import render_template, g


def mod_index():

    page = {
        'pagetitle': '',
        'conf': g.conf,
    }

    return render_template('index.html', **page)
