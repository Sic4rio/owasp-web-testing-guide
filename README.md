
# OWASP Web Testing Guide

This Python script allows you to interactively explore and execute various test cases from the OWASP Testing Guide. You can select categories, view specific test cases, and see detailed instructions for each test case.

## Features

- Interactive menu to select test categories and test cases
- Option to print all test cases within a category
- Detailed instructions for each test case
- Colorful output for enhanced readability

## Prerequisites

- Python 3.x
- `colorama` library for colorful terminal output
- `readline` library for enhanced input handling (included in Python standard library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/owasp-web-testing-guide.git
    cd owasp-web-testing-guide
    ```

2. Install the `colorama` library:
    ```sh
    pip install colorama
    ```

## Usage

Run the script using Python:
```sh
python owasp.py
```

## Script Overview

### Main Functions

- **print_banner()**: Prints the banner at the start of the script.
- **print_categories()**: Prints available test categories.
- **print_test_cases(category)**: Prints available test cases within a selected category.
- **print_all_instructions(category)**: Prints all test cases and their instructions within a selected category.
- **print_instructions(test_case)**: Prints instructions for a selected test case.
- **main()**: Main function to run the interactive menu.

### How It Works

1. **Banner**: Displays a welcome banner.
2. **Categories**: Lists all available test categories.
3. **Category Selection**: Prompts the user to select a category.
4. **Test Case Selection**: Prompts the user to select a test case or print all test cases with instructions.
5. **Instructions**: Displays detailed instructions for the selected test case or all test cases within the category.

## Example Output

```
╔═╗╦ ╦╔═╗╔═╗╔═╗  ╔╦╗┌─┐┌─┐┌┬┐  ╔═╗┬ ┬┬┌┬┐┌─┐
║ ║║║║╠═╣╚═╗╠═╝   ║ ├┤ └─┐ │   ║ ╦│ ││ ││├┤ 
╚═╝╚╩╝╩ ╩╚═╝╩     ╩ └─┘└─┘ ┴   ╚═╝└─┘┴─┴┘└─┘

OWASP Test Cases
Available categories:
[1] Information Gathering
[2] Configuration Management Testing
[3] Authentication Testing
[4] Authorization Testing
[5] Session Management Testing
[6] Input Validation Testing
[7] Error Handling
[8] Cryptography
[9] Client Side Testing

Select a category (or type 'exit' to quit): 1
Available test cases in 'Information Gathering':
[1] OTG-INFO-001: Conduct Search Engine Discovery and Reconnaissance for Information Leakage
[2] OTG-INFO-002: Fingerprint Web Server
...
[0] Print all test cases with instructions

Select a test case (or type '0' to print all): 2
Instructions for 'OTG-INFO-002: Fingerprint Web Server':
1. Use tools like Nmap to identify the web server.
2. Analyze server banners and headers.
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
