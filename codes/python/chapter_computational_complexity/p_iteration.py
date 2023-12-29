"""
File: p_iteration.py
Created Time: 2023-12-29
Author: Max Feng
"""


def for_loop(n: int) -> int:
    """
    循环迭代
    :param n: 迭代次数
    :return: 迭代次数
    """
    result = 0
    # 循环计算1，2，3....n+1的求和
    for i in range(1, n+1):
        result += i
    return result


def while_loop(n: int) -> int:
    """
    循环迭代
    :param n: 迭代次数
    :return: 迭代次数
    """
    result = 0
    # 循环计算1，2，3...n+1的求和
    i = 1
    while i <= n:
        result += i
        i += 1
    return result


def while_loop_2(n: int) -> int:
    """
    循环迭代
    :param n: 迭代次数
    :return: 迭代次数
    """
    result = 0
    # 循环计算某组数据的求和
    i = 1
    while i <= n:
        print(f'i:{i}')
        result += i
        i += 1
        i *= 2
    return result


def nested_loop(n: int) -> int:
    """
    嵌套循环迭代
    :param n: 迭代次数
    :return: 迭代次数
    """
    result = ""
    # 循环计算1，2，3...n+1的求和
    for i in range(1, n+1):
        for j in range(1, n+1):
            result += f"({i}, {j}), "
    return result


if __name__ == "__main__":
    """
    主函数
    """
    n = 5
    res = for_loop(n)
    print(f'\n result for loop = {res}')

    res = while_loop(n)
    print(f'\n result while loop = {res}')

    res = while_loop_2(n)
    print(f'\n result while loop 2 = {res}')

    res = nested_loop(n)
    print(f'\n result nested loop = {res}')