# biggest val key of dict

def best_score(a_dictionary):
    max = 0
    big = str()
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v > max:
                max, big = v, k
        return big
    else:
        return None


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
