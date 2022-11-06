class Serialise:

    @classmethod
    def from_json(cls, _json, *_):

        raise f'Implement {cls}.from_json'

    def to_json(self):

        raise f'Implement {self.__class__}.to_json'

    def __eq__(self, __other):

        return self.to_json() == __other.to_json()

class BaseStore(Serialise):

    __slots__ = 'text', 'modules'

    def __init__(self, text, modules):
        self.text = text
        self.modules = modules

    @classmethod
    def from_json(cls, _json, **module_types):
        return cls(
            _json['text'],
            [Module.from_json(mod, *module_types[mod['name']]) for mod in _json['modules']]
        )

    def to_json(self):
        return {
            'text': self.text,
            'modules': [mod.to_json() for mod in self.modules]
        }

    def apply_all(self):

        for mod in self.modules:
            cx = PartialContext(self, mod)
            mod.todos.apply(cx)

class PartialContext:

    def __init__(self, base, module):
        self.__base = base
        self.module = module

    def add_module(self, module):
        self.__base.modules.append(module)


class Module(Serialise):

    __slots__ = 'todos', 'data', 'name'

    @classmethod
    def from_json(cls, _json, T, D):
        return cls(
            _json['name'],
            T.from_json(_json['todos']),
            D.from_json(_json['data'])
        )

    def __init__(self, name, todos, data):
        self.name = name
        self.todos = todos
        self.data = data

    def to_json(self):
        return {
            'name': self.name,
            'data': self.data.to_json(),
            'todos': self.todos.to_json(),
        }

class Todo(Serialise):

    __slots__ = 'commands'

    def apply(self, cx: PartialContext):
        ...

class TestTodo(Todo):

    @classmethod
    def from_json(cls, _json):
        
        return cls(_json)

    def __init__(self, commands):

        self.commands = commands

    def apply(self, cx):
        
        for i in self.commands:

            if i == 'invert':
                cx.module.data.name = cx.module.name[::-1]
                cx.module.data.age = int(str(cx.module.data.age)[::-1])

    def to_json(self):

        return self.commands

class TestData(Serialise):

    __slots__ = 'name', 'age'

    @classmethod
    def from_json(cls, _json, *_):

        return cls(
            _json['name'],
            _json['age'],
        )

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def to_json(self):
        return {
            'name': self.name,
            'age': self.age,
        }

def test():

    mapping = {
        'test': (TestTodo, TestData)
    }

    mod = Module.from_json(
        {   
            'name': 'test',
            'data': {
                'name': 'luke',
                'age': 103,
            },
            'todos': [
                'invert',
            ]
        },
        TestTodo,
        TestData,
    )

    base = BaseStore.from_json(
        {
            'text': "abcd",
            'modules': [
                mod.to_json()
            ]
        },
        **mapping
    )

    print(mod.to_json())

    assert mod == base.modules[0]

    base.apply_all()

    assert mod != base.modules[0]



if __name__ == '__main__': test()