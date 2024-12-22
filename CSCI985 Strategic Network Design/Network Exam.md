# Network Exam

## I. Multiple-choice Questions

1. What are the advantages of tree network?
   - a. **Robust**
   - b. **Easy fault identification and fault isolation**
   - c. High cost with high demand for cabling
   - d. **High reliability**
2. Which description is correct for power-coercive strategy?
   - a. **People are mostly compliant, do as they're told**
   - b. People oppose loss/disruption but adapt readily
   - c. People are social beings and follow social norms
   - d. People are rational and follow self-interest
3. What are initial architecture/design goals of network projects?
   - a. Upgrade technology/vendor
   - b. **Support new users, applications or devices**
   - c. **Improve performance to part or all of the network**
   - d. **Solve perceived problems within the system**
4. Which of the following IP addresses belongs to Class B address?
   - a. 221.121.16.12
   - b. 200.245.20.11
   - **c. 130.53.42.10**
   - d. 98.62.53.6
   - In IP addressing, the first octet of the IP address determines the address class. Class B IP addresses have the first two octets reserved for the network portion of the address, while the remaining two octets are used for the host portion. The range of Class B IP addresses is from 128.0.0.0 to 191.255.255.255. Option b has a first octet of 200, which falls within this range, making it a Class B IP address.
5. Select a common routing protocol from the following.
   - a. **RIP**
   - b. **BGP**
   - c. TCP
   - d. **OSPF**
   - TCP is a transport layer protocol used to establish a connection between two devices and provide reliable data transmission, not a routing protocol. Among the options, RIP (Routing Information Protocol), BGP (Border Gateway Protocol), and OSPF (Open Shortest Path First) are common routing protocols used in computer networks. RIP is a distance vector protocol, while BGP and OSPF are link-state protocols. These routing protocols are used by routers to exchange routing information and determine the best path for data to travel between devices in a network.
6. Class B address subnet mask is 255.255.255.248, then the number of available host addresses within each subnet is
   - a. 4
   - **b. 6**
   - c. 8
   - d. 10
7. Which of the following is the protocol that provides <u>authentication and encryption/decryption</u> between devices at the network layer?
   - a. UDP
   - b. **IPSec**
   - c. IP
   - d. TCP
   - IPSec (Internet Protocol Security) is a protocol suite used to secure Internet Protocol (IP) communications by authenticating and encrypting each IP packet of a communication session. It provides network-level security by encapsulating the original IP packet and adding a new header that includes security information. UDP and TCP are transport layer protocols, and IP is the main protocol for transmitting data packets across the Internet, but they do not provide authentication and encryption/decryption between devices at the network layer.
8. When designing a performance architecture, multiple traffic types are combined on a common network infrastructure in order to improve overall network performance. What resource control approach should we take?
   - a. Queuing
   - b. Prioritisation
   - c. Scheduling
   - d. **Traffic management**
9. What is the service model used to implement **<u>QoS in MPLS</u>** networking schemes?
   - a. IntServ
   - b. IntATM
   - c. **DiffServ**
   - d. ATM
   - The service model used to implement Quality of Service (QoS) in MPLS (Multiprotocol Label Switching) networking schemes is DiffServ (Differentiated Services). DiffServ is a QoS architecture that uses a differentiated treatment of traffic based on its classification and priority level. It allows network administrators to define different levels of service for different types of traffic. IntServ is another QoS architecture but is less scalable and not typically used in MPLS networks. IntATM is specific to Asynchronous Transfer Mode (ATM) networks, which are not commonly used in modern networks, and ATM is a cell-based switching technology that has been largely replaced.
10. What are the main mechanisms in Network Management Mechanisms?
    - a. **Configuration mechanisms**
    - b. **Monitoring mechanisms**
    - c. **Instrumentation mechanisms**
    - d. **Programming mechanisms**
    - The main mechanisms in network management are configuration mechanisms (used to configure network devices and services), monitoring mechanisms (used to monitor the performance and health of network devices and services), instrumentation mechanisms (used to collect and store data for later analysis), and programming mechanisms (used to automate network management tasks). These mechanisms together form the foundation of network management and enable efficient and effective management of network resources.

## II. Short Answering Questions

### B.02

**Write at least four types of networking devices and their functions.**
There are many types of networking devices used in modern computer networks, each with its own specific functions. Here are four common types:

- **Switches**: Connect multiple devices in a LAN, operate at the data link layer, use MAC addresses for data forwarding, and are crucial for building a reliable LAN infrastructure.
- **Routers**: Connect multiple networks, operate at the network layer, use IP addresses for data forwarding, and are vital for creating a WAN and enabling Internet access.
- **Firewalls**: Protect a network from unauthorized access and Internet attacks, operate at the network or transport layer, and use techniques like packet filtering, etc. to block unwanted traffic.
- **Access Points**: Connect wireless devices to a wired network, operate at the physical and data link layers, and provide wireless coverage or enable user mobility in a LAN.

### B.03

**What are the functions of component architectures?**
Component architectures are software architectures that focus on creating software systems from reusable, modular components. Their functions include:

- **Reusability**: Component architectures promote reusability by breaking software systems down into smaller, independent components that can be used and reused in a variety of different contexts. This allows for the efficient creation of new software systems without having to start from scratch each time.
- **Modularity**: Component architectures encourage modularity by creating software components that are well-defined, independent, and can be easily combined to create larger systems. This allows for greater flexibility in the design and development of software systems, making them easier to understand, maintain, and modify.
- **Interoperability**: Component architectures promote interoperability by ensuring that software components are designed to work seamlessly with other components, regardless of the specific programming language, platform, or technology used. This allows for greater integration and collaboration between different software systems and makes it easier to share data and functionality between systems.
- **Scalability**: Component architectures allow for scalability by enabling the creation of software systems that can be easily scaled up or down to meet changing demands. This is achieved through the use of independent components that can be added or removed as needed, allowing the system to adapt to changing requirements without disrupting the overall architecture. By providing these functions, component architectures help to improve software development efficiency, quality, and maintainability, while also reducing development costs and time-to-market.

### B.04

**What is the reference architecture developed during the network architecture process? Describe what it contains.**
The reference architecture is a high-level blueprint developed during the network architecture process. It provides a framework for the design and implementation of the network and helps to ensure that the network meets the organization's requirements. It contains the following key elements:

- **Network scope and requirements**: Outlines the business and technical requirements for the network, including the types of devices and applications that will be supported, the number of users, and any performance or security requirements.
- **Network topology**: Describes the physical and logical layout of the network, including the locations of devices, the types of connections between devices, and any redundancies or failover mechanisms that will be used.
- **Network services**: Outlines the specific services that the network will provide, such as email, web browsing, file sharing, and remote access. It may also include service level agreements (SLAs) that define the expected performance and availability of these services.
- **Network security**: Describes the security measures that will be implemented to protect the network and its users from threats such as viruses, hackers, and unauthorized access. It may include policies, procedures, and technical controls such as firewalls, intrusion detection systems, and encryption.
- **Network management**: Outlines the processes and tools that will be used to manage the network, including monitoring, reporting, and troubleshooting. It may also include plans for capacity planning, change management, and disaster recovery.

### B.05

**What is IP routing?**
IP routing is the process by which data packets are forwarded across an IP network from their source to their destination. The process involves several steps:

1. Identification of the source and destination IP addresses.
2. Selection of the best path or route for the packet to travel. This is based on factors such as the cost or distance of the route, the availability and reliability of the network links along the route, and any configured policies or access control rules.
3. Forwarding of the packet through each network device along that path. When a device sends a packet to another device on the network, it first checks its routing table to determine the best path for the packet to take to reach its destination. The routing table is a database that contains information about the network topology, including the IP addresses of other devices on the network and the paths or routes that packets can take to reach those devices.

### B.06

**How to manipulate the flow during routing, what are the common ways to do it, and explain its practice.**
Routing can be manipulated in several ways to control the flow of traffic on a network. The common ways include:

- **Static routing**: Involves manually configuring the routing tables on network devices to direct traffic along specific paths. It is simple to configure and effective for small networks with a fixed topology. However, it can be time-consuming and difficult to manage for larger networks with dynamic topologies.
- **Dynamic routing**: Involves using routing protocols, such as OSPF, BGP, or EIGRP, to automatically exchange routing information between network devices and dynamically update routing tables as network topology changes. It is more scalable and flexible than static routing and can adapt to changes in the network quickly.
- **Policy-based routing**: Involves setting policies or rules that dictate how traffic should be routed based on specific criteria, such as the source or destination IP address, the type of traffic, or the time of day. It can be used to prioritize certain types of traffic, direct traffic to specific links or interfaces, or restrict traffic based on security policies.
- **Traffic engineering**: Involves manipulating routing to optimize network performance and resource utilization, typically through the use of advanced techniques such as MPLS. It can be used to reduce network congestion, improve network resilience, and support Quality of Service (QoS) policies.
  In practice, network administrators and engineers may use one or more of these methods to manipulate routing in their networks. For example, a small business with a simple network topology might use static routing to direct traffic between its internal network and the internet, while a large enterprise with a complex network topology might use a combination of dynamic routing and policy-based routing to optimize performance and security.

### B.07

**In IPv4, hosts have several ways of communicating with other hosts, explaining the process of each.**
In IPv4, hosts can communicate with each other using several different methods, including:

- **Unicast**: The most common type of communication. It involves sending a packet from one host to another host on a one-to-one basis. The packet is addressed to a specific IP address, which is typically the destination host's IP address. The source host sends a packet addressed to the destination host's IP address, and the network routes the packet to the destination host based on the destination IP address in the packet header.
- **Broadcast**: A method of sending a packet from one host to all hosts on a local network. The packet is addressed to the broadcast address, which is a special IP address that represents all hosts on the local network. The source host sends a packet addressed to the broadcast address, and the network broadcasts the packet to all hosts on the local network.
- **Multicast**: A method of sending a packet from one host to a group of hosts that have joined a multicast group. The packet is addressed to a multicast address, which is a special IP address that represents a group of hosts. The source host sends a packet addressed to a multicast address, and the network forwards the packet to all hosts that have joined the multicast group associated with that address.
- **Anycast**: A method of sending a packet from one host to the nearest of a group of hosts that share the same IP address. The packet is addressed to a special IP address that is assigned to multiple hosts, and the network routes the packet to the nearest host that shares that IP address.

### B.08

**What is included in the CIA triangle? And explain the meaning of each part.**
The CIA triangle in the field of information security refers to the three core objectives of information security: confidentiality, integrity, and availability.

- **Confidentiality**: Means that data or information is protected from unauthorized disclosure or access. It ensures that sensitive information is accessible only to authorized individuals or systems. Confidentiality is maintained through various mechanisms, such as access controls, encryption, and firewalls.
- **Integrity**: Refers to the accuracy, completeness, and consistency of data over its entire lifecycle. It ensures that data or information is not modified or tampered with by unauthorized individuals or systems. Integrity is maintained through various mechanisms, such as access controls, data backups, and data validation.
- **Availability**: Means that data or information is accessible and usable when needed by authorized individuals or systems. It ensures that systems and services are available for use when required. Availability is maintained through various mechanisms, such as redundancy, fault tolerance, and disaster recovery planning.

### B.09

**What needs to be considered in order to achieve high quality Network Management Architectures?**
To achieve high quality network management architectures, several factors need to be considered:

- **Business requirements**: The network management architecture must align with the organization's business requirements, goals, and objectives. It should support the business processes and workflows, and ensure that the network infrastructure is reliable, scalable, and secure.
- **Scalability**: The network management architecture should be designed to support the current and future needs of the organization. It should be scalable and flexible, so that it can accommodate new technologies, applications, and services.
- **Performance**: The network management architecture should be designed to provide optimal performance and throughput. It should be able to handle large volumes of data and traffic, and ensure that network latency and bottlenecks are minimized.
- **Security**: The network management architecture must be designed to ensure the confidentiality, integrity, and availability of data and systems. It should provide appropriate access controls, encryption, and authentication mechanisms, and be able to detect and respond to security threats and incidents.
- **Standardization**: The network management architecture should be based on industry standards and best practices. This will ensure interoperability, compatibility, and ease of management, and reduce the risk of vendor lock-in.
- **Automation**: The network management architecture should incorporate automation and orchestration tools to simplify and streamline network management tasks. This will help to reduce errors, improve efficiency, and enhance the overall quality of the network.
- **Monitoring**: The network management architecture should include comprehensive monitoring and reporting tools to provide visibility into network performance and identify issues before they become problems. This will help to improve the reliability and availability of the network