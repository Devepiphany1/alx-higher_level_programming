import urllib.request
import urllib.error

def fetch_status(url):
    try:
        # Open the URL and fetch the response
        with urllib.request.urlopen(url) as response:
            # Check if the request was successful (status code 200)
            if response.status == 200:
                print("Status code: 200 OK")
                print("Response body:")
                print(response.read().decode('utf-8'))  # Print the response body
            else:
                print(f"Failed to fetch status. Status code: {response.status}")
    except urllib.error.URLError as e:
        print(f"Error fetching status: {e}")

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)

