# ***Subnetting***

## Table of Contents

- 🧱 [Subnetting basics](#subnetting-basics)
-    [NAT](#nat)

## Subnetting Basics

### What is Subnetting?
- The process of dividing one large network into smaller, more manageable subnetworks.
- Helps improve network management and efficiency.

### CIDR (Classless Inter-Domain Routing)
- A method used for allocating IP addresses efficiently.
- Format: `IP_address/prefix_length` (e.g., `192.168.1.0/24`).
- The prefix length (e.g., `/24`) indicates how many bits are used for the network portion of the IP address.

---

## NAT (Network Address Translation)

### What is NAT?
- NAT translates private IP addresses to public IP addresses, allowing communication between internal devices and the internet.

### How NAT Works:
1. A device with a private IP address sends a request to access the internet.
2. The router, using NAT, translates the device's private IP address to a public IP address.
3. The internet only recognises the public IP address, so it uses this to send responses.
4. When the data returns to the router, NAT translates the public IP back to the device's private IP address.

### Types of NAT:

- **Static NAT**:
  - Maps a single private IP address to a single public IP address.
  - Used for devices like web servers that need to be accessible from the internet at all times (one-to-one mapping).
  
- **Dynamic NAT**:
  - Maps a private IP address to one of many available public IP addresses.
  - When a device no longer needs to communicate with the internet, the public IP is returned to the pool for other devices to use.

- **PAT (Port Address Translation)**:
  - Allows multiple devices on a local network to share a single public IP address but with different port numbers.
  - Most home routers use this method to conserve public IP addresses.

### Why NAT is Important for Engineers:
- **Conserves public IP addresses** by allowing multiple devices to share a single public IP.
- **Enhances network security** by hiding internal IP addresses from external networks.
- **Simplifies network management** by reducing the number of public IP addresses required.
