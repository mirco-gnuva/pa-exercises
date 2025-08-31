alkaline_earth_metals=[(56, "barium"), (4, "beryllium"), (20, "calcium"), (12, "magnesium"), (88, "radium"), (38, "strontium")]
noble_gases = [
    (2, "helium"),
    (10, "neon"),
    (18, "argon"),
    (36, "krypton"),
    (54, "xenon"),
    (86, "radon")
]

def greates_atomic_number(elements: list[tuple]) -> int:
    return max(e[0] for e in elements)

def sort_elements(elements: list[tuple]):
    elements.sort(key=lambda x: x[0])

def to_dict(elements: list[tuple]) -> dict[str, int]:
    return {e[1]: e[0] for e in elements}

if __name__ == '__main__':
    print(greates_atomic_number(alkaline_earth_metals))
    sort_elements(alkaline_earth_metals)
    print(alkaline_earth_metals)

    alkaline_earth_metals = to_dict(alkaline_earth_metals)
    print(to_dict(alkaline_earth_metals))
    
    noble_gases = to_dict(noble_gases)
    print(noble_gases)

    print(sorted(list((alkaline_earth_metals | noble_gases).items()), key=lambda c: c[0]))
