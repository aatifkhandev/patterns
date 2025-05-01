# 📘 Digit Extraction in Python

This README explains the concept of extracting individual digits from a number using Python. The method uses the **modulus `%`** and **integer division `/`** operators to extract digits from **right to left**.

---

## 🔍 Concept Overview

### ➕ Modulus Operator `%`

The **modulus operator** computes the remainder when a number is divided by another. It is useful for extracting the **last digit** of a number.

📌 Example:
```python
N = 7789
last_digit = N % 10  # Result: 9


import math

# Function to extract individual digits of a number
def extractDigits(N):
    ans = []  # Step 1: initialize an empty list

    # Step 2: extract digits
    while N > 0:
        lastDigit = N % 10
        ans.append(lastDigit)
        N = math.floor(N / 10)

    # Step 3: reverse the list to correct order
    ans.reverse()

    # Step 4: return the list of digits
    return ans



def main():
    N = 329823
    print("N:", N)
    digits = extractDigits(N)
    print("Extracted Digits:", end=" ")
    for num in digits:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()



| Iteration | Current N | N % 10 (`lastDigit`) | Updated N (floor(N / 10)) | ans (before reverse) |
|-----------|------------|----------------------|----------------------------|------------------------|
| 1         | 329823     | 3                    | 32982                      | [3]                    |
| 2         | 32982      | 2                    | 3298                       | [3, 2]                 |
| 3         | 3298       | 8                    | 329                        | [3, 2, 8]              |
| 4         | 329        | 9                    | 32                         | [3, 2, 8, 9]           |
| 5         | 32         | 2                    | 3                          | [3, 2, 8, 9, 2]        |
| 6         | 3          | 3                    | 0                          | [3, 2, 8, 9, 2, 3]     |





