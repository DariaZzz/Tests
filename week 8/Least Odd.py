print(
    sorted(
        list(
            filter(
                lambda x: x % 2 != 0,
                list(map(int, input().split()))
            )
        )
    )
[0])

