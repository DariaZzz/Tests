from math import sqrt


print(
    *filter(
        lambda x: x != 0,
        map(
            lambda n: n * (1 not in
                           map(
                               lambda x: n % x == 0,
                               range(2, int(sqrt(n)) + 1)
                           )
                           ),
            tuple(range(2, int(input()) + 1))
        )
    )
)
