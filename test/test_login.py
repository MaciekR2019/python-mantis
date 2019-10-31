def test_login(app):
    app.session.zaloguj("administrator", "root")
    assert app.session.jest_zalogowany_jako("administrator")