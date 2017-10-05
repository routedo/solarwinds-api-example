import requests
from orionsdk import SwisClient
from datetime import datetime, timedelta

def manage_node(state, node_id, swis):
    current = datetime.utcnow()
    nextDay = current + timedelta(days=1)

    if state in 'Unmanage':
        swis.invoke('Orion.Nodes', state, node_id, current, nextDay, False)
    elif state in 'Remanage':
        swis.invoke('Orion.Nodes', state, node_id)


def manage_interface(state, interface_id, swis):
    current = datetime.utcnow()
    nextDay = current + timedelta(days=1)

    if state in 'Unmanage':
        swis.invoke('Orion.NPM.Interfaces', state, interface_id, current, nextDay, False)
    elif state in 'Remanage':
        swis.invoke('Orion.NPM.Interfaces', state, interface_id)
