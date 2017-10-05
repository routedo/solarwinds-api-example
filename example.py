import requests
from orionsdk import SwisClient
from lib.solarfind import find_node_by_ip
from lib.solarfind import find_node_by_name
from lib.solaralert import manage_node
from lib.solaralert import manage_interface
from getpass import getpass

def main():

    ## Provide SolarWinds Webserver IP
    npm_server = '1.1.1.1'
    
    ## Prompts for username and password
    username = input("Enter username: ")
    passwd = getpass('Enter password: ')
    
    ip_addr = '5.5.5.5'
    node = 'lab-switch'
    manage = 'Remanage'
    unmanage = 'Unmanage'
    node_id = 'N:1'
    interface_id = 'I:1'

    ## Creates connection to SolarWinds
    swis = SwisClient(npm_server, username, passwd)
    
    ## Find node by it's IP address
    node_ip = find_node_by_ip(ip_addr, swis)
    
    for row in node_ip:
        print("{NodeID:<5}: {DisplayName} {IPAddress}".format(**row))

    ## Find node by it's name
    node_name = find_node_by_name(node, swis)
    
    for row in node_name:
        print("{NodeID:<5}: {DisplayName} {IPAddress}".format(**row))
    
    ## Unmanage a node in SolarWinds for 1 day
    manage_node(unmanage, node_id, swis)

    ## Manage a node in SolarWinds
    manage_node(manage, node_id, swis)
    
    ## Unmanage an interface in SolarWinds for 1 day
    manage_interface(unmanage, interface_id, swis)

    ## Manage an interface in SolarWinds
    manage_interface(manage, interface_id, swis)

## Disables SSL Check    
requests.packages.urllib3.disable_warnings()

if __name__ == '__main__':
    main()