# Own (v1.0)

**Own** is a minimalist, ultra-lightweight (~53 KB) interpreted scripting language designed for CLI automation. Built with Python and the Lark parser, Own features a clean, straight-to-the-point syntax that is easy to read and write.

## Key Features (v1.0)

* **Ultra-Lightweight**: Minimalist flat architecture with zero bloatware.
* **Native CLI Integration**: Directly access terminal arguments using the `@` symbol (`@1`, `@2`, etc.).
* **Strict File Execution**: Exclusively executes `.own` files, supporting both single-file (default) and multi-file (`-mf`) modes.
* **Rich Data Types**: Supports *Number*, *String*, *Boolean* (`true`, `false`), `null`, *Array*, and *Object/Dictionary*.
* **Control Flow & Modularity**: Equipped with `if`, `for`, `break`, `continue`, `return`, and an `import` system for external `.own` files/packages.

## Installation & Setup

### Prerequisites

* Python 3.8+
* `lark` library

```bash
pip install lark
```

## Running Scripts

1. **Single-File Mode (Default):**
   ```bash
   own examples/test.own
   ```

2. **Multi-File Mode (`-mf`):**
   Execute multiple `.own` files sequentially within the same shared environment:
   ```bash
   own -mf file1.own file2.own
   ```

3. **Passing CLI Arguments:**
   ```bash
   own examples/test.own hello world
   ```

## Syntax Documentation

### 1. Output (`echo`)

Prints text or variable values to the terminal. Supports multiple comma-separated expressions.

```own
echo "Hello, World!"
echo "Result:", 10 + 20
```

### 2. Variables & Data Types (`let`)

Declare variables using the `let` keyword.

```own
let name = "Own"
let version = 1.0
let active = true
let empty = null
```

### 3. Arrays & Objects

Supports 0-based indexing for arrays and dot notation (`.`) for accessing or modifying object properties.

```own
// Array
let numbers = [10, 20, 30]
echo numbers[0] // Output: 10

// Object
let user = { name: "Pypix", role: "Creator" }
echo user.name // Output: Pypix
user.role = "Admin"
```

### 4. CLI Arguments (`@`)

Capture arguments passed from the terminal when executing a script.

```own
// Executed with: own test.own hello
// @0 refers to the script name (test.own), @1 refers to the first argument
echo "First argument:", @1
```

### 5. Math & Logical Operators

* **Arithmetic**: `+`, `-`, `*`, `/`, `^` (exponentiation)
* **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, `^=`
* **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
* **Logical**: `&&` (AND), `||` (OR), `!` (NOT)

### 6. Conditionals (`if`)

```own
let score = 85

if score >= 80 {
    echo "Passed with distinction"
}
```

### 7. Loops (`for`, `break`, `continue`)

Full control over loop execution using `break` to exit the loop early and `continue` to skip the current iteration.

```own
for i in [1, 2, 3, 4, 5] {
    if i == 2 {
        continue
    }
    if i == 4 {
        break
    }
    echo i
}
// Output: 1, 3
```

### 8. Modularity (`import` & `return`)

Import external `.own` packages or modules into your active script.

```own
import math
```

## Roadmap (Next Update)

* [ ] Custom function declarations (`func`)
* [ ] String interpolation (`${variable}`)
* [ ] Expanded built-in standard library

## Notes

Don't forget to set up a global alias or wrapper so you can run `own` directly from your terminal:

**Linux / macOS (`.bashrc` or `.zshrc`):**
```bash
alias own="python3 /path/to/main.py"
```

**Windows (`own.bat`):**
```bat
@echo off
python "C:\path\to\main.py" %*
```