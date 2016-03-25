from __future__ import unicode_literals

from flask import Flask


app = Flask(__name__)
app.config.from_object('settings.shared')
app.config.from_object('settings.api')


if __name__ == '__main__':
    app.run()
