"""
Testing for the namejoin.py file
"""

from mainpackage.namejoin import joinStrings

def testJoinStrings():
  """
  Tests the joinStrings() method
  """

  print("Starting tests for namejoin")

  result = joinStrings("x", "y", "z")
  assert result == "x y z"

  result = joinStrings("x", "y", "z", separator="/")
  expectedresult = "x/y/z"
  assert result == "x/y/z"

  result = joinStrings("x")
  assert result == "x"

  result = joinStrings()
  assert result == ""
  
  print("All tests succeeded for namejoin")

if __name__ == "__main__":
  testJoinStrings()