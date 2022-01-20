from flask import Flask, render_template, request, make_response, redirect, url_for
import json
#aaaa
f = open('static/accounts.json')
print(json.loads(f.read())["test"]['pass'])
f.close()
app = Flask('app')
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

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():

    if request.method == 'POST':
        user = str(request.form['usrnm'])
        f = open('static/accounts.json')
        accounts = f.read()
        accounts_json = json.loads(accounts)
        try:
            json.loads(f.read())[user]['uname']
        except:
            FailedLogin = 'yes'
        finally:
            passfinder = str(accounts_json[user]['pass'])
            usedpass = str(request.form['loginpass'])
            print(passfinder)
            print(usedpass)
            if usedpass == passfinder and FailedLogin != 'yes':
                Logged_In = "True"
            else:
                Logged_In = "False"
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('userID', user)
            resp.set_cookie('Logged_In', Logged_In)
            f.close()
    return resp

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
        return render_template('home.html', value=pyml['name'], loggedin=loggedin(request), dark=isDark)
#    except:
#        return 'this page broke lol'


@app.route('/login')
def login():
    return render_template('login.html',
                           value=pyml['name'],
                           loggedin=loggedin(request))


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'


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
            f = open('static/accounts.json')
            accounts = json.loads(f.read())
            f.close()
            try:
                accounts[newUN]
            except:
                print('a')
            finally:
                if passVerified == 'True':
                    accounts[newUN] = {"uname": newUN, "pass": pwd}
                    f = open('static/accounts.json', 'w')
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


@app.route('/metaballs')
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
                               loggedin=loggedin(request)
                              )
    except:
        return 'this page broke lol'


@app.route('/what')
def what():
    try:
        return render_template('what.html')
    except:
        return 'this page broke lol'

@app.route('/bezier')
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

@app.route('/cube')
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
                               loggedin=loggedin(request)
                              )
    # except:
    #     return 'this page broke lol'

app.run(host='0.0.0.0', port=80, debug=True)
