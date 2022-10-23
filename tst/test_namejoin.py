"""
Testing for the namejoin.py file

This file used to be called `testNameJoin.py`. Naming conventions aside, this did not work with pytest. For pytest to work, your
file names should use lowercase letters and "_".
"""

import pytest
from mainpackage.namejoin import joinStrings


def test_joinStrings():
    """
    Tests the joinStrings() method
    """

    print("Starting tests for namejoin")

    result = joinStrings("x", "y", "z")
    assert result == "x y z"

    result = joinStrings("x", "y", "z", separator="/")
    assert result == "x/y/z"

    result = joinStrings("x")
    assert result == "x"

    result = joinStrings()
    assert result == ""

    print("All tests succeeded for namejoin")


@pytest.mark.skip(reason="to be implemented")
def test_joinStringsSmart():
    """
    Tests the joinStringsSmart() method

    Not yet implemented
    """

    pass


# pytest will run this test function automatically as long as it starts with "test_". We do not need to run it ourselves
# if __name__ == "__main__":
#     test_joinStrings()
