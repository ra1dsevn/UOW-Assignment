**数据库QUIZ11**

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

答案是：

c. Use the -p or --password option on the command line with no password value.

解析： 这个选项不是数据库安全准则。在数据库安全方面，明文存储密码或者在命令行中不提供密码值都是不安全的做法。正确的做法是使用安全的方式管理密码，而不是留空或者以明文方式传递密码。其他选项都是数据库安全准则的一部分，包括使用GRANT和REVOKE语句来控制访问权限，使用SHOW GRANTS语句来检查帐户对数据对象的访问权限，以及创建索引以加速查询处理。

* * *

**You:**

Question 02
Which consistency constraint CANNOT be enforced by CREATE TABLE statement ?

a.
Column type constraint.

b.
Multitable referential integrity constraint.

c.
Candidate key constraint.

d.
NULL/NOT NULL constraint.

* * *

**ChatGPT:**

答案是：

b. Multitable referential integrity constraint.

解析： CREATE TABLE语句通常用于创建单个表，并可以通过列类型约束、候选键约束以及NULL/NOT NULL约束来强制执行一致性约束。然而，它无法直接创建多表的参照完整性约束（Multitable referential integrity constraint）。这种约束涉及多个表之间的关系，通常需要使用ALTER TABLE语句或者其他数据库管理语句来实施。

其他选项中，列类型约束、候选键约束和NULL/NOT NULL约束可以通过CREATE TABLE语句来定义和强制执行。

* * *

**You:**

Question 03
Which method of verification of consistency constraint is not practical ?


a.
Using stored routines.


b.
Listing the all data that satisfy a given consistency constraint.


c.
Using database triggers.


d.
Listing all data that violate a give consistency constraint.

* * *

**ChatGPT:**

答案是：

d. Listing all data that violate a given consistency constraint.

解析： 验证一致性约束时，通常使用以下方法：

a. 使用存储过程（Using stored routines）：这是一种实际可行的方法，通过编写存储过程来检查数据是否符合一致性约束。

b. 列出满足给定一致性约束的所有数据（Listing the all data that satisfy a given consistency constraint）：这也是一种实际可行的方法，可以通过查询来获取符合约束的数据。

c. 使用数据库触发器（Using database triggers）：触发器可以在数据插入、更新或删除时执行自定义的操作，包括验证一致性约束。这是一种实际可行的方法。

d. 列出违反给定一致性约束的所有数据（Listing all data that violate a given consistency constraint）：这个选项不是一个实际可行的方法，因为通常情况下，约束违规的数据可能会很多，不容易手动列出所有违规的数据。更常见的做法是通过查询或触发器来检测违规数据，而不是手动列出它们。

* * *

**You:**

Question 04
A stored routine is


a.
A collection of SQL statements stored in SQL script.


b.
A stored report from processing of SQL script.


c.
A piece of code stored in a text file outside a database systems.


d.
A piece of code stored in a data dictionary.

* * *

**ChatGPT:**

答案是：

a. A collection of SQL statements stored in SQL script.

解析： 存储过程（Stored routine）是一种数据库对象，它是一组存储在数据库中的SQL语句的集合。这些SQL语句可以被命名和存储在数据库中，然后通过调用存储过程来执行它们。存储过程通常用于执行一系列操作，可以接受参数并返回结果，提供了一种有效管理和执行数据库逻辑的方式。所以选项a描述了存储过程的特性。其他选项描述不准确。

* * *

**You:**

Question 05
A database trigger is


a.
A piece of code that is used for implementation of a graphical user interface of a database application.


b.
A piece of code stored in a user relational table to be used as SQL script.


c.
A piece of code that it is automatically activated when a particular event happens and a pre-defined condition is satisfied.


d.
A piece of code stored in SQL script that is automatically activated when the script is processed.

* * *

**ChatGPT:**

答案是：

c. A piece of code that is automatically activated when a particular event happens and a pre-defined condition is satisfied.

解析： 数据库触发器（Database trigger）是一种数据库对象，它包含一段代码，当特定的事件发生并且满足预定义的条件时，该代码会自动触发执行。触发器通常用于监视数据库中的事件，如数据插入、更新或删除，并在事件发生时执行一些特定的操作。因此，选项c描述了数据库触发器的特性，其他选项描述不准确。

* * *

**You:**

Question 06
Which operations on a database CANNOT be reversed with ROLLBACK statement ?

a.
All data insertion and deletion operations.


b.
All data modification operations.


c.
All data definition operations.


d.
All data retrieval operations.

* * *

**ChatGPT:**

答案是：

d. All data retrieval operations.

解析： ROLLBACK语句通常用于撤销数据库事务中的更改，以回滚到之前的状态。然而，数据检索操作（data retrieval operations）通常是只读操作，不会修改数据库的内容，因此它们不需要被回滚，也不能被回滚，因为它们本身不会对数据库进行更改。

其他选项中，数据插入、删除和修改操作可以在事务中使用ROLLBACK语句来撤销，从而恢复到之前的数据库状态。数据定义操作（data definition operations）通常用于创建、修改或删除数据库对象（如表、索引等），也可以通过ROLLBACK来撤销，以回滚到之前的数据库结构状态。

* * *

**You:**

Question 07
What is a difference between physical backup and logical backup ?


a.
Physical backup is stored in persistent storage while a logical backup is stored in a transient memory.


b.
Physical backup is created only by a database administrator and a logical backup can be created by anyone.


c.
Physical backup contains the database contents stored in a binary format while a logical backup contains SQL statements that can be used to recover data.


d.
Physical backup can be used for data recovery while a logical backup can only be used for data archiving.

* * *

**ChatGPT:**

答案是：

c. Physical backup contains the database contents stored in a binary format while a logical backup contains SQL statements that can be used to recover data.

解析： 物理备份（physical backup）是以二进制格式存储数据库内容的备份，通常包括数据库文件的副本。它是一个完整的数据库副本，可以用于数据恢复。

逻辑备份（logical backup）包含用于恢复数据的SQL语句，而不是二进制数据库文件的副本。它通常是SQL导出文件，包含了表、数据和数据库结构的SQL语句，可以用于在不同数据库管理系统之间迁移数据或进行数据恢复。逻辑备份不是二进制副本，因此在某些情况下可能不如物理备份高效，但它提供了更大的灵活性。

其他选项中，a和b描述的是不准确的区别，而d描述的不准确，因为逻辑备份也可以用于数据恢复，不仅仅是数据归档。

* * *

**You:**

Question 08
Which method of securing passwords is extremely insecure ?


a.
Using -pyour_password or --password=your_password option on the command line.

b.
Using the mysql_config_editor utility to store authentication credentials in an encrypted login path file named .mylogin.cnf.

c.
Storing your password in the MYSQL_PWD environment variable.

d.
Storing your password in a file with system variables in a section.

* * *

**ChatGPT:**

答案是：

a. Using -pyour_password or --password=your_password option on the command line.

解析： 在命令行中使用明文密码选项（例如-pyour_password或--password=your_password）是极其不安全的做法。这会导致密码以明文形式出现在命令行历史记录中，可以轻松被他人访问。这种方式将密码暴露在不安全的环境中，因此是极度不安全的。

其他选项中，b描述了使用mysql_config_editor工具来安全存储认证凭据，c描述了将密码存储在环境变量中，而d描述了将密码存储在一个带有系统变量的文件中，这些方法相对来说更安全。

* * *

**You:**

Question 09
What SQL statement can be used to change password to a user account ?


a.
DROP USER statement.

b.
ALTER PASSWORD statement.

c.
ALTER USER statement.

d.
CREATE USER statement.

* * *

**ChatGPT:**

答案是：

c. ALTER USER statement.

解析： 要更改用户帐户的密码，通常可以使用ALTER USER语句，然后指定要更改密码的用户名和新密码。例如，可以使用以下方式来更改密码：

```sql
ALTER USER username IDENTIFIED BY 'new_password';
```

其他选项描述不是更改密码的SQL语句。DROP USER语句用于删除用户，ALTER PASSWORD和CREATE USER也不是标准的SQL语句。

* * *

**You:**

Question 10
Where we can find information about the names of user accounts and passwords ?


a.
In a file /etc/mysql/users.txt.

b.
In mysql database, in user relational table.

c.
In users database, in password relational table.

d.
In system tablespace, in dba_users relational table.

* * *

**ChatGPT:**

答案是：

b. In mysql database, in user relational table.

解析： 用户帐户和密码信息通常存储在数据库管理系统的系统数据库中，MySQL中存储在mysql数据库的用户关系表（user relational table）中。这个表包含了所有用户帐户的信息，包括用户名、密码和相关权限。其他选项中的路径和数据库描述都不准确。

* * *

**You:**

Question 11
How passwords are stored in data dictionary table ?


a.
As plaintext.

b.
As plaintext in a hidden data dictionary table.

c.
As encrypted text using plugin-specific algorithm.

d.
As encrypted text in a hidden column of user relational table.

* * *

**ChatGPT:**

答案是：

c. As encrypted text using plugin-specific algorithm.

解析： 密码通常不以明文形式存储在数据字典表中，以增加安全性。相反，它们通常以加密文本的形式存储，使用特定于插件的算法进行加密。这有助于保护用户帐户的安全，因为即使攻击者能够访问数据字典表，他们也无法轻松地获取明文密码。

其他选项描述的方式都不是通常用于存储密码的方法。密码不应以明文形式存储在数据库中，以防止安全风险。

* * *

**You:**

Question 12
An account resource limit is


a.
System initialisation variable.


b.
One of the global privileges.


c.
A restriction on utilisation of a database server resources.


d.
A restriction on the total number of database used at a server installation stage.




* * *

**ChatGPT:**

答案是：

c. A restriction on the utilization of a database server's resources.

解析： 帐户资源限制是指对数据库服务器资源利用的限制。这些限制可以包括对CPU、内存、连接数等资源的限制，以确保一个帐户或用户不能过度消耗服务器资源，从而影响其他用户或系统性能。这些限制有助于维护数据库服务器的稳定性和性能。

其他选项描述不准确。它不是系统初始化变量，也不是全局特权，也不是与服务器安装阶段的数据库数量有关。

* * *

**You:**

Question 13
How it is possible to set an account resource limit ?


a.
With ALTER USER statement.

b.
With GRANT statement.

c.
With ALTER RESOURCE statement.

d.
With SET statement.

* * *

**ChatGPT:**

答案是：

a. With ALTER USER statement.

解析： 可以使用ALTER USER语句来设置帐户资源限制。ALTER USER语句允许管理员或用户更改特定用户帐户的属性，包括资源限制，例如CPU使用、连接数等。通过指定适当的选项，可以设置和修改帐户的资源限制。

其他选项描述不准确。GRANT语句用于授予权限，ALTER RESOURCE和SET语句不是用于设置帐户资源限制的标准SQL语句。

* * *

**You:**

Question 14
When do we need to lock user account ?


a.
When audit information indicates data security breach by a user.


b.
When a user connects to a database system on public holiday.


c.
When the total number of relational tables created by a user is too large.


d.
When one of the relational tables created by a user is too large.

* * *

**ChatGPT:**

答案是：

a. When audit information indicates data security breach by a user.

解析： 用户帐户可能需要被锁定的情况之一是当审计信息表明用户存在数据安全漏洞或违规行为时。在出现可疑活动或安全问题时，锁定帐户是一种常见的安全措施，以保护数据库的完整性和安全性。

其他选项描述的情况通常不会导致锁定用户帐户。用户在公共假期连接到数据库系统或者创建大量的关系表通常不是锁定帐户的原因。

* * *

**You:**

Question 15
The overall intent of any data integrity technique is


a.
To ensure, that data is recorded exactly as intended and upon later retrieval, ensure he data is the same as it was when it was originally recorded.


b.
To ensure that the amounts of data are consistent with earlier defined database size.


c.
To ensure that data is accessed by the users who have the appropriate rights.


d.
To ensure a correct optimisation of data processing.

* * *

**ChatGPT:**

答案是：

a. To ensure that data is recorded exactly as intended and upon later retrieval, ensure the data is the same as it was when it was originally recorded.

解析： 数据完整性技术的总体目的是确保数据被准确地记录，并在以后检索时确保数据与最初记录时的数据相同。这包括确保数据的准确性、一致性和可靠性，以防止数据的损坏、篡改或丢失。数据完整性是数据库管理中至关重要的方面，以保护数据的完整性和可信度。

其他选项描述的是数据管理中的其他方面，但不是数据完整性技术的主要目标。

* * *

**You:**

你把1-15题及其对应的答案和简要讲解汇总给我。我是让你把完整英文题目和英文选择以及中文讲解发给我。

* * *

**ChatGPT:**

当然，下面是1到15题的完整英文问题、选项和中文解释：

Question 01: Which one of the following guidelines is NOT a database security guideline?

a. Use GRANT and REVOKE statements to control access to MySQL and do not grant more privileges than necessary.

b. Use SHOW GRANTS statement to check which accounts have access to what data objects.

c. Use the -p or --password option on the command line with no password value.

d. Create indexes to speed up query processing.

答案：c 解释：这个选项不是数据库安全准则，因为在数据库安全方面，明文存储密码或者在命令行中不提供密码值都是不安全的做法。

Question 02: Which consistency constraint CANNOT be enforced by CREATE TABLE statement?

a. Column type constraint.

b. Multitable referential integrity constraint.

c. Candidate key constraint.

d. NULL/NOT NULL constraint



* * *

**ChatGPT:**

当然，请查看以下的英文题目和正确选项：

**Question 01:** Which one of the following guidelines is NOT a database security guideline? 

**Answer:** c. Use the -p or --password option on the command line with no password value.

**Question 02:** Which consistency constraint CANNOT be enforced by CREATE TABLE statement? 

**Answer:** b. Multitable referential integrity constraint.

Question 03: Which method of verification of consistency constraint is not practical? 

**Answer:** d. Listing all data that violate a given consistency constraint.

**Question 04:** A stored routine is 

**Answer:** a. A collection of SQL statements stored in SQL script.

**Question 05:** A database trigger is 

**Answer:** c. A piece of code that is automatically activated when a particular event happens and a pre-defined condition is satisfied.

**Question 06**: Which operations on a database CANNOT be reversed with ROLLBACK statement? 

**Answer:** d. All data retrieval operations.

**Question 07:** What SQL statement can be used to change password to a user account? 

**Answer: c**. ALTER USER statement.

**Question 08:** Where we can find information about the names of user accounts and passwords? 

**Answer**: b. In mysql database, in user relational table.

**Question 09:** How passwords are stored in data dictionary table? 

**Answer**: c. As encrypted text using plugin-specific algorithm.

**Question** **10**: An account resource limit is 

**Answer**: c. A restriction on utilisation of a database server resources.

**Question** **11**: How it is possible to set an account resource limit? 

**Answer**: a. With ALTER USER statement.

**Question 12:** When do we need to lock user account? 

**Answer**: a. When audit information indicates data security breach by a user.

**Question 13:** The overall intent of any data integrity technique is 

**Answer**: a. To ensure, that data is recorded exactly as intended and upon later retrieval, ensure the data is the same as it was when it was originally recorded.