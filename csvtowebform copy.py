import csv
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- Configuration ---
FORM_ACTION_URL = 'http://simhajtraining.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon' # Replace with the actual form URL
CSV_FILE_PATH = 'seed4insertmovement.csv'
# ---------------------

def submit_form_from_csv(url, file_path):
    """
    Reads data from a CSV file and submits it to a web form via POST requests.
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                print("CSV file is empty or missing headers.")
                return

            print(f"Submitting data to {url}...")
            retry_strategy = Retry(
                total=5,                          # Total number of retries
                backoff_factor=1,                 # Wait 1s, 2s, 4s... between retries
                status_forcelist=[429, 500, 502, 503, 504] # Retry on these errors
            )
            session = requests.Session()
            adapter = HTTPAdapter(max_retries=retry_strategy)
            session.mount("https://", adapter)
            session.mount("http://", adapter)
            for row in reader:
                # 'row' is a dictionary: {'username': 'user1', 'email': '...', ...}
                # response = requests.post(url, data=row)
                response = session.post(url, data=row)

                # Check the response (status code 200 usually means success)
                if response.status_code == 200:
                    print(f"Successfully submitted data for {row.get('username', 'a user')}.")
                else:
                    print(f"Failed to submit data for {row.get('username', 'a user')}. Status code: {response.status_code}")
                    # Optional: print response.text to debug server-side errors

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    submit_form_from_csv(FORM_ACTION_URL, CSV_FILE_PATH)