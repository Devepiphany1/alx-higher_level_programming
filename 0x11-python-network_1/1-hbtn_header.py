import urllib.request
import sys

def fetch_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.headers
            if 'X-Request-Id' in headers:
                request_id = headers['X-Request-Id']
                print(f"X-Request-Id: {request_id}")
            else:
                print("X-Request-Id not found in response headers.")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_request_id(url)
    else:
        print("Usage: python script.py <URL>")
