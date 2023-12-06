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

#v6t4
class QueryBuilder:
    #other alternative could be to change to def __init__(self, build = And()??? see Pinorakentaja [viikko6] https://ohjelmistotuotanto-hy.github.io/osa4/#pinorakentaja-viikko-6)
    def __init__(self, matcher=None):
        self._matcher = matcher
        self._filter = []

    def playsIn(self, team):
        self._filter.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._filter.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._filter.append(HasFewerThan(value, attr))
        return self

    def build(self):
        return And(*self._filter)


