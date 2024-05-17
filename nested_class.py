class OuterClass():
    def __init__(self) -> None:
        self._name = 'Outer'

    class InnerClass():
        def __init__(self) -> None:
            self._name = 'Inner'
            self.messege = ''
        
        def write_messege(self, input):
            self.messege = input


class Unorganised():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
