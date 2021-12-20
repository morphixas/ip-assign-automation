'''
Made by: Tauras Eicius
'''
import os
import ipaddress as ips

# generates IPs with prefix for "ip add" or "ip del" command
def generate_with_prefix(ip_address):
  ip_with_prefix = []
  ip_address = ips.IPv4Network(ip_address)
  prefix = ip_address.prefixlen
  
  for addr in ip_address:
    ip_with_prefix.append(str(addr) + "/" + str(prefix))

  return ip_with_prefix

# scan the network interfaces
def discover_network_interfaces():
  stream = os.popen("ip -o link show | awk -F': ' '{print $2}'")
  output = stream.read().splitlines()
  return output

# adds IPs to the network interface
def add_ips():
  ip = input("Enter the subnet (with mask, like x.x.x.x/29) you would like to add: ")
  ip = ips.ip_network(ip, strict=False)

  print("\nAddressess that will be added:")
  for addr in ip:
    print(addr)

  output = discover_network_interfaces()

  # network interface selection
  print("\nPlease select the network interface you want to add these IPs to:")
  for i in range(0, len(output)):
    print(i, "-", output[i])
  interface_select = int(input("\nEnter the number: "))

  # execute commands to add IPs
  ips_with_prefix = generate_with_prefix(ip)
  try:
    for i in range(len(ips_with_prefix)):
      executable_command = "ip addr add " + ips_with_prefix[i] + " dev " + output[interface_select]
      os.popen(executable_command)
      executable_command = ""
    print("\nIPs have been added successfully.")
  except:
    print("Error has occured")

# remove IPs from the network interface
def remove_ips():
  ip = input("Enter the subnet (with mask, like x.x.x.x/29) you would like to remove: ")
  ip = ips.ip_network(ip, strict=False)

  print("\nAddressess that will be removed:")
  for addr in ip:
    print(addr)

  output = discover_network_interfaces()

  # network interface selection
  print("\nPlease select the network interface you want to remove these IPs from:")
  for i in range(0, len(output)):
    print(i, "-", output[i])
  interface_select = int(input("\nEnter the number: "))

  # execute commands to remove IPs
  ips_with_prefix = generate_with_prefix(ip)
  try:
    for i in range(len(ips_with_prefix)):
      executable_command = "ip addr del " + ips_with_prefix[i] + " dev " + output[interface_select]
      os.popen(executable_command)
      executable_command = ""
    print("\nIPs have been removed successfully.")
  except:
    print("Error has occured")

#---------------------DRIVER CODE-----------------------------
print("\nThis script can be used as a tool to help assign or delete IP subnets from the network interface\n")

print("Do you want to add or remove IPs?")
print("0 - add IPs")
print("1 - remove IPs\n")

choice = int(input("Enter selection: "))
if choice == 0:
  add_ips()
elif choice == 1:
  remove_ips()
else:
  print("Wrong input supplied.")