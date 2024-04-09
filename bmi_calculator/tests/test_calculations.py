from django import urls
import pytest

class Test_ConvertHeight:
    def test1():
        assert result.height == 63
        assert result.height == 2.4806250000000007
    def test2():
        assert result.height == 67
        assert result.convertHeight == 2.805625
    def test3():
        assert result.height == 69
        assert result.convertHeight == 2.9756250000000004
    def test4():
        assert result.height == 70
        assert bmi.convertHeight == 3.0625

class Test_ConvertWeight:
    def test1():
        assert result.weight == 120
        assert bmi.convertWeight == 54.0
    def test2():
        assert result.weight == 125
        assert bmi.convertWeight == 56.25
    def test3():
        assert result.weight == 175
        assert bmi.convertWeight == 78.75
    def test4():
        assert result.weight == 210
        assert bmi.convertWeight == 94.5

class Test_CalculateBMI:
    def test1():
        assert bmi.calculateBMI(54.0, 3.0625) == 17.632653061224488
    def test2():
        assert bmi.calculateBMI(56.25, 2.480625) == 22.67573696145125
    def test3():
        assert bmi.calculateBMI(78.75, 2.805625) == 28.06861216306527
    def test4():
        assert bmi.calculateBMI(94.5, 2.975625) == 31.75803402646503

