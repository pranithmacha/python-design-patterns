""""
The 'Singleton' DP is all about ensuring that just one instance of a certain class is ever created.
It has a catchy name and is thus enormously popular, but it's NOT a good idea --
it displays different sorts of problems in different object-models.
What we should really WANT, typically, is to let as many instances be created as necessary, BUT all with shared state.
Who cares about identity -- it's state (and behavior) we care about!

You can ensure this in many ways in Python, but the Borg design pattern is almost always best.
Since the self.__dict__ of any instance can be re-bound, just re-bind it in __init__ to a class-attribute dictionary
-- that's all! Now any reference or binding of an instance attribute will actually affect all instances equally

"""


class Borg(object):

    _shared_dict = {}

    def __init__(self):
        self.__dict__ = self._shared_dict


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        Borg._shared_dict.update(kwargs)

    def __str__(self):
        return str(self._shared_dict)


def main():
    one = Singleton(team="ferrari")
    print(one)
    two = Singleton(sport='f1')
    print(two)
    with open('input.txt', 'r') as input_file:
        two._shared_dict.update(content=input_file.read())
    three = Singleton()
    print(three)

    three.content = "dummy content replacedt"
    print(two.content)


if __name__ == "__main__":
    main()







