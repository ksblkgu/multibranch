import requests
from requests.exceptions import HTTPError
# tsetteste3
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.status_code)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err')
    except Exception as err:
        print(f'other error occurred: {err}')
    else:
        print('Success')