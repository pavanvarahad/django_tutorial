from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from google import genai
import json
import re

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
        Return the response EXCLUSIVELY as valid JSON. Do not include any introductory or concluding text, and do not wrap it in markdown code fences. The structure must be:
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

        try:
            client = genai.Client()
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite-preview", contents=final_system_prompt
            )
            raw_text = response.text.strip()

            # Strip markdown code fences if present (```json ... ``` or ``` ... ```)
            raw_text = re.sub(r'^```(?:json)?\s*', '', raw_text)
            raw_text = re.sub(r'\s*```$', '', raw_text)

            quiz_data = json.loads(raw_text)
            questions_json = json.dumps(quiz_data["questions"])
            return render(request, "quiz/quiz_attempt.html", {
                "quiz": quiz_data,
                "duration": quiz_duration,
                "questions_json": questions_json,
            })

        except Exception as e:
            return render(request, "quiz/create_quiz.html", {"error": f"Failed to generate quiz: {str(e)}"})


@login_required
def submit_quiz(request):
    if request.method == "POST":
        # Rebuild questions from hidden fields
        questions_json = request.POST.get("questions_data")
        quiz_title = request.POST.get("quiz_title")
        duration = request.POST.get("duration")

        try:
            questions = json.loads(questions_json)
        except Exception:
            return redirect("create_quiz")

        results = []
        score = 0

        for q in questions:
            q_id = str(q["id"])
            user_answer = request.POST.get(f"question_{q_id}", "")
            correct = q["correct_answer"]
            is_correct = user_answer.strip() == correct.strip()
            if is_correct:
                score += 1
            results.append({
                "id": q["id"],
                "question": q["question"],
                "options": q["options"],
                "user_answer": user_answer,
                "correct_answer": correct,
                "explanation": q["explanation"],
                "is_correct": is_correct,
            })

        total = len(questions)
        percentage = round((score / total) * 100) if total > 0 else 0

        context = {
            "quiz_title": quiz_title,
            "score": score,
            "total": total,
            "wrong": total - score,
            "percentage": percentage,
            "results": results,
            "duration": duration,
        }
        return render(request, "quiz/quiz_result.html", context)

    return redirect("create_quiz")

