from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    height = int(request.GET.get('number1'))
    weight = int(request.GET.get('number2'))

    bmi = 0
    category = ""  
    
    if request.GET.get('Calculate') == "":
        height = height * 0.025
        height = height * height

        weight = weight * 0.45

        bmi = weight/height

        if bmi < 0:
            category = "Error"
        elif bmi < 18.5:
            category = "Underweight"
        elif bmi >= 18.6 and bmi < 25:
            category = "Normal Weight"
        elif bmi >= 25 and bmi < 30 :
            category = "Overweight"
        elif bmi >= 30 :
            category = "Obese"
        else:
            category = "Error"   

    return render(request, 'result.html', {'bmi': bmi, 'category': category})