from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, matchers=All()):
        self._matchers = matchers

    def build(self):
        return self._matchers
    
    def plays_in(self, team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))

    def has_at_least(self, value, attribute):
        return QueryBuilder(And(self._matchers, HasAtLeast(value, attribute)))

    def has_fewer_than(self, value, attribute):
        return QueryBuilder(And(self._matchers, HasFewerThan(value, attribute)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))
