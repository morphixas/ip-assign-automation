# Basic information
Automated IP address assign script for Linux. Written in Python 3, it is a helpful tool when managing servers to assign or remove IPs to NIC. It is based on "ip addr add" command functionality, but is more user friendly to use.

No additional dependencies required, simply run to use. No command line run options yet, therefore user has to supply information while running the script.

Current functions include:
- detection of NICs
- ability to add assign IP ranges to NIC
- ability to remove IP ranges from NIC
- subnets are automatically split into seperate /32 IPs (for example, a /24 will be split into 256 /32 and then assign IPs)

For now, IPv4 support only.
