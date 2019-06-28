class APIException(Exception):
	def __init__(self, message):
		super().__init__(message)

		self.message = message


class UserException(Exception):
	def __init__(self, message):
		super().__init__(message)

		self.message = message