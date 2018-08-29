from bottle import route, run

@route('/hello')
def hello():
    return 'Hello World'

@route('/')
def index():
    return '''
    <a href="/home">Home</a>
    <a href="/bio">Biography</a>
    <a href="/pic">Pictures</a>
    '''

@route('/home')
def home();
    return "You are now on the Home page"

@route('/bio')
def bio();
    return "You are now on the Biography page"

@route('/pic')
def pic();
    return "You are now on the Pictures page"

run(host='localhost', port=8080, debug=True)