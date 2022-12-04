import random


class randomNumGenerator:

    def __init__(self, amount: int, minRange: int, maxRange: int):
        self._amount = amount
        self._minRange = minRange
        self._maxRange = maxRange

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, new_amount: int) -> None:
        self._amount = new_amount

    @property
    def minRange(self) -> int:
        return self._minRange

    @minRange.setter
    def minRange(self, new_minRange: int) -> None:
        self._minRange = new_minRange

    @property
    def maxRange(self) -> int:
        return self._maxRange

    @maxRange.setter
    def maxRange(self, new_maxRange: int) -> None:
        self._maxRange = new_maxRange

    def generate(self) -> list:
        # assert preconditions
        assert self._minRange < self._maxRange, "MinRange must be less than maxRange"
        assert self._amount > 0, "Amount must be greater than 0"

        # generate random numbers
        random_numbers = [random.randint(self._minRange, self._maxRange) for i in range(self._amount)]

        # assert postconditions
        assert len(random_numbers) == self._amount, "Amount of random numbers must be equal to amount parameter"
        assert all([i >= self._minRange and i <= self._maxRange for i in
                    random_numbers]), "All random numbers must be within the range"

        return random_numbers


if __name__ == "__main__":
    r = randomNumGenerator(10, -100, 100)
    print(r.generate())

    print("Second commit")
    print("Third commit")
