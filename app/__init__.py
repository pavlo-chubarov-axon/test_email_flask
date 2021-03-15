import os

from flask import Flask, request

# initialization
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])  # for ex. config.StagingConfig in config.py

from .email import send_email


@app.route('/email/send/')
def hello_world():
    user_email = request.args.get('email')
    send_email([user_email])
    return f'The email send to {user_email}'
