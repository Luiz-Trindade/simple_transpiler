# Simple Transpiler Written In Python.

## Introduction
This is a simple transpiler written in Python by Luiz Gabriel Magalhães Trindade. The purpose of this transpiler is to convert a custom programming language into C code, which can then be compiled into an executable using a C compiler.

## Features
- **Print Statements:** Use the `print` statement to display content on the console.
- **Variable Declaration:** Declare variables with the `number` and `string` statements.
- **Variable View:** View the value of a variable using the `view` statement.
- **Math Operations:** Perform basic mathematical operations with the `math` statement.
- **System Commands:** Execute system commands using the `SYSTEM` statement.
- **Control Flow:** Use labels (`section` and `goto`) to control the flow of the program.
- **Program Termination:** Use the `end` statement to terminate the program.

## License
Distributed under the [GPL3 License](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text).

## Usage
1. Save your code in a file with the custom programming language syntax.
2. Run the transpiler using the command: `python3 transpiler.py your_program_file`

## Example
Here is a sample program in the custom language:

```python
print Hello, World!
number x 5
string greeting Hello from the transpiler
view x
view greeting
math 3.5 + 2.7 result
print The result is: result
end
