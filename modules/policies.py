from flask import g, render_template


def mod_policies():
    page = {
        'pagetitle': 'Sua Privacidade',
        'conf': g.conf,
    }
    return render_template('policies.html', **page)