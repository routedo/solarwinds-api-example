"""
Manage/Unmanage node or interface in SolarWinds.
"""

from datetime import datetime, timedelta
from orionsdk import SwisClient

def manage_node(state, node_id, swis):
    """
    This function allows you to unmanage and remanage a node in SolarWinds.
    """
    current = datetime.utcnow()
    next_day = current + timedelta(days=1)

    if state in 'Unmanage':
        swis.invoke('Orion.Nodes', state, node_id, current, next_day, False)
    elif state in 'Remanage':
        swis.invoke('Orion.Nodes', state, node_id)

def manage_interface(state, interface_id, swis):
    """
    This function allows you to unmanage and remanage an interface in SolarWinds.
    """
    current = datetime.utcnow()
    next_day = current + timedelta(days=1)

    if state in 'Unmanage':
        swis.invoke('Orion.NPM.Interfaces', state, interface_id, current, next_day, False)
    elif state in 'Remanage':
        swis.invoke('Orion.NPM.Interfaces', state, interface_id)
