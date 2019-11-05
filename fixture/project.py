from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def utworz(self, project):
        wd = self.app.wd
        self.przejdz_do_zarzadzania()
        self.przejdz_do_zarzadzania_projektami()
        self.dodaj_projekt()
        self.wypelnij_dane_projektu(project)
        self.zapisz_projekt()

    def przejdz_do_zarzadzania(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, '/manage_overview_page')]").click()

    def przejdz_do_zarzadzania_projektami(self):
        wd = self.app.wd
        self.przejdz_do_zarzadzania()
        wd.find_element_by_xpath("//a[contains(@href, '/manage_proj_page')]").click()

    def dodaj_projekt(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[text()='Stwórz nowy projekt']").click()

    def wypelnij_dane_projektu(self, project):
        self.wprowadz_wartosc_pola("name", project.name)
        self.wprowadz_wartosc_pola("description", project.description)

    def wprowadz_wartosc_pola(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)

    def zapisz_projekt(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Dodaj projekt']").click()

    def pobierz_liste_projektow(self):
        wd = self.app.wd
        self.przejdz_do_zarzadzania_projektami()
        list = []
        for element in wd.find_elements_by_xpath(
                "//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
            td = element.find_elements_by_tag_name("td")
            name = td[0].text
            description = td[4].text
            list.append(Project(name=name, description=description))
        return list

    def wybierz_projekt_po_nazwie(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[text()='%s']" % name).click()

    def usun_projekt_po_nazwie(self, name):
        wd = self.app.wd
        self.wybierz_projekt_po_nazwie(name)
        wd.find_element_by_xpath("//input[@value='Usuń projekt']").click()
        # potwierdzenie usunięcia
        wd.find_element_by_xpath("//input[@value='Usuń projekt']").click()

