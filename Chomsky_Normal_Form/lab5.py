class Grammar():
    def __init__(self):
        self.P = {
            'S' : ['bA', 'BC'],
            'A' : ['a', 'aS', 'bCaCa'],
            'B' : ['A', 'bS', 'bCAa'],
            'C' : ['eps', 'AB'],
            'D' : ['AB']
            }
        self.V_N = ['S','A','B','C','D']
        self.V_T = ['a', 'b']
    
    def RemoveEpsilon(self):
        #1. remove epsilon productions
        #find non-terminal symbols that derive into empty string
        nt_epsilon = []
        for key, value in self.P.items():
            s = key
            productions = value
            for p in productions:
                if p == 'eps':
                    nt_epsilon.append(s)
        
        for key, value in self.P.items():
            #traverse each non-terminal that has epsilon production
            for ep in nt_epsilon:
                #traverse each production 
                for v in value:
                #check non-erminal with eps prod is in current production
                    prod_copy = v
                    if ep in prod_copy:
                        for c in prod_copy:
                            #delete epsilon prod and add new prod
                            if c == ep:
                                value.append(prod_copy.replace(c, ''))
        #initialize a copy with added prod
        P1 = self.P.copy()
        #remove eps prod from copy
        for key, value in self.P.items():
            for v in value:
                if v == 'eps':
                    P1[key].remove(v)
        
        P_final = {}
        for key,value in P1.items():
            if len(value) != 0:
                P_final[key] = value
            else:
                self.V_N.remove(key)
        
        print(f"1. After removing epsilon productions:\n{P_final}")
        self.P = P_final.copy()
        return  P_final
    
    def EliminateUnitProd(self):
        #2. Eliminate any renaiming (unit productions)
        #new productions for next step
        P2 = self.P.copy()
        for key, value in self.P.items():
            #replace unit productions
            for v in value:
                if len(v) == 1 and v in self.V_N:
                    P2[key].remove(v)
                    for p in self.P[v]:
                        P2[key].append(p)
        print(f"2. After removing unit productions:\n{P2}")
        self.P = P2.copy()
        return P2

    def EliminateInaccesible(self):
        #3. Eliminate inaccesible symbols
        P3 = self.P.copy()
        accesible_symbols = [i for i in self.V_N]
        #find elements that are inaccesible
        for key, value in self.P.items():
            for v in value:
                for s in v:
                    if s in accesible_symbols:
                        accesible_symbols.remove(s)
        #remove inaccesible symbols
        for el in accesible_symbols:
            del P3[el]
        print(f"3. After removing inaccesible symbols:\n{P3}")
        print(self.V_N)
        self.P = P3.copy()
        return P3

    def RemoveUnprod(self):
        #4. Remove unproductive symbols
        P4 = self.P.copy()

        #Check the keys
        for key,value in self.P.items():
            count = 0
            #identify unproductive symbols
            for v in value:
                for a in v:
                    # print(key,'   ', a)
                    # print(self.V_N)
                    if a.isupper() and a in self.V_N:
                        count+=1
                if len(v) == 1 and v in self.V_T:
                    count+=1
            
            #remove unproductive symbols
            if count==0:
                del P4[key]
                # for k, v in self.P.items():
                #     for e in v:
                #         if k == key:
                #             break
                #         else:
                #             if key in e:
                #                 P4[key].remove(e)

        #Check the values
        for key, value in self.P.items():
            for v in value:
                for c in v:
                    if c.isupper() and c not in P4.keys():
                        P4[key].remove(v)
                        break
        
        print(f"4. After removing unproductive symbols:\n{P4}")
        self.P = P4.copy()
        return P4

    def TransformToCNF(self):
        #5. Obtain CNF
        P5 = self.P.copy()
        temp = {}

        #define a list of free symbols
        vocabulary = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V', 'W','X','Y','Z']
        free_symbols = [v for v in vocabulary if v not in self.P.keys()]
        for key, value in self.P.items():
            for v in value:

                #check if oriduction satisfies CNF
                if (len(v) == 1 and v in self.V_T) or (len(v) == 2 and v.isupper()):
                    continue
                else:

                    #split production into two parts
                    left = v[:len(v)//2]
                    right = v[len(v)//2:]

                    #get the new symbols for each half
                    if left in temp.values():
                        temp_key1 = ''.join([i for i in temp.keys() if temp[i] == left])
                    else:
                        temp_key1 = free_symbols.pop(0)
                        temp[temp_key1] = left
                    if right in temp.values():
                        temp_key2 =''.join( [i for i in temp.keys() if temp[i] == right])
                    else:
                        temp_key2 = free_symbols.pop(0)
                        temp[temp_key2] = right
                    
                    #replace the production with the new symbols
                    P5[key] = [temp_key1 + temp_key2 if item == v else item for item in P5[key]]

        #add new productions
        for key, value in temp.items():
            P5[key] = [value]

        print(f"5. Final CNF:\n{P5}")
        return P5
    
    def ReturnProductions(self):
        print(f"Initial Grammar:\n{self.P}")
        P1 = self.RemoveEpsilon()
        P2 = self.EliminateUnitProd()
        P3 = self.EliminateInaccesible()
        P4 = self.RemoveUnprod()
        P5 = self.TransformToCNF()
        return P1, P2, P3, P4, P5
if __name__ == "__main__":
    g = Grammar()
    P1, P2, P3, P4, P5 = g.ReturnProductions()