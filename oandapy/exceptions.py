"""Exceptions."""


class OandaError(Exception):
    """ Generic error class, catches oanda response errors
    """

    def __init__(self, error_response):
        self.error_response = error_response
        msg = f"OANDA API returned error code {error_response['code']} ({error_response['message']}) " 

        super(OandaError, self).__init__(msg)


class BadEnvironment(Exception):
    """environment should be: sandbox, practice or live."""
    def __init__(self, environment):
        msg = f"Environment '{environment}' does not exist"
        super(BadEnvironment, self).__init__(msg)
