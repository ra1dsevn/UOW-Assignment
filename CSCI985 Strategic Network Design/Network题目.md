1. What are the advantages of tree network?

a. Robust

b. Easy fault identification and fault isolation

c. High cost

**d. High reliability**

Explanation: 树型网络的优点包括易于识别和隔离故障（选项b）以及高可靠性（选项d）。成本高不是树型网络的优势，而是一种劣势。

2. Which description is correct for power-coercive strategy?

**a. People are mostly compliant, do as they're told.**

b. People tend to resist.

c. People tend to comply when there's no better alternative.

d. People will comply if it's in their best interest.

Explanation: 权力强制策略的正确描述是大多数人会遵从指令（选项a），因为在这种策略下，人们通常会按照指示行事以避免负面后果。

3. What are initial architecture/design goals of network projects?

**a. Support legacy applications**

**b. Support new users, applications, or devices**

**c. Improve performance to part or all of the network**

**d. Solve perceived problems within the system**

Explanation: 网络项目初期架构/设计目标通常包括支持遗留应用、支持新用户或设备、改善网络性能的一部分或全部以及解决系统内已知的问题。

4. Which of the following IP addresses belongs to Class B address?

a. 10.53.42.10

b. 172.16.10.5

**c. 130.53.42.10**

d. 192.168.1.1

Explanation: 属于B类地址的是130.53.42.10（选项c），B类IP地址范围是从128.0.0.0到191.255.255.255。

5. Select a common **routing protocol** from the following.

**a. RIP**

**b. BGP**

c. HTTP

**d. OSPF**

Explanation: 常见的路由协议包括RIP（Routing Information Protocol）、BGP（Border Gateway Protocol）和OSPF（Open Shortest Path First），HTTP是一个超文本传输协议，不是路由协议。

6. Class B address subnet mask is 255.255.255.248, then the number of available host addresses within each subnet is

a. 2

**b. 6**

c. 8

d. 14

Explanation: 当子网掩码为255.255.255.248时，每个子网可用的主机地址数是6个（选项b），因为最后8位中只有3位用于主机部分，这提供了8个地址，其中去掉全0和全1两个特殊地址后剩下6个。

7. Which of the following is the protocol that provides authentication and encryption/decryption between devices at the network layer?

a. SSL/TLS

**b. IPSec**

c. HTTPS

d. SNMP

Explanation: 提供网络层设备之间认证和加密/解密的协议是IPSec（选项b）。

8. When designing a performance architecture, multiple traffic types are combined on a common network infrastructure in order to improve overall network performance. What resource control approach should we take?

**a. Traffic shaping**

b. Traffic policing

c. Traffic management

d. Traffic monitoring

Explanation: 设计性能架构时，应该采取流量整形（Traffic shaping）的方法来控制资源，以优化整体网络性能。

9. What is the service model used to implement QoS in MPLS networking schemes?

a. RSVP

b. IntServ

**c. DiffServ**

d. Best Effort

Explanation: 在MPLS网络方案中实现QoS的服务模型是DiffServ（Differentiated Services，选项c）。

10. What are the main mechanisms in Network Management Mechanisms?

**a. Configuration mechanisms**

**b. Monitoring mechanisms**

**c. Instrumentation mechanisms**

d. Programming mechanisms

Explanation: 网络管理机制主要包括配置机制、监控机制和工具机制（选项abc）。

Short Answer Questions:
- Write at least four types of networking devices and their functions.

Networking devices include:

- Routers (forward packets between networks)
- Switches (connect devices within a network)
- Firewalls (protect networks from unauthorized access)
- Hubs (connect multiple devices in a network)

网络设备至少包括：

- 路由器（在不同网络间转发数据包）
- 交换机（连接网络内部设备）
- 防火墙（保护网络免受未经授权的访问）
- 集线器（在一个网络中连接多个设备）

- What are the functions of component architectures?

Component architectures define how software components interact, specify interfaces, and separate concerns for easier maintenance and scalability.

组件架构定义了软件组件如何交互，规定接口，并分离关注点以便更容易维护和扩展。

- What is the reference architecture developed during the network architecture process? Describe what it contains.

The reference architecture serves as a template containing guidelines, standards, and practices for network design, including components, relationships, and constraints.

参考架构在网络架构过程中作为模板使用，包含网络设计的指导方针、标准和实践，包括组件、关系和约束条件。

- What is IP routing?

IP routing is the process by which data packets travel across multiple networks to reach their destination using IP addresses.

IP路由是指数据包通过使用IP地址穿越多个网络到达目的地的过程。

- How to manipulate the flow during routing, what are the common ways to do it, and explain its practice.

Manipulate flow through routing policies like policy-based routing, route maps, and access lists; practice involves configuring routers to follow these policies.

通过路由策略（如基于策略的路由、路由映射和访问列表）来操纵流量；实践涉及配置路由器以遵循这些策略。

- In IPv4, hosts have several ways of communicating with other hosts, explaining the process of each.

Hosts can communicate directly via:

- Unicast (one-to-one)
- Broadcast (one-to-all on a network)
- Multicast (one-to-many, specific groups)
- Anycast (one-to-nearest of multiple servers)

在IPv4中，主机可以通过以下方式通信：

- 单播（一对一）
- 广播（一对所有）
- 组播（一对多，特定组）
- 任播（一对最近的一个服务器）