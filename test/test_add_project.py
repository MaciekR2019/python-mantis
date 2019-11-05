def test_dodaj_projekt(app, data_projects):
    old_projects = app.project.pobierz_liste_projektow()
    project = data_projects
    app.project.utworz(project)
    print("\nDodano projekt: ", project)
    new_projects = app.project.pobierz_liste_projektow()
    old_projects.append(project)
    assert old_projects == new_projects

