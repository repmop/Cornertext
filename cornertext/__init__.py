import flask
import memetext
import makehtmlform
import sys, os
app = flask.Flask(__name__)


path='/var/www/html/faithinnothing.me/cornertext/cornertext/logs.txt'
@app.route('/', methods=['POST', 'GET'])# ,subdomain="cornertext")
def enter(name=None):
    return flask.render_template('Entry.html', name=name)
@app.route('/handle', methods=['POST', 'GET'])#, subdomain="cornertext")
def handle():
    text = flask.request.form['input']
    log = open(path,'wb')
    log.close()
    log = open(path,'wb')
    log.write(text)
    log.close()
    return flask.redirect('/cornertext/entered')
@app.route('/entered')# ,subdomain="cornertext")
def show_meme(name=None):
    txt = open(path, 'r').read()
    raw = memetext.memeify(txt)
    if raw==None: raw=""
    makehtmlform.makeform(raw)
    return flask.render_template('form.html', name=name)

if __name__ == '__main__':
    
    app.run(host= '127.0.1.1', port=5001, debug=True)
