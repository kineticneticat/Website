from flask import Flask, render_template, request, make_response, redirect, url_for, Response
import pickle
import json
from werkzeug.exceptions import HTTPException
import hashlib
import datetime

app = Flask(__name__)
app.config['SITEMAP_IGNORE_ENDPOINTS'] = ['/prpo', '/tos', '/debug']
app.config['ROBOTS_IGNORE_ENDPOINTS'] = []
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
            usedpass = encrypt(request.form['loginpass'],
                               accounts[user]['uname'])

            if usedpass == passfinder and FailedLogin != 'yes':
                Logged_In = "True"
            else:
                Logged_In = "False"
            resp = make_response(redirect(url_for('home')))
            date = datetime.datetime.today()
            resp.set_cookie('userID',
                            user,
                            expires=datetime.datetime(date.year + 1,
                                                      date.month, date.day,
                                                      date.hour + 1,
                                                      date.minute, date.second,
                                                      date.microsecond))
            resp.set_cookie('Logged_In',
                            Logged_In,
                            expires=datetime.datetime(date.year + 1,
                                                      date.month, date.day,
                                                      date.hour + 1,
                                                      date.minute, date.second,
                                                      date.microsecond))
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
    resp.set_cookie('userID', "nut", expires=datetime.datetime.today())
    resp.set_cookie('Logged_In', "False", expires=datetime.datetime.today())
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


############ Projects #############


@app.route('/projects')
def projects():
    return render_template('projects.html',
                           pages=[['metaballs', 'Metaballs', False],
                                  ['cube', 'Three.js Cube', False],
                                  ['web', 'Web', True],
                                  ['triangle', 'Triangle', True],
                                  ['iocircle', 'Countdown', False],
                                  ['hilbert', 'Hilbert Curve', False],
                                  ['boids', 'Boids', True],
								  ['iso', 'Isometric', True],
																 ['3d', '3D', True],
																 ['astar', 'A* Algorithm', True],
																 ['periodic', 'Periodic Table', True]])



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


@app.route('/projects/iocircle')
def iocircle():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('iocircle.html', value=pyml)


@app.route('/projects/hilbert')
def hilbert():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('hilbert.html', value=pyml, request=request)


@app.route('/projects/boids')
def boids():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('boids.html', value=pyml, request=request)

@app.route('/projects/iso')
def iso():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('iso.html', value=pyml, request=request)

@app.route('/projects/isogame')
def isogame():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('isogame.html', value=pyml, request=request)

@app.route('/projects/3d')
def threed():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"
    return render_template('3d.html', value=pyml, request=request)


###################Projects#################


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
                           source=source,
                           noindex='True')


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
                           source=source,
                           noindex='True')


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
    xml = render_template('sitemap.xml',
                          urls=urls,
                          base_url='https://kineticcat.ml',
                          mimetype='text/xml')

    return Response(xml, mimetype='text/xml')


@app.route('/robots.txt')
def robots():
    txt = render_template('robots.txt',
                          urls=app.config['ROBOTS_IGNORE_ENDPOINTS'],
                          base_url='https://kineticcat.ml',
                          mimetype='text/plain')
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


@app.route('/debug')
def debug():
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml = "Login"

    urls = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            urls.append(url)
    return render_template('debug.html',
                           value=pyml,
                           loggedin=loggedin(request),
                           urls=urls,
                           noindex='True')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
