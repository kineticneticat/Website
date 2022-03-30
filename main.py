from flask import Flask, render_template, request, make_response, redirect, url_for, Response
import requests
import pickle
import json
from werkzeug.exceptions import HTTPException
import hashlib
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SITEMAP_IGNORE_ENDPOINTS'] = ['/prpo', '/tos']
print(app.config)
pyml = None


def encrypt(data, salt):
    m = hashlib.sha256()
    m.update(bytes(salt + data, encoding='utf-8'))
    return m.digest()


def loggedin(request):
    if request.cookies.get('Logged_In') != 'True':
        output = 'False'
    else:
        output = 'True'
    return output


def user_check(page):
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == True:
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return [page, pyml, Logged_In]


@app.route('/setcookie', methods=['POST'])
def setcookie():
    print('testt')
    if request.method == 'POST':
        user = str(request.form['usrnm'])
        print('testt')
        f = open('secrets/accounts', 'rb')
        accounts = pickle.load(f)
        try:
            accounts[user]['uname']
            FailedLogin = 'no'
        except:
            FailedLogin = 'yes'
        finally:
            try:
                passfinder = accounts[user]['pass']
            except:
                passfinder = None
            usedpass = encrypt(request.form['loginpass'], accounts[user]['uname'])
            print(f'  pass : {passfinder}')
            print(f'  pass : {type(passfinder)}')
            print(f'inpass : {usedpass}')
            print(f'inpass : {type(usedpass)}')
            print(f'match: {passfinder == usedpass}')

            if usedpass == passfinder and FailedLogin != 'yes':
                Logged_In = "True"
            else:
                Logged_In = "False"
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('userID', user)
            resp.set_cookie('Logged_In', Logged_In)
            f.close()
            return resp
    else:
        return "Failed"


isDark = "True"


@app.route('/')
def home():
    #    try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('home.html',
                           name=pyml,
                           loggedin=loggedin(request),
                           dark=isDark)


#    except:
#        return 'this page broke lol'


@app.route('/login')
def login():
    return render_template('login.html',
                           value=pyml,
                           loggedin=loggedin(request))


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for("login")))
    resp.set_cookie('userID', "nut")
    resp.set_cookie('Logged_In', "False")
    print(resp)
    return resp


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    passVerified = None
    accounts = {}
    if request.method == 'POST':
        newUN = request.form['newUN']
        pwd = request.form['signuppass']
        repass = request.form['repass']
        if pwd == repass:
            passVerified = 'True'
        else:
            passVerified = 'False'
        f = open('secrets/accounts', 'rb')
        try:
            accounts = pickle.load(f)
        except EOFError as e:
            accounts = {}
            print(f'error:\n {e}')
        f.close()
        try:
            accounts[newUN]
        except:
            print('a')
        finally:
            if passVerified == 'True':
                accounts[newUN] = {"uname": newUN, "pass": encrypt(pwd, newUN)}
                f = open('secrets/accounts', 'wb')
                pickle.dump(accounts, f)
                f.flush()
                f.close()
    return render_template('signup.html',
                           loggedin=loggedin(request),
                           isPassVerified=passVerified)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/projects/metaballs')
def metaballs():
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('metaballs.html',
                           value=pyml,
                           loggedin=loggedin(request))


@app.route('/what')
def what():
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('what.html', value=pyml, loggedin=loggedin(request))


@app.route('/projects/bezier')
def bezier():
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('bezier.html',
                           value=pyml,
                           loggedin=loggedin(request))


# @app.errorhandler(404)
# def error404():
#   return '404', 404


@app.route('/projects/cube')
def cube():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('cube.html', value=pyml, loggedin=loggedin(request))


@app.route('/projects/web')
def web():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('web.html', value=pyml, loggedin=loggedin(request))


# except:
#     return 'this page broke lol'


@app.route('/tos')
def tos():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    try:
        source = request.args['source']
    except KeyError:
        source = 'unknown'
    return render_template('tos.html',
                           value=pyml,
                           loggedin=loggedin(request),
                           source=source)


# except:
#     return 'this page broke lol'


@app.route('/prpo')
def prpo():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    try:
        source = request.args['source']
    except KeyError:
        source = 'unknown'
    return render_template('prpo.html',
                           value=pyml,
                           loggedin=loggedin(request),
                           source=source)


# except:
#     return 'this page broke lol'


@app.route('/account')
def account():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    print(pyml)
    return render_template('account.html',
                           name=pyml,
                           loggedin=loggedin(request),
                           test='aaaaaaaaaaaaaaa')

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route('/sitemap.xml')
def sitemap():

    urls = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if url not in app.config['SITEMAP_IGNORE_ENDPOINTS']:
                urls.append(url)
    xml = render_template('sitemap.xml', urls=urls, base_url='https://kineticcat.ml', mimetype='text/xml')

    return Response(xml, mimetype='text/xml')

@app.route('/robots.txt')
def robots():
    urls = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if url in app.config['SITEMAP_IGNORE_ENDPOINTS']:
                urls.append(url)
    txt = render_template('robots.txt', urls=urls, base_url='https://kineticcat.ml', mimetype='text/plain')
    return Response(txt, mimetype='text/plain')

@app.errorhandler(HTTPException)
def handle_exception(e):
    if e.code == 404:
        return render_template('404.html')
    else:
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response


@app.route('/projects/triangle')
def triangle():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('triangle.html', value=pyml)


@app.route('/cookies')
def cookies():
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('cookie_desc.html',
                           value=pyml,
                           loggedin=loggedin(request))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)