class NeedleTooLongError:
    pass


class EX6(NeedleTooLongError):

    def __init__(self, needle: str, haystack: str):

        self.needle = needle
        self.haystack = haystack

    def needle_in_haystack(self) -> bool:

        if len(self.needle) > len(self.haystack):
            raise Exception(NeedleTooLongError)

        for i in range(len(self.haystack)):
            if self.needle == self.haystack[i : len(self.needle) + i]:
                return True

        return False


if __name__ == "__main__":

    needle = "su"
    haystack = "tiramiu"

    ex = EX6(needle, haystack)
    print(ex.needle_in_haystack())
