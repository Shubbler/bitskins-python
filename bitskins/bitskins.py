import os

import requests
from requests.compat import urljoin
import pyotp

from bitskins.exceptions import *
from bitskins.const import *


class BitSkins:
	def __init__(self, api_key=os.environ.get("api_key"), secret=os.environ.get("secret")):

		if api_key is None or secret is None:
			raise UserException("An 'api_key' and a 'secret' must be provided either when creating a BitSkins object or set environment variables.")

		session = requests.session()
		session.params.update(api_key=api_key)

		self._session = session
		self._auth = pyotp.TOTP(secret)

	def __getattr__(self, endpoint):
		def hook(**params):
			url = urljoin(BASE_URL, endpoint)
			self._session.params.update(code=self._auth.now())

			response = self._session.get(url, params=params)

			return response.json()

		return hook
