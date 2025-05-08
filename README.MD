# 💼 Capgemini Technical Interview – Rounds 1 & 2

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/nitinkumar30/Capgemini-AutomationEngineer-Interview/test.yml?label=GitHub%20Actions&logo=github)
![Latest Commit](https://img.shields.io/github/last-commit/nitinkumar30/Capgemini-AutomationEngineer-Interview?color=green)
![Interview Round 1](https://img.shields.io/badge/Interview-Round%201-orange)
![Interview Round 2](https://img.shields.io/badge/Interview-Round%202-orange)

---

Welcome! 👋
This repository contains Python-based coding solutions from my **Technical Interview Rounds** with **Capgemini** for the position of **Automation Engineer**.

---

## 🧠 Interview Overview

### 🟠 Round 1 – *May 6, 2025*

* ⏰ **Duration:** 30 minutes
* 🧪 **Format:** Technical Interview (Live coding)
* 💬 **Topics Covered:**

  * Core Python programming
  * Logical and algorithmic problem-solving
  * Basic API Testing (conceptual discussion)

### 🔵 Round 2 – *May 8, 2025*

* ⏰ **Duration:** \~20 minutes
* 🧪 **Format:** Single coding problem with explanation
* 💬 **Focus Area:**

  * String manipulation and dictionary handling
  * In-place logic explanation and optimization

---

## 📌 Problem Statements & Solutions

### 🔹 Round 1

#### 1️⃣ `ques1.py` – Sum Keys Based on Vowel Values

🔍 **Problem:**
Given a dictionary `D = {1:"a", 7:"b", 3:"e", 11:"z", 21:"o"}`, calculate the sum of keys whose values are vowels.

💡 **Approach:**
Used a generator expression with `sum()` to filter key-value pairs where values are in a set of vowels.

---

#### 2️⃣ `ques2.py` – Second Highest in a List

🔍 **Problem:**
Find the second highest number in a list like `ls = [72, 35, 83]` without using built-in methods like `sort()`.

💡 **Approach:**
Iterated through the list using a single pass, maintaining `first` and `second` max variables for efficiency.

---

#### 3️⃣ `ques3.py` – Longest Common Prefix

🔍 **Problem:**
Given `strs = ["flower", "flow", "flight"]`, determine the longest common prefix.

💡 **Approach:**
Iteratively reduced the prefix string using `startswith()` until all strings shared the same starting substring.

---

### 🔹 Round 2

#### 4️⃣ `round2_ques1.py` – Reverse Dictionary Values

🔍 **Problem:**
Given a dictionary like:

```python
intro = {'name': 'Nitin', 'phone': 9137887, 'City': 'Pune'}
```

Transform the dictionary such that each value is reversed. For strings, reverse the string; for integers, convert to string, reverse, then cast back to integer.

📥 **Expected Output:**

```python
{'name': 'nitiN', 'phone': 7887319, 'City': 'enuP'}
```

💡 **Approach:**

* Wrote a helper function `reverse_string()` using a loop.
* Applied this function conditionally on values, converting integers to strings before reversing.
* Constructed a new dictionary with reversed values.

---

## ⚙️ Running the Scripts

You can execute each file using Python 3:

```bash
python Round1/ques1.py
python Round1/ques2.py
python Round1/ques3.py
python Round2/round2_ques1.py
```

---

## Interviee

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)

