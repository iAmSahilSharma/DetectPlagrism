from django.shortcuts import render     #render our hrml file
from difflib import SequenceMatcher
import json

def button(request):
    return render(request,'home.html')

def output(request):
    with open('/home/linux/allHere/Project-Py/Project2.0/plagrism2/plagrism2/file1.txt') as file1, open('/home/linux/allHere/Project-Py/Project2.0/plagrism2/plagrism2/file2.txt') as file2:
    
        file1_data = file1.read()
        file2_data = file2.read()
        similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
        data = json.dumps(similarity)
        return render(request,'home.html',{'data':int(similarity*100)})
