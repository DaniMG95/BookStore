from unittest import TestCase
from fastapi.testclient import TestClient
from app.main import app
from app.models.author import Author
from unittest.mock import patch


class TestAuthor(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    @patch("app.models.author.Author.get_id")
    def test_read_main(self, mock_author):
        expected_author = {"id": "1", "name": "dsssdadsadas", "books": []}

        mock_author.return_value = Author(id=1, name="dsssdadsadas", books=[])
        response = self.client.get("/author/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_author)

    def test_write_main(self):

        response = self.client.post("/author", json={"name": "sdasaddsasda"})

        self.assertEqual(response.status_code, 200)
