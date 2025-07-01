from collections.abc import Mapping
from typing import Literal, TypeAlias

TroolValue: TypeAlias = Literal['true', 'false', 'joke']

class Trool:
    def evaluate(self, subs: Mapping[str, TroolValue]) -> TroolValue:
        raise NotImplementedError

    def get_distinct_vars(self) -> set[str]:
        raise NotImplementedError

class Const(Trool):
    const: TroolValue
    def __init__(self, const: TroolValue):
        self.const = const
    
    def evaluate(self, subs: Mapping[str, TroolValue]):
        return self.const
    
    def get_distinct_vars(self) -> set[str]:
        return set()

class Var(Trool):
    var: str
    def __init__(self, var: str):
        self.var = var

    def evaluate(self, subs: Mapping[str, TroolValue]):
        return subs[self.var]
    
    def get_distinct_vars(self) -> set[str]:
        return {self.var}

class Not(Trool):
    expr: Trool
    def __init__(self, expr: Trool):
        self.expr = expr
    
    def evaluate(self, subs: Mapping[str, TroolValue]):
        return self.expr.evaluate(subs)
        
    def get_distinct_vars(self) -> set[str]:
        return self.get_distinct_vars()
    
class And(Trool):
    a: Trool
    b: Trool

    def __init__(self, a: Trool, b: Trool):
        self.a = a
        self.b = b
    
    def evaluate(self, subs: Mapping[str, TroolValue]):
        ...
        
    

