import json

def task(filename: str) -> float:
    i = 0
    with open(filename) as file:
        data = json.load(file)
    summed_values = sum([item["score"] * item["weight"] for item in data])
    return round(summed_values, 3)

print(task('input.json'))
