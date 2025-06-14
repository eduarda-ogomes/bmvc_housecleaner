from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')

@app.route('/change username')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/login', methods=['GET'])
def action_login():
    return ctl.render('login')

@app.route('/cadastro', method=['GET'])
def action_cadastro():
    return ctl.render('cadastro')

@app.route('/homepage', method=['GET'])
def action_homepage():
    return ctl.render('homepage')


#-----------------------------------------------------------------------------


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
