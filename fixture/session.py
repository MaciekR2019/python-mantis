class SessionHelper:

    def __init__(self, app):
        self.app = app

    def zaloguj(self, username, password):
        wd = self.app.wd
        self.app.otworz_strone_startowa()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_xpath("//input[@value='Zaloguj się']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Zaloguj się']").click()

    def wyloguj(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, '/logout_page.php')]").click()

    def jest_zalogowany(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def jest_zalogowany_jako(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//li//a[contains(text(), 'administrator')]").text

    def ensure_wyloguj(self):
        # wd = self.app.wd
        if self.jest_zalogowany():
            self.wyloguj()

    def ensure_zaloguj(self, username, password):
        # wd = self.app.wd
        if self.jest_zalogowany():
            if self.jest_zalogowany_jako(username):
                return
            else:
                self.wyloguj()
        self.zaloguj(username, password)
