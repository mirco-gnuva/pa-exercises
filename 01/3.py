scales_map = {'kelvin': {'from': lambda x: x-273.15, 'to': lambda x: x+273.15},
'fahrenheit': {'from': lambda x: (x-32) * 5/9, 'to': lambda x: x * 9/5 + 32},
'rankine': {'from': lambda x: (x - 491.67) * 5/9, 'to': lambda x: (x + 273.15) * 9/5},
'delisle': {'from': lambda x: 100 - x * 2/3, 'to': lambda x: (100 - x) * 3/2},
'newton': {'from': lambda x: x * 100/33, 'to': lambda x: x * 33/100},
'réaumur': {'from': lambda x: x * 5/4, 'to': lambda x: x * 4/5},
'romer': {'from': lambda x: (x - 7.5) * 40/21, 'to': lambda x: x * 21/40 +7.5},
'celsius': {'from': lambda x: x, 'to': lambda x: x}}

def table(celsius: float) -> str:
    result = '\n'.join(f'{functions['to'](celsius)} {scale}' for scale, functions in scales_map.items())

    return result


def toAll(temperature: float, scale: str) -> list[tuple]:
    celsius = scales_map[scale]['from'](temperature)
    d = {s: scales_map[s]['to'](celsius) for s, functions in scales_map.items()}

    return sorted(list(d.items()),key= lambda e: e[1])

if __name__ == '__main__':
    print(table(5))
    print(toAll(5, 'celsius'))
    print(toAll(5, 'romer'))


