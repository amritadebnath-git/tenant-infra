import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_register_page_loads(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post("/register", data={
            "username": "testuser04",
            "password": "testpass04"
        }, follow_redirects=True)
        print(response.data);
        self.assertIn(b"Account created! Please login.", response.data)

if __name__ == "__main__":
    unittest.main()
