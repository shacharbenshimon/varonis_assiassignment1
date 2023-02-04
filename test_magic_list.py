import pytest
from contextlib import nullcontext as does_not_raise
from dataclasses import dataclass
from magic_list import MagicList


@pytest.mark.parametrize("index1, value1, index2, value2, expectation",
                         [(0, 4, 1, 9, does_not_raise()),
                          (0, 4, 2, 9, pytest.raises(IndexError))],
                         ids=['indexes and values that will pass',
                              'indexes and values that will raise exception'])
def test_magic_list_without_class_type(index1, value1, index2, value2, expectation):
    b = MagicList()
    with expectation:
        b[index1] = value1
        assert b == [value1]
        b[index2] = value2
        assert b == [value1, value2]


@pytest.mark.parametrize("ClassName, class_attribute, index1, value1, index2,"
                         " value2, expectation",
                         [('Person', 'age', 0, 4, 1, 9, does_not_raise()),
                          ('Person', 'age', 0, 4, 7, 9, pytest.raises(IndexError))],
                         ids=['indexes and values that will pass', 'indexes and values that will raise exception'])
def test_magic_list_with_class(ClassName, class_attribute, index1, value1, index2, value2, expectation):
    @dataclass
    class ClassName:
        class_attribute: int = 1
    d = MagicList(class_type=ClassName)
    with expectation:
        d[index1].class_attribute = value1
        assert d == [ClassName(class_attribute=value1)]
        d[index2].class_attribute = value2
        assert d == [ClassName(class_attribute=value1),
                     ClassName(class_attribute=value2)]
