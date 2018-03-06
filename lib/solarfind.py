"""
Find SolarWinds node by IP or name.
"""

from orionsdk import SwisClient

def find_node_by_ip(ip_addr_find, swis):
    """
    This function allows you to find a node based on it's IP address.
    """

    results = swis.query("SELECT NodeID, IPAddress, DisplayName FROM Orion.Nodes WHERE IPAddress = '" + ip_addr_find.strip() + "'")

    return results['results']

def find_node_by_name(node_host_name, swis):
    """
    This function allows you to find a node based on it's name.
    """

    results = swis.query("SELECT NodeID, IPAddress, DisplayName FROM Orion.Nodes WHERE DisplayName = '" + node_host_name.strip() + "'")

    return results['results']
