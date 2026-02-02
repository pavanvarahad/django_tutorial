from django.shortcuts import render,redirect
from google import genai
from dotenv import load_dotenv
load_dotenv()


client = genai.Client()

output = "Hello"
# Create your views here.
def user_input_ui(request):
    return render(request,"diet_planner/index.html")

def show_output(request):
    return render(request,"diet_planner/output.html",{'output_text':output})

def process_input(request):
    # input_data = request.POST.get()
    user_data = {
        'user_name' : request.POST.get('name'),
        'age' : request.POST.get('age'),
        'current_weight' : request.POST.get('current_weight'),
        'target_weight' : request.POST.get('target_weight'),
        'prev_medical_history' :  request.POST.get('prev_medical_history'),
    }
    user_prompt = f"""
    You are a expert dietition, you are responsible to suggest a proper diet to the user based on theier input 
    input is given as below in a dictionary 
    ----------
    {user_data}
    ----------
    return output in a structured HTML format with proper headings, subheadings and bullet points and tables with inline styles.
    """ 
    
    response = client.models.generate_content(model="gemini-flash-lite-latest", contents=user_prompt)
    output = response.text
    output = output.replace('```html','').replace('```','')
    # print(user_prompt)
    return render(request,"diet_planner/output.html",{'output_text':output})

