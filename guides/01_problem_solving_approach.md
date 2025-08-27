# Solving DSA Problems: A Step-by-Step Framework

This guide covers structured approaches to solving algorithmic problems.

The proposed framework consists of the following key steps:

1.  **Understand the Problem:** Before anything else, slow down and ensure you can explain the problem and its examples in your own words.
2.  **Check Constraints:** Analyze the given constraints (e.g., input size `n`) to determine the required time complexity, which will guide your choice of algorithm. For instance, an input of `n = 10^5` suggests a solution of `O(n log n)` or better is likely needed.
3.  **Identify Edge Cases:** Actively think about potential edge cases before coding. Consider scenarios like empty inputs, duplicates, negative numbers, or single-element inputs, etc.
4.  **Formulate a Brute Force Solution:** Start by mentally outlining or writing pseudocode for a simple, straightforward solution that works, even if it's inefficient. This provides a foundation to build upon.
5.  **Optimize the Solution:** Improve upon the brute force approach. Look for patterns, consider using more efficient data structures like hash maps, or apply algorithms like binary search to reduce time complexity.
6.  **Code, Test, and Refactor:** Write clean, readable code. Test it against the edge cases you identified earlier. Once it's working, review your code to see if it can be made cleaner or more efficient.
7.  **Practice Consistently:** Treat DSA as a skill that requires regular practice. The author recommends daily, focused sessions on learning concepts and solving a few problems, emphasizing quality over quantity.

---

**Source:** [🚀 Best Way to Solve DSA Problems!! — Let’s Get Real and Become Pros](https://medium.com/@adarshrai3011/best-way-to-solve-dsa-problems-lets-get-real-and-become-pros-1a130cf24692)

To master each pattern before moving on, I suggest a "Crawl, Walk, Run" approach. This ensures you build a deep, lasting understanding instead of just memorizing solutions.

---
# How to learn Algorithmic Patterns

### Step 1: Crawl - Understand the Core Concept 🧠

Before writing a single line of code, your goal is to understand the **what, why, and when** of the pattern.

* **Watch a Video:** Find a high-quality video explanation (NeetCode is a great resource) that breaks down the theory.
* **Trace it by Hand:** Take a simple example problem and manually trace the algorithm on paper or a whiteboard. For the **Sliding Window** pattern, you would physically draw an array and slide your fingers or a box across it, tracking the state of your variables. This is the single most important step for building intuition.
* **Write Pseudocode:** Describe the steps of the pattern in plain English. This forces you to solidify your understanding of the logic.

You're ready to move to the next step when you can explain the pattern to someone else in your own words.

---

### Step 2: Walk - Solidify with Easy Problems 🚶

Now, translate theory into practice. Your goal here is to learn the **code template** and recognize the pattern's signature.

* **Find Tagged Problems:** Use a platform like LeetCode and filter for problems tagged with the specific pattern (e.g., "Two Pointers").
* **Solve 3-5 Easy Problems:** Start with the easiest ones. Focus on implementing the basic template correctly. Don't worry about speed; focus on accuracy.
* **Analyze and Reflect:** After each problem, ask yourself: "What part of this problem statement hinted that I should use this pattern?" For example, a question asking for the "longest/shortest contiguous subarray" is a huge clue for the **Sliding Window** pattern.

You're ready for the next step when you can code the basic template for the pattern from memory without much difficulty.

---

### Step 3: Run - Adapt with Medium Problems 🏃

This is where true learning happens. Medium problems test your ability to adapt the standard pattern to new scenarios and handle edge cases.

* **Solve 3-5 Medium Problems:** These problems will often require a slight modification of the pattern or combine it with another simple idea.
* **Timebox Your Efforts:** Give yourself a reasonable amount of time (e.g., 25-40 minutes) to try and solve it on your own.
* **Study the Solution:** If you get stuck, it's okay! **The goal is to learn, not just to solve.** Carefully study the solution and, most importantly, understand *why* it works. Then, try to re-implement it yourself without looking.

---

### When Are You Ready to Move On? ✅

You're ready to move to the **next pattern** in the roadmap when you can confidently check off these points:

1.  You can **explain** the pattern's logic and its common use cases.
2.  You can **recognize** when a new problem is a good fit for the pattern.
3.  You can implement the code for a **medium-level** problem for that pattern, even if you need a little time to work through the logic.

**A crucial tip:** Don't get stuck on "Hard" problems yet. They often combine multiple complex patterns and are best saved for after you have a working knowledge of all the foundational patterns. Circle back to them during a final review phase before interviews.
