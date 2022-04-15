def get_smallest_pair(numbers: []) -> list:
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return [m1, m2]


def smallest_sum(v: int, length: int, numbers: []) -> int:
    """
   :param v: not greater than
   :param length: size of input
   :param numbers: array of numbers
   :return: quantity of the given numbers that can be added up
   with other two of these numbers so that the result is not greater than v.

   We get the smallest 2 elements, and to try with other numbers.
   but for the first min element: we sum up with second, third.
   and the second min element: we sum up with first and third.
   """
    count = 0

    first_smallest_pair = get_smallest_pair(numbers)
    smallest_element = first_smallest_pair[0]
    numbers.remove(smallest_element)

    second_smallest_pair = get_smallest_pair(numbers)
    second_smallest_element = second_smallest_pair[0]
    numbers.remove(second_smallest_element)

    count += 1 if smallest_element + sum(second_smallest_pair) <= v else 0
    count += 1 if second_smallest_element + smallest_element + second_smallest_pair[1] <= v else 0

    sum_smallest_elements = sum(first_smallest_pair)

    elements = list(filter(lambda number: sum_smallest_elements + number <= v, numbers))
    return len(elements) + count


if __name__ == '__main__':
    assert get_smallest_pair([1, 2, 3, 4]) == [1, 2]
    assert get_smallest_pair([-1, -2, -3, 4]) == [-3, -2]
    assert get_smallest_pair([0, 4, 1, 2]) == [0, 1]
    assert get_smallest_pair([0, 0, 1, 4]) == [0, 0]
    assert get_smallest_pair([4, 1, 0, 0]) == [0, 0]

    assert smallest_sum(15, 5, [12, 2, 5, 14, 1]) == 4
    assert smallest_sum(6, 3, [1, 2, 3]) == 3
    assert smallest_sum(-20, 6, [25, 15, 5, -5, -15, -25]) == 5
    assert smallest_sum(100, 3, [33, 34, 35]) == 0

    # Driver, you can uncomment it.
    # v = int(input())
    # size = int(input())
    # numbers = list(map(int, input().split(" ")))
    # print(smallest_sum(v, size, numbers))

