import random
import string


class CommonUtils:

    @staticmethod
    def random_gen_str(length=7):
        return 'AutoTest' + ''.join(random.sample(string.ascii_letters + string.digits, length))

    @staticmethod
    def random_gen_number(length=9):
        return '18' + ''.join(random.sample(string.digits, length))