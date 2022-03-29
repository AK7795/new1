import pytest
import main


#@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(3,2,5),(1,5,6),(5,7,12)])
def test_add(a,b,c):
    r1 = main.add(a,b)
    assert c == r1


@pytest.mark.parametrize("a,b,c",[(3,2,1),(1,5,-4),(5,7,-2)])
def test_sub(a,b,c):
    r1 = main.sub(a,b)
    assert c==r1


@pytest.mark.parametrize("a,b,c",[(3,2,6),(1,5,5),(5,7,35)])
def test_mul(a,b,c):
    r1 = main.mul(a,b)
    assert c == r1


@pytest.mark.parametrize("a,b,c",[(4,2,2),(10,5,2),(15,3,5)])
def test_div(a,b,c):
    r1 = main.div(a,b)
    assert c == r1
