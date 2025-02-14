from django.shortcuts import render
from .predictor_logic import make_prediction

def predict(request):
    if request.method == 'POST':
        try:
            # Retrieve and convert form data
            age = float(request.POST.get('age'))
            sex = int(request.POST.get('sex'))
            cp = int(request.POST.get('cp'))
            trestbps = float(request.POST.get('trestbps'))
            chol = float(request.POST.get('chol'))
            fbs = int(request.POST.get('fbs'))
            restecg = int(request.POST.get('restecg'))
            thalach = float(request.POST.get('thalach'))
            exang = int(request.POST.get('exang'))
            oldpeak = float(request.POST.get('oldpeak'))
            slope = int(request.POST.get('slope'))
            ca = int(request.POST.get('ca'))
            thal = int(request.POST.get('thal'))
            
            # Pack the features into a list (make sure the order matches your model)
            features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            prediction = make_prediction(features)
        except Exception as e:
            prediction = f"Error: {str(e)}"
        return render(request, 'predictor/result.html', {'prediction': prediction})
    
    # Render the form for GET requests
    return render(request, 'predictor/index.html')
