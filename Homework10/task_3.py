# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a, b, c, expected", [
    pytest.param(10, 5, 2, 1),
    (100, 25, 4, 1),
    pytest.param(10, 0, 2, None, marks=pytest.mark.skip(reason="Skipping division by zero")),
], ids=["smoke_test", "normal_test", "skip_test"])
def test_division(a, b, c, expected):
    assert all_division(a, b, c) == expected
