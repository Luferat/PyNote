from flask import g, render_template


def mod_view(id):
    
    # print('\n\n\n ID:', id, '\n\n\n')
    
    page = {
        'pagetitle': 'Título da Nota',
        'conf': g.conf,
    }
    return render_template('view.html', **page)