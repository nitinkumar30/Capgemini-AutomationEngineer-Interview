# 💼 Capgemini Technical Interview – Round 1

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/nitinkumar30/Capgemini-AutomationEngineer-Interview/test.yml?label=GitHub%20Actions&logo=github)
![Latest Commit](https://img.shields.io/github/last-commit/nitinkumar30/Capgemini-AutomationEngineer-Interview?color=green)
![Interview Round](https://img.shields.io/badge/Interview-Round%201-orange)


Welcome! 👋  
This repository contains the solutions to Python-based coding questions asked during my **1st Technical Interview Round** with **Capgemini**, held on 🗓️ *May 6, 2025*.

---

## 🧠 Interview Overview

- ⏰ **Duration:** 30 minutes  
- 🧪 **Type:** Technical Interview  
- 💬 **Topics Covered:**  
  - Python programming 🐍  
  - API Testing (discussed, but not coded)  
  - Focus on logic building and implementation  
  - Real-time code explanation and reasoning  


---

## 📌 Problem Statements & Solutions

### 1️⃣ `ques1.py` – Sum Keys Based on Vowel Values

🔍 **Task:**  
Given a dictionary `D = {1:"a", 7:"b", 3:"e", 11:"z", 21:"o"}`, find the **sum of keys** whose corresponding **values are vowels** (a, e, i, o, u).

💡 **Logic Used:**  
Used a generator expression with `sum()` to iterate over key-value pairs and filter based on vowel values.

---

### 2️⃣ `ques2.py` – Second Highest in a List

🔍 **Task:**  
Given a list `ls = [72, 35, 83]`, find the **second highest number** without using built-in functions like `sort()`.

💡 **Logic Used:**  
Maintained `first` and `second` highest values using a single loop for optimal time complexity.

---

### 3️⃣ `ques3.py` – Longest Common Prefix

🔍 **Task:**  
Given `strs = ["flower", "flow", "flight"]`, find the **longest common prefix** among them.

💡 **Logic Used:**  
Used `startswith()` in a loop to reduce the prefix until all strings match the prefix.

---

## ⚙️ Running the Scripts

You can run each file individually using Python 3:

```bash
python Round1/ques1.py
python Round1/ques2.py
python Round1/ques3.py
