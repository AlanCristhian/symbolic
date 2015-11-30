import cassowary


# The argument_sender() coroutine-object will be store the values passed
# with the .send() method. I will use this values as function arguments later.
# Then yield the value like a producer.

def argument_sender():
    value = None
    while True:
        # If I not yield the value, the following line return the None value.
        # None value can cause some problems inside the generator expression.
        value = yield value
        yield value


# To build the generator-expression, Python3 need that the
# `input sequence` object in the generator-expression have the
# .__iter__() method. This method should return an iterable. The IterableMeta
# metaclass do that.

class Iterable(type):
    """Make a class that is an iterable object."""
    def __iter__(cls):
        # !!!: the iter method return the argument_sender() coroutine-object
        sender = argument_sender()
        # To get a co-routine to run properly, you have to
        # ping it with a next() operation first
        next(sender)
        return sender


class Variables(metaclass=Iterable):
    pass


def solve(expression):
    send = expression.gi_frame.f_locals['.0'].send
    var_names = expression.gi_code.co_varnames[1:]
    variables = [cassowary.Variable(name) for name in var_names]
    send(variables)
    constraints = next(expression)
    solver = cassowary.SimplexSolver()
    for constraint in constraints:
        solver.add_constraint(constraint)
    return variables
