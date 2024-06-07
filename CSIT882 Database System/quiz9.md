---
title: "数据库事务是什么？"
source: "https://chat.openai.com/c/19441c69-3276-489e-94dd-d9753b017662"
---

**You:**

这个对话用来你帮助我的数据库作业Quiz9，我会给你题目，然后你直接给我正确答案英文选项和中文解析讲解，明白？以下开始第一题：
Question 01
A database transaction is
a.
A sequence of read and/or write operations on data items.
b.
A database application, that transfers money between bank account.
c.
A partially ordered set of read and/or write operations on data items.
d.
A collection of documents describing a process of database design.

* * *

**ChatGPT:**

明白了。这是关于数据库事务的问题。

正确答案是: a. A sequence of read and/or write operations on data items.

中文解析: 数据库事务指的是对数据项的一系列读取和/或写入操作。它通常包括多个步骤，这些步骤要么全部成功，要么全部失败，确保数据的一致性和完整性。这是数据库管理中的一个基本概念，确保事务是原子性的、一致性的、隔离的和持久的，通常被简称为ACID属性。

* * *

**You:**

Question 02
A database transaction controlled by timestamp ordering must not access a data item, that has
a.
 A higher timestamp than the transaction's timestamp.
b.
A lower timestamp than the transaction's timestamp.
c.
More than one timestamp.
d.
A timestamp exactly the same at the transaction's timestamp.

* * *

**ChatGPT:**

正确答案是: b. A lower timestamp than the transaction's timestamp.

中文解析: 在基于时间戳排序的数据库事务控制中，事务不得访问时间戳低于其自身时间戳的数据项。时间戳机制用于维持事务的串行化顺序，确保数据的一致性。如果事务尝试访问时间戳更早的数据项，这可能导致不一致性和冲突，因此这种访问是不被允许的。简单来说，时间戳排序要求事务只能按照时间戳的顺序访问数据，从而防止了潜在的并发冲突。

* * *

**You:**

Question 03
A phantom phenomenon happens when
a.
A phantom transaction is created when a user brakes a database connection.
b.
A transaction is aborted by a scheduler and its phantom still exists in the system.
c.
A transaction counts the total number or rows at least two times and at least two times it gets different results.
d.
A transaction is created by another transaction.

* * *

**ChatGPT:**

正确答案是: c. A transaction counts the total number or rows at least two times and at least two times it gets different results.

中文解析: 所谓“幻读”现象，是指在数据库事务处理中，一个事务多次读取同一范围的记录时，由于其他事务的插入或删除操作，导致每次读取的结果不一致，即总行数发生变化。这通常发生在并发事务环境中，一个事务在读取数据时，另一个事务正在对同一数据集进行修改（如插入或删除），从而影响了第一个事务的读取结果。幻读是并发控制中需要解决的问题之一，通常需要通过锁机制等手段来防止或控制。

* * *

**You:**

Question 04
A dirty read phenomenon happens when
a.
A transaction reads a data item earlier created by a phantom transaction.
b.
A transaction reads a data item earlier written by an aborted transaction.
c.
A transaction reads a data item earlier read by an aborted transaction.
d.
A transaction reads a data item earlier written by an uncommitted transaction.

* * *

**ChatGPT:**

正确答案是: d. A transaction reads a data item earlier written by an uncommitted transaction.

中文解析: “脏读”现象指的是一个事务读取了另一个尚未提交的事务所写入的数据。在这种情况下，如果写入数据的事务最终失败或回滚，那么读取这些数据的事务就会得到错误或不一致的数据。脏读主要发生在数据库的并发控制中，特别是在没有足够严格的隔离级别时。为了避免脏读，数据库系统通常通过实施适当的事务隔离级别来控制并发访问，确保数据的一致性和完整性。

* * *

**You:**

Question 05
A non-repeatable read happens when a transaction
a.
Is aborted because it tries to read the same data item twice.
b.
Is not allowed to repeat a read operation on the same data item twice.
c.
Reads a data item at least two times and at least two times gets a different result.
d.
Reads a data item at least two times and at least one time a read operation fails.

* * *

**ChatGPT:**

正确答案是: c. Reads a data item at least two times and at least two times gets a different result.

中文解析: “不可重复读”是指在数据库事务中，一个事务对同一数据项进行了至少两次读取，且至少两次得到了不同的结果。这通常是因为另一个并发事务在两次读取之间修改了这些数据项（例如，更新操作）。不可重复读的问题通常与数据库的事务隔离级别有关，不同的隔离级别提供了不同程度的保护以防止此类问题。提高事务的隔离级别可以减少这种现象的发生，但可能会降低系统的并发性能。

* * *

**You:**

Question 06
A transaction, that is assigned to the read committed isolation level can experience
a.
Phantom phenomenon.
b.
None of the phenomena.
c.
Non-serializable write phenomenon.
d.
Dirty read phenomenon.

* * *

**ChatGPT:**

正确答案是: a. Phantom phenomenon.

中文解析: 在“读已提交”（Read Committed）隔离级别下的事务可以经历“幻读”现象。在这种隔离级别下，一个事务只能读取到已经被其他事务提交的数据，这可以避免脏读现象。然而，它并不能防止在事务执行过程中由于其他事务的插入或删除操作导致的数据集变化，即幻读现象。因此，即使在读已提交的隔离级别下，事务仍可能遇到数据集中新添加或删除的行，这就是幻读。提高隔离级别到“可重复读”（Repeatable Read）或更高可以帮助防止幻读现象。

* * *

**You:**

Question 07
If all transactions are assigned to the serializable isolation level then
a.
None of the phenomena may happen.
b.
Phantom phenomenon and non-repeatable read and dirty read may happen.
c.
Phantom phenomenon and non-repeatable read may happen.
d.
Phantom phenomenon may happen.

* * *

**ChatGPT:**

正确答案是: a. None of the phenomena may happen.

中文解析: 如果所有事务都被分配到“可串行化”（Serializable）隔离级别，那么不会出现幻读、不可重复读和脏读现象。可串行化是最高的事务隔离级别，它通过严格的锁机制保证了事务执行的结果就像是依次顺序执行一样，从而避免了并发事务可能引起的各种不一致现象。在这个级别下，数据库系统会防止多个事务同时操作同一数据集，从而确保了数据的完整性和一致性。然而，这种高级别的隔离也会带来性能上的损失，因为它限制了事务的并发执行能力。

* * *

**You:**

Question 08
Atomicity principle demands, that
a.
A database transaction is indivisible, and it must be processed entirely or not.
b.
A database transaction consist of atomic operations on data items.
c.
A database transaction operates only on atomic data items.
d.
A database transaction can be processed only by an atomic hardware.

* * *

**ChatGPT:**

正确答案是: a. A database transaction is indivisible, and it must be processed entirely or not.

中文解析: 原子性原则要求数据库事务是不可分割的，必须要么完全处理，要么完全不处理。这意味着在一个事务中的所有操作都必须成功执行，以保证数据的完整性和一致性。如果事务中的任何一个操作失败，整个事务都会回滚到最初状态，就好像这个事务从未发生过一样。原子性是数据库ACID特性中的“A”，它是确保数据库可靠性的关键要素之一。简单来说，原子性确保了事务中的所有操作要么全部成功，要么全部失败，没有中间状态。

* * *

**You:**

Question 09
Isolation principle demands, that
a.
Each transaction must be processed independently.
b.
Processing of data manipulation operations must be isolated from processing of search operations.
c.
A transaction is allowed to operate on only one relational table at a time.
d.
Database applications are not allowed to communicate.

* * *

**ChatGPT:**

正确答案是: a. Each transaction must be processed independently.

中文解析: 隔离性原则要求每个事务都必须独立处理。这意味着一个事务的操作和数据不应该被其他事务干扰，直到它完成。隔离性是数据库ACID特性中的“I”，它的目的是为了防止事务之间发生干扰，特别是在并发环境下。通过保持事务的隔离性，可以防止多种并发问题，如脏读、不可重复读和幻读。不同的隔离级别提供了不同程度的隔离保护，但隔离级别越高，可能对系统性能的影响也越大。简单来说，隔离性确保每个事务在不受其他事务影响的情况下独立执行。

* * *

**You:**

Question 10
Durability principle demands, that
a.
All modifications of transactions must permanently recorded in a data dictionary.
b.
All modifications of data performed by the committed transactions must be permanently recorded in a database
c.
All transactions must permanently write their logs.
d.
All transactions must be permanently recorded in the logs.

* * *

**ChatGPT:**

正确答案是: b. All modifications of data performed by the committed transactions must be permanently recorded in a database.

中文解析: 持久性原则要求，所有由提交的事务执行的数据修改必须永久记录在数据库中。这意味着一旦事务提交，其所做的所有更改都必须永久保存，即使系统发生故障，这些更改也不会丢失。持久性是数据库ACID特性中的“D”，它确保了事务对数据库的影响是持久的，提供了数据可靠性的保证。数据库通过将更改写入持久存储（如硬盘）来实现持久性，确保即使在系统崩溃或其他故障后，这些更改也能保持不变。简单来说，持久性确保提交的事务所做的更改在系统任何故障之后都是可恢复的。

* * *

**You:**

Question 11
View serializability correctness criterion requires a nonserial schedule of database transactions to
a.
Produce the same results as other nonserial schedule.
b.
Produce the correct contents of the views of relational table.
c.
Produce different results from all serial schedules.
d.
Produce the same results as certain serial schedule.

* * *

**ChatGPT:**

正确答案是: d. Produce the same results as certain serial schedule.

中文解析: 视图可串行性正确性标准要求非串行的事务调度与某个特定的串行调度产生相同的结果。这意味着即使事务是以并发方式执行的，它们的最终结果应该与这些事务如果按顺序执行时的结果一致。视图可串行性是衡量并发事务调度正确性的一种方式，确保了即使在并发环境中，数据库的最终状态仍然保持一致和正确。这个标准比单纯的冲突可串行性提供了更宽松的并发控制，允许更多的并发事务执行，同时仍保证数据的一致性。简单来说，视图可串行性确保并发执行的事务最终产生的效果，与它们按照某种特定顺序串行执行时的效果相同。

* * *

**You:**

Question 12
Two database operations conflict they act on the same data items and
a.
None of them is write operation.
b.
Both of them is read operation.
c.
One of them is read operations.
d.
At least one of them is write operation.

* * *

**ChatGPT:**

正确答案是: d. At least one of them is write operation.

中文解析: 如果两个数据库操作作用于同一数据项，并且至少有一个操作是写操作，则这两个操作存在冲突。这种情况通常指的是，至少有一个操作是对数据项进行修改（写操作），而另一个操作可能是读取或写入。如果两个操作都是读操作，则它们之间不会产生冲突，因为读操作不会改变数据项的状态。但是，如果至少有一个操作是写操作，就可能导致数据不一致的问题，特别是在并发事务环境中。这就是为什么在数据库的并发控制机制中，需要特别注意写操作和与之相关的潜在冲突。简单来说，只要涉及到写操作，就可能存在操作之间的冲突。

* * *

**You:**

Question 13
A nonserial schedule of database transactions is conflict serializable when
a.
An order of conflicting operations is the same as in one of the serial schedules.
b.
An order of conflicting operations is the same as in any other nonserial schedule of the same database transactions
c.
An order of conflicting operations is different from all serial schedules.
d.
An order of conflicting operations is the same as in all serial schedules.

* * *

**ChatGPT:**

正确答案是: a. An order of conflicting operations is the same as in one of the serial schedules.

中文解析: 当非串行的数据库事务调度中冲突操作的顺序与某个串行调度中的顺序相同时，该调度就是冲突可串行化的。冲突可串行化是一种确保并发执行的事务调度在最终结果上与按照某种特定顺序串行执行的事务相同的方式。这意味着即使事务是并发执行的，只要它们之间冲突的操作遵循与某个串行调度相同的顺序，最终的数据库状态就会与串行执行这些事务时的状态一致。冲突可串行化是并发事务调度正确性的一个重要标准，它允许一定程度的并发执行，同时保持数据的一致性和完整性。简单来说，冲突可串行化的调度在处理冲突操作时，其执行顺序与至少一个串行调度的执行顺序相同。

* * *

**You:**

Question 14
Serialization graph testing protocol testing protocol detects not conflict serializable schedules when
a.
A serialization graph contains a cycle.
b.
A serialization graph does not contain a cycle.
c.
A serialization graph does not contain more edges than nodes.
d.
A serialization graph contains at least one edge between any two nodes.

* * *

**ChatGPT:**

正确答案是: a. A serialization graph contains a cycle.

中文解析: 序列化图测试协议用于检测非冲突可串行化的调度，当序列化图中包含循环时，它就会检测到不可串行化的调度。序列化图是一种图形表示方法，用于表示事务之间的依赖和冲突关系。在这个图中，节点代表事务，边代表事务之间的冲突操作顺序。如果这个图中存在循环，这意味着存在一组事务，它们之间相互依赖，不能找到一个符合冲突可串行化的执行顺序。这种情况下，事务调度就不是冲突可串行化的。简单来说，如果序列化图中存在循环，这表明并发执行的事务无法被重排为一个没有冲突的串行执行顺序。

* * *

**You:**

Question 15
A database transaction controlled by the two-phase locking protocol must
a.
Release all locks at its commit point.
b.
Acquire all lock at its start point.
c.
Release all locks before acquiring any lock.
d.
Acquire all locks before releasing any lock.

* * *

**ChatGPT:**

正确答案是: d. Acquire all locks before releasing any lock.

中文解析: 在两阶段锁定协议控制下的数据库事务必须在释放任何锁之前获取所有锁。两阶段锁定协议是数据库并发控制中常用的一种协议，它包含两个阶段：锁定阶段和解锁阶段。在锁定阶段，事务可以获取所需的任何锁，但一旦开始释放锁，它就不能再获取新的锁。这种方法的目的是确保事务的一致性和隔离性，避免出现诸如脏读、不可重复读等并发问题。简单来说，两阶段锁定协议要求事务在开始释放锁之前，必须先获取它需要的所有锁。