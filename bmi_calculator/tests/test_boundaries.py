import pytest

#Runs 3 tests to make sure Underweight boundaries are correct       
class Test_Underweight:
    def test1(self):
        assert bmi.categorize(-0.1) == "Error"
    def test2(self):
        assert bmi.categorize(0) == "Underweight"
    def test3(self):
        assert bmi.categorize(18.4) == "Underweight"
    def test4(self):
        assert bmi.categorize(18.5) == "Normal Weight"
    def test5(self):
        assert bmi.categorize(18.6) == "Normal Weight"

#Runs 5 tests to make sure Normal Weight boundaries are correct       
class Test_normalWeight:
    def test1(self):
        assert bmi.categorize(18.4) == "Underweight"
    def test2(self):
        assert bmi.categorize(18.5) == "Normal Weight"
    def test3(self):
        assert bmi.categorize(18.6) == "Normal Weight"
    def test4(self):
        assert bmi.categorize(24.9) == "Normal Weight"
    def test5(self):
        assert bmi.categorize(25) == "Overweight"

#Runs 5 tests to make sure Overweight boundaries are correct
class Test_Overweight:
    def test1(self):
        assert bmi.categorize(24.9) == "Normal Weight"
    def test2(self):
        assert bmi.categorize(25) == "Overweight"
    def test3(self):
        assert bmi.categorize(25.5) == "Overweight"
    def test4(self):
        assert bmi.categorize(29.9) == "Overweight"
    def test5(self):
        assert bmi.categorize(30) == "Obese"

#Runs 3 tests to make sure Obese boundaries are correct
class Test_Obese:
    def test1(self):
        assert bmi.categorize(29.9) == "Overweight"
    def test2(self):
        assert bmi.categorize(30) == "Obese"
    def test3(self):
        assert bmi.categorize(30.1) == "Obese"