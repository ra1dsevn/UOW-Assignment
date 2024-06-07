---
title: "1NF in Relational Tables"
source: "https://chat.openai.com/c/bcba43ca-3b47-43b8-ab96-a9369c02c5cb"
---

**You:**

CSIT882 (JI123) Data Management Systems Assignment Assistance: Question 01
A relational table is in 1NF when


a.
All occurrences of rows have only one value.


b.
All occurrences of rows contain nested values only.


c.
All occurrences of rows contain the same values.


d.
All occurrences of rows contain the same number of values and include the atomic values only.

* * *

**ChatGPT:**

The correct answer for the given options is:

d. All occurrences of rows contain the same number of values and include the atomic values only.

Explanation: A relational table is in First Normal Form (1NF) when it satisfies the following conditions:

1. There are no duplicate rows.
2. Each column contains only atomic (indivisible) values.
3. All entries in a column are of the same kind or type.
4. The order in which data is stored doesn't matter.

Option d best captures the essence of 1NF, emphasizing that each row must have the same number of values (ensuring that there's a value for every attribute/column in the table for every row) and that these values must be atomic.

* * *

**You:**

Question 02
Let R be a relational schema (A, B, C). If A → B and B → C then


a.
C is a minimal key.


b.
C is transitively dependent on A.


c.
A is transitively dependent on C.


d.
B is a minimal key.

* * *

**ChatGPT:**

Given the functional dependencies A→BA \rightarrow BA→B and B→CB \rightarrow CB→C:

Transitive dependency in relation to normalization, especially in the context of 3NF (Third Normal Form), refers to a situation where X→YX \rightarrow YX→Y in a schema, but Y is not a prime attribute (i.e., not part of any candidate key) and X is not a super key.

Given the dependencies:

1. A→BA \rightarrow BA→B
2. B→CB \rightarrow CB→C

From the above, we can derive A→CA \rightarrow CA→C through transitive property.

Considering the provided options:

a. C is a minimal key. - This is not necessarily true based on the provided dependencies.

b. C is transitively dependent on A. - This is true because we have A→BA \rightarrow BA→B and B→CB \rightarrow CB→C, implying A→CA \rightarrow CA→C. Here, if A is not a super key and C is not a prime attribute, then C would be transitively dependent on A.

c. A is transitively dependent on C. - This is incorrect. The direction of the dependency matters, and there's no information given that would suggest C→AC \rightarrow AC→A.

d. B is a minimal key. - This is not necessarily true based only on the provided dependencies.

So, the correct answer is:

b. C is transitively dependent on A.

* * *

**You:**

Question 03
Let R be a relational schema (A, B) and let A → B. The highest normal form valid for R is


a.
1NF


b.
3NF


c.
2NF


d.
BCNF

* * *

**ChatGPT:**

Given a relational schema R(A,B)R(A, B)R(A,B) and the functional dependency A→BA \rightarrow BA→B:

The key for relation RRR would be AAA because AAA determines BBB.

Now, let's check the given relation against various normal forms:

1. 1NF: A relation is in 1NF if it only has atomic values, and there are no repeating groups or arrays. The given information does not violate 1NF.
    
2. 2NF: A relation is in 2NF if it is in 1NF and there are no partial dependencies of any column on the primary key. Since RRR has only two attributes and AAA determines BBB, there are no partial dependencies. So, the relation is in 2NF.
    
3. 3NF: A relation is in 3NF if it is in 2NF and there are no transitive dependencies of non-prime attributes on the primary key. Given the dependency A→BA \rightarrow BA→B and considering AAA as the primary key, there's no transitive dependency. So, the relation is in 3NF.
    
4. BCNF: A relation is in BCNF if for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX is a superkey. In our case, for the dependency A→BA \rightarrow BA→B, AAA is a superkey (in fact, it's the primary key). Thus, the relation is in BCNF.
    

So, the highest normal form valid for RRR is:

d. BCNF.

* * *

**You:**

Question 04
Let R be a relational schema (A, B, C). If A → B and B → C. Then the highest normal form valid for R  is


a.
1NF


b.
2NF


c.
3NF


d.
BCNF

* * *

**ChatGPT:**

Given a relational schema R(A,B,C)R(A, B, C)R(A,B,C) with functional dependencies A→BA \rightarrow BA→B and B→CB \rightarrow CB→C:

For the highest normal form for RRR, let's evaluate:

1. 1NF: The schema would generally be in 1NF if all attributes have atomic values. The provided functional dependencies do not violate 1NF.
    
2. 2NF: A relation is in 2NF if it's in 1NF and no non-prime attribute is partially dependent on the primary key. The given dependencies don't indicate any partial dependency, so RRR is in 2NF.
    
3. 3NF: A relation is in 3NF if it's in 2NF and there is no transitive dependency for non-prime attributes. In our given functional dependencies, we can see that A→BA \rightarrow BA→B and B→CB \rightarrow CB→C, leading to a transitive dependency A→CA \rightarrow CA→C. If AAA is a candidate key (or primary key), then CCC is transitively dependent on AAA through BBB. This would violate 3NF.
    
4. BCNF: A relation is in BCNF if for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX is a superkey. Given the dependencies, if BBB isn't a superkey, then B→CB \rightarrow CB→C violates BCNF.
    

So, considering the provided functional dependencies, the highest normal form valid for RRR is:

b. 2NF.

* * *

**You:**

Question 05
A relational schema R is in BCNF if whenever functional dependency X → A holds in R then


a.
X is a superkey in R.


b.
X is a superkey in R and A is a prime attribute.


c.
X is a minimal key in R.


d.
X is a superkey in R or A is a prime attribute.

* * *

**ChatGPT:**

For a relational schema RRR to be in Boyce-Codd Normal Form (BCNF), the following condition must be satisfied:

For every non-trivial functional dependency X→AX \rightarrow AX→A in RRR:

* XXX is a superkey in RRR.

From the given options, the correct statement is:

a. X is a superkey in R.

* * *

**You:**

Question 06
Let R be a relational schema (A, B, C). If A → BC. Then the highest normal form valid for R is


a.
BCNF


b.
3NF

c.
2NF


d.
1NF

* * *

**ChatGPT:**

Given a relational schema R(A,B,C)R(A, B, C)R(A,B,C) with the functional dependency A→BCA \rightarrow BCA→BC:

The key for relation RRR would be AAA because AAA determines both BBB and CCC.

Let's evaluate the normal forms:

1. 1NF: The schema is in 1NF if it only has atomic values, and there are no repeating groups or arrays. The given information does not suggest any violation of 1NF.
    
2. 2NF: A relation is in 2NF if it is in 1NF and there are no partial dependencies of any column on the primary key. Since RRR has AAA determining both BBB and CCC, there are no partial dependencies. Thus, RRR is in 2NF.
    
3. 3NF: A relation is in 3NF if it is in 2NF and there are no transitive dependencies of non-prime attributes on the primary key. Given the dependency A→BCA \rightarrow BCA→BC and considering AAA as the primary key, there's no transitive dependency. So, RRR is in 3NF.
    
4. BCNF: A relation is in BCNF if, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX is a superkey. In our case, for the dependency A→BCA \rightarrow BCA→BC, AAA is a superkey (in fact, it's the primary key). Thus, the relation is in BCNF.
    

Therefore, the highest normal form valid for RRR is:

a. BCNF.

* * *

**You:**

Question 07
Let R be a relational schema (A, B, C) and no nontrivial functional dependencies are valid in R. Then the highest normal form valid for R is


a.
BCNF


b.
2NF


c.
3NF


d.
1NF

* * *

**ChatGPT:**

Given a relational schema R(A,B,C)R(A, B, C)R(A,B,C) with no nontrivial functional dependencies:

If there are no nontrivial functional dependencies, then there are no dependencies to violate the rules of any normal forms.

Let's evaluate the normal forms:

1. 1NF: As long as all attributes in the relation have atomic values, the relation is in 1NF.
    
2. 2NF: Since there are no nontrivial functional dependencies, there can't be any partial dependencies that violate 2NF. Therefore, the relation is in 2NF.
    
3. 3NF: With no nontrivial functional dependencies, there can't be any transitive dependencies of non-prime attributes on the primary key. So, the relation is in 3NF.
    
4. BCNF: The main criterion for BCNF is that for any non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Since there are no nontrivial functional dependencies, the relation is automatically in BCNF.
    

Hence, the highest normal form valid for RRR is:

a. BCNF.

* * *

**You:**

Question 08
Minimal key is a superkey K with an additional property such that


a.
The total number of attributes is equal to one.


b.
Removal of any attribute from K will cause K not to be a superkey.


c.
The total number of attributes is equal to the total number of attributes in a relational schema


d.
Addition of any attribute to K will cause K to be a superkey.

* * *

**ChatGPT:**

A minimal key, also known as a candidate key, is a superkey with the property that no proper subset of it is a superkey. In other words, if you remove any attribute from the minimal key, it will no longer be a superkey.

Therefore, the correct option is:

b. Removal of any attribute from K will cause K not to be a superkey.

* * *

**You:**

Question 09
Prime attribute is an attribute from relational schema R which is

a.
The first attribute in a schema R.

b.
A member of at least one foreign key.

c.
A member of at least one candidate key in R

d.
The last attribute in a schema R.

* * *

**ChatGPT:**

A prime attribute is an attribute that is a part of any candidate key of the relation.

Therefore, the correct option is:

c. A member of at least one candidate key in R.

* * *

**You:**

Question 10
If a set of attributes X is superkey in a relational schema R then


a.
X is functionally determined by all attributes in R.

b.
X includes only superattributes in R.


c.
X functionally determines all attributes in R.


d.
X is not empty.

* * *

**ChatGPT:**

If a set of attributes XXX is a superkey in a relational schema RRR, it means that XXX can uniquely identify any tuple (or row) in RRR. Thus, XXX must functionally determine all other attributes in RRR.

The correct option is:

c. X functionally determines all attributes in R.

* * *

**You:**

Question 11
Relational schema R is in 2NF


a.
If every nonprime attribute A in R is fully functionally dependent on a primary key of schema R.


b.
If every prime attribute A in R is fully functionally dependent on primary key of schema R.


c.
If every nonprime attribute A in R is not fully functionally dependent on a primary key of schema R.


d.
If every prime attribute A in R is not fully functionally dependent on a primary key of schema R.

* * *

**ChatGPT:**

A relational schema RRR is in Second Normal Form (2NF) if:

1. It is in 1NF.
2. There is no partial dependency of any column on the primary key.

Partial dependency means that a non-prime attribute is dependent on a part (or subset) of the primary key, rather than the entire primary key.

Given the above, the correct option is:

a. If every nonprime attribute A in R is fully functionally dependent on a primary key of schema R.

* * *

**You:**

Question 12
Let R be a relational schema (A, B, C). If A → B and B → C then a minimal key is


a.
C


b.
ABC


c.
A


d.
B

* * *

**ChatGPT:**

Given the functional dependencies A→BA \rightarrow BA→B and B→CB \rightarrow CB→C:

1. A→BA \rightarrow BA→B: This means attribute A can determine B.
2. B→CB \rightarrow CB→C: This means attribute B can determine C.

Using the transitive property, AAA can determine CCC as well. Thus, AAA can determine both BBB and CCC.

A minimal key (or candidate key) is the smallest set of attributes that can uniquely determine all other attributes in the relation.

Given the dependencies, attribute AAA can determine all other attributes in the relation, so AAA is the minimal key.

The correct answer is:

c. A.

* * *

**You:**

Question 13
If all minimal keys in a relational schema consist of only one attribute then such schema is always in


a.
3NF


b.
2NF


c.
4NF

d.
BCNF

* * *

**ChatGPT:**

If all minimal keys (candidate keys) in a relational schema consist of only one attribute, then there cannot be any partial dependencies. Partial dependency occurs when a non-prime attribute is dependent on part of a composite primary key. Since the candidate keys are single attributes, there are no composite keys, and thus no partial dependencies.

1. The schema is definitely in 2NF because there are no partial dependencies.
    
2. 3NF requires no transitive dependencies of non-prime attributes on the primary key. Since any transitive dependency would involve a relation between multiple attributes, and we've established that all candidate keys are single attributes, any functional dependency in the schema is driven by a single attribute. Therefore, the schema is also in 3NF.
    
3. BCNF requires that for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX is a superkey. Given that every minimal key is a single attribute, any functional dependency with a single attribute on the left-hand side would satisfy the BCNF condition.
    
4. 4NF is about multivalued dependencies, and a schema being in 3NF or BCNF does not necessarily guarantee it's in 4NF.
    

Given the provided options and the above reasoning, the highest normal form that is always guaranteed is:

d. BCNF.

* * *

**You:**

Question 14
Let R be a relational schema (A, B, C). If A → B and A → C then a minimal key is


a.
CB


b.
BC


c.
ABC


d.
A

* * *

**ChatGPT:**

Given the functional dependencies A→BA \rightarrow BA→B and A→CA \rightarrow CA→C:

1. A→BA \rightarrow BA→B: This means attribute A can determine B.
2. A→CA \rightarrow CA→C: This means attribute A can determine C.

Given these dependencies, attribute AAA can determine both BBB and CCC.

A minimal key (or candidate key) is the smallest set of attributes that can uniquely determine all other attributes in the relation.

Given the dependencies, attribute AAA can determine all other attributes in the relation, so AAA is the minimal key.

The correct answer is:

d. A.

* * *

**You:**

Question 15
Relational schema R is in 3NF if it is in 2NF and


a.
All attributes in a schema are transitively dependent on the primary key.


b.
No nonprime attribute of R is transitively dependent on the primary key.


c.
At least one attribute is transitively dependent on the primary key.


d.
One of nonprime attributes functionally depends on a subject of the primary key.

* * *

**ChatGPT:**

For a relational schema RRR to be in Third Normal Form (3NF):

1. It must be in 2NF.
2. No non-prime attribute is transitively dependent on the primary key.

Given the options, the statement that accurately describes 3NF is:

b. No nonprime attribute of R is transitively dependent on the primary key.

* * *

**You:**

Question 16
Let R be a relational schema (A, B, C). If A → B then a minimal key is


a.
AB


b.
AC


c.
B


d.
A

* * *

**ChatGPT:**

Given the functional dependency A→BA \rightarrow BA→B:

This means attribute A can determine B.

A minimal key (or candidate key) is the smallest set of attributes that can uniquely determine all other attributes in the relation.

Given the dependency, attribute AAA can determine BBB, so AAA alone is sufficient to be a minimal key.

The correct answer is:

d. A.

* * *

**You:**

Question 17
Let R be a relational schema (A, B, C). If no nontrivial functional dependencies are valid in the schema then a minimal key is


a.
ABC


b.
BC


c.
AC


d.
AB

* * *

**ChatGPT:**

If there are no nontrivial functional dependencies in the schema R(A,B,C)R(A, B, C)R(A,B,C), it means that no attribute or combination of attributes can determine any other attribute in the schema.

To uniquely identify a tuple (or row) in the relation, we would need all the attributes. Therefore, the minimal key (or candidate key) would be the combination of all the attributes.

The correct answer is:

a. ABC.

* * *

**You:**

Question 18
Full functional dependency is a functional dependency X → Y such that


a.
Addition of any attribute A to X causes that XA → Y is not valid in R


b.
Removal of any attribute A from X causes that (X-A) → Y is not valid in R


c.
Addition of any attribute A to X causes that XA → Y is still valid in R


d.
Removal of any attribute A from X causes that (X-A) → Y is still valid in R

* * *

**ChatGPT:**

A full functional dependency is a type of functional dependency where the dependency still holds true if and only if removing any attribute from the left-hand side (the determinant) would make the dependency no longer hold true.

Given the options, the statement that accurately describes a full functional dependency is:

b. Removal of any attribute A from X causes that (X-A) → Y is not valid in R.

* * *

**You:**

Question 19
A functional dependency A → BC is valid in a relational schema R(A, B, C). A minimal key is (A). The highest normal form valid for the relational schema is


a.
3NF


b.
1NF


c.
2NF


d.
BCNF

* * *

**ChatGPT:**

Given: Functional dependency A→BCA \rightarrow BCA→BC and minimal key is AAA.

Let's evaluate the normal forms:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: Since AAA is the minimal key and it's not a composite key, there are no partial dependencies (because partial dependencies only arise from composite keys). So, RRR is in 2NF.
    
3. **3NF**: For a schema to be in 3NF, no non-prime attribute should be transitively dependent on the primary key. Given the functional dependency A→BCA \rightarrow BCA→BC and the fact that AAA is the minimal key, both BBB and CCC are determined by AAA. Since there's no transitive dependency of non-prime attributes on AAA, RRR is in 3NF.
    
4. **BCNF**: For a relation to be in BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Here, A→BCA \rightarrow BCA→BC is the given functional dependency and AAA is a superkey (minimal key). Thus, RRR satisfies BCNF.
    

Given this evaluation, the highest normal form valid for RRR is:

d. BCNF.

* * *

**You:**

Question 20
A functional dependency A → B is valid in a relational schema R(A, B, C). A minimal key is (AC). The highest normal form valid for the relational schema is


a.
3NF


b.
1NF


c.
BCNF


d.
2NF

* * *

**ChatGPT:**

Given: Functional dependency A→BA \rightarrow BA→B and the minimal key is ACACAC.

Let's evaluate the normal forms based on the given information:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: For a relation to be in 2NF, it should be in 1NF, and there should be no partial dependency of any column on the primary (or minimal) key. Given the minimal key ACACAC and the functional dependency A→BA \rightarrow BA→B, we see a partial dependency because AAA alone determines BBB, without needing CCC. So, RRR is not in 2NF.
    
3. **3NF**: Since RRR is not in 2NF, it can't be in 3NF or BCNF.
    

Given this evaluation, the highest normal form valid for RRR is:

b. 1NF.

* * *

**You:**

Question 21
The functional dependencies A → B and B → C are valid in a relational schema R(A, B, C). A minimal key is (A). The highest normal form valid for the relational schema is


a.
1NF


b.
3NF


c.
2NF


d.
BCNF

* * *

**ChatGPT:**

Given: Functional dependencies A→BA \rightarrow BA→B and B→CB \rightarrow CB→C, and the minimal key is AAA.

From the given functional dependencies:

* A→BA \rightarrow BA→B: AAA determines BBB.
* B→CB \rightarrow CB→C: BBB determines CCC. By transitivity, AAA determines CCC as well. So, AAA determines all attributes in the relation RRR.

Let's evaluate the normal forms based on the given information:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: Since AAA is the minimal key and it's not a composite key, there are no partial dependencies. So, RRR is in 2NF.
    
3. **3NF**: For a relation to be in 3NF, it should be in 2NF, and there should be no transitive dependencies of non-prime attributes on the primary key. Here, AAA determines BBB and BBB (which is non-prime) determines CCC (another non-prime). This is a transitive dependency. However, AAA (the primary key) also determines CCC directly, so the transitive dependency does not violate 3NF. Thus, RRR is in 3NF.
    
4. **BCNF**: For a relation to be in BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Here, B→CB \rightarrow CB→C is a functional dependency where BBB is not a superkey (since the minimal key is AAA). So, RRR is not in BCNF.
    

Given this evaluation, the highest normal form valid for RRR is:

b. 3NF.

* * *

**You:**

Question 22
No nontrivial functional dependencies are valid in a relational schema R(A, B, C). A minimal key is (A,B,C). The highest normal form valid for the relational schema is


a.
1NF


b.
2NF


c.
3NF


d.
BCNF

* * *

**ChatGPT:**

Given: No nontrivial functional dependencies in the schema R(A,B,C)R(A, B, C)R(A,B,C), and the minimal key is A,B,CA,B,CA,B,C.

If there are no nontrivial functional dependencies, then there's nothing to cause violations of the higher normal forms.

Let's evaluate the normal forms:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: Since there are no nontrivial functional dependencies and the minimal key is a composite key A,B,CA,B,CA,B,C, there are no partial dependencies (because no attribute can be determined by part of the key). So, RRR is in 2NF.
    
3. **3NF**: Given there are no nontrivial functional dependencies, there can be no transitive dependencies of non-prime attributes on the primary key. Thus, RRR is in 3NF.
    
4. **BCNF**: For a relation to be in BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Since there are no nontrivial functional dependencies, RRR satisfies BCNF by default.
    

Given this evaluation, the highest normal form valid for RRR is:

d. BCNF.

* * *

**You:**

Question 23
A functional dependency A → B is valid in a relational schema R(A, B). A minimal key is (A). The highest normal form valid for the relational schema is


a.
3NF


b.
1NF


c.
2NF


d.
BCNF

* * *

**ChatGPT:**

Given: Functional dependency A→BA \rightarrow BA→B in the schema R(A,B)R(A, B)R(A,B), and the minimal key is AAA.

From the given functional dependency:

* A→BA \rightarrow BA→B: AAA determines BBB.

Let's evaluate the normal forms based on the given information:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: Since AAA is the minimal key and it's not a composite key, there are no partial dependencies. So, RRR is in 2NF.
    
3. **3NF**: For a relation to be in 3NF, it should be in 2NF, and there should be no transitive dependencies of non-prime attributes on the primary key. Given that AAA determines BBB, and AAA is the minimal key, there are no transitive dependencies. Thus, RRR is in 3NF.
    
4. **BCNF**: For a relation to be in BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Here, AAA determines BBB and AAA is the minimal key (and hence a superkey). So, RRR is in BCNF.
    

Given this evaluation, the highest normal form valid for RRR is:

d. BCNF.

* * *

**You:**

Question 23
A functional dependency A → B is valid in a relational schema R(A, B). A minimal key is (A). The highest normal form valid for the relational schema is


a.
3NF


b.
1NF


c.
2NF


d.
BCNF

* * *

**ChatGPT:**

Given: Functional dependency A→BA \rightarrow BA→B in the schema R(A,B)R(A, B)R(A,B), and the minimal key is AAA.

Let's evaluate the normal forms based on the given information:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: Since AAA is the minimal key and it's not a composite key, there are no partial dependencies. So, RRR is in 2NF.
    
3. **3NF**: For a relation to be in 3NF, it should be in 2NF, and there should be no transitive dependencies of non-prime attributes on the primary key. Given that AAA determines BBB, and AAA is the minimal key, there are no transitive dependencies. Thus, RRR is in 3NF.
    
4. **BCNF**: For a relation to be in BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Given A→BA \rightarrow BA→B and AAA being a superkey, RRR satisfies BCNF.
    

Given this evaluation, the highest normal form valid for RRR is:

d. BCNF.

* * *

**You:**

Question 24
The functional dependencies A → B and B → A are valid in a relational schema R(A, B, C). The minimal keys are (A) and (B). The highest normal form valid for the relational schema is


a.
3NF


b.
1NF


c.
2NF


d.
BCNF

* * *

**ChatGPT:**

Given: Functional dependencies A→BA \rightarrow BA→B and B→AB \rightarrow AB→A in the schema R(A,B,C)R(A, B, C)R(A,B,C). The minimal keys are AAA and BBB.

Let's evaluate the normal forms:

1. **1NF**: If all attributes in RRR have atomic values, then RRR is in 1NF.
    
2. **2NF**: Since the keys AAA and BBB are not composite keys, there can't be any partial dependencies on them. So, RRR is in 2NF.
    
3. **3NF**: A relation is in 3NF if every non-prime attribute is non-transitively dependent on every key of the relation. Given our functional dependencies and the keys, there are no transitive dependencies. So, RRR is in 3NF.
    
4. **BCNF**: For a relation to be in BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey. Given A→BA \rightarrow BA→B and B→AB \rightarrow AB→A, both AAA and BBB are superkeys. So, RRR satisfies BCNF.
    

Given this evaluation, the highest normal form valid for RRR is:

d. BCNF.

* * *

**You:**

Question 25
The functional dependencies A → B and B → C are valid in a relational schema R(A, B, C). A minimal key is (A). A decomposition that brings the schema into BCNF and preserves all functional dependencies is


a.
(A) (B)


b.
(A,B) (A,C)


c.
(A) (B) (C)


d.
(A,B) (B,C)

* * *

**ChatGPT:**

Given: Functional dependencies A→BA \rightarrow BA→B and B→CB \rightarrow CB→C in the schema R(A,B,C)R(A, B, C)R(A,B,C). The minimal key is AAA.

For BCNF, for every non-trivial functional dependency X→YX \rightarrow YX→Y, XXX must be a superkey.

Given the functional dependency A→BA \rightarrow BA→B, AAA is a superkey, so it meets the BCNF requirement.

However, for the functional dependency B→CB \rightarrow CB→C, BBB is not a superkey. This violates the BCNF condition.

To bring the schema into BCNF while preserving all functional dependencies, we need to decompose the schema. One way to decompose is:

1. R1(A,B)R1(A, B)R1(A,B) with the functional dependency A→BA \rightarrow BA→B
2. R2(B,C)R2(B, C)R2(B,C) with the functional dependency B→CB \rightarrow CB→C

This decomposition satisfies the BCNF condition and preserves all functional dependencies.

Thus, the correct decomposition is:

d. (A,B) (B,C)

* * *

**You:**

Question 26
If the highest normal form valid for a relational schema is BCNF then what other normal forms are valid for the schema ?


a.
1NF and 2NF and 3NF only


b.
1NF only


c.
0NF only


d.
1NF and 2NF only

* * *

**ChatGPT:**

When a relational schema is in BCNF, it must first satisfy the requirements of the previous normal forms. BCNF is stricter than 3NF, which is stricter than 2NF, and 2NF is stricter than 1NF.

Therefore, if a relational schema is in BCNF, it is also in:

1. 1NF
2. 2NF
3. 3NF

So the correct answer is:

a. 1NF and 2NF and 3NF only.

* * *

**You:**

Question 27
If the highest normal form valid for a relational schema is 3NF then what other normal forms are valid for the schema ?


a.
BCNF only


b.
0NF only


c.
1NF only


d.
1NF and 2NF only

* * *

**ChatGPT:**

If a relational schema is in 3NF, it has already satisfied the requirements for the preceding normal forms. Specifically:

1. To achieve 3NF, a schema must first be in 2NF.
2. To achieve 2NF, a schema must first be in 1NF.

However, being in 3NF does not guarantee that a schema is in BCNF, as BCNF has stricter requirements than 3NF.

Therefore, if a relational schema is in 3NF, it is also in:

1. 1NF
2. 2NF

So the correct answer is:

d. 1NF and 2NF only.

* * *

**You:**

Question 28
If the highest normal form valid for a relational schema is 2NF then what other normal forms are valid for the schema ?


a.
1NF only


b.
1NF and 3 NF only


c.
0NF only


d.
BCNF only

* * *

**ChatGPT:**

If a relational schema is in 2NF, it has already satisfied the requirements of the preceding normal forms:

1. To achieve 2NF, a schema must first be in 1NF.

However, being in 2NF does not guarantee that a schema is in 3NF, BCNF, or any higher normal form, as each subsequent normal form has stricter requirements.

Therefore, if a relational schema is in 2NF, it is also in:

1. 1NF

So the correct answer is:

a. 1NF only.

* * *

**You:**

Question 29
If the highest normal form valid for a relational schema is 1NF then what other normal forms are valid for the schema ?


a.
0NF only


b.
2NF only


c.
No other normal form is valid for the schema


d.
BCNF only

* * *

**ChatGPT:**

If the highest normal form valid for a relational schema is 1NF, it means the schema does not meet the requirements for 2NF, 3NF, BCNF, or any higher normal forms.

1NF is essentially a step up from an unnormalized form (0NF), where data is organized but may still contain repeating groups and doesn't ensure the elimination of partial dependencies.

So, if a schema is in 1NF but no higher normal form, then the only other "lower" state it inherently satisfies is 0NF.

Therefore, the correct answer is:

a. 0NF only.

* * *

**You:**

Question 30
Normalization of relational tables is performed to


a.
Enforce higher levels of data security


b.
Improve performance of relational database systems


c.
Eliminate redundancies from relational tables


d.
Simplify database administration

* * *

**ChatGPT:**

Normalization is primarily a process of efficiently organizing data in a database. Its main goals are to eliminate redundant data (for example, storing the same data in more than one table) and ensure data dependencies make sense (i.e., only storing related data in a table).

Therefore, the most accurate answer to the question is:

c. Eliminate redundancies from relational tables.