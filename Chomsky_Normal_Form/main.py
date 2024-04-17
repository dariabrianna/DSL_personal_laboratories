class Grammar:
    def __init__(self):
        self.productions = {
            'S': ['bA', 'BC'],
            'A': ['a', 'aS', 'bCaCa'],
            'B': ['A', 'bS', 'bCAa'],
            'C': ['eps', 'AB'],
            'D': ['AB']
        }
        self.non_terminals = ['S', 'A', 'B', 'C', 'D']
        self.terminals = ['a', 'b']

    def display_grammar(self):
        for key, prods in self.productions.items():
            productions_str = " | ".join(prods)
            print(f"{key} -> {productions_str}")

    def remove_epsilon_productions(self):
        eps_producers = {nt for nt, prods in self.productions.items() if 'eps' in prods}
        for nt in eps_producers:
            self.productions[nt].remove('eps')
            for key, prods in list(self.productions.items()):
                new_prods = []
                for prod in prods:
                    positions = [i for i, char in enumerate(prod) if char == nt]
                    for i in range(1 << len(positions)):
                        new_prod = ''.join(prod[j] for j in range(len(prod)) if not (1 << j & i))
                        if new_prod:
                            new_prods.append(new_prod)
                self.productions[key].extend(new_prods)
                self.productions[key] = list(set(self.productions[key]))

    def eliminate_unit_productions(self):
        unit_prods = {nt: prods for nt, prods in self.productions.items() if all(len(prod) == 1 and prod.isupper() for prod in prods)}
        for nt, prods in unit_prods.items():
            self.productions[nt] = []
            for prod in prods:
                self.productions[nt].extend(self.productions[prod])

    def remove_inaccessible_symbols(self):
        accessible = set('S')
        stack = ['S']
        while stack:
            nt = stack.pop()
            for prod in self.productions.get(nt, []):
                for char in prod:
                    if char in self.non_terminals and char not in accessible:
                        accessible.add(char)
                        stack.append(char)
        self.productions = {nt: prods for nt, prods in self.productions.items() if nt in accessible}

    def remove_unproductive_symbols(self):
        productive = set()
        change = True
        while change:
            change = False
            for nt, prods in self.productions.items():
                for prod in prods:
                    if all(char in self.terminals or char in productive for char in prod):
                        if nt not in productive:
                            productive.add(nt)
                            change = True
        self.productions = {nt: [prod for prod in prods if all(char in self.terminals or char in productive for char in prod)] for nt, prods in self.productions.items() if nt in productive}

    def transform_to_CNF(self):
        # Placeholder for the actual CNF conversion logic
        pass

    def execute_transformations(self):
        print("Initial Grammar:")
        self.display_grammar()
        self.remove_epsilon_productions()
        print("After Removing Epsilon Productions:")
        self.display_grammar()
        self.eliminate_unit_productions()
        print("After Eliminating Unit Productions:")
        self.display_grammar()
        self.remove_inaccessible_symbols()
        print("After Removing Inaccessible Symbols:")
        self.display_grammar()
        self.remove_unproductive_symbols()
        print("After Removing Unproductive Symbols:")
        self.display_grammar()
        self.transform_to_CNF()
        print("Final CNF:")
        self.display_grammar()

if __name__ == "__main__":
    grammar = Grammar()
    grammar.execute_transformations()
