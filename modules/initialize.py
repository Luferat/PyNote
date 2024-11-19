from flask import g


def mod_init(mysql):

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

    g.conf = {}
    for row in rows:
        g.conf[row['var']] = row['val']

    # print('\n\n\n ROW:', rows, '\n\n\n')
    # print('\n\n\n CONF:', g.conf, '\n\n\n')

    pass
