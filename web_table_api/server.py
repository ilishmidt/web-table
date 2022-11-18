import flask
from flask import Flask

server = Flask(__name__, template_folder='../templates')


@server.route("/logs")
def logs():
    return flask.render_template('logs.html')
