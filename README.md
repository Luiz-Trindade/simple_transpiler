<image src="https://www.gnu.org/graphics/gplv3-127x51.png">

# Simple Transpiler Written In Python.

## Introduction
This is a simple transpiler written in Python by Luiz Gabriel Magalhães Trindade. The purpose of this transpiler is to convert a custom programming language into C code, which can then be compiled into an executable using a C compiler.

## Features
- **Print Statements:** Use the `print` statement to display content on the console.
- **Variable Declaration:** Declare variables with the `number` and `string` statements.
- **Variable View:** View the value of a variable using the `view` statement.
- **Keyboard Input Data** Use the `input` command to recieve keyboard data.
- **Math Operations:** Perform basic mathematical operations with the `math` statement.
- **System Commands:** Execute system commands using the `SYSTEM` statement.
- **Control Flow:** Use labels (`section` and `goto`) to control the flow of the program.
- **Control Time Sleep:** Use `sleep` for waiting.
- **Program Termination:** Use the `end` statement to terminate the program.

## License
Distributed under the [GPL3 License](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text).

## Usage
1. Save your code in a file with the custom programming language syntax.
2. Run the transpiler using the command: `python3 simple_transpiler.py your_program_file`

## Examples
1. Here is a sample program in the custom language:

```python
print Hello, World!

number x 5
number n1 3.5
number n2 2.7
number result 0

string greeting Hello from the transpiler

newline
view x
newline
view greeting
newline

math n1 + n2 result

print The result is:
view result
newline
```
2. Here is a simple counter that counts from 1 to 999999:

```python
number init 0
number inc 1
number goal 999999

newline

section soma
math init + inc init
view init

newline

comp init == goal final
goto soma

section final
print Fim!
newline
```
