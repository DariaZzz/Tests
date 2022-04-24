from functools import reduce

print(
    *reduce(
        lambda a, b: list(
            map(
                lambda a1: abs(int(a1[0]) - int(a1[1])),
                zip(a, b)
            )
        ),
        list(
            map(
                lambda x: x.rstrip().split(),
                open('input.txt', 'r', encoding='UTF-8')
            )
        )[1:]
    )
)
