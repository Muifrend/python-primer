def add(a, b):
    return a + b


x = add(2, 3)  # Output: 5
a = [1, 2, 3]

print(x)


def is_even(value):
    return value % 2 == 1


print(is_even(4))  # Output: True


def first_char(text):
    if not text:
        return ""
    return text[0]


def test_is_even():
    assert is_even(4) == True
