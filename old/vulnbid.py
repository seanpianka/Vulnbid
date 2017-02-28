from flask import render_template, Flask
application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
    user = {'nickname': 'Me'}  # fake user
    return render_template('index.html', title='Home', user=user)

@application.route('/signin')
def signin():
    user = {'nickname': 'Me'}  # fake user
    return render_template('signin.html', title='Sign In', user=user)

@application.route('/signup')
def signup():
    user = {'nickname': 'Me'}  # fake user
    return render_template('signup.html', title='Sign Up', user=user)

if __name__ == '__main__':
    # Debug mode: script was invoked directly. Start the Flask server.
    # bind_ip: OVH (primary) 158.69.55.64; All interfaces 0.0.0.0
    bind_ip = '0.0.0.0'
    bind_port = 8080
    application.config["TEMPLATES_AUTO_RELOAD"] = True
    application.run(bind_ip, bind_port)
