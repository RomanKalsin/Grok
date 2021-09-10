states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stantions = {"kone": set(["id", "nv", "ut"]), "ktvo": set(["mt", "wa", "id"]), 
             "khtree": set(["or", "nv","ca"]), "kfour": set(["nv", "ut"]),
             "kfive": set(["ca", "az"])
             }
final_stantion = set()
while states_needed:
    best_stantion = None
    states_covered = set()
    for stantion, states in stantions.items():     
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_stantion = stantion
            states_covered = covered
    states_needed -= states_covered
    final_stantion.add(best_stantion)

print(final_stantion)