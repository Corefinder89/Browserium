from utility.browser_configuration import BrowserConfiguration

class Dummy(BrowserConfiguration):
    def check_func(self):
        self.chrome_configuration("disable_extension","ignore_certificate_errors","sandbox")

d = Dummy()
d.check_func()