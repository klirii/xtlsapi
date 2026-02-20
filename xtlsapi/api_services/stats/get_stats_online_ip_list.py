import grpc
from xtlsapi.xray_api.app.stats.command import command_pb2

from .._base import BaseService


class StatsOnlineIpList(BaseService):
    def stats_online_ip_list(self, user, reset=False) -> dict:
	"""
	Returns a dictionary of online IPs for the given user.

	Args:
	    user: The email of the user to query.

	Returns:
	    A dictionary mapping IP addresses to last cleanup time of expired ip's.
	"""

        try:
            return self.stats_stub.GetStatsOnlineIpList(
                command_pb2.GetStatsRequest(
                    name=f"user>>>{user}>>>online",
                    reset=reset
                )
            ).ips
        except grpc.RpcError:
            raise
            return None
