from django.shortcuts import render

# Create your views here.
from openai import OpenAI

client = OpenAI(api_key="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")
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Configure your OpenAI API key

@csrf_exempt
def generate_blog_titles(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            blog_content = data.get("content", "")

            if not blog_content:
                return JsonResponse({"error": "No blog content provided."}, status=400)

            prompt = f"Generate three engaging blog post titles for the following content:\n\n{blog_content}\n\nTitles:"

            response = client.chat.completions.create(model="gpt-3.5-turbo-1106",  # Adjust model as needed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            n=3,
            stop=["\n"])

            titles = [choice["message"]["content"] for choice in response.choices]

            return JsonResponse({"titles": titles})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)

# In your Django urls.p