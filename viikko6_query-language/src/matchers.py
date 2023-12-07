class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

#v6t2
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
#v6t2
class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)

#v6t2
class All:
    def test(self, player):
        return True

#v6t3
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

#v6t4 improved and v6t5
class QueryBuilder:
    def __init__(self, matchers=None):
        self._matchers = matchers or All()

    #chaining additional conditions (e.g. PlaysIn(team)) with conditions included already in the self._matchers instance
    def playsIn(self, team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matchers, HasAtLeast(value, attr)))
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matchers, HasFewerThan(value, attr)))
    
    #creating instance where conditions m1 and m2 are combined
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
    
    def build(self):
        return self._matchers