import numpy as np
import itertools

def solveAnvil(target, rules):
    options = np.array([-15,-9,-6,-3,2,7,13,16])
    target += -1 * np.sum(rules)
    quotient = (target // options[options > 0])
    index = np.argmin(quotient)
    sub = options[options > 0][index] * quotient[index] 
    print(sub)
    steps = [options[options > 0][index]] * quotient[index]
    iter = 1

    while True:
        for i in itertools.combinations_with_replacement(options, iter):
            if (sub + np.sum(i)) == target:
                return steps + list(i) + rules
        iter += 1

def decodeRules(rules_list):
   key = {
      "Draw":-15,
      "Hit":[-9,-6,-3],
      "Punch":2,
      "Bend":7,
      "Upset":13,
      "Shrink":16
   }
   decoded_rules = []
   for rule, value in rules_list.items():
       if isinstance(value, list):
           # Handle "Not Last" case
            for v in value:
                decoded_rules.insert(-1*len(decoded_rules),key[v]) if isinstance(key[v], int) else decoded_rules.insert(-1*len(decoded_rules),key[v][2])
       else:
           decoded_value = key[value] if isinstance(key[value], int) else key[value][1]
           if rule == "Last":
               decoded_rules.insert(len(decoded_rules),decoded_value)
           elif rule == "Second Last":
               decoded_rules.insert(-1*len(decoded_rules),decoded_value)
           elif rule == "Third Last":
               decoded_rules.insert(-2*len(decoded_rules),decoded_value)
           else:
               decoded_rules.append(decoded_value)
   
   return decoded_rules

def translateToSteps(numbers):
    key = {
        -15: "Draw",
        -9: "Heavy Hit",
        -6: "Medium Hit",
        -3: "Light Hit",
        2: "Punch",
        7: "Bend",
        13: "Upset",
        16: "Shrink"
    }
    
    translated = []
    for num in numbers:
        if num in key:
            translated.append(key[num])
        else:
            translated.append(str(num))  # If the number is not in the key, keep it as a string
    
    return " -> ".join(translated)

def solveAllHits(target):

  options = np.array([-15,-9,-6,-3,2,7,13,16])
  quotient = (target // options[options > 0])
  index = np.argmin(quotient)
  sub = options[options > 0][index] * quotient[index]
  steps = [options[options > 0][index]] * quotient[index]
  iter = 1

  while True:
    for i in itertools.combinations_with_replacement([-9,-6,-3], 3):
        for j in itertools.combinations_with_replacement(options, iter):
            if (sub + np.sum(i) + np.sum(j)) == target:
                return steps + list(j) + list(i)
        iter += 1