import random

class DecisionMaker:
    def __init__(self, rules: List[Dict[str, str]]):
        self.rules = rules

    def make_decision(self, input_data: Dict[str, str]) -> str:
        for rule in self.rules:
            if all(input_data[key] == value for key, value in rule.items()):
                return rule['output']
        return random.choice(['yes', 'no'])  # default decision

# Example usage:
# rules = [
#     {'input': 'user_is_admin', 'value': 'True', 'output': 'yes'},
#     {'input': 'user_is_guest', 'value': 'True', 'output': 'no'}
# ]
# decision_maker = DecisionMaker(rules)
# input_data = {'user_is_admin': 'True'}
# result = decision_maker.make_decision(input_data)
# print(result)
