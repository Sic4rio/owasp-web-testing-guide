import colorama
from colorama import Fore, Style
import readline

colorama.init(autoreset=True)

# List of OWASP test cases (This is a simplified example. You should refer to the official OWASP Testing Guide for a complete list.)
owasp_test_cases = {
    "Information Gathering": [
        "OTG-INFO-001: Conduct Search Engine Discovery and Reconnaissance for Information Leakage",
        "OTG-INFO-002: Fingerprint Web Server",
        "OTG-INFO-003: Review Webserver Metafiles for Information Leakage",
        "OTG-INFO-004: Enumerate Applications on Webserver",
        "OTG-INFO-005: Review Webpage Content for Information Leakage",
        "OTG-INFO-006: Identify Application Entry Points",
        "OTG-INFO-007: Map Execution Paths Through Application",
        "OTG-INFO-008: Fingerprint Web Application Framework",
        "OTG-INFO-009: Fingerprint Web Application"
    ],
    "Configuration Management Testing": [
        "OTG-CONFIG-001: Test Network/Infrastructure Configuration",
        "OTG-CONFIG-002: Test Application Platform Configuration",
        "OTG-CONFIG-003: Test File Extensions Handling for Sensitive Information",
        "OTG-CONFIG-004: Review Old, Backup, and Unreferenced Files for Sensitive Information",
        "OTG-CONFIG-005: Enumerate Infrastructure and Application Admin Interfaces",
        "OTG-CONFIG-006: Test HTTP Methods",
        "OTG-CONFIG-007: Test HTTP Strict Transport Security",
        "OTG-CONFIG-008: Test RIA Cross Domain Policy"
    ],
    "Authentication Testing": [
        "OTG-AUTHN-001: Testing for Credentials Transported over an Encrypted Channel",
        "OTG-AUTHN-002: Testing for Default Credentials",
        "OTG-AUTHN-003: Testing for Weak lock out mechanism",
        "OTG-AUTHN-004: Testing for Bypassing Authentication Schema",
        "OTG-AUTHN-005: Test Remember Password Functionality",
        "OTG-AUTHN-006: Testing for Browser Cache Weaknesses",
        "OTG-AUTHN-007: Testing for Weak Password Policy",
        "OTG-AUTHN-008: Testing for Weak Security Question Answer",
        "OTG-AUTHN-009: Testing for Weak Password Change or Reset Functionalities",
        "OTG-AUTHN-010: Testing for Weaker Authentication in Alternative Channel"
    ],
    "Authorization Testing": [
        "OTG-AUTHZ-001: Testing Directory Traversal File Include",
        "OTG-AUTHZ-002: Testing for Bypassing Authorization Schema",
        "OTG-AUTHZ-003: Testing for Privilege Escalation",
        "OTG-AUTHZ-004: Testing for Insecure Direct Object References"
    ],
    "Session Management Testing": [
        "OTG-SESS-001: Testing for Session Management Schema",
        "OTG-SESS-002: Testing for Cookies Attributes",
        "OTG-SESS-003: Testing for Session Fixation",
        "OTG-SESS-004: Testing for Exposed Session Variables",
        "OTG-SESS-005: Testing for Cross Site Request Forgery",
        "OTG-SESS-006: Testing for Logout Functionality",
        "OTG-SESS-007: Test Session Timeout",
        "OTG-SESS-008: Testing for Session Puzzling",
        "OTG-SESS-009: Testing for One Session Limit",
        "OTG-SESS-010: Testing for Session Hijacking"
    ],
    "Input Validation Testing": [
        "OTG-INPUT-001: Testing for Reflected Cross Site Scripting",
        "OTG-INPUT-002: Testing for Stored Cross Site Scripting",
        "OTG-INPUT-003: Testing for DOM-based Cross Site Scripting",
        "OTG-INPUT-004: Testing for Cross Site Flashing",
        "OTG-INPUT-005: SQL Injection",
        "OTG-INPUT-006: Testing for LDAP Injection",
        "OTG-INPUT-007: Testing for ORM Injection",
        "OTG-INPUT-008: Testing for XML Injection",
        "OTG-INPUT-009: Testing for SSI Injection",
        "OTG-INPUT-010: Testing for XPath Injection",
        "OTG-INPUT-011: IMAP/SMTP Injection",
        "OTG-INPUT-012: Testing for Code Injection",
        "OTG-INPUT-013: Testing for Command Injection",
        "OTG-INPUT-014: Testing for Buffer overflow",
        "OTG-INPUT-015: Testing for Incubated Vulnerability",
        "OTG-INPUT-016: Testing for HTTP Splitting/Smuggling",
        "OTG-INPUT-017: Testing for HTTP Verb Tampering",
        "OTG-INPUT-018: Testing for HTTP Parameter Pollution"
    ],
    "Error Handling": [
        "OTG-ERROR-001: Analysis of Error Codes",
        "OTG-ERROR-002: Analysis of Stack Traces"
    ],
    "Cryptography": [
        "OTG-CRYPST-001: Testing for Weak SSL/TLS Ciphers, Insufficient Transport Layer Protection",
        "OTG-CRYPST-002: Testing for Padding Oracle",
        "OTG-CRYPST-003: Testing for Sensitive information sent via unencrypted channels",
        "OTG-CRYPST-004: Testing for Weak Encryption",
        "OTG-CRYPST-005: Testing for Insecure TLS Renegotiation",
        "OTG-CRYPST-006: Testing for Sensitive Information Exposed in URL"
    ],
    "Client Side Testing": [
        "OTG-CLIENT-001: Testing for DOM-based Cross Site Scripting",
        "OTG-CLIENT-002: Testing for JavaScript Execution",
        "OTG-CLIENT-003: Testing for HTML Injection",
        "OTG-CLIENT-004: Testing for CSS Injection",
        "OTG-CLIENT-005: Testing for Client Side URL Redirect",
        "OTG-CLIENT-006: Testing for Client Side Resource Manipulation",
        "OTG-CLIENT-007: Test Cross Origin Resource Sharing",
        "OTG-CLIENT-008: Testing for Cross Site Flashing",
        "OTG-CLIENT-009: Testing for Clickjacking",
        "OTG-CLIENT-010: Testing WebSockets",
        "OTG-CLIENT-011: Testing Web Messaging",
        "OTG-CLIENT-012: Test Local Storage",
        "OTG-CLIENT-013: Test Cross Site Script Inclusion"
    ]
}

# Dictionary containing instructions for each test case
owasp_instructions = {
    "OTG-INFO-001": "1. Use search engines to find information related to the target. 2. Analyze results for sensitive information.",
    "OTG-INFO-002": "1. Use tools like Nmap to identify the web server. 2. Analyze server banners and headers.",
    "OTG-INFO-003": "1. Look for files like robots.txt and sitemap.xml. 2. Analyze these files for sensitive information.",
    "OTG-INFO-004": "1. Enumerate subdomains and directories. 2. Identify applications hosted on the web server.",
    "OTG-INFO-005": "1. Review the content of web pages. 2. Look for comments, hidden fields, and other information leakage.",
    "OTG-INFO-006": "1. Identify all possible entry points in the application. 2. Document these entry points for further testing.",
    "OTG-INFO-007": "1. Map the application's execution paths. 2. Identify potential areas for vulnerabilities.",
    "OTG-INFO-008": "1. Identify the web application framework in use. 2. Look for known vulnerabilities related to the framework.",
    "OTG-INFO-009": "1. Fingerprint the web application. 2. Analyze the application for known issues.",
    "OTG-CONFIG-001": "1. Analyze network and infrastructure configuration. 2. Identify misconfigurations and security weaknesses.",
    "OTG-CONFIG-002": "1. Review the application platform configuration. 2. Ensure that security best practices are followed.",
    "OTG-CONFIG-003": "1. Test how the server handles different file extensions. 2. Look for sensitive information exposure.",
    "OTG-CONFIG-004": "1. Review old, backup, and unreferenced files. 2. Ensure that no sensitive information is exposed.",
    "OTG-CONFIG-005": "1. Enumerate admin interfaces. 2. Check for secure access controls.",
    "OTG-CONFIG-006": "1. Test HTTP methods supported by the server. 2. Ensure that only necessary methods are allowed.",
    "OTG-CONFIG-007": "1. Check if HTTP Strict Transport Security (HSTS) is implemented. 2. Ensure that all communications are secure.",
    "OTG-CONFIG-008": "1. Test RIA cross-domain policy files. 2. Ensure that they are securely configured.",
    "OTG-AUTHN-001": "1. Check if credentials are transmitted over encrypted channels. 2. Ensure that secure protocols are used.",
    "OTG-AUTHN-002": "1. Test for default credentials. 2. Ensure that all default credentials are changed.",
    "OTG-AUTHN-003": "1. Test for weak lockout mechanisms. 2. Ensure that proper lockout policies are in place.",
    "OTG-AUTHN-004": "1. Test for ways to bypass authentication. 2. Ensure that all authentication mechanisms are secure.",
    "OTG-AUTHN-005": "1. Test the 'Remember Password' functionality. 2. Ensure that it is implemented securely.",
    "OTG-AUTHN-006": "1. Test for browser cache weaknesses. 2. Ensure that sensitive information is not cached.",
    "OTG-AUTHN-007": "1. Test for weak password policies. 2. Ensure that strong password policies are enforced.",
    "OTG-AUTHN-008": "1. Test for weak security question answers. 2. Ensure that security questions are strong and secure.",
    "OTG-AUTHN-009": "1. Test for weak password change/reset functionalities. 2. Ensure that these functionalities are secure.",
    "OTG-AUTHN-010": "1. Test for weaker authentication in alternative channels. 2. Ensure that all authentication channels are secure.",
    "OTG-AUTHZ-001": "1. Test for directory traversal vulnerabilities. 2. Ensure that file access is properly restricted.",
    "OTG-AUTHZ-002": "1. Test for ways to bypass authorization. 2. Ensure that proper authorization controls are in place.",
    "OTG-AUTHZ-003": "1. Test for privilege escalation vulnerabilities. 2. Ensure that users cannot escalate privileges.",
    "OTG-AUTHZ-004": "1. Test for insecure direct object references. 2. Ensure that object references are properly secured.",
    "OTG-SESS-001": "1. Test the session management schema. 2. Ensure that sessions are managed securely.",
    "OTG-SESS-002": "1. Test for secure cookie attributes. 2. Ensure that cookies are configured securely.",
    "OTG-SESS-003": "1. Test for session fixation vulnerabilities. 2. Ensure that sessions cannot be fixed.",
    "OTG-SESS-004": "1. Test for exposed session variables. 2. Ensure that session variables are not exposed.",
    "OTG-SESS-005": "1. Test for cross-site request forgery (CSRF) vulnerabilities. 2. Ensure that CSRF protections are in place.",
    "OTG-SESS-006": "1. Test the logout functionality. 2. Ensure that it works properly.",
    "OTG-SESS-007": "1. Test session timeout functionality. 2. Ensure that sessions time out appropriately.",
    "OTG-SESS-008": "1. Test for session puzzling vulnerabilities. 2. Ensure that sessions are managed properly.",
    "OTG-SESS-009": "1. Test for single session enforcement. 2. Ensure that only one session per user is allowed.",
    "OTG-SESS-010": "1. Test for session hijacking vulnerabilities. 2. Ensure that sessions cannot be hijacked.",
    "OTG-INPUT-001": "1. Test for reflected cross-site scripting (XSS) vulnerabilities. 2. Ensure that inputs are properly sanitized.",
    "OTG-INPUT-002": "1. Test for stored cross-site scripting (XSS) vulnerabilities. 2. Ensure that stored inputs are properly sanitized.",
    "OTG-INPUT-003": "1. Test for DOM-based cross-site scripting (XSS) vulnerabilities. 2. Ensure that the DOM is properly sanitized.",
    "OTG-INPUT-004": "1. Test for cross-site flashing vulnerabilities. 2. Ensure that flash content is properly secured.",
    "OTG-INPUT-005": "1. Test for SQL injection vulnerabilities. 2. Ensure that SQL queries are properly sanitized.",
    "OTG-INPUT-006": "1. Test for LDAP injection vulnerabilities. 2. Ensure that LDAP queries are properly sanitized.",
    "OTG-INPUT-007": "1. Test for ORM injection vulnerabilities. 2. Ensure that ORM queries are properly sanitized.",
    "OTG-INPUT-008": "1. Test for XML injection vulnerabilities. 2. Ensure that XML data is properly sanitized.",
    "OTG-INPUT-009": "1. Test for SSI injection vulnerabilities. 2. Ensure that SSI commands are properly sanitized.",
    "OTG-INPUT-010": "1. Test for XPath injection vulnerabilities. 2. Ensure that XPath queries are properly sanitized.",
    "OTG-INPUT-011": "1. Test for IMAP/SMTP injection vulnerabilities. 2. Ensure that email commands are properly sanitized.",
    "OTG-INPUT-012": "1. Test for code injection vulnerabilities. 2. Ensure that code inputs are properly sanitized.",
    "OTG-INPUT-013": "1. Test for command injection vulnerabilities. 2. Ensure that command inputs are properly sanitized.",
    "OTG-INPUT-014": "1. Test for buffer overflow vulnerabilities. 2. Ensure that input lengths are properly validated.",
    "OTG-INPUT-015": "1. Test for incubated vulnerabilities. 2. Ensure that potential vulnerabilities are identified early.",
    "OTG-INPUT-016": "1. Test for HTTP splitting/smuggling vulnerabilities. 2. Ensure that HTTP headers are properly handled.",
    "OTG-INPUT-017": "1. Test for HTTP verb tampering vulnerabilities. 2. Ensure that HTTP methods are properly restricted.",
    "OTG-INPUT-018": "1. Test for HTTP parameter pollution vulnerabilities. 2. Ensure that HTTP parameters are properly handled.",
    "OTG-ERROR-001": "1. Analyze error codes returned by the application. 2. Ensure that detailed error information is not exposed.",
    "OTG-ERROR-002": "1. Analyze stack traces returned by the application. 2. Ensure that stack traces are not exposed.",
    "OTG-CRYPST-001": "1. Test for weak SSL/TLS ciphers. 2. Ensure that strong ciphers are used.",
    "OTG-CRYPST-002": "1. Test for padding oracle vulnerabilities. 2. Ensure that padding is handled securely.",
    "OTG-CRYPST-003": "1. Test for sensitive information sent via unencrypted channels. 2. Ensure that all sensitive information is encrypted.",
    "OTG-CRYPST-004": "1. Test for weak encryption algorithms. 2. Ensure that strong encryption algorithms are used.",
    "OTG-CRYPST-005": "1. Test for insecure TLS renegotiation. 2. Ensure that TLS renegotiation is secure.",
    "OTG-CRYPST-006": "1. Test for sensitive information exposed in URLs. 2. Ensure that sensitive information is not included in URLs.",
    "OTG-CLIENT-001": "1. Test for DOM-based cross-site scripting (XSS) vulnerabilities. 2. Ensure that the DOM is properly sanitized.",
    "OTG-CLIENT-002": "1. Test for JavaScript execution vulnerabilities. 2. Ensure that JavaScript is properly sanitized.",
    "OTG-CLIENT-003": "1. Test for HTML injection vulnerabilities. 2. Ensure that HTML inputs are properly sanitized.",
    "OTG-CLIENT-004": "1. Test for CSS injection vulnerabilities. 2. Ensure that CSS inputs are properly sanitized.",
    "OTG-CLIENT-005": "1. Test for client-side URL redirect vulnerabilities. 2. Ensure that URL redirects are properly handled.",
    "OTG-CLIENT-006": "1. Test for client-side resource manipulation vulnerabilities. 2. Ensure that client-side resources are properly protected.",
    "OTG-CLIENT-007": "1. Test cross-origin resource sharing (CORS) policies. 2. Ensure that CORS policies are securely configured.",
    "OTG-CLIENT-008": "1. Test for cross-site flashing vulnerabilities. 2. Ensure that flash content is properly secured.",
    "OTG-CLIENT-009": "1. Test for clickjacking vulnerabilities. 2. Ensure that clickjacking protections are in place.",
    "OTG-CLIENT-010": "1. Test WebSockets for vulnerabilities. 2. Ensure that WebSockets are properly secured.",
    "OTG-CLIENT-011": "1. Test web messaging for vulnerabilities. 2. Ensure that web messaging is properly secured.",
    "OTG-CLIENT-012": "1. Test local storage for vulnerabilities. 2. Ensure that local storage is properly secured.",
    "OTG-CLIENT-013": "1. Test for cross-site script inclusion vulnerabilities. 2. Ensure that scripts are properly included."
}

def print_banner():
    banner = f"""
{Fore.RED}{Style.BRIGHT}
╔═╗╦ ╦╔═╗╔═╗╔═╗  ╔╦╗┌─┐┌─┐┌┬┐  ╔═╗┬ ┬┬┌┬┐┌─┐
║ ║║║║╠═╣╚═╗╠═╝   ║ ├┤ └─┐ │   ║ ╦│ ││ ││├┤ 
╚═╝╚╩╝╩ ╩╚═╝╩     ╩ └─┘└─┘ ┴   ╚═╝└─┘┴─┴┘└─┘
	SICARIOS OWASP REFERENCE  
{Style.RESET_ALL}
    """
    print(banner)

def print_categories():
    print(f"{Fore.GREEN}Available categories:{Style.RESET_ALL}")
    for idx, category in enumerate(owasp_test_cases.keys(), 1):
        print(f"{Fore.BLUE}[{idx}] {category}{Style.RESET_ALL}")

def print_test_cases(category):
    print(f"{Fore.GREEN}Available test cases in '{category}':{Style.RESET_ALL}")
    for idx, test_case in enumerate(owasp_test_cases[category], 1):
        print(f"{Fore.YELLOW}[{idx}] {test_case}{Style.RESET_ALL}")

def print_all_instructions(category):
    print(f"{Fore.GREEN}All test cases in '{category}' with instructions:{Style.RESET_ALL}")
    for test_case in owasp_test_cases[category]:
        print(f"{Fore.YELLOW}{test_case}{Style.RESET_ALL}")
        instructions = owasp_instructions.get(test_case.split(":")[0], "Instructions not available.")
        print(f"{Fore.CYAN}Instructions: {instructions}{Style.RESET_ALL}\n")

def print_instructions(test_case):
    instructions = owasp_instructions.get(test_case.split(":")[0], "Instructions not available.")
    print(f"{Fore.CYAN}Instructions for '{test_case}':\n{instructions}{Style.RESET_ALL}")

def main():
    print_banner()
    while True:
        print(f"\n{Fore.GREEN}OWASP Test Cases{Style.RESET_ALL}")
        print_categories()
        category_index = input(f"{Fore.MAGENTA}Select a category (or type 'exit' to quit): {Style.RESET_ALL}")
        
        if category_index.lower() == 'exit':
            break
        
        try:
            category_index = int(category_index) - 1
            category = list(owasp_test_cases.keys())[category_index]
        except (ValueError, IndexError):
            print(f"{Fore.RED}Invalid category. Please try again.{Style.RESET_ALL}")
            continue
        
        print_test_cases(category)
        print(f"{Fore.YELLOW}[0] Print all test cases with instructions{Style.RESET_ALL}")
        test_case_index = input(f"{Fore.MAGENTA}Select a test case (or type '0' to print all): {Style.RESET_ALL}")
        
        if test_case_index == '0':
            print_all_instructions(category)
        else:
            try:
                test_case_index = int(test_case_index) - 1
                test_case = owasp_test_cases[category][test_case_index]
            except (ValueError, IndexError):
                print(f"{Fore.RED}Invalid test case. Please try again.{Style.RESET_ALL}")
                continue
            
            print_instructions(test_case)

if __name__ == "__main__":
    main()

