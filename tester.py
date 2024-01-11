import requests

def website_tester(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return "Website is working fine"
    except requests.exceptions.RequestException as e:
        return "Error occurred: {}".format(e)

# Get user input for the website URL
url_to_test = input("Enter the website URL to test: ")

# Test the website
result = website_tester(url_to_test)
print(result)
