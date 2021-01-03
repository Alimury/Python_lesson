from model.add_new import Add_New


def test_delete_first_new(app):
    if app.contact.count() == 0:
        app.contact.create_new(Add_New(firstname="Sidorov"))
    app.contact.test_delete_first_new()
