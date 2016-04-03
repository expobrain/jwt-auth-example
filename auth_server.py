from __future__ import unicode_literals

import json

from flask import Flask, request
import jwt


app = Flask(__name__)
app.config.from_object('settings.shared')
app.config.from_object('settings.auth')


@app.route("/", methods=['POST', 'GET'])
def authenticate():
    data = request.json
    token = jwt.encode(
        {'user': data['username']},
        app.config['SECRET_KEY']
    )
    output = json.dumps({'token': token})

    return output, 200, {
        'Content-Type': 'application/json'
    }


if __name__ == '__main__':
    app.run()
