class RuleDTO:
    def __init__(self, rule_id, rule_name, skip):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.skip = skip

    def getId(self):
        return self.rule_id

    def getName(self):
        return self.rule_name

    def getSkip(self):
        return self.skip

    def setSkip(self, skip):
        self.skip = skip

