import pytest
from unittest.mock import patch
from xtlsapi import XrayClient

def test_stats_online_ip_list():
    xray = XrayClient("127.0.0.1", 53357)
    with patch.object(xray, 'stats_online_ip_list', return_value={'212.58.119.246': 1763418412}):
        result = xray.stats_online_ip_list("1")
        assert result == {'212.58.119.246': 1763418412}
