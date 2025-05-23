from bottle import template


class Application():

    def __init__(self):
        self.pages = {
            'login': self.login,
            'cadastro': self.cadastro,
            'homepage': self.homepage
        }


    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()


    def helper(self):
        return template('app/views/html/helper')
    
    def login(self):
        return template('app/views/html/login')
    
    def cadastro(self):
        return template('app/views/html/cadastro')
    
    def homepage(self):
        return template('app/views/html/homepage')
