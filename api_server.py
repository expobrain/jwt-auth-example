from __future__ import unicode_literals

from flask import Flask, request, abort
import jwt


app = Flask(__name__)
app.config.from_object('settings.shared')
app.config.from_object('settings.api')


@app.route("/greetings/")
def greetings():
    # Get header
    authorization_header = request.headers.get('Authorization')

    if not authorization_header:
        abort(400, 'Missing Authorization header')

    if not authorization_header.startswith('Bearer'):
        abort(400, 'Invalid token type')

    # Get token
    type_, token = authorization_header.split()

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
    except jwt.DecodeError:
        abort(400, 'Invalid token')

    # Return response
    output = 'Hello {}'.format(data['user'])

    return output


if __name__ == '__main__':
    app.run()
