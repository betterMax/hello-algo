"""
File: p_iteration.py
Created Time: 2023-12-29
Author: Max Feng
"""


def recur(n: int) -> int:
    """递归"""
    # 终止条件
    if n == 1:
        return 1
    # 递归调用
    res = recur(n - 1)
    # 归：返回结果
    return n + res


def fib(n: int) -> int:
    """斐波那契数列"""
    # 终止条件
    if n == 1 or n == 2:
        return n - 1
    # 递归调用
    res = fib(n - 1) + fib(n - 2)
    # 归：返回结果f(n)
    return res


def for_loop_recur(n: int) -> int:
    """使用迭代模拟递归"""
    # 使用一个显式的栈来模拟系统调用栈
    stack = []
    res = 0
    # 递：递归调用
    for i in range(n, 0, -1):
        # 通过“入栈操作”模拟“递”
        stack.append(i)
    # 归：返回结果
    while stack:
        # 通过“出栈操作”模拟“归”
        res += stack.pop()
    # res = 1+2+3+...+n
    return res


def tail_recur(n, res):
    """尾递归"""
    if n == 0:
        return res
    return tail_recur(n - 1, n + res)


if __name__ == '__main__':
    n = 5
    print(f"递归：{recur(n)}")
    print(f"斐波那契数列：{fib(n)}")
    print(f"使用迭代模拟递归：{for_loop_recur(n)}")
    print(f"尾递归：{tail_recur(n, 0)}")