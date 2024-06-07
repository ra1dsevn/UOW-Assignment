**数据库QUIZ10**

Question 01
Data buffer cache is used to


a.
Speed up processing of SQL statements.
b.
Store the compiled SQL statements such that there is no need to compile the statements again.
c.
Store user names and passwords of the user connected to a database system.
d.
Store the results of queries such that they can be used later on.

* * *

**ChatGPT:**

答案: a. Speed up processing of SQL statements.

解析: 数据缓冲区（Data buffer cache）主要用于加速SQL语句的处理。它通过将数据存储在内存中，减少了对硬盘的访问次数，从而加快了数据的读写速度。当数据库需要访问数据时，它首先查看缓冲区中是否已经有这些数据。如果有，就可以直接从内存中读取，而不需要从硬盘上读取，这样大大提高了处理速度。其他选项，如b. 存储编译过的SQL语句，c. 存储数据库系统用户的用户名和密码，d. 存储查询结果以供后用，这些都不是数据缓冲区的主要用途。

* * *

**You:**

Question 02
What is a principle of Mandatory Access Control (MAC) in database systems ?
a.
In Mandatory Access Control(MAC) access to data objects is at discretion of database administrator.
b.
In Mandatory Access Control (MAC) access to data objects is controlled by system-wide policies that cannot be changed by the individual users.
c.
In Mandatory Access Control(MAC) access to data objects is  controlled by the access rights (privileges) on specific data objects.security levels.
d.
In Mandatory Access Control (MAC) access to data objects is controlled by mandatory access to data dictionary tables.

* * *

**ChatGPT:**

答案: b. In Mandatory Access Control (MAC) access to data objects is controlled by system-wide policies that cannot be changed by the individual users.

解析: 强制访问控制（Mandatory Access Control, MAC）是一种安全模型，其中对数据对象的访问是由整个系统范围内的策略控制的，这些策略不可由单个用户改变。这种模式通常用于需要高度安全性的环境，如政府或军事机构。在MAC中，访问权限基于安全标签（如机密级别），并且这些安全标签由系统而非用户管理。与之相对的是自主访问控制（Discretionary Access Control, DAC），在DAC中，用户（或数据的拥有者）可以控制对其拥有的数据对象的访问。选项a、c和d描述的不是MAC的核心原则。

* * *

**You:**

Question 03
A database privilege is
a.
A right to store data in a relational table.
b.
A right to grant access to a database objects.
c.
A right to perform an operation on a database or to access in read or write mode a data object stored in a database
d.
A right to set query optimisation objectives.

* * *

**ChatGPT:**

答案: c. A right to perform an operation on a database or to access in read or write mode a data object stored in a database.

解析: 数据库权限（Database privilege）指的是在数据库中执行操作或以读写模式访问存储在数据库中的数据对象的权利。这包括但不限于对表、视图、存储过程等数据库对象的读取、修改、删除等操作。权限管理是数据库安全的重要组成部分，它确保只有授权的用户才能对数据库中的数据执行特定的操作。选项a、b和d所述的权限类型或者功能，虽然也可能存在于数据库系统中，但它们不是数据库权限的标准定义。特别是b选项，虽然赋予权限是一种权限，但它更准确地被视为特权（Privilege）的一个子集，而不是定义数据库权限的核心。

* * *

**You:**

Question 04
In MySQL database privileges apply to


a.
A database and all objects within it.


b.
All databases controlled by a database server.


c.
All files a database system consists of.


d.
All relational tables.

* * *

**ChatGPT:**

答案: a. A database and all objects within it.

解析: 在MySQL中，数据库权限适用于一个数据库及其内部的所有对象。这意味着当你给某个用户或角色分配权限时，这些权限将适用于特定数据库中的表、视图、存储过程等所有对象。例如，如果授予某用户对某数据库的SELECT权限，该用户将能够查询该数据库中的所有表。其他选项，如b. 控制数据库服务器的所有数据库、c. 数据库系统包含的所有文件、d. 所有关系表，这些描述不精确地反映了MySQL中权限的应用范围。在MySQL中，权限可以非常具体，也可以更广泛地应用，但标准的权限控制通常是针对特定数据库及其内部对象。

* * *

**You:**

Question 05
In MySQL table privileges apply to

a.
All tables controlled by a database server.


b.
All files a relational table consists of.


c.
A relational table and its columns.


d.
All tables in a given database.

* * *

**ChatGPT:**

答案: c. A relational table and its columns.

解析: 在MySQL中，表权限适用于关系表及其列。这意味着当你给某个用户或角色分配表级别的权限时，这些权限将适用于特定表及其列。例如，如果授予某用户对某表的SELECT权限，该用户将能够查询该表的所有列。这种权限控制提供了更细粒度的安全管理，允许数据库管理员精确控制用户对每个表甚至每个列的访问。其他选项，如a. 数据库服务器控制的所有表、b. 关系表包含的所有文件、d. 给定数据库的所有表，这些描述不准确地反映了MySQL中表权限的应用范围。表权限是特定于单个表的，可以进一步细化到列级别。

* * *

**You:**

Question 06
In MySQL column privileges apply to


a.
The columns in a relational table.


b.
All columns in all relational tables.


c.
All columns in a given relational table except primary key columns.


d.
All columns in a given relational table.

* * *

**ChatGPT:**

答案: a. The columns in a relational table.

解析: 在MySQL中，列权限适用于关系表中的列。这意味着当你给某个用户或角色分配列级别的权限时，这些权限将特定于被指定的列。这允许数据库管理员对特定列进行更细致的访问控制，比如只允许用户访问某个表中的某些列。其他选项，如b. 所有关系表的所有列、c. 给定关系表中除主键列之外的所有列、d. 给定关系表的所有列，这些描述不精确地反映了MySQL中列权限的应用范围。列权限是非常具体的，通常用于对敏感数据进行更细粒度的保护。

* * *

**You:**

Question 07
In MySQL global privileges apply to


a.
All relational tables that have global access rights.


b.
All databases on a given server.


c.
All global system initialisation variables.


d.
All global database servers at different sites.

* * *

**ChatGPT:**

答案: b. All databases on a given server.

解析: 在MySQL中，全局权限（Global Privileges）适用于给定服务器上的所有数据库。这种权限级别是最高的，影响着服务器上所有数据库的访问和管理。当你授予某个用户全局权限时，这些权限将在服务器上的所有数据库中生效。例如，授予用户全局的SELECT权限，那么该用户将能够查询服务器上所有数据库的表。其他选项，如a. 拥有全局访问权的所有关系表、c. 所有全局系统初始化变量、d. 不同站点的所有全局数据库服务器，这些描述不正确地反映了MySQL中全局权限的作用范围。全局权限是针对整个MySQL服务器的，而不是特定于某个表、变量或跨站点的服务器。

* * *

**You:**

Question 08
Why database systems need many database engines ?


a.
To adjust the implementation details to data characteristics and to speed up data processing.

b.
To increase security of database systems.


c.
To increase complexity of database systems.


d.
To reduce data vulnerabilities.

* * *

**ChatGPT:**

答案: a. To adjust the implementation details to data characteristics and to speed up data processing.

解析: 数据库系统需要多种数据库引擎的原因主要是为了调整实现细节以适应数据特性，并加快数据处理速度。不同的数据库引擎针对不同类型的数据操作和数据存储需求进行了优化。例如，一些引擎可能针对大量读取操作进行了优化，而其他引擎可能更适合频繁的写入操作或复杂的事务处理。通过选择适合特定应用需求的数据库引擎，可以提高数据库系统的整体性能和效率。

选项b、c和d，虽然在某些情况下可能是考虑因素，但它们不是数据库系统需要多种数据库引擎的主要原因。安全性和减少数据漏洞是重要的考虑因素，但这些通常通过设计和安全策略来解决，而不是简单地通过使用多种数据库引擎来实现。增加系统复杂性通常是多引擎带来的副作用，而非目的。

* * *

**You:**

Question 09
Which layer of software is not implemented in a typical relational database system ?


a.
DDL and DML processing.


b.
Network based client-server tools.


c.
Database storage engines.


d.
Artificial neural networks for data analysis.

* * *

**ChatGPT:**

答案: d. Artificial neural networks for data analysis.

解析: 典型的关系数据库系统不实现的软件层是人工神经网络用于数据分析。人工神经网络是一种用于机器学习和人工智能领域的技术，通常用于数据挖掘和复杂的模式识别任务。而关系数据库系统主要专注于数据存储、管理和查询，其核心组件包括数据定义语言（DDL）和数据操纵语言（DML）处理、网络基础的客户端-服务器工具、数据库存储引擎等。这些组件支持数据库的基本操作和管理，而人工神经网络属于更高级的数据分析工具，通常不包含在标准的关系数据库系统中。

* * *

**You:**

Question 10
System initialisation variables are used
a.
To speed up query processing.
b.
To increase data consistency.
c.
To determine functionality of a database server.
d.
To increase data security.

* * *

**ChatGPT:**

答案: c. To determine functionality of a database server.

解析: 系统初始化变量用于确定数据库服务器的功能。这些变量在数据库系统启动时设置，决定了数据库服务器的各种配置和操作参数。例如，它们可以控制数据库的内存使用、连接设置、性能优化参数等。通过调整这些初始化变量，数据库管理员可以对服务器的行为进行精细控制，以满足特定的性能和功能需求。

尽管这些变量间接影响到查询处理的速度（选项a）、数据一致性（选项b）和数据安全性（选项d），它们的主要作用是确定和配置数据库服务器的基本功能和行为。因此，c选项是最准确的描述。

* * *

**You:**

Question 11
What should be done if we would like to change a value of system initialisation variable that is not dynamic ?


a.
Use SET statement.

b.
Shutdown the server, use SET statement and restart the server.

c.
It is impossible to change a value of system initialisation variable that is not dynamic.


d.
Shutdown the server, restart it and use SET statement.

* * *

**ChatGPT:**

答案: b. Shutdown the server, use SET statement and restart the server.

解析: 如果我们想要改变一个非动态系统初始化变量的值，需要先关闭服务器，然后使用SET语句设置新的值，最后重启服务器。非动态系统初始化变量是在数据库服务器启动时设置的，不能在数据库运行时更改。因此，要更改这些变量，必须先关闭数据库服务器，修改配置文件中的相应设置，然后重新启动服务器以使更改生效。

选项a是错误的，因为SET语句通常用于修改动态变量，这些变量可以在数据库运行时更改。选项c也是错误的，因为虽然非动态变量不能在运行时更改，但可以在服务器重启过程中进行更改。选项d的顺序不正确，应先设置新值再重启服务器。

* * *

**You:**

Question 12
Assume that a relational table PROJECT is located in a database X and a relational table DEPARTMENT is located in a database Y. What method should be used to join the relational tables PROJECT and DEPARTMENT ?

a.
Make a database X default and use Y as a prefix to a name of a relational table DEPARTMENT.

b.
Copy a relational table PROJECT to a database Y.

c.
It is impossible to join the relational tables located in different databases.


d.
Make both databases X and Y default.

* * *

**ChatGPT:**

答案: a. Make a database X default and use Y as a prefix to a name of a relational table DEPARTMENT.

解析: 当需要连接位于不同数据库中的关系表时，一种常用方法是将一个数据库设为默认（在这个例子中是数据库X），然后使用数据库名作为前缀来引用另一个数据库（Y）中的表。在这种情况下，可以将数据库X设为默认，然后在查询中使用数据库Y的名字作为表DEPARTMENT的前缀。这样，即使表PROJECT和DEPARTMENT位于不同的数据库中，也可以在一个查询中联接它们。

选项b（将表PROJECT复制到数据库Y）是一种可能的方法，但这不是最有效的方法，因为它涉及数据的冗余复制。选项c（不可能联接位于不同数据库的表）不正确，因为许多数据库管理系统支持跨数据库的查询和联接。选项d（将数据库X和Y都设为默认）在实际操作中并不可行，因为通常一次只能有一个默认数据库。

* * *

**You:**

Question 13
Database security means


a.
Protection of database administrator account against unauthorised access, either intentional or unintentional.


b.
Protection of operating systems against unauthorised access, either intentional or unintentional.


c.
Protection of computer hardware use to run a  database system.


d.
Protection of a database against unauthorised access, either intentional or unintentional.

* * *

**ChatGPT:**

答案: d. Protection of a database against unauthorised access, either intentional or unintentional.

解析: 数据库安全是指保护数据库防止未经授权的访问，无论这种访问是故意的还是无意的。这包括保护数据库中的数据不受未授权访问、窃取、篡改或破坏。数据库安全措施包括实现访问控制、加密数据、监控和审计数据库活动等。

选项a只关注数据库管理员账户的安全，而数据库安全的范围更广泛。选项b关注的是操作系统的安全，而不是数据库安全。同样，选项c关注的是运行数据库系统的计算机硬件的安全，这虽然是整体安全的一部分，但不是数据库安全的直接定义。正确答案是d，因为它全面描述了数据库安全的核心目的。

* * *

**You:**

Question 14
Which one of the threats listed below is not a threat that affects a database system ?


a.
Failure of air conditioning system.


b.
Failure of security mechanisms.


c.
Illegal entry by hacker.


d.
Unauthorised amendment or copying of data.

* * *

**ChatGPT:**

答案: a. Failure of air conditioning system.

解析: 虽然空调系统的故障可能对维护数据库服务器的物理环境有影响，但它本身不直接影响数据库系统的运行或安全。选项a所述的空调系统故障更多地关联于硬件设备的物理环境管理，而不是数据库系统内部的安全和运行。

相比之下，选项b（安全机制的故障）、选项c（黑客的非法入侵）和选项d（未经授权的数据修改或复制）都是直接影响数据库系统安全和完整性的威胁。这些威胁可能导致数据丢失、数据泄露、数据篡改或服务中断等严重后果。因此，从数据库系统的视角来看，空调系统的故障不被视为直接威胁。

* * *

**You:**

Question 15
What is a principle of Discretionary Access Control (DAC) in database systems ?


a.
In Discretionary Access Control (DAC) each user is given the access rights (privileges) on the specific database objects.


b.
In Discretionary Access Control (DAC) access to data objects is at discretion of database administrator.


c.
In Discretionary Access Control (DAC) each user is given access to data repository tables that contain access information.


d.
In Discretionary Access Control (DAC) the users are granted clearance levels and data objects are granted security levels.

* * *

**ChatGPT:**

答案: a. In Discretionary Access Control (DAC) each user is given the access rights (privileges) on the specific database objects.

解析: 自主访问控制（Discretionary Access Control, DAC）的原则是每个用户被授予对特定数据库对象的访问权（权限）。在DAC模型中，数据的所有者或拥有者可以自行决定谁可以访问其数据，并控制对这些数据的具体访问权限，如读取、写入、修改或删除等。这种访问控制模型在多数商业数据库系统中被广泛采用。

选项b描述的是数据库管理员控制访问权限的情况，这更类似于强制访问控制（MAC）而不是DAC。选项c描述的是用户访问包含访问信息的数据存储表，这并不是DAC的核心原则。选项d涉及清除级别和数据对象的安全级别，这实际上是强制访问控制（MAC）的特征，而非DAC。因此，选项a是正确答案。

* * *

**You:**

你把1-15题及其对应的答案和简要讲解汇总给我。我是让你把完整英文题目和英文选择以及中文讲解发给我。

* * *

**ChatGPT:**

当然，以下是1-15题及其对应的答案和简要讲解的汇总：

1. **Data buffer cache is used to**
   
    * 答案: a. Speed up processing of SQL statements.
    * 讲解: 数据缓冲区主要用于加速SQL语句的处理，通过减少对硬盘的访问次数来加快数据的读写速度。
2. **What is a principle of Mandatory Access Control (MAC) in database systems?**
   
    * 答案: b. In Mandatory Access Control (MAC) access to data objects is controlled by system-wide policies that cannot be changed by the individual users.
    * 讲解: MAC的原则是通过系统范围的策略来控制对数据对象的访问，这些策略不能被单个用户更改。
3. **A database privilege is**
   
    * 答案: c. A right to perform an operation on a database or to access in read or write mode a data object stored in a database.
    * 讲解: 数据库权限指在数据库中执行操作或以读写模式访问存储在数据库中的数据对象的权利。
4. **In MySQL database privileges apply to**
   
    * 答案: a. A database and all objects within it.
    * 讲解: 在MySQL中，数据库权限适用于一个数据库及其内部的所有对象。
5. **In MySQL table privileges apply to**
   
    * 答案: c. A relational table and its columns.
    * 讲解: 在MySQL中，表权限适用于关系表及其列。
6. **In MySQL column privileges apply to**
   
    * 答案: a. The columns in a relational table.
    * 讲解: 在MySQL中，列权限适用于关系表中的列。
7. **In MySQL global privileges apply to**
   
    * 答案: b. All databases on a given server.
    * 讲解: 全局权限在MySQL中适用于给定服务器上的所有数据库。
8. **Why database systems need many database engines?**
   
    * 答案: a. To adjust the implementation details to data characteristics and to speed up data processing.
    * 讲解: 多种数据库引擎用于调整实现细节以适应数据特性，并加快数据处理速度。
9. **Which layer of software is not implemented in a typical relational database system?**
   
    * 答案: d. Artificial neural networks for data analysis.
    * 讲解: 典型的关系数据库系统中不实现人工神经网络用于数据分析。
10. **System initialisation variables are used**
    
    * 答案: c. To determine functionality of a database server.
    * 讲解: 系统初始化变量用于确定数据库服务器的功能。
11. **What should be done if we would like to change a value of system initialisation variable that is not dynamic?**
    
    * 答案: b. Shutdown the server, use SET statement and restart the server.
    * 讲解: 对于非动态的系统初始化变量，需要关闭服务器，使用SET语句设置新值，然后重启服务器。
12. **Assume that a relational table PROJECT is located in a database X and a relational table DEPARTMENT is located in a database Y. What method should be used to join the relational tables PROJECT and DEPARTMENT?**
    
    * 答案: a. Make a database X default and use Y as a prefix to a name of a relational table DEPARTMENT.
    * 讲解: 将一个数据库设为默认，然后使用另一个数据库的名字作为前缀来联接位于不同数据库中的表。
13. **Database security means**
    
    * 答案: d. Protection of a database against unauthorised access, either intentional or unintentional.
    * 讲解: 数据库安全是指保护数据库防止未经授权的访问。
14. **Which one of the threats listed below is not a threat that affects a database system?**
    
    * 答案: a. Failure of air conditioning system.
    * 讲解: 空调系统的故障不直接影响数据库系统的运行或安全。
15. **What is a principle of Discretionary Access Control (DAC) in database systems?**
    
    * 答案: a. In Discretionary Access Control (DAC) each user is given the access rights (privileges) on the specific database objects.
    * 讲解: DAC的原则是每个用户被授予对特定数据库对象的访问权。

* * *

**You:**

Question 01
Which one of the following guidelines is NOT a database security guideline ?


a.
Use GRANT and REVOKE statements to control access to MySQL and do not grant more privileges than necessary.

b.
Use SHOW GRANTS statement to check which accounts have access to what data objects.

c.
Use the -p or --password option on the command line with no password value.

d.
Create indexes to speed up query processing.

* * *

**ChatGPT:**

答案: d. Create indexes to speed up query processing.

解析: 创建索引以加速查询处理并不是一个数据库安全指南。虽然索引对于提高数据库查询性能非常重要，但它们与数据库的安全性无直接关联。数据库安全指南通常涉及控制和管理对数据库的访问，如使用GRANT和REVOKE语句来控制对MySQL的访问（选项a），或使用SHOW GRANTS语句来检查哪些账户可以访问哪些数据对象（选项b）。选项c（在命令行上使用-p或--password选项而不带密码值）也与安全相关，尽管这通常被视为不安全的做法。因此，d选项是不符合数据库安全指南的。