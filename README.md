<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Transpiler</title>
</head>

<body>

    <h1>Simple Transpiler Written In Python</h1>

    <h2>Introduction</h2>
    <p>This is a simple transpiler written in Python by Luiz Gabriel Magalhães Trindade. The purpose of this transpiler
        is to convert a custom programming language into C code, which can then be compiled into an executable using a C
        compiler.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Print Statements:</strong> Use the <code>print</code> statement to display content on the console.
        </li>
        <li><strong>Variable Declaration:</strong> Declare variables with the <code>number</code> and
            <code>string</code> statements.</li>
        <li><strong>Variable View:</strong> View the value of a variable using the <code>view</code> statement.</li>
        <li><strong>Math Operations:</strong> Perform basic mathematical operations with the <code>math</code>
            statement.</li>
        <li><strong>System Commands:</strong> Execute system commands using the <code>SYSTEM</code> statement.</li>
        <li><strong>Control Flow:</strong> Use labels (<code>section</code> and <code>goto</code>) to control the flow of
            the program.</li>
        <li><strong>Program Termination:</strong> Use the <code>end</code> statement to terminate the program.</li>
    </ul>

    <h2>License</h2>
    <p>Distributed under the <a href="https://www.gnu.org/licenses/gpl-3.0.en.html#license-text">GPL3 License</a>.</p>

    <h2>Usage</h2>
    <ol>
        <li>Save your code in a file with the custom programming language syntax.</li>
        <li>Run the transpiler using the command: <code>python3 transpiler.py your_program_file</code></li>
    </ol>

    <h2>Example</h2>
    <p>Here is a sample program in the custom language:</p>

    <pre>
<code>
print Hello, World!
number x 5
string greeting Hello from the transpiler
view x
view greeting
math 3.5 + 2.7 result
print The result is: result
end
</code>
    </pre>

    <p>After transpiling and compiling, you can run the generated executable to see the output.</p>

    <h2>How to Run</h2>
    <p>Ensure you have a C compiler installed (tcc or gcc) before running the transpiler.</p>

    <pre>
<code>
python3 transpiler.py your_program_file
./your_program_file_exec
</code>
    </pre>

    <h2>Notes</h2>
    <ul>
        <li>This transpiler is a basic example and may not cover all language features.</li>
        <li>Error handling is minimal; unexpected input may lead to undefined behavior.</li>
        <li>Be cautious when using the <code>SYSTEM</code> statement, as it executes system commands directly.</li>
    </ul>

    <p>Feel free to explore, modify, and extend this transpiler for educational purposes or as a starting point for
        building more sophisticated transpilers.</p>

</body>

</html>
