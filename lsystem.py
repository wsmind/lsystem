
def grow(l_system, iterations):
    plant = l_system["axiom"]
    rules = l_system["rules"]

    for i in range(iterations):
        plant = "".join([rules.get(atom, atom) for atom in plant])

    return plant

def grow_barnsley(iterations):

    barnsley_plant = {
    "axiom": "X",
    "rules": {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF"
        }
    }

    return grow(barnsley_plant, iterations)


def main():
    test_plant = {
        "axiom": "A",
        "rules": {
            "A": "AB",
            "B": "A"
        }
    }

    zero_iterations = grow(test_plant, 0)
    assert(zero_iterations == "A")

    first_iteration = grow(test_plant, 1)
    assert(first_iteration == "AB")

    more_iterations = grow(test_plant, 7)
    print(more_iterations)
    assert(more_iterations == "ABAABABAABAABABAABABAABAABABAABAAB")

if __name__ == '__main__':
    main()
