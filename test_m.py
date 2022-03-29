import pytest
import main


@pytest.mark.parametrize("a,b",[(3,2),(1,5),(5,7)])
def test_add(a,b):
    r1 = main.add(a,b)


@pytest.mark.parametrize("a,b",[(3,2),(1,5),(5,7)])
def test_sub(a,b):
    r1 = main.sub(a,b)


@pytest.mark.parametrize("a,b",[(3,2),(1,5),(5,7)])
def test_mul(a,b):
    r1 = main.mul(a,b)


@pytest.mark.parametrize("a,b",[(3,2),(1,5),(5,7)])
def test_div(a,b):
    r1 = main.div(a,b)