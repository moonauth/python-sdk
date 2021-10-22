class MoonException(Exception):
    pass

class client:

    def __init__(self, privatekey):

        self.privatekey = privatekey

        if privatekey is None:
            raise MoonException(
                "All methods require an API key. See "
                "https://developers.moonauth.com/docs/authentication "
                "for how to authenticate properly."
            )
        else:
            pass

    def instance(self):
        print (self)