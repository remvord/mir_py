class A1():
    _yes = ''

    def __init__(self):
        pass

    def info(self):
        return self._yes


class A2(A1):
    def __init__(self):
        self._yes = 'Yeee'
        pass

    def __init__(self, _yes):
        self._yes = yes
        pass

    def info(self):
        return f'----------{self._yes}--------'
