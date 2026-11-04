
import requests

def main():
    try:
        response = requests.get(
            "https://chatgpt.com/share/6aeb497b-5aa4-83ea-bfc9-6bff02369ba8",
            timeout=10
        )

        response.raise_for_status()

        results = response.json()

        print(results)

    except requests.exceptions.HTTPError:
        print("Your request returned an unsuccessful HTTP status.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the server.")

    except requests.exceptions.Timeout:
        print("The request timed out.")

    except requests.exceptions.JSONDecodeError:
        print("The server did not return valid JSON.")

main()
