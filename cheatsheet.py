# 1. Arrays & Strings
# Common Keywords/Patterns:

# “Contiguous subarray” → Sliding Window or Prefix Sum
# “Maximum subarray sum” → Kadane’s algorithm (Dynamic Programming on arrays)
# “Two sorted arrays” → Two Pointers or Merge approach
# “Remove duplicates” → In-place array modifications, Two Pointers
# “Rotation,” “Rearrangement” → In-place swapping, Reverse
# “Longest substring/subsequence” → Possibly Dynamic Programming, or Sliding Window if substring
# “Partition” / “Dutch National Flag problem” → Two/Three Pointers partitioning approach
# Potential Data Structures:

# Arrays (Built-in)
# String (Built-in)
# Slices/substring manipulations
# Typical Approaches:

# Two pointers
# Sliding window
# Prefix sums
# Sorting & scanning
# 2. Linked List
# Common Keywords/Patterns:

# “Cycle in a linked list” → Floyd’s Tortoise and Hare cycle detection
# “Reverse a linked list” → Iterative or recursive reversal
# “Merge two lists” → Pointer manipulation
# “Remove Nth node from end” → Two pointers
# “Partition a linked list” → Rearranging nodes by pointer re-linking
# “Linked list palindrome” → Slow/Fast pointers + Reverse second half
# Potential Data Structures:

# Singly linked list
# Doubly linked list
# Typical Approaches:

# Pointer manipulation
# Fast/slow pointer patterns
# Reversal of sub-lists
# 3. Stacks & Queues
# Common Keywords/Patterns:

# “Validate parentheses” → Stack
# “Next greater element” → Monotonic stack
# “Evaluate postfix/prefix expression” → Stack
# “Min stack” or “Implement queue using stacks” → Stack data structure
# “Breadth-first search (BFS)” → Queue usage in graph/tree traversal
# “Sliding window maximum” → Deque (Double-ended queue) / Monotonic queue
# Potential Data Structures:

# Stack
# Queue
# Deque / Double-ended queue
# Typical Approaches:

# Monotonic stacks or queues
# BFS usage (queue in graphs/trees)
# LIFO patterns (stack)
# 4. Trees & Binary Search Trees
# Common Keywords/Patterns:

# “Level order traversal” → Queue (BFS)
# “Preorder/inorder/postorder traversal” → Stack (DFS) or Recursion
# “Lowest common ancestor” → DFS, BST property, or binary lifting
# “Balanced binary tree,” “height of tree” → Recursion, DFS
# “Serialize/deserialize” → BFS or DFS traversal
# “Binary search tree insertion/search” → BST property (left < root < right)
# “Segment tree,” “Fenwick tree” (for range queries) → Advanced tree data structures
# Potential Data Structures:

# Binary trees
# Binary search trees
# N-ary trees
# Segment/Fenwick (BIT) for range queries
# Typical Approaches:

# DFS (recursive or stack)
# BFS (queue)
# Divide & Conquer
# Tree-specific recursion
# 5. Graphs
# Common Keywords/Patterns:

# “Connected components” → DFS or BFS
# “Shortest path in an unweighted graph” → BFS
# “Shortest path in weighted graph” → Dijkstra’s algorithm, Bellman-Ford, Floyd-Warshall
# “Detect cycle in a graph” → Union-Find (Disjoint Set), DFS with visited set
# “Topological sort” → Directed Acyclic Graph (DAG) + DFS or Kahn’s Algorithm
# “Number of islands” → Grid BFS/DFS, Union-Find
# “Minimum spanning tree” → Kruskal’s (with Union-Find) or Prim’s algorithm
# Potential Data Structures:

# Adjacency list / adjacency matrix
# Union-Find (Disjoint set)
# Priority queue (for Dijkstra/Kruskal)
# Stack/Queue (for DFS/BFS/Topological sort)
# Typical Approaches:

# DFS/BFS
# Union-Find
# Dijkstra’s / Bellman-Ford / Floyd-Warshall
# Topological sort
# 6. Heaps / Priority Queues
# Common Keywords/Patterns:

# “Kth largest/smallest element” → Min-heap or Max-heap, Quickselect
# “Median of data stream” → Two heaps (max-heap, min-heap)
# “Reorganize string based on frequency” → Max-heap based on counts
# “Merge k sorted lists/arrays” → Min-heap
# “Find top k frequent elements” → Max-heap or Min-heap with size k
# Potential Data Structures:

# Heap (priority queue)
# Typical Approaches:

# Keep heap size to k for top-k queries
# Use min-heap for large sets where you only keep the largest k
# Use max-heap for smallest k or frequency-based sorting
# 7. Dynamic Programming (DP)
# Common Keywords/Patterns:

# “Number of ways to do X,” “Count ways,” “Coin change,” “Knapsack” → DP formulation
# “Longest increasing subsequence,” “Longest common subsequence” → DP approach
# “Min cost,” “Max profit,” “Optimal path” → DP table or recursion + memoization
# “Partition problem,” “Subset sum problem” → DP on subsets/states
# “Catalan numbers,” “Unique BSTs” → Combinatorial DP
# Potential Data Structures:

# DP arrays
# 2D arrays
# Bitmask DP
# Typical Approaches:

# Bottom-up tabulation
# Top-down memoization
# State-space optimization (bitmask, rolling arrays)
# 8. Backtracking / DFS with State
# Common Keywords/Patterns:

# “Generate all combinations/permutations/subsets” → Backtracking
# “N-queens,” “Sudoku solver” → Backtracking with constraints
# “Combination sum,” “Subset sum” → Backtracking or DFS + pruning
# “Path existence in a matrix with constraints” → DFS or backtracking
# Potential Data Structures:

# Recursion stack
# Temporary state arrays / boolean used[] arrays
# Typical Approaches:

# DFS + state tracking
# Pruning techniques
# Recursively build solutions
# 9. Binary Search (on arrays or “search space”)
# Common Keywords/Patterns:

# “Find element in sorted array” → Binary search
# “Search in rotated sorted array” → Modified binary search
# “Find peak element” or “Find min in rotated sorted array” → Binary search patterns
# “Minimum x such that condition holds,” “Split array largest sum” → Binary search on the answer / search space
# Potential Data Structures:

# Arrays (sorted or rotated)
# Searching “mid” in a numeric range (when searching for feasible solutions)
# Typical Approaches:

# Classic binary search
# Binary search on search space (e.g., searching for min feasible value)
# 10. Bit Manipulation
# Common Keywords/Patterns:

# “Single number,” “XOR,” “Bitwise operations” → Bitwise XOR, AND, OR
# “Check if power of two” → x & (x-1) trick
# “Count set bits,” “Reverse bits” → Bit counting, shifting
# “Subsets via bitmask” → Bitmask enumeration
# Potential Data Structures:

# Integer bit operations
# Bitmask arrays (for DP)
# Typical Approaches:

# XOR properties
# Shift operations
# Masks for subsets/permutations
# Using the Cheatsheet
# When you read a LeetCode problem:

# Identify keywords in the prompt.
# Match those keywords to the data structure or algorithm above.
# Cross-check patterns (“Kth,” “connected,” “subarray,” “shortest path,” “LCA,” etc.).
# Sometimes problems combine approaches—e.g., Tree + DFS + DP, or Array + Sliding Window + Heap.