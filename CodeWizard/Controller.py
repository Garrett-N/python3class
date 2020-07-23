import web

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
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

class PostRegistration:
    def POST(self):
        post_data = web.input()
        return post_data


if __name__ == "__main__":
    app.run()