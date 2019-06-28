# bitskins-python

bitskins-python is a Python 3 library for accessing the [BitSkins API](https://bitskins.com/api).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bitskins-python.

```bash
pip install bitskins-python
```

## Usage

```python
import bitskins


api_key = os.environ.get("api_key")
secret = os.environ.get("secret")

b = BitSkins(api_key=api_key, secret=secret)

b.get_account_balance() #{'status': 'success', 'data': {'available_balance': '1', 'pending_withdrawals': '0.0000', 'withdrawable_balance': '1', 'couponable_balance': '0.0000'}}


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
