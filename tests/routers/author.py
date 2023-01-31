from unittest import TestCase
from fastapi.testclient import TestClient
from app.app import app
from app.models.author import Author
from unittest.mock import patch


class TestAuthor(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    @patch("app.models.author.Author.get_id")
    def test_read_main(self, mock_author):
        mock_author.return_value = Author(id=1, name="dsssdadsadas", books=[])
        response = self.client.get("/author/1")
        assert response.status_code == 200
        print(response.json())
