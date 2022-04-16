import base64
import random
import string


def b64decode(b_str):
    return str(base64.b64decode(b_str), "utf-8")


def b64encode(str):
    return base64.b64encode(str)


class RandomHelper:
    @classmethod
    def text(cls):
        val = random.randint(0x4e00, 0x9fbf)
        return chr(val)

    @classmethod
    def more_text(cls, num: int):
        var = ""
        for i in range(num):
            var += cls.text()
        return var

    @classmethod
    def number(cls):
        return str(random.randint(0, 9))

    @classmethod
    def more_number(cls, num: int):
        var = ""
        for i in range(num):
            var += cls.number()
        return var

    @classmethod
    def str_char(cls, num: int, str_c=string.ascii_letters + string.digits):
        return "".join(random.choices(str_c, k=num))

