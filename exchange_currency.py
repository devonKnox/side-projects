import requests

# Access API
API_KEY = 'c77481e4841095fc67a8703d'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

def get_exchange_rate(base_currency, target_currency, value=0):
    url = f'{BASE_URL}{base_currency}'
    response = requests.get(url)
    
    if response.status_code == 200:  # HTTP request was successful
        data = response.json()
        if 'conversion_rates' in data:
            rates = data['conversion_rates']
            rate = rates.get(target_currency, None)
            
            if rate is not None:
                if value != 0:
                    converted_value = rate * value
                    return rate, converted_value
                else:
                    return rate
            else:
                return 'Currency not found'
        else:
            return 'Error retrieving rates'
    else:
        print(f"Response Text: {response.text}")
        return 'Error connecting to API'

# Example usage
base_currency = 'EUR'
target_currency = 'USD'
value_to_convert = 5

exchange_rate, converted_value = get_exchange_rate(base_currency, target_currency, value_to_convert)
print(f"Exchange rate from {base_currency} to {target_currency}: {exchange_rate}")
print(f"{value_to_convert} {base_currency} = {converted_value} {target_currency}")
