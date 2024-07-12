
# OWASP Web Testing Guide

This Python script allows you to interactively explore various test cases from the OWASP Testing Guide. You can select categories, view specific test cases, and see detailed instructions for each test case.

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
    git clone https://github.com/Sic4rio/owasp-web-testing-guide.git
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

Do what you like tothis script. Feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

All rights go to my dog.

