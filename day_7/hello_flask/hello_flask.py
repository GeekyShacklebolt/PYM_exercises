#!/home/coderunner/Public/GithubRepos/PYM_exercises/day_5/virtual/virtual1/bin/python3

import flask

# creating the application
APP = flask.Flask('__name__')

@APP.route('/')
def index():
    """ Display the index page accessible at '/'"""
    return flask.render_template("index.html")


@APP.route('/hello/<name>/')
def hello(name):
    """ Display greatings to the visitor."""
    return flask.render_template('hello.html', name=name)


if __name__=='__main__':
    APP.debug=True
    APP.run()
