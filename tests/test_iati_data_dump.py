from datetime import datetime
import pytz
import requests
from dateutil.parser import parse as date_parse


class TestIATIDataDump:
    """
    Test IATI Data Dump
    """
    def test_metadata(self):
        """
        Test metadata was created in the last 24 hours
        """
        url = "https://gist.githubusercontent.com/" + \
              "codeforIATIbot/efd190029713c6775c43962444dcb8df/" + \
              "raw/metadata.json"
        resp = requests.get(url)
        assert resp.status_code == 200
        j = resp.json()
        created_at = j["created_at"]
        delta_since = (datetime.now(pytz.utc) - date_parse(created_at))
        assert delta_since.days == 0
