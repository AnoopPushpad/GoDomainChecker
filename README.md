# GoDomainChecker

GoDomainChecker is a Python script that allows users to check the availability of domain names either one at a time or from a list provided in a text file.

## Usage

1. **Installation**

    - Ensure you have Python installed on your system.
    - Install the `whois` library using pip: `pip install python-whois`

2. **Running the Script**

    - Run the script by executing `python main.py` in your terminal.
    - Follow the on-screen instructions to select an option.

3. **Options**

    - **Check availability of a single domain**: Enter option 1 and provide the domain name when prompted.
    - **Check domains from a text file**: Enter option 2 and ensure a text file named `listdomainshere.txt` exists in the same directory. If not, the script will create one.
  
4. **Output**

    - The script will provide real-time feedback on the availability of each domain.
    - It will also generate a CSV file named `Domain Status Data {timestamp}.csv` containing the domain names and their availability status.

## Dependencies

- [Python Whois](https://pypi.org/project/python-whois/): A Python module for retrieving WHOIS information of domains.

## Author

- Anoop Pushpad

## License

This project is licensed under the [MIT License](LICENSE).
