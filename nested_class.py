class OuterClass():
    def __init__(self) -> None:
        self._name = 'Outer'

    class InnerClass():
        def __init__(self) -> None:
            self._name = 'Inner'
            self.messege = ''
        
        def write_messege(self, input):
            self.messege = input
