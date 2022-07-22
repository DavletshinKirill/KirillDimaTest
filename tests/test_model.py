from unittest import TestCase
from app import create_app, db
from app.model import Users


class TestModel(TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_find_user(self):
        user = Users.query.filter_by(email="kirichka27@gmail.com").first()
        self.assertTrue(user is not None)

    # def test_not_find_user(self):
    #     user = Users.query.filter_by(email="kirichka2711@gmail.com").first()
    #     self.assertFalse(user is not None)
    #
    # def test_password_verification(self):
    #     u = Users(password_hash='asd')
    #     self.assertTrue(u.check_password(generate_password_hash('asd')))

