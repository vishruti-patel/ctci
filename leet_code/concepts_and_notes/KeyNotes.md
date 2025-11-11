

#Defualtdict -  provides a default VALUE to keys.
-- d = defaultdict(list). --> This will create dictionary with empty list as a value to the given key.  

#Tuple  -> can be used when a function wants to return multiple values
        -> Can be used as a key (as tuples are immutable- cant be changed) in dictionary because list cannot be used as dictionary key (list are changable- mutable)

#use ASCII concept when checking for anagrams in a list

        

##🧩 Coding Interview Pattern Cheat Sheet
#1. Arrays & Strings
When to use: Searching, grouping, frequency counts, subarrays.

Patterns:
Hash Map (frequency) → Two Sum, Group Anagrams
Sorting + Two Pointers → 3Sum, Container With Most Water
Prefix Sum → Subarray Sum = K

2. Two Pointers
When to use: Array is sorted / can be sorted, or need to shrink/expand range.

Patterns:
Opposite ends → Container With Most Water
Slow/Fast pointers → Linked List Cycle

--> 


3. Sliding Window
When to use: Substring/subarray optimization (min/max/longest).

Patterns:
Fixed window → Max Average Subarray
Expand/Shrink → Longest Substring Without Repeating
Min window → Minimum Window Substring

4. Binary Search

When to use: Sorted arrays, monotonic property.

Patterns:
Classic → Binary Search\
Rotated → Search in Rotated Sorted Array
First/Last occurrence → Find Minimum in Rotated Array

5. Linked List

When to use: Reversal, merging, cycle detection.

Patterns:
Dummy head pointer for clean code.
Slow/Fast pointer → detect middle/cycle.
In-place reversal → Reverse Linked List

6. Stack / Monotonic Stack

When to use: Previous/next greater/smaller element, parentheses.

Patterns:
Valid Parentheses
Min/Max tracking → Min Stack
Monotonic Stack → Daily Temperatures, Next Greater Element

7. Trees (DFS/BFS)

When to use: Traversal, path sums, depth, validation.

Patterns:
DFS recursion → Max Depth, Path Sum
BFS with queue → Level Order Traversal
BST property → Validate BST, Kth Smallest

8. Graphs

When to use: Connectivity, cycles, shortest path.

Patterns:
DFS/BFS → Number of Islands
Topological Sort → Course Schedule
Union-Find → Connected Components

9. Dynamic Programming

When to use: Optimal substructure + overlapping subproblems.

Patterns:
1D DP → Climbing Stairs, House Robber
2D DP (grid) → Unique Paths, Coin Change
Subsequences → Longest Increasing/ Common Subsequence, Edit Distance

10. General Strategy

Restate the problem.
Identify input type (array, string, tree, graph).
Recall common pattern from above.
Start with brute force, then refine.
Communicate trade-offs.
Test edge cases (empty, single element, large input).



## BASIC SORTING ALGO:
-> QUICK SORT
--> QUICK SELECT (Hoare's selection algo)

