import os
from bs4 import BeautifulSoup
import re

# Function to replace header content in an HTML file
def replace_header_footer(file_path, new_header, new_footer):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            header_tag = soup.find('header', class_='kl-header')
            footer_tag = soup.find('footer', class_='kl-footer')

            if header_tag:
                new_header = update_links_paths(new_header, file_path)
                header_tag.replace_with(BeautifulSoup(new_header, 'html.parser'))

            if footer_tag:
                new_footer = update_links_paths(new_footer, file_path)
                footer_tag.replace_with(BeautifulSoup(new_footer, 'html.parser'))

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")

# Function to recursively search for HTML files and replace header and footer content
def process_directory(directory_path, new_header, new_footer):
    print(f"Starting to process directories")
    count = 0
    print(f"Searching for HTML files in {directory_path}...")
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.html'):
                file_path = os.path.join(root, file_name)
                print(f"Processing file {file_path}...")
                count += 1
                replace_header_footer(file_path, new_header, new_footer)
                print(f"Processed {count} files.")
        print(f"Total Processed {count} files.")

def update_links_paths(html_content, file_path):
    # Get the depth of the subdirectory
    subdirectory_depth = file_path.count(os.sep)

    if subdirectory_depth <= 1:
        relative_path = ""
    # Add '../' based on the subdirectory depth
    else:
        relative_path = '../' * (subdirectory_depth - 1 )
        print(relative_path)

    # Adjust links, URLs, and paths based on the relative path
    updated_content = re.sub(r'src="(?!https?://)', f'src="{relative_path}', html_content)
    updated_content = re.sub(r'href="(?!https?://)', f'href="{relative_path}', updated_content)

    return updated_content

if __name__ == "__main__":
    directory_path = input("Enter the directory path to search for HTML files: ")
    print(f"Searching for HTML files in {directory_path}...")

    with open("header_template.html", 'r', encoding='utf-8') as header_template_file:
        new_header = header_template_file.read()


    with open("footer_template.html", 'r', encoding='utf-8') as footer_template_file:
        new_footer = footer_template_file.read()

    print(f"Searching for HTML files in {directory_path}...")

    process_directory(directory_path, new_header, new_footer)
    print("HTML files have been updated with the new header and footer.")
