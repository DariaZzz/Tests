from functools import reduce


print(
    reduce(
        lambda a, b: a * b,
        list(
            map(
                lambda x: x ** 5,
                list(map(int, input().split()))
            )
        )
    )
)
