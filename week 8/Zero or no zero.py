print(
    '0' in set(
            open('input.txt', 'r', encoding='utf8').read()[1::].split()
    )
)
