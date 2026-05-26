# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Ex8:

    def _digits_counter(self, n: int) -> int:
        position_finder = abs(n)
        n_digits = 0
        while True:
            position_finder = position_finder // 10
            if position_finder == 0:
                break
            n_digits += 1

        return n_digits

    def reverse_integer_by_digit_extraction(self, n: int) -> int:

        n_digits = self._digits_counter(n)

        print(f"The number has {n_digits+1} digits")

        inv_n = 0
        n_placeholder = abs(n)

        while n_digits >= 0:

            print(f"inv_n: {inv_n}")
            inv_n = inv_n + (n_placeholder % 10) * (10 ** (n_digits))
            n_placeholder = n_placeholder // 10
            n_digits -= 1

        if n < 0:
            return -inv_n

        return inv_n

    def reverse_integer_by_shifting(self, n: int) -> int:

        inv_n = 0
        n_placeholder = abs(n)
        while n_placeholder > 0:
            inv_n = inv_n * 10 + (n_placeholder % 10)
            n_placeholder = n_placeholder // 10

        if n < 0:
            return -inv_n

        return inv_n


if __name__ == "__main__":

    n = 123456
    ex = Ex8()
    print(ex.reverse_integer_by_digit_extraction(n))

    print(ex.reverse_integer_by_shifting(n))
