import requests
from orionsdk import SwisClient

def find_node_by_ip(ip_addr_find, swis):
    
    results = swis.query("SELECT NodeID, IPAddress, DisplayName FROM Orion.Nodes WHERE IPAddress = '" + ip_addr_find.strip() + "'")
    
    return(results['results'])
    
def find_node_by_name(node_host_name, swis):

    results = swis.query("SELECT NodeID, IPAddress, DisplayName FROM Orion.Nodes WHERE DisplayName = '" + node_host_name.strip() + "'")
    
    return(results['results'])






