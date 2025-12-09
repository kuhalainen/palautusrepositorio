from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self.q_list = []

    def has_at_least(self, value, attr):
        new = QueryBuilder()
        new.q_list = self.q_list + [HasAtLeast(value, attr)]
        return new

    def plays_in(self, team):
        new = QueryBuilder()
        new.q_list = self.q_list + [PlaysIn(team)]
        return new

    def has_fewer_than(self, value, attr):
        new = QueryBuilder()
        new.q_list = self.q_list + [HasFewerThan(value, attr)]
        return new

    def build(self):
        query_list = [All()] + self.q_list
        return And(*query_list)

    def build_without_and(self):
        query_list = [All()] + self.q_list
        return And(*query_list)

    def one_of(self, *querys):
        matchers = [query.build() for query in querys]
        new = QueryBuilder()
        new.q_list = self.q_list + [Or(*matchers)]
        return new