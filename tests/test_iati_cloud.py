from datetime import datetime
import pytz
import requests
from dateutil.parser import parse as date_parse


class TestDatastoreClassic:
    """
    Test IATI.cloud
    """
    def test_healthy(self):
        """
        Test API self-reports as healthy
        """
        url = "https://api.aida.tools/api"
        resp = requests.get(url)
        assert resp.status_code == 200
        j = resp.json()
        assert j["status"] == 'healthy'
