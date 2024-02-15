
class Grammar:
    def __init__(self):
        self.VN = {'S', 'A', 'B', 'C'}
        self.VT = {'a', 'b', 'c', 'd'}
        self.P = {
            'S': ['dA'],
            'A': ['aB', 'b'],
            'B': ['bC', 'd'],
            'C': ['cB', 'aA']
        }

    def generate_valid_strings(self, symbol='S', depth=0):
        if depth > 10 or symbol not in self.VN:  # Limit depth to prevent infinite recursion
            return [symbol]
        results = []
        for production in self.P[symbol]:
            partial_results = ['']
            for char in production:
                new_partial_results = []
                for pr in partial_results:
                    for expansion in self.generate_valid_strings(char, depth + 1):
                        new_partial_results.append(pr + expansion)
                partial_results = new_partial_results
            results.extend(partial_results)
        return results

    def generate_five_valid_strings(self):
        valid_strings = self.generate_valid_strings()
        return valid_strings[:5]


class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transition_function = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state):
        self.states.add(state)

    def add_transition(self, from_state, input_char, to_state):
        if from_state not in self.transition_function:
            self.transition_function[from_state] = {}
        self.transition_function[from_state][input_char] = to_state

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)

    def check_string(self, input_string):
        current_state = self.start_state
        for char in input_string:
            if char in self.transition_function.get(current_state, {}):
                current_state = self.transition_function[current_state][char]
            else:
                return False
        return current_state in self.accept_states


def grammar_to_automaton(grammar):
    fa = FiniteAutomaton()
    fa.set_start_state('start')
    fa.add_accept_state('accept')

    for symbol in grammar.VN:
        fa.add_state(symbol)
        if symbol == 'S':  # Assuming 'S' is always the start symbol
            fa.set_start_state(symbol)

    for left, productions in grammar.P.items():
        for production in productions:
            if production.islower():  # Assuming lowercase are terminal symbols
                fa.add_transition(left, production, 'accept')
            else:
                for char in production:
                    if char.isupper():  # Assuming uppercase are non-terminal symbols
                        fa.add_transition(left, char, char)
                    else:
                        fa.add_state(char + '_mid')
                        fa.add_transition(left, char, char + '_mid')
                        fa.add_transition(char + '_mid', '', 'accept')

    return fa


grammar = Grammar()

# Check if a string can be obtained via the state transition from the automaton
fa = grammar_to_automaton(grammar)

# Test the FA with a valid string and an invalid string
test_strings = ['dabcbaabab', 'invalid']
results = {ts: fa.check_string(ts) for ts in test_strings}
print("Testing strings against the finite automaton:")
for ts in test_strings:
    result = fa.check_string(ts)
    print(f"'{ts}': {result}")

five_valid_strings = grammar.generate_five_valid_strings()

# Print the 5 valid strings
print("Five valid strings generated from the grammar:")
for string in five_valid_strings:
    print(string)

# test_string = "some_string"
# print(fa.check_string(test_string))