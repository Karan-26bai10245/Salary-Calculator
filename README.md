# Salary Calculator

A simple, interactive command-line Python utility to calculate an employee's net salary. The script takes the basic salary as input, processes standard allowances and deductions, and generates a clean, formatted salary slip.

## Features

- **Interactive Prompts:** Takes employee name and basic salary via standard input.
- **Input Validation:** Implements `try-except` blocks to ensure only valid numeric inputs are accepted.
- **Automated Computation:** Instantly calculates HRA, DA, Income Tax, and Provident Fund based on predefined logic.
- **Formatted Output:** Generates a structured and easy-to-read salary slip directly in the terminal.

## Calculation Logic

The net salary is determined using the following percentages:
- **HRA (House Rent Allowance):** + 20% of Basic Salary
- **DA (Dearness Allowance):** + 10% of Basic Salary
- **Tax:** - 5% of Basic Salary
- **PF (Provident Fund):** - 12% of Basic Salary

**Formula:**
`Net Salary = Basic Salary + HRA + DA - Tax - PF`

## Prerequisites

- Python 3.x (No external libraries required)

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
