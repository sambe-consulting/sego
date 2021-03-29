# ************************************************************************#
# Title:                    Sego  Exception                               #
# Description:              This class is the main Exception for Sego     #
# Author:                   Sambe Consulting <development@sambe.co.za>a     #
# Original Date:            29 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

class SegoBaseException(Exception):
    """Base class for other exceptions in Sego"""

    exception_name = "SegoBaseException"
    message = "Sego error"

    def __init__(self, message=None, exception_name=None):
        if exception_name is not None:
            self.exception_name = exception_name
        else:
            self.exception_name = self.__class__.__name__
        if message is not None:
            self.message = message



        super().__init__(self.message)

    def __str__(self):
        return f"""A Sego Exception has occurred\n
                     Exception name: {self.exception_name},
                     Exception message: {self.message}
                    """
