import os
from bs4 import BeautifulSoup

# Function to replace header content in an HTML file
def replace_header_footer(file_path, new_header, new_footer):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            header_tag = soup.find('header', class_='header jsHeader')
            footer_tag = soup.find('footer', class_='footer')

            if header_tag:
                header_tag.replace_with(BeautifulSoup(new_header, 'html.parser'))
            if footer_tag:
                footer_tag.replace_with(BeautifulSoup(new_footer, 'html.parser'))

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")

# Function to recursively search for HTML files and replace header and footer content
def process_directory(directory_path, new_header, new_footer):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.html'):
                file_path = os.path.join(root, file_name)
                replace_header_footer(file_path, new_header, new_footer)

if __name__ == "__main__":
    directory_path = input("Enter the directory path to search for HTML files: ")
    
    with open("header_template.html", 'r', encoding='utf-8') as header_template_file:
        new_header = header_template_file.read()
    
    with open("footer_template.html", 'r', encoding='utf-8') as footer_template_file:
        new_footer = footer_template_file.read()

    process_directory(directory_path, new_header, new_footer)
    print("HTML files have been updated with the new header and footer.")
