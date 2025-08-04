# 🚀 DSA & Interview Prep Reference

Welcome to my personal Data Structures, Algorithms, and interview preparation repository! This project serves as a centralized and organized reference for key computer science concepts, common problem-solving patterns, and practical coding solutions in Python.

The goal is to create a living document that grows over time, making it the ultimate study guide for technical interviews and a general refresher for core CS topics.

## Repository Structure

The repository is organized into two main sections: comprehensive guides for theoretical knowledge and a curated list of problems for hands-on practice.

```
dsa-reference/
├── 📚guides/
│ ├── 01_problem_solving_approach.md
│ ├── 02_data_structures.md
│ ├── 03_algorithmic_patterns.md
│ └── 04_big_o_cheatsheet.md
│
├── 💻coding_questions/
│ ├── 📂arrays_and_strings/
│ │  ├── 🧩two_sum/
│ │  │ ├── README.md (Problem Statement)
│ │  │ ├── solution.py (Python Solution)
│ │  │ └── test_solution.py (Test Cases)
│ │  └── ...
│ └── ...
│
└── README.md
```

## How to Use This Repository

1. **Start with the Guides**: If you need to refresh a concept, begin in the 📚`guides` directory. These files provide a high-level overview of everything from Big O to specific data structures.

2. **Pick a Topic to Practice**: Navigate to the 💻`problems` directory and choose a category you want to work on, like 📂`arrays_and_strings` or 📂`trees_and_graphs`.

3. **Solve a Coding Question**: Inside each category, coding questions are grouped by the pattern used to solve them. Try to solve a coding question on your own first by reading its `README.md` file.

4. **Review and Test**: Compare your approach with the provided `solution.py` and run the `test_solution.py` file to verify correctness.

## Content Overview

### 📚 Guides

- This section contains the core theoretical knowledge needed for technical interviews.

#### TODO: add links of folders to content overview

- 01: General Problem-Solving Approach: A step-by-step framework for tackling any coding question.

- 02: Data Structures Overview: A detailed summary of common data structures, their use cases, and complexity analysis.

- 03: Algorithmic Patterns: A breakdown of recurring problem patterns (e.g., Sliding Window, Two Pointers, DFS/BFS) and when to use them.

- 04: Big O Cheatsheet: A quick reference for the time and space complexities of major algorithms and data structure operations.

### 💻 Problems

This section is for hands-on practice. Problems are categorized first by the primary data structure and then by the **algorithmic** pattern used.

#### TODO: add links of folders to problems

- Arrays & Strings
- Linked Lists
- Stacks & Queues
- Trees & Graphs
- Heaps
- (...and more as they are added)

Each problem folder contains a `README.md` with the problem description, a `solution.py` with a clean and commented solution, and a `test_solution.py` to validate the code.

### Tech Stack

- Language: Python 3
- Testing: `pytest`

To run the tests for a specific problem, navigate to its directory and run:

```
pytest
```

Happy coding! ✨
