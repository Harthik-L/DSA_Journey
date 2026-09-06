# Week 1 — Python Fundamentals


## Overview
This week focused on building solid Python fundamentals before moving into DSA (Data Structures & Algorithms): functions, loops, strings, lists, dictionaries, and an introduction to recursion.

---

## Day 1 — Basic Functions & Loops
**Topics covered:** conditionals, loops, string indexing, modulus operator
**Problems solved:**
- `is_prime(n)` — check if a number is prime using loop up to square root
- `reverse_string(s)` — reverse a string manually using string concatenation in a loop
- `find_largest(nums)` — find max value in a list without using `max()`
- `count_vowels(s)` — count vowels using membership check (`in`)
- `fizzbuzz` — classic conditional/modulus practice with `if/elif/else`
**Key concept:** The modulus operator (`%`) gives remainder of division — used constantly for even/odd checks, divisibility, and digit extraction.

---

## Day 2 — Lists & Dictionaries
**Topics covered:** list building, dictionary as a frequency counter
**Problems solved:**
- `get_evens(nums)` — filter list using a condition
- `remove_duplicates(nums)` — build a new list while checking membership
- `char_count(s)` — frequency counter pattern using a dictionary
- `common_elements(list1, list2)` — find shared elements between two lists
- `second_largest(nums)` — single-pass tracking of two values simultaneously
**Key concept:** The "frequency counter" pattern (dictionary tracking counts) — one of the most reused patterns in coding interviews.
**Bug I hit:** misplaced `return` statement inside a loop instead of after it, causing early exit before checking all list items. Lesson: always check whether a line should run once per loop iteration or once after the loop finishes.

---

## Day 3 — Strings Deeper + Intro to Recursion
**Topics covered:** two-pointer technique, base case vs recursive case
**Problems solved:**
- `is_palindrome(s)` — two-pointer approach comparing from both ends
- `word_frequency(sentence)` — frequency counter applied to words instead of characters
- `factorial(n)` — first recursive function (base case: n=0 or 1)
- `sum_to_n(n)` — recursion summing numbers down to 0
- `is_anagram(s1, s2)` — compare frequency dictionaries of two strings
**Key concept:** Every recursive function needs a **base case** (where it stops) and a **recursive case** (where it calls itself with a smaller input, moving toward the base case).

---

## Day 4 — Nested Data & Recursion in New Contexts
**Topics covered:** recursion on nested lists, working with dictionary values
**Problems solved:**
- `flatten(lst)` — recursively flatten nested lists
- `most_common(nums)` — find element with highest frequency
- `is_sorted(nums)` — check ascending order
- `reverse_recursive(s)` — reverse a string recursively using slicing
- `running_sum(nums)` — build cumulative sum list
**Bug I hit:** flipped comparison operator in `is_sorted` (`<` instead of `>`), which caused correct sorted lists to be flagged as unsorted. Lesson: trace through one concrete example by hand before trusting the logic.

---

## Day 5 — Searching & More Recursion
**Topics covered:** linear search, brute-force pair matching, Fibonacci recursion
**Problems solved:**
- `linear_search(nums, target)` — find index of a target value
- `is_perfect_square(n)` — loop-based square check
- `pair_sum(nums, target)` — brute-force nested loop to find pairs summing to a target
- `fib(n)` — recursive Fibonacci (two base cases: n=0 and n=1)
- `remove_vowels(s)` — inverse of Day 1's vowel counter
**Key concept (noted for later):** naive recursive Fibonacci recalculates the same values repeatedly — inefficient for large `n`. Will revisit with **memoization** during DSA month.

---

## Day 6 — Sorting Basics
**Topics covered:** bubble sort, math-based tricks, digit manipulation via recursion
**Problems solved:**
- `bubble_sort(nums)` — sort a list using nested loops and adjacent swaps
- `missing_number(nums, n)` — use sum formula (n(n+1)/2) to find a missing value
- `only_digits(s)` — check if a string is entirely numeric characters
- `sum_digits(n)` — recursive digit-sum using `% 10` and `// 10`
- `group_by_length(words)` — group strings into a dictionary keyed by length
**Bug I hit:** mismatched comparison and swap indices in bubble sort (`nums[j-1]` vs `nums[j+1]`), plus learned that Python's negative indexing silently wraps around instead of erroring — a subtle source of hidden bugs.

---

## Patterns I now recognize across problems
1. **Frequency counter pattern** (dictionary tracking counts) — Days 2, 3, 4, 6
2. **Two-pointer technique** — Day 3
3. **Recursion: base case + recursive case** — Days 3, 4, 5, 6
4. **Single-pass tracking of multiple values** — Day 2 (`second_largest`), Day 4 (`most_common`)
5. **Building a new list/dict while iterating an existing one** — nearly every day

## Common mistakes I'm learning to catch
- Misplaced `return` (wrong indentation level)
- Flipped comparison operators (`<` vs `>`)
- Mismatched indices in swaps/comparisons
- Not tracing through examples by hand before trusting code

## Next week (Week 2) preview
Continuing Python fundamentals into more sorting algorithms, basic searching techniques (binary search), and starting to think about time complexity — how "fast" or "slow" different approaches are, which becomes critical once real DSA topics (arrays, strings as patterns, hashing) begin in Month 3.
