from datetime import datetime
import pytz
import requests
from dateutil.parser import parse as date_parse


class TestDatastoreClassic:
    """
    Test Datastore Classic
    """
    def test_healthy(self):
        """
        Test API self-reports as healthy
        """
        url = "https://datastore.codeforiati.org/api/1/about/"
        resp = requests.get(url)
        assert resp.status_code == 200
        j = resp.json()
        assert j["status"] == 'healthy'
