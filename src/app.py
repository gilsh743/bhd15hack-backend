from flask import Flask, request

from queries import *
from db import *

import v1

ORIGINAL = "orig"
TRANSLATED = "translated"

app = Flask(__name__, static_folder='static')
app.register_blueprint(v1.bp, url_prefix='/api')
mysql = get_mysql_by_app(app)


@app.route('/api/addTranslation', methods=['GET', 'POST'])
def add_translation():
    """
    add translated texts to the db
    """
    with mysql.connect() as curr:
        content = request.json
        sentences = content["transSentences"]
        insertion = []
        insert_query = INSERT_QUERY
        for row in sentences:
            insertion.append(str((row[ORIGINAL], row[TRANSLATED])))
            insert_query += u"('{0}','{1}'),".format(row[ORIGINAL], row[TRANSLATED])

        insert_query = insert_query[:-1] + ";"
        curr.execute(insert_query)
    return ""
