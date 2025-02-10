import requests
from bs4 import BeautifulSoup

def extract_content(url, element_type):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        extracted_content = []
        for element in soup.find_all(element_type):
            text = element.get_text(strip=True)
            if text:
                extracted_content.append(text)
        return extracted_content

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example:
url = "https://www.google.com"  # Replace with the website URL
element_type = "p"  # Example: Extract all paragraphs

content = extract_content(url, element_type)

if content is None:
    print("Failed to get the website.")
elif content:
    print("Extracted content:")
    for item in content:
        print(item)
else:
    print("No matching elements found.")