#SDEV 220    11/20/2023
#M05 Programming Assignment
#https://realpython.com/python-testing/#testing-your-code
#Testing Your Code

def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"
    
def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")