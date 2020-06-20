# Data Structures & Algorithms Nanodegree - Udacity

##About the Nanodegree Program

In this Nanodegree program, I have learned various Data Strutures and Algorithms in Computer Science. For each topic, I have solved the given problem that gave me an in-depth knowledge of the concept. I solved 100+ DS and Algorithmic problems and it was quite fun to code in Python. All code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/ "PEP8 style guidelines").

## Technologies and Tools
- Python 3
- Jupyter Notebook
- Visual Studio Code
- Git Bash
- Pip

## Course Contents
### Data Structures
- Arrays, Linked Lists, Stacks and Queues, Recursion, Sets, Maps and Hashing
- Trees: Binary, Binary Search, Complete Binary, Red-black, Heap
- Tree Traversals: BFS, DFS: In-order, Pre-order, Post-order

### Big-O Notations
- O(1)
- O( n)
- O(n^2)
- O(logn)
- O(nlogn)
- O(2^n)
- O(n!)

### Basic Algorithms
- Bubble Sort
- Merge Sort
- Quick Sort
- Heap Sort

### Advanced Algorithms
- Greedy Algorithms: Dijkstra's Algorithm
- Graph Algorithms
	- DFS, BFS
	- Uniform Cost Search Algorithm
	- A* Algorithm
- Dynamic Programming
	- 0/1 Knapsack
	- Coin Change
	- Stock Prices

## Projects
### Project 1. Unscramble Computer Science Problems
#### About
Deconstruct a series of open-ended problems into smaller components (e.g., inputs, output, series of functions).

#### Task 1
Given the data of calls and text messages of a telemarketing company.
What is the first record of texts and what is the last record of calls?

#### Task 2
How many different telephone numbers are there in the records?

#### Task 3
Which telephone number spent the longest time on the phone during the period? Don't forget that time spent answering a call is also time spent on the phone.

#### Task 4
- Part 1. Find all of the area codes and mobile prefixes called by people
in Bangalore.
- Part 2. What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore?

#### Task 5
The telephone company want to identify numbers that might be doing telephone marketing. Create a set of possible telemarketers:
- These numbers make outgoing calls.
- Never send texts, receive texts or receive incoming calls.

#### Task 6

### Project 2. Show Me the Data Structures
#### About
Solve a series if open-ended practice problems. Hone your skills to identify and implement appropriate data structures and corresponding methods that meet given constraints.

#### Task 1. Least Recently Used (LRU) Cache.
Use an appropriate data structure(s) to implement the LRU cache.
- In case of a cache hit, your get() operation should return the value.
- In case of a cache miss, your get() should return -1.
- While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first  and then insert the element.
- All operations must take O(1) time.

#### Taks 2. File Recursion
Write code for finding all files under a directory and all directories beneath it that end with ".c". Find all files beneath path with file name suffix.

#### Task 3. Huffman Algorithm
Implement Huffman Encoding and Decoding for data compression.

#### Task 4. Active Directory
In context of groups and users in Windows OS, users can be part of a group and one group can also be a part of another group. In that case all users of child group becomes the users of parent group. If the username/id and group passed as input parameters, return True/False whether the user is part of that group or not. In the place of username/id, a child group name can also be passed.

#### Task 5. Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time (GMT) when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

#### Task 6. Union and Intersection of Two Linked Lists
Implement the union and intersection functions. The union of two sets A and B, A ∪ B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.

### Project 3. Problems vs. Algorithms
#### About
A series of real-world problems which train you to apply suitable data structures and algorithms under different contexts.

#### Task 1. Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root. For example, if the given number is 16, then the answer would be 4. If the given number is 27, the answer would be 5 because,
sqrt(5) = 5.196 whose floor value is 5.

#### Task 2. Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.
Example: [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

You are given a target value to search. If found in the array return its index, otherwise return -1. You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

#### Task 3. Rearrange Array Digits
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

For example, [1, 2, 3, 4, 5]
The expected answer would be [531, 42].
Another expected answer can be [542, 31].
If there are more than one possible answers, return any one.

#### Task 4. Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2. Sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

#### Task 5. Autocomplete with Trie - Finding Suffixes
Suppose, we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie.

For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

#### Task 6. Unsorted Integer Array
Find the max and min values in an unsorted array.
Find the smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

#### Task 7. HTTP Router using a Trie
Implement an HTTP Router like you would find in a typical web server using the Trie data structure.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

### Project 4. Route Planner
#### About
Build a route-planner algorithm like the one used in Google Maps to calculate the shortest path between two points on a map.

#### Task
Given the coordinates of locations as map.interactions and roads as map.roads.
Using A* algorithm, find the shortest path between 2 locations on the map.

## Author
- [Himel Das] (https://www.linkedin.com/in/himeldas)

## Acknowledgements
- The incredible team at Udacity.
