Problem Statement : Detect Unsafe Pattern Matching :
Write the Python program to detect vulnerabilities in C, C++. For example, flag cases where user-controlled input is directly used in RegExp constructors without sanitization.
Note: Without sanitization was eventually removed from the question

Introduction

What are Format String Vulnerabilities?

Format string vulnerabilities occur when user input is improperly handled as a format string in functions like `printf`. This can lead to:

- Information leakage (e.g., memory contents).
- Unauthorized memory modification.
- Crashes or execution of arbitrary code.

Why Should You Care?

1. These vulnerabilities are easy to exploit but challenging to detect.
2. They exist in many programming languages (C, Java, JavaScript, etc.).
3. Learning to detect and fix them improves the security and reliability of code.

Understanding Format String Vulnerabilities

Safe Code Example

In safe code, format specifiers are explicitly defined and controlled by the developer:

```c
printf("Hello, %s", user_name);  // Safe usage
```

Vulnerable Code Example

In vulnerable code, user-controlled input is passed directly as the format string:

```c

printf(input);  // Dangerous if `input` is user-controlled
```

Exploitation Example

An attacker could provide a malicious format string to exploit vulnerabilities:

```c
// Attacker-controlled input
input = "%x %x %x %x";  // Dumps memory content
printf(input);  // Exploited function
```

Detecting Vulnerabilities with Parsers

Parsers analyze source code to identify patterns and potential vulnerabilities.

Python Parser for C Code

This parser scans for unsafe use of format specifiers like `%x`, `%p`, and `%n`.

Code

```python
import re

def detect_vulnerabilities(code):
    vulnerabilities = []

    Detect unsafe printf patterns
    pattern = r'printf\s*\(([^)]*)\)'
    matches = re.findall(pattern, code)

    for match in matches:
        if '%n' in match:
            vulnerabilities.append("Warning: Use of %n detected.")
        if '%x' in match:
            vulnerabilities.append("Warning: Use of %x detected.")
        if '%p' in match:
            vulnerabilities.append("Warning: Use of %p detected.")
    return vulnerabilities
```

Input

```c
printf("%n", &variable);
printf("%p", &pointer);
```

Output

```makefile
Warning: Use of %n detected.
Warning: Use of %p detected.1. Stack-Based Buffer Overruns
```

Language-Specific Examples

C Language

Vulnerable Code

```c
printf(user_input);  // Unsafe
```

Safe Code

```c
printf("%s", user_input);  // Safe
```

Java

Vulnerable Code

```java
System.out.printf(userInput);  // Unsafe
```

Safe Code

```java
System.out.printf("%s", userInput);  // Safe
```

JavaScript

Vulnerable Code

```jsx
console.log(userInput);  // Unsafe
```

Safe Code

```jsx
console.log("%s", userInput);  // Safe
```

Test Case Generation

Generating test cases ensures your vulnerability detection system works as expected.

Example: C Code Test Case

Input Code

```c
printf("%x", variable);
```

Expected Output

```makefile
Warning: Use of %x detected.
```

Test Case Implementation

```python
def test_vulnerability_detection():
    code = 'printf("%x", variable);'
    expected = ["Warning: Use of %x detected."]
    result = detect_vulnerabilities(code)
    assert result == expected
```

Fixing Vulnerabilities

Steps to Fix Format String Vulnerabilities

1. Avoid Dynamic Format Strings:
    - Replace `printf(user_input)` with `printf("%s", user_input)`.
2. Validate User Input:
    - Ensure user-provided strings do not include harmful specifiers.
3. Use Secure Functions:
    - Replace unsafe functions with safer alternatives like `snprintf`.

Exploit Payloads

Attackers often use specific payloads to exploit vulnerabilities:

- `%n`: Writes data to memory.
- `%p`: Prints memory addresses.
- `%x`: Dumps memory content.

Example