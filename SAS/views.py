from django.shortcuts import render
import pickle
from .models import *

# Create your views here.



def index(request):
    params = {'d':0}
    if request.method == "POST":
        text = request.POST.get('text')
        result,confidence = analysis(text)
        classes = {0:'Negative',1:'Positive'}
        con = float(confidence[0][result] * 100 )
        c = "{:.2f}".format(con)

        h = History(text=text,result = result[0],Confidence = con)
        h.save()
        audio = "Your text belongs to {} class with confidence of {} percentage".format(classes[result[0]],c)
        params={'result':classes[result[0]],"confidence":c,'d':1,'text':text}
    return render(request, 'index.html',params)


def history(request):
    past = History.objects.all().order_by('-id')[:10]
    params = {"past":reversed(past)}
    return render(request, 'history.html',params)




def analysis(text):

    with open('static/models/cvl_pickle','rb') as c:   
        cv = pickle.load(c)

    with open('static/models/MLPmodel_pickle','rb') as f:
        model = pickle.load(f)

    text_cv = cv.transform([text])
    result = model.predict(text_cv)
    confidence = model.predict_proba(text_cv)

    return result,confidence



