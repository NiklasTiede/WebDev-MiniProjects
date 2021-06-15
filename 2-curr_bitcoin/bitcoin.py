
from typing import Tuple
import requests

def bitcoin_value() -> Tuple[float]:
    """ Returns Bitcoins current value as Dollar/Euro. """
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful")
    data = res.json()
    return (round(data["bpi"]["USD"]["rate_float"]), round(data["bpi"]["EUR"]["rate_float"]))


if __name__ == "__main__":
    BC_in_dollar, BC_in_EUR = bitcoin_value()
    print(f"Current Bitcoin Value: {BC_in_dollar} $ or {BC_in_EUR} €")
