import web
from Models import RegisterModel, LoginModel

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration',
    '/login', 'Login',
    '/check-login', 'CheckLogin'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

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
            return isCorrect

        return "error"


if __name__ == "__main__":
    app.run()