# -*- coding: utf-8 -*-
from model.add_new import Add_New


def test_add_new(app):
    app.contact.create_new(Add_New(firstname="Petrov", lastname="Petr", address="Moscow", telephone="8-905-323-50-26", email="petrov@yandex.ru"))

