import web
from Models import RegisterModel, LoginModel

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/login', 'Login',
    '/logout', 'Logout',
    '/check-login', 'CheckLogin'
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout",
                             globals={'session': session_data, 'current_user': session_data["user"]})

# Classes/Routes

class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()

class Login:
    def GET(self):
        return render.Login()

class PostRegistration:
    def POST(self):
        post_data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(post_data)
        return post_data.username

class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return "success"

if __name__ == "__main__":
    app.run()