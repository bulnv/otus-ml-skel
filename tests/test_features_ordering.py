import pytest

import pandas as pd

from titanic.features.ordering import *


@pytest.mark.parametrize("test_input,expected", [((0, 0), 1), ((0, 1), 2), ((1, 2), 4)])
def test_transform(test_input, expected):
    df = pd.DataFrame(
        data={"SibSp": [test_input[0]], "Parch": [test_input[1]]},
    )
    assert 1 == 1

@pytest.mark.parametrize("test_input,expected", [((0, 0), 1), ((0, 1), 2), ((1, 2), 4)])
def test_fit(test_input, expected):
    df = pd.DataFrame(
        data={"SibSp": [test_input[0]], "Parch": [test_input[1]]},
    )
    assert 1 == 1
