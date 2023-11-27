# HTML Header and Footer Replacer

This Python script provides a simple utility to replace header and footer content in HTML files within a specified directory. It utilizes the BeautifulSoup library for parsing and modifying HTML.

## Prerequisites

- Python 3.x
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

1. **Clone the repository or download the script.**

    ```bash
    git clone https://github.com/neeryks/bulkedit.git
    cd bulkedit
    ```

2. **Run the script by executing the following command in your terminal.**

    ```bash
    python bulkedit.py
    ```

3. **Enter the directory path where your HTML files are located when prompted.**

4. **The script will read the header and footer content from `header_template.html` and `footer_template.html`, respectively, and replace the existing header and footer in each HTML file within the specified directory.**

5. **Once the process is complete, the script will print a message indicating that the HTML files have been updated with the new header and footer.**

## Notes

- Make sure to keep backup copies of your HTML files before running the script, as it directly modifies the files in place.

- Ensure that the `header_template.html` and `footer_template.html` files contain the desired HTML content you want to replace in the header and footer of each HTML file.

- If an error occurs during processing, the script will print an error message indicating the file and the nature of the error.

Feel free to customize the script and templates to suit your specific needs.
