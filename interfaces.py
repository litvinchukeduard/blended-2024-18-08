from abc import ABC, abstractmethod

# interface BasicInterface:
#     def abstract_method(self)


class BasicAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    # def non_abstract_method(self):
#     print("I am not abstract")


class ConcreteClass(BasicAbstractClass):
    pass


# basic_abstract_class = BasicAbstractClass()
concrete_class = ConcreteClass()
