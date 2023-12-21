# Shelby - Information Processing and Utility Application

![SHELBY Logo](ipinfogen_logo.png)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=MdSagorMunshi.SHELBY)](https://github.com/MdSagorMunshi/SHELBY)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/MdSagorMunshi/GSHELBY)

Shelby is a versatile command-line tool that provides various functionalities for information processing and utility tasks. It's designed to be a handy Swiss Army knife for developers, system administrators, and anyone who needs quick access to a range of tools.

## Features

- **Check HTTP Status Code**: Verify the HTTP status code of a given URL.
- **Generate Password**: Create strong and random passwords.
- **Encrypt/Decrypt File**: Encrypt and decrypt files for added security.
- **Network Information Tool**: Retrieve information about the network, including IP addresses, hostname, open ports, and gateway. (Dependencies: `socket`, `os`)
- **GitHub Repository Analyzer**: Analyze GitHub repositories for key information like name, description, language, stars, forks, and last update. (Dependency: `github`)
- **System Resource Monitor**: Monitor CPU usage, memory usage, and disk usage. (Dependency: `psutil`)
- **Generate Random IPs**: Generate random IPv4 addresses. (Dependency: `Faker`)
- **Generate Random Proxies**: Generate random IPv4 proxy addresses. (Dependency: `Faker`)
- **Generate Random User-Agents**: Generate random user-agent strings. (Dependency: `fake-useragent`)
- **URL Shortener**: Shorten long URLs using the Bitly API. (Dependencies: `requests`)
- **Rickroll**: Surprise your friends with a classic Rickroll! (Dependency: `subprocess`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/MdSagorMunshi/SHELBY.git
    ```

2. Navigate to the Shelby directory:

    ```bash
    cd SHELBY
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the tool:

    ```bash
    python shelby.py
    ```

5. Follow the on-screen prompts to select and use the desired tool.


## Dependencies

- colorama==0.4.4
- cryptography==3.4.7
- fake-useragent==0.1.11
- Faker==9.1.4
- github==1.2.7
- psutil==5.8.0
- requests==2.26.0

## Author

- **Ryan Shelby**

## Feedback

Your feedback is valuable! If you encounter issues, have suggestions, or want to contribute, please open an issue or submit a pull request.

## Copyright

© 2023 Ryan Shelby. All Rights Reserved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
