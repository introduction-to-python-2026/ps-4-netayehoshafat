def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    
    return split_formula


def split_at_first_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix_letters = formula [:i]
            suffix_numbers = formula [i:]
            return (prefix_letters, int(suffix_numbers))
    return (formula, 1)
