# Week 2 — Searching, Data Structures, and Trees

## Overview
This week moved beyond core Python syntax into real data structures and algorithmic techniques: binary search, stacks, queues, sliding window, linked lists, two pointers, hashing, matrices, and an introduction to trees.

---

## Day 7 — Binary Search + Time Complexity Intro
**Topics covered:** binary search (iterative and recursive), brute-force pair counting, list rotation

**Problems solved:**
- `binary_search(nums, target)` — iterative binary search using left/right pointers
- `binary_search_recursive(nums, target, left, right)` — same logic, recursive form
- `pairs_with_diff_k(nums, k)` — brute-force O(n²) pair counting
- `intersection_point(list1, list2)` — first common element between two lists
- `rotate_list(nums, k)` — rotate a list using slicing

**Key concept:** Binary search only works on sorted data, and is dramatically faster than linear search because each check eliminates half the remaining search space.

---

## Day 8 — Stacks, Queues, Sliding Window
**Topics covered:** stack/queue data structures (as classes), sliding window technique

**Problems solved:**
- `is_valid(s)` — valid parentheses checker using a stack
- `Stack` class — push, pop, peek, is_empty
- `Queue` class — enqueue, dequeue, is_empty
- `power(base, exp)` — recursive power function
- `max_sum_subarray(nums, k)` — sliding window for max sum of k consecutive elements

**Key concept:** Sliding window avoids recalculating overlapping work by adding/removing only the elements entering/leaving the window, rather than resumming from scratch each time.

---

## Day 9 — Linked Lists
**Topics covered:** singly linked lists, Node class, recursive reversal

**Problems solved:**
- `Node` class + `print_list(head)` — build and traverse a linked list
- `list_length(head)` — count nodes
- `contains(head, target)` — search for a value
- `reverse_list(head)` — recursive linked list reversal
- `power_mod(base, exp, mod)` — recursive power with modulus

**Key concept:** Linked lists can only be traversed forward node-by-node via `.next` — no direct indexing like Python lists. Recursive reversal was the trickiest pattern so far: recurse to the end first, then rewire links while unwinding.

**Bug I hit:** stray comma in a constructor call — fixed by reading Python's error message directly.

---

## Day 10 — Two Pointers + Big O Notation
**Topics covered:** two-pointer technique on sorted data, in-place array modification, introduction to time complexity

**Problems solved:**
- `two_sum_sorted(nums, target)` — O(n) two-pointer sum finder (vs O(n²) brute force)
- `remove_element(nums, val)` — in-place removal using a slow/fast pointer pattern
- `merge_sorted(list1, list2)` — merge two sorted lists with two pointers
- `climb_stairs(n)` — recursive Fibonacci-shaped counting problem
- `valid_mountain(nums)` — validate strictly increasing-then-decreasing shape

**Key concept:** Big O notation (O(1), O(log n), O(n), O(n²)) describes how runtime scales with input size — now labeling every function's complexity going forward.

**Bug I hit:** compared every element to a fixed last element (`nums[n-1]`) instead of its immediate neighbor (`nums[i+1]`) — passed the given test cases by coincidence but failed on an edge case with a hidden second peak. Lesson: test cases beyond the given examples matter.

---

## Day 11 — Hashing Deep Dive + Matrices
**Topics covered:** frequency-based hashing patterns, 2D lists (matrices), list comprehensions

**Problems solved:**
- `first_unique_char(s)` — first non-repeating character using a frequency map
- `group_anagrams(words)` — group words by sorted-letter key
- `matrix_sum(matrix)` — sum all elements in a 2D list
- `transpose(matrix)` — flip rows/columns using list comprehension
- `sum_to_n_iterative(n)` — iterative version of Day 3's recursive function, comparing O(1) vs O(n) space

**Key concept:** Sorting a word's letters gives a canonical key for grouping anagrams. Iterative solutions use constant space vs recursion's call-stack space — an important interview trade-off to be able to explain.

---

## Day 12 — Trees Introduction
**Topics covered:** binary trees, recursive tree traversal, breadth-first traversal (queue-based)

**Problems solved:**
- `TreeNode` class + `inorder_traversal(root)` — left-root-right recursive traversal
- `tree_height(root)` — recursive max depth calculation
- `count_nodes(root)` — recursive total node count
- `two_sum_indices(nums, target)` — optimal O(n) hash-map two-sum (review/upgrade of Day 1's brute force)
- `max_depth_iterative(root)` — breadth-first (level-by-level) depth using a queue, connecting back to Day 8

**Key concept:** The "1 + recurse(left) + recurse(right)" pattern is the backbone of most tree problems. In-order traversal on a binary search tree always yields sorted output — not a coincidence, a structural property.

---

## Patterns I now recognize across problems (Week 2 additions)
1. **Two-pointer technique** on sorted data — Days 7, 10
2. **Sliding window** — avoiding redundant recalculation — Day 8
3. **Stack/Queue as classes wrapping a list** — Day 8, reused conceptually in Day 12's BFS
4. **Linked list traversal via `.next`** — Day 9
5. **Hash map for O(n) lookups** replacing O(n²) brute force — Days 10 (implicitly), 12
6. **Recursive tree pattern**: base case on `None`, combine results from left/right — Day 12

## Common mistakes I'm learning to catch
- Comparing against a fixed reference value instead of the correct neighboring element (valid_mountain bug)
- Testing only the given examples instead of constructing edge cases myself
- Small typos in function/variable names (interative, palidrome) — cosmetic but worth catching before finalizing

## Next week (Week 3) preview
Continuing with more tree problems (BST-specific operations, tree traversal variants), graph basics (BFS/DFS on graphs, not just trees), and starting to combine techniques (hashing + two pointers, recursion + memoization) as problems get closer to real medium-difficulty interview questions.
