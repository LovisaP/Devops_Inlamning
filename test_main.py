import requests
import sys

def test_api():

    lon = 17.0
    lat = 59.0
    url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"

    # Anropa API:t
    response = requests.get(url)
    code = response.status_code


    if code == 200:
        print("API response successful: Status code 200")
    else:
        print(f"API request failed with status code {code}")
        sys.exit(1) 

    try:
        data = response.json()
    except ValueError:
        print("Invalid JSON response")
        sys.exit(1)

    if "timeSeries" not in data or len(data["timeSeries"]) == 0:
        print("No timeSeries found in the response")
        sys.exit(1)

    if "parameters" not in data["timeSeries"][0] or len(data["timeSeries"][0]["parameters"]) == 0:
        print("No parameters found in the response")
        sys.exit(1)

    print("API response and data format are correct")

if __name__ == "__main__":
    test_api()

