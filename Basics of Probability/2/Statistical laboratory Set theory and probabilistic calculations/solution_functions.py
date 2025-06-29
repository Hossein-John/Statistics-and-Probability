def create_set(input_ls):
    return set(input_ls)

def union(first_set, second_set):
    return first_set.union(second_set)

def intersection(first_set, second_set):
    return first_set.intersection(second_set)

def difference(first_set, second_set):
    return first_set.difference(second_set)

def complement(universal_set, first_set):
    return universal_set - first_set

def is_empty(the_set):
    return len(the_set) == 0

def is_subset(first_set, second_set):
    return first_set.issubset(second_set)

def is_member(the_set, element):
    return element in the_set

def power_set_number(the_set):
    return 2 ** len(the_set)

def probability_of_event(events, sample_space) -> float:
    return len(events) / len(sample_space)

def conditional_probability(events, sample_space) -> float:
    return len(intersection(events, sample_space)) / len(sample_space)

def are_independent(events1, events2, sample_space) -> float:
    x = probability_of_event(events1, sample_space) * probability_of_event(events2, sample_space)
    y = probability_of_event(intersection(events1, events2), sample_space)
    return abs(x - y) < 1e-9

def bayes_theorem(events1, events2, sample_space) -> float:
    x = conditional_probability(events1, events2) * probability_of_event(events2, sample_space)
    return x / probability_of_event(events1, sample_space)
