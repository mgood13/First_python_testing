def test_add_three():
    """This tests the function which is intended to add three numbers together.
    """
    from Add_Divide	import add_three
    s = add_three(1,2,3)
    assert s == 6

def test_divide_by_three():
    """This tests the function which is intended to divide a number by three.
    """
    from Add_Divide import divide_by_three
    d = divide_by_three(3)
    assert d == 1.0

