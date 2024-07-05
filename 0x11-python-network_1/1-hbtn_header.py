import requests

def fetch_request_id(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Check if 'X-Request-Id' is present in the response headers
            if 'X-Request-Id' in response.headers:
                request_id = response.headers['X-Request-Id']
                print(f"X-Request-Id: {request_id}")
            else:
                print("X-Request-Id not found in response headers.")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    url = input("Enter URL: ")
    fetch_request_id(url)
