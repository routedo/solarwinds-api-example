# About Project
  This project shows examples of how to leverage the [SolarWinds python API](https://github.com/solarwinds/orionsdk-python) to better manage network devices.  This was accomplished using the orionsdk package.  

# System requirements

###### Tested using:
	python 3.5.1
	orionsdk 0.0.6
	requests 2.17.3

###### Dependencies
	SolarWinds Python API
	 pip install orionsdk 
	 
	requests
     pip install requests
	 
# Example

###### example.py

	This file contains the following examples:
		# find_node_by_ip(ip_addr_find, swis)
			This function allows you to find a node based on it's IP address.
			The code for this function is located in the lib folder in a file named solarfind.py.
			
		# find_node_by_name(node_host_name, swis)
			This function allows you to find a node based on it's name.
			The code for this function is located in the lib folder in a file named solarfind.py.
			
		# manage_node(state, node_id, swis)
			This function allows you to unmanage and remanage a node in SolarWinds.
			The code for this function is located in the lib folder in a file named solaralert.py.
			
		# manage_interface(state, interface_id, swis)
			This function allows you to unmanage and remanage an interface in SolarWinds.
			The code for this function is located in the lib folder in a file named solaralert.py.
		
# License
  Apache License 2.0

# Author Information
  [Matthew McGeehan](http://routedo.com/)
