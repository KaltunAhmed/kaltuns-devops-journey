## Difference Between `else` and `elif` in Bash

In Bash scripting, `else` and `elif` are used in conditional statements to control the flow of execution based on conditions. Here’s how they differ:

### `else`

- **Purpose:** The `else` keyword specifies a block of code that should be executed if none of the preceding `if` or `elif` conditions are true.
- **Placement:** `else` must follow an `if` or `elif` block and does not have a condition. It acts as a catch-all for any scenario that does not match the conditions specified before it.
- **Syntax:**

```bash
if [ condition ]; then
      # code to execute if condition is true
  else
      # code to execute if condition is false
  fi
```
- **Example:**

```bash
if [ $a -gt 10 ]; then
    echo "a is greater than 10"
else
    echo "a is 10 or less"
fi

```

### `elif`

- **Purpose:** The `elif` (short for "else if") keyword specifies additional conditions to test if the initial `if` condition is false. It allows for multiple conditional checks in a single `if` statement.
- **Placement:** `elif` must follow an `if` or another `elif` block and is followed by its own condition.
- **Syntax:**

```bash
if [ condition1 ]; then
    # code to execute if condition1 is true
elif [ condition2 ]; then
    # code to execute if condition2 is true
else
    # code to execute if neither condition1 nor condition2 is true
fi
```

- **Example:**

```bash
if [ $a -gt 10 ]; then
    echo "a is greater than 10"
elif [ $a -eq 10 ]; then
    echo "a is exactly 10"
else
    echo "a is less than 10"
fi
```

### Summary

- **`else`**: Used for a default action if all previous conditions fail. It does not require a condition.
- **`elif`**: Provides additional conditions to be checked if the preceding `if` or `elif` conditions are not met. It allows multiple conditional branches.
