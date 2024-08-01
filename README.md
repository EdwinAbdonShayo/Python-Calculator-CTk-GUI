## Python Calculator CTk (GUI)
Introduction
This project is a graphical user interface (GUI) calculator application built using the customtkinter library in Python. The calculator features both standard and programmer modes, offering functionalities for basic arithmetic operations, trigonometric calculations, and number system conversions (binary, decimal, hexadecimal, and octal).

Features
Standard Mode
Basic arithmetic operations: addition, subtraction, multiplication, and division.
Trigonometric functions: sine, cosine, tangent, arcsine, arccosine, and arctangent.
Square and square root calculations.
Percentage and plus/minus operations.
Clear and erase functions.
Switching between light and dark appearance modes.
Programmer Mode
Number system conversions: binary, decimal, hexadecimal, and octal.
Clear function.
Switching between standard and programmer modes.
Appearance mode options (light and dark).
Installation
To run this application, you'll need to have Python installed on your machine. You can install the required library customtkinter using pip:

bash
Copy code
pip install customtkinter
Usage
Run the script to open the calculator application. You can switch between standard and programmer modes using the respective buttons provided in the GUI.

Code Overview
The main parts of the code include:

Importing Libraries: Import necessary modules including customtkinter, math, and threading.

Creating the Main Window: Initialize the main application window with a title and fixed size.

Standard Mode Functions:

appearance: Function to change the appearance mode of the application.
clear: Function to clear all inputs.
erase: Function to clear the current input in the first entry box.
operation: Function to handle basic arithmetic operations.
equalize: Function to evaluate the arithmetic expressions.
trigonometric: Function to perform trigonometric calculations.
multiop: Function to handle percentage, square, and square root operations.
plus_min: Function to toggle the sign of the current input.
to_programmer: Function to switch to the programmer mode of the calculator.
button_click: Function to handle number button clicks.
Programmer Mode Functions:

appearance: Function to change the appearance mode of the application.
to_standard: Function to switch back to the standard mode.
clear: Function to clear all inputs.
conversion: Function to perform number system conversions.
opchange1 and opchange2: Functions to handle changes in the conversion options.
button_click: Function to handle number button clicks.
GUI Layout:

Standard mode layout with buttons for numbers, operations, and trigonometric functions.
Programmer mode layout with buttons for number system conversions and number buttons for hexadecimal inputs.
