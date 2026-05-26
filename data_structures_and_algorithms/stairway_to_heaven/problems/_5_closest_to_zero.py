class EX5:

    def closest_to_zero(self, values: list):

        abs_values = [abs(value) for value in values]
        min_abs = min(abs_values)

        candidates = [c for c in abs_values if abs(c) == min_abs]

        return max(candidates)


if __name__ == "__main__":

    values = [1, 2, 3, -6, 7, -4, -2]

    ex = EX5()
    print(ex.closest_to_zero(values))
