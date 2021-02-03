import time
from selenium.common.exceptions import TimeoutException


def waiting_for_clickability(element, timeout):

    _poll = 1
    end_time = time.time() + timeout

    while True:

        try:
            element.click()
            return True
        except:
            pass

        time.sleep(_poll)
        if time.time() > end_time:
            break
    raise TimeoutException()