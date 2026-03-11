from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from google import genai

from dotenv import load_dotenv
load_dotenv()
# Create your views here.
@login_required
def dashboard(request):
    return render(request, "quiz/dashboard.html")

@login_required
def create_quiz(request):
    if request.method == "GET":
        return render(request, "quiz/create_quiz.html")
    if request.method == "POST":
        quiz_title = request.POST.get("quiz_title")
        subject = request.POST.get("subject")
        topic = request.POST.get("topic")
        num_questions = request.POST.get("num_questions")
        quiz_duration = request.POST.get("quiz_duration")
        difficulty = request.POST.get("difficulty")
        description = request.POST.get("description")

        # Basic validation — ensure required fields are filled
        if not all([quiz_title, subject, topic, num_questions, quiz_duration, difficulty]):
            return render(request, "quiz/create_quiz.html", {"error": "Please fill in all required fields."})

        system_prompt = """
        **Role:** You are an Elite Educational Assessment Designer. Your goal is to generate high-quality, pedagogically sound multiple-choice quizzes based on specific user parameters.

        **Input Parameters:**
        - Quiz Title, Subject, Topic, Number of Questions, Difficulty (Easy, Medium, Hard), and Description (Optional).

        **Output Format:**
        Return the response EXCLUSIVELY as a Python dictionary. Do not include any introductory or concluding text. The structure must be:
        {
            "quiz_title": "string",
            "metadata": {
                "subject": "string",
                "topic": "string",
                "difficulty": "string",
                "description": "string"
            },
            "questions": [
                {
                    "id": 1,
                    "question": "string",
                    "options": ["Option A", "Option B", "Option C", "Option D"],
                    "correct_answer": "string",
                    "explanation": "string"
                }
            ]
        }

        **Content Guidelines:**
        1. **Difficulty Calibration:**
        - Easy: Focus on basic recall and definitions.
        - Medium: Focus on application and conceptual understanding.
        - Hard: Focus on analysis, synthesis, and complex problem-solving.
        2. **Distractor Quality:** Ensure the three incorrect options are plausible and related to the topic. Avoid "None of the above" or "All of the above" unless necessary.
        3. **Clarity:** Questions must be unambiguous. Use professional and academic language.
        4. **Explanations:** Provide a concise explanation (2-3 sentences) detailing why the correct answer is right and, if helpful, why other options are incorrect.
        5. **Validation:** Ensure the `correct_answer` matches exactly one of the strings in the `options` list.   
        
        """

        user_input_data = f"""
        Quiz Title: {quiz_title}
        Subject: {subject}
        Topic: {topic}
        Number of Questions: {num_questions}
        Duration: {quiz_duration} minutes
        Difficulty: {difficulty}
        Description: {description}
        """
        final_system_prompt = system_prompt + "\n User input data:" + user_input_data

        client = genai.Client()
        response = client.models.generate_content(
                model="gemini-3-flash-preview", contents=final_system_prompt
            )
        print(response.text)

        # AI generation logic will go here
        return render(request, "quiz/create_quiz.html", {"success": "Quiz created successfully! Generating your quiz..."})
