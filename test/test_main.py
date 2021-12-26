from unittest.mock import Mock, patch
import sys

sys.path.append("/Users/pinarkaymaz/Documents/GitHub/infrastructure/src")

from main import get_cat_fact


@patch("requests.get")
def test_get_cat_fact(mock_req):
    response_m = Mock()
    response_m.status_code = 200
    response_m.json = Mock(return_value={"fact": "some-cat-fact", "length": "42"})
    mock_req.return_value = response_m
    assert get_cat_fact() == "some-cat-fact"