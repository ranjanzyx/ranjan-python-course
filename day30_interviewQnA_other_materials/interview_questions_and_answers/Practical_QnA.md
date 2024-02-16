## Coding Interview QnA

## 1. Find the Duplicate in an Array of N+1 Integers
Sample Input: [1,3,4,2,2]
Sample Output: 2

```python
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return hare

# Sample Input
nums = [1,3,4,2,2]
# Sample Output
print(findDuplicate(nums))  # Output: 2
```

## 2. Determine if a String has All Unique Characters
Sample Input: "hello"
Sample Output: False
```python
def isUniqueChars(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

# Sample Input
s = "hello"
# Sample Output
print(isUniqueChars(s))  # Output: False
```

## 3. Check if One String is a Permutation of the Other
Sample Input: str1 = "abc", str2 = "bca"
Sample Output: True
```python
from collections import Counter

def arePermutations(str1, str2):
    return Counter(str1) == Counter(str2)

# Sample Input
str1 = "abc"
str2 = "bca"
# Sample Output
print(arePermutations(str1, str2))  # Output: True
```

## 4. Perform Basic String Compression
Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"

```python
def compressString(s):
    compressed = []
    count_consecutive = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count_consecutive += 1
        else:
            compressed.append(s[i - 1] + str(count_consecutive))
            count_consecutive = 1
    compressed.append(s[-1] + str(count_consecutive))
    return ''.join(compressed) if len(compressed) < len(s) else s

# Sample Input
s = "aabcccccaaa"
# Sample Output
print(compressString(s))  # Output: "a2b1c5a3"
```

## 5. Delete a Node in a Singly Linked List
Given access only to the node to be deleted, we can't perform the usual unlinking process since we don't have access to the previous node. Instead, we copy the data from the next node into the current node and then delete the next node.
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    # Copy the next node's value to the current node
    node.val = node.next.val
    # Delete the next node
    node.next = node.next.next

# Assuming a list 4 -> 3 -> 2 -> 1 and we want to delete the node with value 3.
# Create the linked list 4 -> 3 -> 2 -> 1
head = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))

# Assume we want to delete the node with value 3, normally we would have access to that node somehow
node_to_delete = head.next  # This represents the node with value 3
delete_node(node_to_delete)  # Now the list is 4 -> 2 -> 1
```

## 6. Find the kth to Last Element of a Singly Linked List
To find the kth to last element, we can use the two-pointer technique.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_kth_to_last(head, k):
    slow = fast = head
    # Move fast k steps ahead
    for _ in range(k):
        if not fast:
            return None  # Out of bounds
        fast = fast.next
    
    # Move both at the same pace until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow
# Sample Invocation:
# For a list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the result should be 4.
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
kth_to_last = find_kth_to_last(head, 2)
print(kth_to_last.val)  # Outputs: 4
```
## 7. Detect Loop in a Linked List and Find the Start of the Loop
We can use Floyd's Tortoise and Hare algorithm to detect a loop. 
To find the start of the loop, we use two pointers, one starting at the head and the other at the meeting point inside the loop, and move them at the same pace.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def detect_and_find_start_of_loop(head):
    slow = fast = head
    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No loop
        return None

    # Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Sample Invocation:
# Let's create a looped list: 1 -> 2 -> 3 -> 4 -> 2 ....
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
loop_start = head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Creates a loop back to node with value 2

loop_entry = detect_and_find_start_of_loop(head)
print(loop_entry.val)  # Outputs: 2
```
## Interview Questions to practice
1. Determine if a String has All Unique Characters.
2. Find the Duplicate in an Array of N+1 Integers.
3. Check if a String is a Palindrome.
4. Implement an Algorithm to find the Kth to Last Element of a Singly Linked List.
5. Write a Function to Delete a Node in a Linked List given only access to that Node.
6. Given a Sorted Array, Create a Binary Search Tree with Minimal Height.
7. Implement a Function to Check if a Binary Tree is Balanced.
8. Find the Lowest Common Ancestor of Two Nodes in a Binary Search Tree.
9. Implement a Queue using Two Stacks.
10. Design a Stack that Supports push, pop, top, and retrieving the Minimum Element in Constant Time.
11. Write an Algorithm to Rotate an Array to the Right by K Steps.
12. Implement a Function to Merge Two Sorted Lists into a New Sorted List.
13. Design a Data Structure that Implements an LRU Cache.
14. Write a Function to Reverse Words in a String.
15. Determine if Two Strings are Anagrams of Each Other.
16. Find the First Non-Repeating Character in a String.
17. Count the Number of Islands in a 2D Grid.
18. Implement a Function to Perform Integer Division without Using the Division Operator.
19. Design an Algorithm to Print All Valid Combinations of N Pairs of Parentheses.
20. Implement the Merge Sort Algorithm.
21. Solve the Tower of Hanoi Problem with Recursive Solutions.
22. Detect a Cycle in a Graph.
23. Find the Maximum Depth of a Binary Tree.
24. Implement a Trie (Prefix Tree).
25. Design a Data Structure that Supports Add and Find Operations for a Data Stream.
26. Compute the Intersection of Two Arrays.
27. Implement an Algorithm to Convert a Roman Numeral to an Integer.
28. Write a Function to Flatten a Multilevel Doubly Linked List.
29. Solve the Sudoku Solver Problem.
30. Implement the Power Function without Using the Built-in pow Method.
31. Find All Subsets of a Set.
32. Implement an Algorithm to Print a Spiral Matrix.
33. Calculate the Maximum Subarray Sum.
34. Find the Longest Consecutive Sequence in an Unsorted Array.
35. Implement a Function to Perform a Binary Search on a Rotated Sorted Array.
36. Write an Algorithm to Determine if a Number is "Happy".
37. Find the Majority Element in an Array that Appears More than N/2 Times.
38. Implement QuickSort Algorithm.
39. Determine if a Sudoku is Valid.
40. Design a Tic-Tac-Toe Game.
41. Write a Function to Convert a Number from Decimal to Binary Format.
42. Implement an Algorithm to Find All Possible Permutations of a String.
43. Calculate the Angle Between Hour and Minute Hands on a Clock.
44. Implement a Function to Check for Prime Numbers.
45. Find the Kth Largest Element in an Array.
46. Solve the N-Queens Problem.
47. Implement a Circular Queue.
48. Find the Missing Number in an Array Containing 1 to N.
49. Write a Program to Implement a Graph Using Adjacency Lists.
50. Implement a Function to Check Whether a Graph is Bipartite.
