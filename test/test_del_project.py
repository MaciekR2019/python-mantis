import random

def test_usun_projekt(app, data_projects):
    if len(app.project.pobierz_liste_projektow()) == 0:
        project = data_projects
        app.project.utworz(project)
        print("\nDodano projekt: ", project)
    old_projects = app.project.pobierz_liste_projektow()
    chosen_project = random.choice(old_projects)
    app.project.usun_projekt_po_nazwie(chosen_project.name)
    print("\nUsunięto projekt: ", chosen_project)
    new_projects = app.project.pobierz_liste_projektow()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(chosen_project)
    assert old_projects == new_projects
    print("\nUdało się, wszystko działa!")







