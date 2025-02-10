import requests 
import logging

#configure logging
logging.basicConfig(level=logging.INFO)

# Example API URL (searching for books about Python)
API_URL = "http://openlibrary.org/search.json?q=python"

def fetch_data():
    "fetch the data from open library api"
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status() #raise an exception for http errors
        data = response.json()
        logging.info("Data fetched successfully")
        return data
    except requests.exceptions.RequestException as e:
        logging.error("Error fetching the data: %s", e)
        return None

if __name__ == '__main__':
    data = fetch_data()
    print(data)