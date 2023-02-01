from unittest import TestCase
from app.auth import verify_password, pr


class TestAuth(TestCase):
    def test_verify_password(self):
        hash_password = "$2b$12$ROBHCSujOAexMq6FLjyH8uIWMQeJRXshQCz8THnmnbRTuapx2xr76"
        password = "dssaddsa"

        verify = verify_password(hashed_password=hash_password, plain_password=password)

        self.assertTrue(verify)

    def test_verify_password_error(self):
        hash_password = "$2b$12$ROBHCSujOAexMq6FLjyH8uIWMQeJRXshQCz8THnmnbRTuapx2xr76"
        password = "dssaddsaa"

        verify = verify_password(hashed_password=hash_password, plain_password=password)

        self.assertFalse(verify)

    def test_pr(self):
        self.assertEqual(pr(), "dsasasd")
