# ACE Selection Task README

## Table of Contents
1. [Introduction](#introduction)
2. [Task Description](#task-description)
3. [Input Format](#input-format)
4. [Output Format](#output-format)
5. [Evaluation Criteria](#evaluation-criteria)
6. [Setup Instructions](#setup-instructions)
7. [Execution Instructions](#execution-instructions)
8. [Examples](#examples)
9. [Troubleshooting](#troubleshooting)

## Introduction
The ACE (Association of Computer Enthusiasts) club organizes various activities and tasks to engage its members and promote learning and collaboration in the field of computer science. This README provides detailed instructions on how to understand, set up, and execute the ACE selection task.

## Task Description
The ACE selection task is designed to help the club select the most appropriate options for different scenarios, such as project assignments, event planning, or resource allocation. Each option has a set of attributes, and the selection criteria are based on these attributes. The goal is to make informed decisions that reflect the club's objectives and member preferences.

## Input Format
The input for the ACE selection task includes:
- A list of options, where each option is represented by a dictionary of attributes.
- Selection criteria, which outline the rules or preferences for choosing the best option(s).

### Example
```json
{
  "options": [
    {"id": 1, "name": "Project A", "difficulty": 3, "interest": 5},
    {"id": 2, "name": "Project B", "difficulty": 2, "interest": 7},
    {"id": 3, "name": "Project C", "difficulty": 4, "interest": 6}
  ],
  "criteria": {
    "difficulty": "min",
    "interest": "max"
  }
}
```

## Output Format
The output should be a list of selected options that best meet the given criteria.

### Example
```json
{
  "selected_options": [
    {"id": 2, "name": "Project B", "difficulty": 2, "interest": 7}
  ]
}
```

## Evaluation Criteria
The selection of options will be evaluated based on:
- Adherence to the given selection criteria.
- Accuracy in identifying the best options.
- Justification for the selections made.

## Setup Instructions
1. Ensure you have a Python environment set up on your machine.
2. Install any required libraries (e.g., pandas, numpy) using pip:
   ```sh
   pip install pandas numpy
   ```

## Execution Instructions
1. Prepare your input data in the specified format.
2. Run the script to process the input and generate the output.
3. Review the output to ensure it meets the selection criteria.

### Script Example
```python
import json

def select_options(data):
    options = data['options']
    criteria = data['criteria']
    
    # Example selection logic based on criteria
    selected = []
    if criteria.get('difficulty') == 'min':
        min_difficulty = min(options, key=lambda x: x['difficulty'])
        selected.append(min_difficulty)
    if criteria.get('interest') == 'max':
        max_interest = max(options, key=lambda x: x['interest'])
        selected.append(max_interest)
    
    return {"selected_options": selected}

# Load input data
with open('input.json') as f:
    data = json.load(f)

# Select options
result = select_options(data)

# Save output data
with open('output.json', 'w') as f:
    json.dump(result, f, indent=4)
```

## Examples
Refer to the [Input Format](#input-format) and [Output Format](#output-format) sections for examples of the input and output JSON structures.

## Troubleshooting
- **Issue:** Incorrect options selected.
  - **Solution:** Ensure the selection logic correctly implements the criteria specified in the input.
- **Issue:** Script errors.
  - **Solution:** Check for syntax errors or missing dependencies. Ensure all required libraries are installed.
