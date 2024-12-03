
# Layer 3: Networking Fundamentals

## Overview
- **What is Layer 3?**  
  Layer 3, also called the **Network Layer**, is part of the OSI model. Its main job is to handle communication between devices across different networks.  

- **Why Do We Need Layer 3?**  
  Layer 2 (the Data Link Layer) enables communication within a local network (like a home or office). However, devices in separate networks, such as those across cities or continents, require Layer 3 to connect them.  

- **Key Responsibilities of Layer 3**:  
  1. Identifying devices using **IP addresses**.  
  2. Determining the best path for data to travel between networks (**routing**).  
  3. Ensuring data reaches the correct device, even across multiple networks.

---

## Layer 3 in Action: Connecting Two Isolated LANs

### Scenario: Two LANs (Local Area Networks)
1. **LAN1 and LAN2**:  
   - These are two separate networks where devices can communicate internally but not externally.  
   - For example, LAN1 could be a company’s network in New York, and LAN2 could be its branch office in London.

2. **Layer 2 Protocols**:  
   - **Ethernet**: Commonly used for local communication in LANs.  
   - Other Layer 2 protocols like **PPP (Point-to-Point Protocol)**, **MPLS**, or **ATM** are used for long-distance communication.  

3. **Challenge**:  
   - Devices in LAN1 and LAN2 cannot communicate directly because they are on different networks.  
   - Layer 3 solves this by using a universal protocol: **Internet Protocol (IP)**.

---

## Layer 3 Components: How It Works

### 1. **Internet Protocol (IP)**
   - **What It Does**:  
     IP acts as a universal “language” for devices, allowing communication across different networks.  

   - **How It Helps**:  
     IP ensures that data can travel across intermediate networks (called “hops”) to reach its destination.  

---

### 2. **IP Addresses**
   - **What They Are**:  
     IP addresses are unique identifiers for devices, like mailing addresses for homes.  

   - **Format**:  
     - IPv4: Written as four numbers separated by dots (e.g., `192.168.1.1`).  
     - IPv6: Longer addresses for modern networks (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).  

   - **Role**:  
     - **Source IP**: The address of the device sending data.  
     - **Destination IP**: The address of the intended recipient.

---

### 3. **Routers**
   - **What They Are**:  
     Routers are Layer 3 devices that connect networks and move data between them.

   - **How They Work**:  
     - A router receives data (in the form of packets) from one network.  
     - It determines the best path to forward the data toward its destination.  
     - The packet is **encapsulated** in a new Layer 2 frame specific to the next network.  
     - At each hop, the process repeats until the packet reaches its destination.

---

## Key Layer 3 Concepts: IP and Packets

### 1. **What Are Packets?**
   - Packets are the basic units of data sent at Layer 3.  
   - Think of them as envelopes containing data (payload), along with source and destination IP addresses.  

---

### 2. **How Packets Are Delivered**
   - **Encapsulation**:  
     Packets are placed inside Layer 2 frames to move through local networks.  
     - Example: A packet might be encapsulated in an Ethernet frame in LAN1, then re-encapsulated in an MPLS frame for long-distance travel, and finally in another Ethernet frame in LAN2.  

   - **Consistency**:  
     The IP packet remains unchanged throughout the journey, while the Layer 2 frame is replaced at each network transition.

---

## Anatomy of an IP Packet
1. **Source IP Address**: Identifies the device sending the data.  
2. **Destination IP Address**: Specifies the intended recipient device.  
3. **Protocol Field**: Indicates the Layer 4 protocol used (e.g., TCP, UDP, or ICMP).  
4. **Payload (Data)**: Contains the actual information from the Layer 4 protocol.  
5. **Time-to-Live (TTL)**: Limits the number of hops a packet can take before being discarded, preventing infinite loops.  

---

## Example: Sending a Packet Across Networks
1. **Step 1**: A computer in LAN1 (IP: `192.168.1.10`) sends a message to a computer in LAN2 (IP: `10.0.0.20`).  
2. **Step 2**: The router in LAN1 encapsulates the packet in an Ethernet frame for local transmission.  
3. **Step 3**: The router forwards the packet to the next network, where it is encapsulated in a new frame.  
4. **Step 4**: The process repeats until the packet reaches LAN2, where it is delivered to the destination.  

---

## Key Takeaways
- **Layer 3 bridges networks**: It connects isolated LANs, enabling global communication.  
- **IP is universal**: Regardless of the underlying Layer 2 protocols, IP ensures data can travel across networks.  
- **Routers are the backbone**: They determine paths for packets and encapsulate them in frames specific to each network.  
- **Packets are constant**: While frames change at each hop, the IP packet remains unchanged, ensuring data integrity.
