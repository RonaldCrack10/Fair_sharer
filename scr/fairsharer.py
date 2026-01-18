

def fair_sharer(values: list, num_iterations: int, share: float = 0.1) -> list:

    highest_value = max(values)
    values_new = []

    for index, value in enumerate(values):
        if values[index] == highest_value:
            highest_value_index = index

            for i in range(num_iterations):
                values[highest_value_index + 1] += share * values[highest_value_index]
                values[highest_value_index - 1] += share * values[highest_value_index]

                
    return values


fair = fair_sharer([10, 20, 30, 40, 50, 0], 4, 0.1)
print(fair)
