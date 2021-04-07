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
        Test metadata was created recently
        """
        url = "https://gist.githubusercontent.com/" + \
              "codeforIATIbot/efd190029713c6775c43962444dcb8df/" + \
              "raw/metadata.json"
        req = requests.get(url)
        assert req.status_code == 200
        j = req.json()
        created_at = j["created_at"]
        delta_since = (datetime.now(pytz.utc) - date_parse(created_at))
        assert delta_since.days == 0
