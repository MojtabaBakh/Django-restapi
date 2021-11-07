from django.shortcuts import redirect, render
import requests
import json




def student_list(request):
    response=requests.get("http://127.0.0.1:8000/student-list/").json()
    context={
         "students":response
    }

    return render ( request , "testapp\studentlist.html" , context )


def student_save(request):
    instance={"Name":"Mohammad" , "Family" : "Bagheri" , "Code" : "1234"} 
    headers={'content-type':"application/json"}   
    json_data = json.dumps(instance)
    print(json_data)
    requests.post("http://127.0.0.1:8000/student-save" , data=json_data , headers = headers )
    return redirect(student_list)