"""Sum numbers with different approaches."""
import pint

ureg = pint.UnitRegistry()

#from line_profiler import profile

#@profile
def sum_numbers_for(nums: list[int]) -> int:
    """Sum integers within list."""
    total: int = 0
    for num in nums:
        total = total + num
    return total

def sum_numbers_for_plus(nums: list[int]) -> int:
    """Sum integers within list."""
    total: int = 0
    for num in nums:
        total += num
    return total

#@profile
def sum_numbers_list(nums: list[int]) -> int:
    total: int = 0
    total = sum(nums)
    return total


def main() -> None:
    N: int = 10_000_000
    numbers: list[int] = list(range(1, N + 1))

    res_1 = sum_numbers_for(numbers)
    res_2 = sum_numbers_list(numbers)
    res_3 = sum_numbers_for_plus(numbers)

    print(f"{res_1=}\n{res_2=}")


if __name__ == "__main__":
    main()
