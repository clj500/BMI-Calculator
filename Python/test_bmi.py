import bmi

#Runs 4 tests to make sure the equation is giving the right answer
class Test_ConvertHeight:
    def test1(self):
        assert bmi.convertHeight(63) == 2.4806250000000007
    def test2(self):
        assert bmi.convertHeight(67) == 2.805625
    def test3(self):
        assert bmi.convertHeight(69) == 2.9756250000000004
    def test4(self):
        assert bmi.convertHeight(70) == 3.0625

#Runs 4 tests to make sure the equation is giving the right answer
class Test_ConvertWeight:
    def test1(self):
        assert bmi.convertWeight(120) == 54.0
    def test2(self):
        assert bmi.convertWeight(125) == 56.25
    def test3(self):
        assert bmi.convertWeight(175) == 78.75
    def test4(self):
        assert bmi.convertWeight(210) == 94.5

#Runs 4 tests to make sure BMI is calculated properly and gives the right answer
class Test_CalculateBMI:
    def test1(self):
        assert bmi.calculateBMI(54.0, 3.0625) == 17.632653061224488
    def test2(self):
        assert bmi.calculateBMI(56.25, 2.480625) == 22.67573696145125
    def test3(self):
        assert bmi.calculateBMI(78.75, 2.805625) == 28.06861216306527
    def test4(self):
        assert bmi.calculateBMI(94.5, 2.975625) == 31.75803402646503

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
