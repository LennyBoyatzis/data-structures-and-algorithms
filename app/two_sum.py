from typing import List


def two_sum(arr: List[int], target: int) -> List[int]:
    """Returns a pair summing to target if exists"""
    compliments = set()

    for num in arr:
        diff = target - num
        if diff in compliments:
            return [num, diff]
        compliments.add(diff)
    return []

if __name__ == '__main__':
    arr = [1, 2, 4, 10]
    target = 3
    result = two_sum(arr, target)
    assert result == [1, 2]
