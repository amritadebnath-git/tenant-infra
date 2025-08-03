import unittest
import uuid
from app.app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_register_page_loads(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        random_username = f"user_{uuid.uuid4().hex[:6]}"
        random_password = f"pass_{uuid.uuid4().hex[:6]}"
        response = self.client.post("/register", data={
            "username": random_username,
            "password": random_password
        }, follow_redirects=True)

        print(f"Tested with username: {random_username}, password: {random_password}")
        self.assertIn(b"Account created! Please login.", response.data)

if __name__ == "__main__":
    unittest.main()
