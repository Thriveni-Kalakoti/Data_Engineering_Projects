import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def extract_api_data(api_url: str = API_URL) -> list[dict]:
    """
    Extract data from a public REST API.

    Args:
        api_url: API endpoint URL.

    Returns:
        A list of dictionaries containing API response data.
    """
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Expected API response to be a list of records.")

    return data


if __name__ == "__main__":
    records = extract_api_data()
    print(f"Records extracted: {len(records)}")
    print(records[0])