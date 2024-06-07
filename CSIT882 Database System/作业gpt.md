**You:**

Question 01
A data model provides


a.
A standard for implementation of a relational database database system.


b.
An abstract view of data, that can be used for data definition, data manipulation, data retrieval , and data administration.


c.
Automatic implementation of a database system, that is consistent with a given set of user requirements.


d.
A standard for implementation of non-relational database system.

* * *

**ChatGPT:**

A data model primarily provides:

b. An abstract view of data, that can be used for data definition, data manipulation, data retrieval, and data administration.

A data model is an abstract representation of the organizational data, often used to depict the relationships, constraints, rules, and structures of the data in a way that’s independent of any specific technology or implementation. It aids in organizing and defining how data should be stored and accessed, serving as a blueprint for developers, database administrators, and other IT professionals.

* * *

**You:**

Question 02
A NULL constraint says, that


a.
An attribute (column) in a relational table must have only NULL values .


b.
An attribute (column) in a relational table may have NULL values.


c.
An attribute (column) in a relational table must be completely empty.


d.
An attribute (column) in a relational table may have no values at all.

* * *

**ChatGPT:**

It seems there may be a slight misunderstanding in the question phrasing. Constraints in databases are typically used to limit the type of data that can go into a table. So, when you talk about a "NULL constraint," it's often in the context of specifying whether a column should allow NULL values or not.

The NOT NULL constraint is used to specify that a column cannot have NULL values. If there is no NOT NULL constraint, then:

b. An attribute (column) in a relational table may have NULL values.

This option is the most accurate description, given that without a NOT NULL constraint, a column may have NULL values, meaning it is allowed to have such values in some or all of its rows.

* * *

**You:**

你翻一下这个题目

* * *

**ChatGPT:**

当然可以。这个题目翻译成中文是：

问题 02 NULL 约束表明：

a. 关系表中的一个属性（列）必须只有 NULL 值。

b. 关系表中的一个属性（列）可能有 NULL 值。

c. 关系表中的一个属性（列）必须完全为空。

d. 关系表中的一个属性（列）可能根本没有值。

* * *

**You:**

那应该怎么选？

* * *

**ChatGPT:**

应该选择：

b. 关系表中的一个属性（列）可能有 NULL 值。

这个选项意味着，在没有 NOT NULL 约束的情况下，表的一个属性（列）是允许有 NULL 值的。

* * *

**You:**

讲一下约束

* * *

**ChatGPT:**

在数据库管理系统中，约束（Constraints）用于限制表中数据列的数据类型及数据的值，确保数据的完整性和准确性。以下是几种常见的约束：

### 1. 主键约束（PRIMARY KEY）

* 确保某列（或两个列以上的组合）有唯一值。
* 每个表都应该有一个主键。
* 主键的列不能有 NULL 值。

### 2. 唯一约束（UNIQUE）

* 确保某列的所有值都是唯一的。
* 与主键不同，唯一约束的列允许有 NULL 值。

### 3. 外键约束（FOREIGN KEY）

* 用于建立两个表之间的链接。
* 外键中的值必须对应另一张表中的主键的值。

### 4. 非空约束（NOT NULL）

* 确保某列不能有 NULL 值。

### 5. 检查约束（CHECK）

* 确保某列中的所有值满足特定条件。
* 例如，可以设置检查约束，以确保薪资列的值大于 0。

### 6. 默认约束（DEFAULT）

* 为某列设置默认值。如果插入行时没有为该列指定值，则会使用默认值。

### 示例：

```sql
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT CHECK (Age > 0),
    Salary FLOAT DEFAULT 50000.00,
    DepartmentID INT,
    UNIQUE (Name),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
```

在此示例中：

* `ID` 是主键，要求唯一，且不允许 NULL 值。
* `Name` 列有唯一约束，要求其值唯一，且由于有非空约束，不允许 NULL 值。
* `Age` 列有检查约束，要求其值必须大于 0。
* `Salary` 列有默认约束，如果未指定值，则默认为 50000.00。
* `DepartmentID` 是外键，引用了 Departments 表的 DepartmentID 列。

* * *

**You:**

Question 03
An entity integrity constraint says, that


a.
A relational table must be integrated with a respective class of objects.


b.
No column belonging to a primary or candidate key is allowed to take on NULL in any row.


c.
The rows in a relational table represent the real world entities.


d.
It should be possible to integrate two or more relational tables into one relational table.

* * *

**ChatGPT:**

An entity integrity constraint refers to the concept in database theory which ensures that every table has a primary key and that the column or columns chosen to be the primary key should be unique and not null. This is to uniquely identify each record in a table. So, the correct answer is:

b. No column belonging to a primary or candidate key is allowed to take on NULL in any row.

* * *

**You:**

Question 04
A foreign key is


a.
An alien minimal key.


b.
A set of attributes in a relational table, such the combination of values of the attributes either contains NULLs or else matches the combination of values of a candidate or primary key in some other or the same relational table.


c.
A primary key in a relational table, such the combination of values of the attributes either contains NULLs or else matches the combination of values of a candidate or primary key in some other or the same relational table.


d.
A primary key in a relational table, such that combination of its values is the same as a combination of values of another primary key in another relational table.

* * *

**ChatGPT:**

A foreign key is a field (or collection of fields) in one table, that refers to the PRIMARY KEY in another table. The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table. The correct answer is:

b. A set of attributes in a relational table, such that the combination of values of the attributes either contains NULLs or else matches the combination of values of a candidate or primary key in some other or the same relational table.

* * *

**You:**

翻译一下

* * *

**ChatGPT:**

当然可以。下面是这个问题的中文翻译：

问题 04 外键是

a. 一个外来的最小键。

b. 关系表中的一组属性，这组属性的值组合要么包含 NULLs，要么与其他表或同一关系表中的候选键或主键的值组合相匹配。

c. 关系表中的一个主键，该主键的属性值组合要么包含 NULLs，要么与其他表或同一关系表中的候选键或主键的值组合相匹配。

d. 关系表中的一个主键，其值的组合与另一个表中的另一个主键的值组合相同。

* * *

**You:**

Question 05
A domain constraint is


a.
A condition imposed on implementation technique of the values of attributes.


b.
A condition imposed on the meaningful names of attributes and relational schemas.


c.
A condition imposed on the values of an attribute, that determines the allowed values of the attribute.


d.
A condition imposed on a relational schema, that allows only for the attributes of the given type.

* * *

**ChatGPT:**

A domain constraint is related to the permissible values that an attribute (or column) can have in a table within a relational database. So, the correct answer would be:

c. A condition imposed on the values of an attribute, that determines the allowed values of the attribute.

This means that domain constraints define the valid set of values for an attribute, often by specifying a data type, format, or range, thus ensuring data integrity and consistency across the database.

* * *

**You:**

Question 06
Referential integrity rule is in force when


a.
The columns of primary key have the values identical to the respective foreign key in another relational table.


b.
The columns of foreign key either have NULLs in at least one column that allows NULLs.


c.
The columns of foreign key have no NULLs and a combination of all its values is equal to the combination of primary key values in the other relational table.


d.
The columns of foreign key either have NULLs in at least one column that allows NULLs or have no NULLs and a combination of all its values is equal to the combination of primary key values in the other relational table.

* * *

**ChatGPT:**

Referential integrity is a concept in relational databases which ensures that relationships between tables remain consistent. It means that when one table has a foreign key to another table, the values in these columns must match the value in the referenced table's primary key, or be NULL.

So, the correct answer would be:

d. The columns of foreign key either have NULLs in at least one column that allows NULLs or have no NULLs and a combination of all its values is equal to the combination of primary key values in the other relational table.

* * *

**You:**

Question 07
A relational data model provides a view of a database as


a.
A collection of nested and linked records.


b.
A collection of mathematical relations over alphanumerical domains.


c.
A collection of two dimensional tables, that consist of a header, rows and columns.


d.
A collection of related classes of objects.

* * *

**ChatGPT:**

The relational data model conceptualizes the database as composed of a collection of tables (also referred to as relations), and each table has a header (columns or attributes) and rows (tuples or records). Each table represents a certain entity and the relationship between entities are maintained by using common attributes/columns between tables.

So, the most accurate answer would be:

c. A collection of two-dimensional tables, that consist of a header, rows, and columns.

* * *

**You:**

Question 08
Why the original E. F. Codd's definition of a relational table is not completely consistent with the properties of relational tables ?


a.
The original definition does not include a concept of association.


b.
The original definition does not include a concept of a key.


c.
The original definition imposes a given order of rows in a relational table.


d.
The original definition imposes a given order of columns in a relational table.

* * *

**ChatGPT:**

E.F. Codd's original definition of a relational model is considered seminal in the field of database design. However, the initial relational model as proposed by Codd had a set-based perspective, meaning it was based on set theory and did not impose any order on the rows or the columns in a table. In a true relational database, the order of rows and columns is irrelevant, and data is accessed based on data values and conditions, not on a row or column number.

Given this, the option that is most aligned with the inconsistencies between the original definition by Codd and the properties of modern relational tables is:

c. The original definition imposes a given order of rows in a relational table.

This option seems to address the idea that imposing an order of rows is inconsistent with the principles of the relational model, although it’s more accurate to say that in the true definition, there shouldn’t be any imposed order on rows or columns. If the choice was implying that the original definition does not impose any order, then the phrasing might be a bit misleading. The original relational model by Codd indeed does not impose any order on the rows or the columns in a table, making it a set-based model.

* * *

**You:**

Question 09
A relational table is in 1NF (First Normal Form) when


a.
It consists of less than 1 billion rows.


b.
It occupies less than 1 Gb of persistent storage.


c.
It has no multivalued and composite attributes.


d.
It has at least one nested attribute.

* * *

**ChatGPT:**

A table is in First Normal Form (1NF) when it adheres to the following conditions:

* All entries in a column are of the same data type.
* Each column has a unique name.
* Each row is unique (distinct).
* The order in which data is stored does not matter.

And, importantly:

* It contains no repeating groups or arrays, i.e., it has no multivalued or composite attributes.

So, the correct answer would be:

c. It has no multivalued and composite attributes.

* * *

**You:**

Question 10
Access to the rows by contents rule says


a.
We can only retrieve the rows by their numbers in a relational table.


b.
We can only retrieve the rows by their contents.


c.
We can only retrieve the rows by the values of primary key or candidate keys.


d.
We can only retrieve the rows by the physicals addresses of rows also called row identifiers.

* * *

**ChatGPT:**

The "Access to the rows by contents" rule, also known as the Information rule, is one of Codd’s twelve rules which states that all data should be accessible and modifiable solely by the use of relational operations, typically SQL queries, which rely on the data values themselves, and not on any form of physical pointers or addresses.

So, the closest answer would be:

b. We can only retrieve the rows by their contents.

This means that access to data is done through the content values and not through any form of location-based addressing or via pointers.

* * *

**You:**

Question 11
The unique rows principle says. that


a.
A relational table cannot contain two identical rows.


b.
A relational table must contain at least 2 identical rows.


c.
A relational table can contain at more than 2 identical rows.


d.
A relational table must not contain any unique rows.

* * *

**ChatGPT:**

The unique rows principle in the context of a relational database implies that every row/tuple in a table should be unique, meaning there should be no duplicate rows in a table.

So, the correct answer would be:

a. A relational table cannot contain two identical rows.

* * *

**You:**

Question 12
A key in a relational table is


a.
A nonempty set of attributes whose values are 'key-1', ', key-2', 'key-3', 'key-4', 'key-5', … .


b.
A nonempty set of attributes, such that it uniquely identifies each row.


c.
A nonempty set of attributes, that have only numerical values.


d.
A nonempty set of attributes whose values are 1, 2, 3, 4, 5, … .

* * *

**ChatGPT:**

A key in a relational table is indeed a very crucial concept. A key, in the context of databases, is a set of attributes within a table that can uniquely identify each record within that table.

So, the correct answer would be:

b. A nonempty set of attributes, such that it uniquely identifies each row.

* * *

**You:**

Question 13
A minimal key is


a.
A set of attributes whose values are the smallest values in the domains of attributes involved.


b.
A set of attributes such that a new set of attributes obtained by removal of any attribute from the original set is no longer a key.


c.
A set of attributes such that does not exists a large set of attributes that is a key.


d.
A set of attributes,  such that all attributes have the smallest values.

* * *

**ChatGPT:**

A minimal key in a relational database is a set of attributes that uniquely identify a record in a table with the minimum number of attributes possible. In other words, no attribute can be removed from the minimal key without losing the property of uniquely identifying each record.

So, the correct answer is:

b. A set of attributes such that a new set of attributes obtained by removal of any attribute from the original set is no longer a key.

* * *

**You:**

Question 14
A candidate key is


a.
Any minimal key in a relational schema.


b.
Any key in a relational schema.


c.
Any not minimal key in a relational schema.


d.
Any primary key in a relational schema.

* * *

**ChatGPT:**

A candidate key is a set of one or more attributes that can uniquely identify tuples (rows) in a table. A candidate key is essentially a minimal superkey, meaning there are no redundant attributes in a candidate key. It's called a "candidate key" because it is a candidate for being chosen as the primary key of the table.

So, the correct answer would be:

a. Any minimal key in a relational schema.

* * *

**You:**

Question 15
A primary key is


a.
Any not minimal key in a relational schema.


b.
One of candidate keys in a relational schema.


c.
Any key in a relational schema.


d.
The first key in a relational schema.

* * *

**ChatGPT:**

A primary key is a specific choice of a minimal superkey (candidate key) for a relational schema. There can be multiple candidate keys in a relational schema, but only one can be selected as the primary key. The primary key's purpose is to uniquely identify each record in a table.

So, the correct answer would be:

b. One of the candidate keys in a relational schema.

* * *

**You:**

Question 16
A relational table is called as "relational" because


a.
Originally, its contents have been defined as a subset of Relational product


b.
Originally, its contents have been defined as a subset of Cartesian product


c.
It contains information about the relations between the tables


d.
It represents the relations between the classes of objects

* * *

**ChatGPT:**

The term "relational" in "relational table" or "relational database" comes from the mathematical concept of a relation. In the context of relational databases, a relation is a set of tuples that have the same attributes—a subset of the Cartesian product of a list of domains. E.F. Codd introduced the term “relational” to denote this specific mathematical concept in the context of database systems. So, the relational table is "relational" because it represents a mathematical relation, and it is formed as a subset of the Cartesian product of the associated domains.

So, the correct answer is:

b. Originally, its contents have been defined as a subset of Cartesian product.

* * *

**You:**

Question 17
A process of logical design transforms a class of objects
ENROLMENT
student-number ID
subject-number ID
grade

a.
A single relational table ENROLMENT where student-number is a candidate key and subject-number is a primary key


b.
A single relational table ENROLMENT where (student-number, subject-number, grade) is a primary key


c.
A single relational table ENROLMENT where student-number is a primary key and subject-number is a candidate key


d.
A single relational table ENROLMENT where (student-number, subject-number) is a primary key

* * *

**ChatGPT:**

Logical design involves defining the structure of your database to fulfill the requirements, and it is crucial in determining how data is to be stored, accessed, and managed.

Given a class of objects ENROLMENT with attributes student-number, subject-number, and grade, it appears that each enrollment is uniquely identified by a combination of a student-number and a subject-number, as a student can be enrolled in multiple subjects and each subject can have multiple students enrolled.

Therefore, a logical choice for the primary key would be a composite key consisting of both student-number and subject-number. This would make each row in the table unique based on the combination of student-number and subject-number.

So, the correct option would be:

d. A single relational table ENROLMENT where (student-number, subject-number) is a primary key.

* * *

**You:**

Question 18
A process of logical design transforms a class of objects
STUDENT
student-number ID1
medicare-number ID2
full-name
degree

a.
A relational table STUDENT(student-number,medicare-number,full-name,degree) where primary key = (medicare-number,student-number)

b.
A relational table STUDENT(student-number,medicare-number,full-name,degree) where primary key = (student-number,medicare-number) and candidate key = (medicare-number)

c.
A relational table STUDENT(student-number,medicare-number,full-name,degree) where primary key = (medicare-number,student-number) and candidate key = (student-number)

d.
A relational table STUDENT(student-number,medicare-number,full-name,degree) where primary key = (student-number) and candidate key = (medicare-number)



* * *

**ChatGPT:**

In the context of relational database design, both student-number and medicare-number are given as identifiers (ID1 and ID2) which implies that they both uniquely identify a student. So, both can be candidate keys because a candidate key is a minimal superkey, which means it uniquely identifies each record in the table.

However, only one of the candidate keys can be selected as the primary key, and the others remain as alternate keys (or candidate keys).

So, the correct option would be:

d. A relational table STUDENT(student-number, medicare-number, full-name, degree) where primary key = (student-number) and candidate key = (medicare-number)

This means student-number is chosen as the primary key to uniquely identify records in the STUDENT table, and medicare-number remains as an alternate key which also uniquely identifies records.

* * *

**You:**

Question 19
A process of logical design transforms a class of objects
DRIVER
licence-numberID
full-name
registrations-of-cars-owned[0..*]

into


a.
Three relational tables
DRIVER(licence-number, full-name)
CARS-OWNED(licence-number,car-registration-number)
CAR(car-registration-number)

b.
Two relational tables
DRIVER(licence-number, full-name)
CARS-OWNED(licence-number,car-registration-number)

c.
Two relational tables
DRIVER(licence-number, full-name)
CARS-OWNED(licence-number,full-name,car-registration-number)

d.
A single relational table
DRIVER(licence-number, full-name, registrations-of-cars-owned)

* * *

**ChatGPT:**

In the given class of objects "DRIVER," a driver can own zero or more cars, indicated by "registrations-of-cars-owned[0..*]." This represents a one-to-many relationship between a driver and cars owned, as one driver can own multiple cars, but each car is owned by one driver.

Given this relationship, you will need a table to represent the drivers, another table to represent the relationships between the drivers and the cars they own (where each row represents one ownership relation), and possibly another table to represent the cars.

Option (a) Three relational tables DRIVER(licence-number, full-name), CARS-OWNED(licence-number,car-registration-number), and CAR(car-registration-number) seem the most logical choice. This is because it represents the driver details in the DRIVER table, the cars' details in the CAR table, and the relationships between drivers and their owned cars in the CARS-OWNED table.

So, the correct answer would be:

a. Three relational tables DRIVER(licence-number, full-name) CARS-OWNED(licence-number,car-registration-number) CAR(car-registration-number)

* * *

**You:**

Question 20
A process of logical design transforms a class of objects
DRIVER
licence-number ID
full-name
hobbies[0..*]
into

a.
Two relational tables
DRIVER(licence-number, full-name)
HAS-HOBBIES(licence-number,full-name,hobby)

b.
Three relational tables
DRIVER(licence-number, full-name)
HAS-HOBBIES(licence-number,hobby)
HOBBY(hobby)

c.
Two relational tables
DRIVER(licence-number, full-name)
HAS-HOBBIES(licence-number, hobby)

d.
A single relational table
DRIVER(licence-number, full-name, hobbies)

* * *

**ChatGPT:**

In the given scenario, you have a DRIVER class with a one-to-many relationship to hobbies, as indicated by "hobbies[0..*]." This implies that a driver can have zero or more hobbies.

Given this, you will need a table to represent the drivers and another table to represent the relationships between the drivers and their hobbies. You don't necessarily need a separate table just for hobbies unless there is more information about each hobby that needs to be stored.

So, the logical transformation would result in a DRIVER table to store information about each driver and a HAS-HOBBIES table to represent the many hobbies a driver can have. The HAS-HOBBIES table should have a foreign key relationship back to the DRIVER table using the licence-number.

So the correct answer would be:

c. Two relational tables DRIVER(licence-number, full-name) HAS-HOBBIES(licence-number, hobby)

* * *

**You:**

为什么19是三个关系而20是两个关系，没懂19题

* * *

**ChatGPT:**

问题19和问题20涉及到的逻辑设计不完全一样，这是因为它们处理的实体和关系有不同的性质。

在问题19中，我们有一位驾驶员和他拥有的汽车。这里有三个明确的实体集合：驾驶员、汽车和车辆所有权关系。这是一个典型的多对多关系，一个驾驶员可以拥有多辆汽车，一辆汽车可以被多个驾驶员拥有（例如，家庭共享的汽车）。这就是为什么我们需要三个表来准确地表示这种关系的原因。

1. DRIVER 表用来存储驾驶员的信息。
2. CAR 表用来存储每辆汽车的信息。
3. CARS-OWNED 表用来存储驾驶员和他们所拥有的汽车之间的关系。

而在问题20中，我们有一位驾驶员和他的爱好。这里的“爱好”不是独立的实体，而是驾驶员的一个属性。一个驾驶员可以有多个爱好，但一个爱好不能属于多个驾驶员。因此，我们只需要两个表：

1. DRIVER 表用来存储驾驶员的信息。
2. HAS-HOBBIES 表用来存储驾驶员和他们的爱好之间的关系。

简而言之，问题19涉及到了更复杂的多对多关系，需要三个表来准确表示。而问题20涉及到了更简单的一对多关系，所以只需要两个表。

* * *

**You:**

Question 21
A process of logical design transforms one-to-many association DRIVER Owns CAR
DRIVER
licence-number ID
first-name
last-name
Owns -&gt;
CAR
registration ID
make
model

into


a.
Three relational tables
DRIVER(licence-number,first-name,last-name)
OWNS(licence-number,registration-number)
CAR(registration-number,make,model)

b.
Two relational tables
DRIVER(licence-number,first-name,last-name)
CAR(registration-number,make,model)

c.
One relational table
DRIVER(licence-number,first-name,last-name,registration-number,make,model)

d.
Two relational tables
DRIVER(licence-number,first-name,last-name)
CAR(registration-number,make,model,licence-number)

* * *

**ChatGPT:**

在一个一对多（one-to-many）关系中，一个实体（在这个例子中是DRIVER）可以与另一个实体（在这个例子中是CAR）的多个实例相关联，但这些实例只能与一个DRIVER实体相关联。在这种情况下，通常会在“多”端的实体（CAR）中添加一个外键来引用“一”端的实体（DRIVER）。

因此，最合适的设计方案会是：

d. 两个关系表 DRIVER(licence-number, first-name, last-name) CAR(registration-number, make, model, licence-number)

在这个设计中，CAR表中的licence-number是一个外键，它引用了DRIVER表中的licence-number，建立了DRIVER和CAR之间的一对多关系。

* * *

**You:**

Question 22
A process of logical design transforms one-to-many association ASSIGNMENT Consists-of TASKS

ASSIGNMENT(task-number)
assignment-number ID
subject-code ID
topic

Consists-of
-&gt;
0..1

TASK
specification
total-marks

into
a.
Two relational tables
ASSIGNMENT(subject-code,assignment-number,topic)
TASK(assignment-number,task-number,specification,total-marks)

b.
Two relational tables
ASSIGNMENT(subject-code,assignment-number,topic)
TASK(subject-code,assignment-number,task-number,specification,total-marks)

c.
A relational table
ASSIGNMENT(subject-code, assignment-number,topic,task-number,specification, total-marks)

d.
Three relational tables
ASSIGNMENT(subject-code,assignment-number,topic)
CONSISTS-OF(subject-code,assignment-number,task-number)
TASK(task-number,specification,total-marks)

* * *

**ChatGPT:**

在逻辑设计过程中，一对多（one-to-many）关系常常通过在“多”的一端（在本例中是TASK）中放置一个外键来实现，该外键引用“一”的一端（在本例中是ASSIGNMENT）的主键。

考虑到这一点，最合适的设计应该是：

a. 两个关系表 ASSIGNMENT(subject-code, assignment-number, topic) TASK(assignment-number, task-number, specification, total-marks)

这里，TASK表中的assignment-number是一个外键，它引用了ASSIGNMENT表中的assignment-number，从而建立了ASSIGNMENT和TASK之间的一对多关系。同时，task-number可以被用作TASK表的主键。

* * *

**You:**

Question 23
A process of logical design transforms many-to-many association DRIVER Uses CAR
DRIVER
licence-number ID
first-name
last-name

Uses
-&gt;
*   *

CAR
registration ID
make
mode l
into

a.
Three relational tables
DRIVER(licence-number,first-name,last-name)
CAR(registration,make,model)
OWNS(registration,licence-number)

b.
Two relational tables
DRIVER(licence-number,first-name,last-name,registration)
CAR(registration,make,model)

c.
Two relational tables
DRIVER(licence-number,first-name,last-name)
CAR(registration,make,model,licence-number)

d.
One relational table DRIVER(licence-number,first-name,last-name,registration,make,model)

* * *

**ChatGPT:**

When transforming a many-to-many association between two entities into relational tables, an associative table (also known as a junction table or linking table) is typically used to break down the many-to-many relationship into two one-to-many relationships. This table usually contains the primary keys of the associated tables as foreign keys.

Given this, the correct choice to represent a many-to-many relationship between `DRIVER` and `CAR` would involve three tables: one for `DRIVER`, one for `CAR`, and an associative table, possibly named `USES` or something similar, to represent the relationship between them.

So, the best choice among the provided options would likely be:

a. Three relational tables DRIVER(licence-number, first-name, last-name) CAR(registration, make, model) OWNS(registration, licence-number)

However, the name of the third table, `OWNS`, does not accurately represent the `Uses` relationship mentioned in the question. A more accurate name might be `USES` or similar. But, among the given options, option a is the most accurate in terms of structure, with the note that the name of the third table should ideally be more representative of the “uses” relationship.

* * *

**You:**

Question 24
A process of logical design transforms many-to-many association with link attribute SUPPLIER
supplier-name ID
fax
phone

Supplies 
-&gt;
*   *

PART
part-name ID
manufacturer

There is also a "price" in the middle of them from the supplies -&gt; branch
into

a.
Three relational tables
SUPPLIER(supplier-name,fax,phone)
PART(part-name,manufacturer)
SUPPLIES(supplier-name,part-name,price)

b.
Two relational tables
SUPPLIER(supplier-name,fax,phone,part-name)
PART(part-name,manufacturer,price)

c.
Two relational tables
SUPPLIER(supplier-name,fax,phone,part-name)
PART(part-name,manufacturer,price,supplier-name)

d.
One relational table SUPPLIER(supplier-name,fax,phone,part-name,manufacturer,price)

* * *

**ChatGPT:**

When you have a many-to-many association with a link attribute, you typically create three tables: one for each entity and one associative table to hold the many-to-many relationship and the associated link attribute.

In this case, the “Supplies” relationship has a link attribute "price". Thus, you would create an associative table, “SUPPLIES”, with foreign keys referencing “SUPPLIER” and “PART”, and an additional attribute for the "price".

So, the correct choice would be:

a. Three relational tables SUPPLIER(supplier-name, fax, phone) PART(part-name, manufacturer) SUPPLIES(supplier-name, part-name, price)

* * *

**You:**

Question25
A process of logical design transforms many-to-many association with association class SUPPLIER Supplies(SHIPMENT) PART
SUPPLIER
supplier-name ID
fax
phone

Supplies 
-&gt;
*   *

PART
part-name ID
manufacturer

Shipment
price
There is a Shipment "price" in the middle of them from the supplies -&gt; branch
into
into


a.
Three relational tables
SUPPLIER(supplier-name,fax,phone)
PART(part-name,manufacturer)
SHIPMENT(supplier-name,part-name,price)


b.
Two relational tables
SUPPLIER(supplier-name,fax,phone,part-name)
PART(part-name,manufacturer,price)


c.
One relational table SUPPLIER(supplier-name,fax,phone,part-name,manufacturer,price)


d.
Two relational tables
SUPPLIER(supplier-name,fax,phone,part-name)
PART(part-name,manufacturer,price,supplier-name)

* * *

**ChatGPT:**

When dealing with a many-to-many association that has an association class, you would usually create three tables. One for each entity class and a third table to represent the association class. The association class table would typically have foreign keys to the entity class tables and fields for the attributes of the association class.

In this case, “SUPPLIER” and “PART” are the entity classes and “SHIPMENT” is the association class with an attribute "price". So, the “SHIPMENT” table would have foreign keys to both “SUPPLIER” and “PART” tables and a field for "price".

So, the correct choice would be:

a. Three relational tables SUPPLIER(supplier-name,fax,phone) PART(part-name,manufacturer) SHIPMENT(supplier-name,part-name,price)

* * *

**You:**

Question 26
When a superset method is used, a process of logical design transforms generalization CAR,TRUCK ISA VEHICLE
VEHICLE
registration ID
make
model

CAR
total-seats

TRUCK
capacity
into

a.
Three relational tables
VEHICLE(registration,make,model)
CAR(registration,total-seats)
TRUCK(registration,capacity)

b.
Two relational tables
CAR(registration,make,model,total-seats)
TRUCK(registration,make,model,capacity)

c.
Three relational tables
VEHICLE(registration)
CAR(registration,make,model,total-seats)
TRUCK(registration,make,model,capacity)

d.
One relational table
VEHICLE(registration,make,model,total-seats,capacity,vehicle-type)

* * *

**ChatGPT:**

When a superset method is used in database design for representing a generalization hierarchy, a single table (superset) is created to include all the attributes of the generalization hierarchy including the attributes of the superclass and all its subclasses. Also, an additional attribute (often called a ‘type’ attribute) is usually included to indicate to which subclass each row belongs.

So, in this case, the correct representation would be:

d. One relational table VEHICLE(registration,make,model,total-seats,capacity,vehicle-type)

* * *

**You:**

Question 27
When a subset method is used, a process of logical design transforms generalization CAR,TRUCK ISA VEHICLE
VEHICLE
registration ID
make
model

CAR
total-seats

TRUCK
capacity
into

a.
Three relational tables
VEHICLE(registration,make,model)
CAR(registration,total-seats)
TRUCK(registration,capacity)

b.
Three relational tables
VEHICLE(registration,make,model)
CAR(registration,make,model,total-seats)
TRUCK(registration,make,model,capacity)

c.
One relational table
VEHICLE(registration,make,model,total-seats,capacity,vehicle-type)

d.
Two relational tables
CAR(registration,make,model,total-seats)
TRUCK(registration,make,model,capacity)

* * *

**ChatGPT:**

When using the subset method for handling generalizations in the relational database design, separate tables are created for the superclass and each of its subclasses. The tables for subclasses will include the primary key attribute(s) of the superclass as a foreign key, which also serves as the primary key for the subclass tables. The attributes that are common to all the entities in the hierarchy will be placed in the superclass table, and the attributes that are specific to the entities of the subclass will be placed in the respective subclass tables.

So, in this case, the correct answer is:

a. Three relational tables VEHICLE(registration,make,model) CAR(registration,total-seats) TRUCK(registration,capacity)

* * *

**You:**

Question 28
When an association method is used, a process of logical design transforms generalization CAR,TRUCK ISA VEHICLE
quiz3-28
into

a.
One relational table
VEHICLE(registration,make,model,total-seats,capacity,vehicle-type)

b.
Three relational tables
VEHICLE(registration,make,model)
CAR(registration,total-seats)
TRUCK(registration,capacity)

c.
Two relational tables
CAR(registration,make,model,total-seats)
TRUCK(registration,make,model,capacity)

d.
Three relational tables
VEHICLE(registration)
CAR(registration,make,model,total-seats)
TRUCK(registration,make,model,capacity)



* * *

**ChatGPT:**

When an association (or “class table inheritance”) method is used, a separate table is created for the general class (superclass) and for each subclass, and the subclass tables will hold both the attributes of the superclass and their unique attributes. The primary key of the superclass is also the primary key of the subclass tables.

Considering this, the most accurate answer would be:

d.  
Three relational tables  
VEHICLE(registration)  
CAR(registration,make,model,total-seats)  
TRUCK(registration,make,model,capacity)

* * *

**You:**

Question 29
Consider the following relational tables

PATIENT(insurance-number,first-name, last-name,date-of-birth)
TREATMENT(insurance-number,treatment-date,hospital-name)

Then

a.
An attribute insurance-number is a primary key in a relational table PATIENT and a pair of attributes (insurance-number,treatment-date) is a foreign key in a relational table TREATMENT and a pair of attributes (insurance-number,treatment-date) is a primary key in a relational table TREATMENT

b.
An attribute insurance-number is a primary key in a relational table PATIENT and an attribute insurance-number is a foreign key in a relational table PATIENT and a pair of attributes (insurance-number,treatment-date) is a primary key in a relational table TREATMENT

c.
An attribute insurance-number is a primary key in a relational table PATIENT and an attribute insurance-number is a foreign key in a relational table TREATMENT and a pair of attributes (insurance-number,treatment-date) is a primary key in a relational table TREATMENT

d.
An attribute insurance-number is a foreign key in a relational table PATIENT and an attribute insurance-number is a primary key in a relational table TREATMENT and a pair of attributes (insurance-number,treatment-date) is a foreign key in a relational table TREATMENT

* * *

**ChatGPT:**

In the given scenario:

* `insurance-number` is the primary key in the `PATIENT` table because it uniquely identifies each row in this table.
* `insurance-number` in the `TREATMENT` table is a foreign key referring to the `PATIENT` table, ensuring referential integrity between the two tables.
* A combination of `(insurance-number, treatment-date)` in the `TREATMENT` table is likely the primary key because it uniquely identifies each treatment record.

So, the correct answer would be:

c. An attribute insurance-number is a primary key in a relational table PATIENT and an attribute insurance-number is a foreign key in a relational table TREATMENT and a pair of attributes (insurance-number,treatment-date) is a primary key in a relational table TREATMENT

* * *

**You:**

Question 30
Consider the following relational tables

PATIENT(insurance-number,first-name, last-name,date-of-birth)
VISITS(insurance-number,visit-date,hospital-name)
HOSPITAL(hospital-name,address,total-staff-number)

Then

a.
An attribute insurance-number is a primary key in a relational table PATIENT, and an attribute hospital-name is a primary key in a relational table HOSPITAL, and a triple of attributes (insurance-number,hospital-name,visit-date) is a foreign key in a relational table VISIT. An attribute insurance number is a primary key in a relational table VISIT. An attribute hospital-name is a candidate key in a relational table VISIT

b.
An attribute insurance-number is a primary key in a relational table PATIENT, and an attribute hospital-name is a primary key in a relational table HOSPITAL, and a pair of attributes (insurance-number,hospital-name) is a primary key in a relational table VISIT. An attribute insurance number is a foreign key in a relational table VISIT. An attribute hospital-name is a foreign key in a relational table VISIT

c.
An attribute insurance-number is a primary key in a relational table PATIENT, and an attribute hospital-name is a primary key in a relational table HOSPITAL, and an attribute insurance-number is a primary key in a relational table VISIT, and an attribute hospital-name is a candidate key in a relational table VISIT. An attribute insurance number is a foreign key in a relational table VISIT. An attribute hospital-name is a foreign key in a relational table VISIT

d.
An attribute insurance-number is a primary key in a relational table PATIENT, and an attribute hospital-name is a primary key in a relational table HOSPITAL, and a triple of attributes (insurance-number,hospital-name,visit-date) is a primary key in a relational table VISIT. An attribute insurance number is a foreign key in a relational table VISIT. An attribute hospital-name is a foreign key in a relational table VISIT



* * *

**ChatGPT:**

In the given scenario:

* `insurance-number` is the primary key in the `PATIENT` table.
* `hospital-name` is the primary key in the `HOSPITAL` table.
* A combination of `(insurance-number, hospital-name, visit-date)` would be the primary key in the `VISITS` table because a patient can visit the same hospital multiple times on different dates.
* `insurance-number` in the `VISITS` table is a foreign key referring to the `PATIENT` table.
* `hospital-name` in the `VISITS` table is a foreign key referring to the `HOSPITAL` table.

So, the correct answer would be:

d. An attribute insurance-number is a primary key in a relational table PATIENT, and an attribute hospital-name is a primary key in a relational table HOSPITAL, and a triple of attributes (insurance-number,hospital-name,visit-date) is a primary key in a relational table VISIT. An attribute insurance number is a foreign key in a relational table VISIT. An attribute hospital-name is a foreign key in a relational table VISIT