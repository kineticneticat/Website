from flask import Flask, render_template, request, make_response, redirect, url_for
import json
from flask_sitemap import Sitemap
from werkzeug.exceptions import HTTPException
#aaaa
app = Flask(__name__)
ext = Sitemap(app=app)
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
app.config['SITEMAP_URL_SCHEME'] = 'https'
app.config['SITEMAP_IGNORE_ENDPOINTS'] = '/prpo'
pyml = {}


def loggedin(request):
    if request.cookies.get('Logged_In') != 'True':
        output = 'False'
    else:
        output = 'True'
    return output


def user_check(page):
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == True:
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    return [page, pyml['name'], Logged_In]


@app.route('/setcookie', methods=['POST'])
def setcookie():
    print('testt')
    if request.method == 'POST':
        user = str(request.form['usrnm'])
        print('testt')
        f = open('secrets/accounts.json')
        accounts = f.read()
        accounts_json = json.loads(accounts)
        try:
            accounts_json[user]['uname']
            FailedLogin = 'no'
        except:
            FailedLogin = 'yes'
        finally:
            try:
                passfinder = str(accounts_json[user]['pass'])
            except:
                passfinder = None
            usedpass = str(request.form['loginpass'])
            print(f'pass : {passfinder}')
            print(f'inpass : {usedpass}')

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
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    return render_template('home.html',
                           name=pyml['name'],
                           loggedin=loggedin(request),
                           dark=isDark)


#    except:
#        return 'this page broke lol'


@app.route('/login')
def login():
    return render_template('login.html',
                           value=pyml['name'],
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
    try:
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
            f = open('secrets/accounts.json')
            accounts = json.loads(f.read())
            f.close()
            try:
                accounts[newUN]
            except:
                print('a')
            finally:
                if passVerified == 'True':
                    accounts[newUN] = {"uname": newUN, "pass": pwd}
                    f = open('secrets/accounts.json', 'w')
                    f.write(json.dumps(accounts, indent=2))
                    f.flush()
                    f.close()
        return render_template('signup.html',
                               loggedin=loggedin(request),
                               isPassVerified=passVerified)
    except:
        return 'this page broke lol'


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/projects/metaballs')
def metaballs():
    try:
        Logged_In = request.cookies.get('Logged_In')
        if Logged_In == "True":
            pyml['name'] = request.cookies.get('userID')
        else:
            Logged_In = "False"
            pyml['name'] = "Login"
        print(pyml['name'])
        return render_template('metaballs.html',
                               value=pyml['name'],
                               loggedin=loggedin(request))
    except:
        return 'this page broke lol'


@app.route('/what')
def what():
    try:
        return render_template('what.html')
    except:
        return 'this page broke lol'


@app.route('/projects/bezier')
def bezier():
    try:
        Logged_In = request.cookies.get('Logged_In')
        if Logged_In == "True":
            pyml['name'] = request.cookies.get('userID')
        else:
            Logged_In = "False"
            pyml['name'] = "Login"
        print(pyml['name'])
        return render_template('bezier.html',
                               value=pyml['name'],
                               loggedin=loggedin(request))
    except:
        return 'this page broke lol'


# @app.errorhandler(404)
# def error404():
#   return '404', 404


@app.route('/projects/cube')
def cube():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    return render_template('cube.html',
                           value=pyml['name'],
                           loggedin=loggedin(request))

@app.route('/projects/web')
def web():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    return render_template('web.html',
                           value=pyml['name'],
                           loggedin=loggedin(request))
  

# except:
#     return 'this page broke lol'


@app.route('/tos')
def tos():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    try:
      source=request.args['source']
    except KeyError:
      source = 'unknown'
    return render_template('tos.html',
                           value=pyml['name'],
                           loggedin=loggedin(request),
                           source=source)


# except:
#     return 'this page broke lol'


@app.route('/prpo')
def prpo():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    try:
      source=request.args['source']
    except KeyError:
      source = 'unknown'
    return render_template('prpo.html',
                           value=pyml['name'],
                           loggedin=loggedin(request),
                           source=source)


# except:
#     return 'this page broke lol'


@app.route('/account')
def account():
    # try:
    Logged_In = request.cookies.get('Logged_In')
    if Logged_In == "True":
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    return render_template('account.html',
                           name=pyml['name'],
                           loggedin=loggedin(request),
                           test='aaaaaaaaaaaaaaa')


# @app.route('/robots.txt')
# def robots(e):
#   with open('templates/robots.txt') as f:
#     response = make_response()
#     response.data = f.read()
#     response.content_type = 'text/plain'
#     return 'aaaaaa'



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
        pyml['name'] = request.cookies.get('userID')
    else:
        Logged_In = "False"
        pyml['name'] = "Login"
    print(pyml['name'])
    return render_template('triangle.html',
                           value=pyml['name'],
                           loggedin=loggedin(request))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)