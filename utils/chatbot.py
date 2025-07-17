import base64
import groq
import random

import requests
from bs4 import BeautifulSoup
from transformers import pipeline

import os
from dotenv import load_dotenv

# Initialize Hugging Face Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(url):
    """Fetch article content and generate a concise AI-powered summary in bullet points."""
    try:
        # Fetch the article content
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            return "⚠️ Unable to retrieve the article."

        # Parse the article content
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        article_text = " ".join([p.get_text().strip() for p in paragraphs[:10]])  # Extract 10 meaningful paragraphs

        # Ensure extracted text is meaningful
        if len(article_text) < 500 or "news app" in article_text.lower():
            return "⚠️ Unable to extract relevant content for summarization."

        # Generate summary using Hugging Face model
        summary = summarizer(article_text, max_length=150, min_length=50, do_sample=False)
        summary_text = summary[0]['summary_text']

        # Convert the summary into bullet points
        bullet_points = summary_text.split(". ")  # Split sentences by period
        bullet_points = [f"• {point.strip()}" for point in bullet_points if point.strip()]  # Add bullet points
        bullet_points = "\n".join(bullet_points)  # Join into a single string with line breaks

        return bullet_points

    except requests.exceptions.RequestException as e:
        return f"⚠️ Error fetching article: {str(e)}"
    except Exception as e:
        return f"⚠️ Summarization Error: {str(e)}"


# API Key (Make sure it's securely stored)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = groq.Client(api_key=GROQ_API_KEY)

def encode_image(uploaded_file):
    """Convert uploaded image to a base64 string."""
    return base64.b64encode(uploaded_file.getvalue()).decode('utf-8')

def analyze_image(uploaded_image):
    """Analyze an uploaded image and generate an ESG rating based on nutritional values."""
    base64_image = encode_image(uploaded_image)
    
    prompt = (
        "Analyze the nutritional values from the uploaded image and provide a short ESG rating. "
        "Include only 1-2 pros and 1-2 cons about the product’s environmental impact. "
        "Keep the response short and to the point.\n\n"
        "Example response:\n"
        "**ESG Rating: 7/10**\n"
        "**Pros:** Uses organic ingredients, Low carbon footprint.\n"
        "**Cons:** High water consumption, Plastic packaging.\n\n"
        "Now analyze the provided image and generate a similar response."
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
            ]},
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.01,
    )
    
    return chat_completion.choices[0].message.content.strip()

def get_carbon_emission(question, distance_km, mode):
    """Get a short and to-the-point carbon emission analysis."""
    #user_query = f"Give a brief carbon emission analysis for a journey of {distance_km} km using {mode}. Keep it under 3 sentences."
    user_query = (
        f"Respond to this sustainability-related question while taking into account a {distance_km} km journey using {mode}: {question}. "
        "Ensure the answer is relevant, concise (under 4 sentences), and highlights the environmental impact."
    )

    messages = [
        {"role": "system", "content": "You are an expert on sustainability and carbon footprint analysis."},
        {"role": "user", "content": user_query}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=150  # ✅ Ensure concise response
    )

    return response.choices[0].message.content.strip()

# ✅ **Adding the Missing Function**
def generate_sustainability_report(distance_km, mode):
    """Generate an AI-powered sustainability report based on travel mode & distance."""
    messages = {
        "Car": [
            f"🚗 You traveled {distance_km} km by car, emitting approximately {round(distance_km * 0.21, 2)} kg of CO₂. "
            "Consider switching to public transport or biking for shorter trips to reduce emissions.",
            f"🚗 Driving {distance_km} km releases greenhouse gases equivalent to burning {round(distance_km * 0.21 / 2.3, 2)} liters of gasoline. "
            "Carpooling or using an electric vehicle could significantly cut your carbon footprint.",
        ],
        "Walk": [
            f"🚶‍♂️ Fantastic! You walked {distance_km} km, producing **zero** carbon emissions. Walking regularly not only saves CO₂ but also improves health! 🌱",
            f"🚶‍♂️ Walking {distance_km} km instead of driving saved you around {round(distance_km * 0.21, 2)} kg of CO₂. Keep up the great work!",
        ],
        "Bicycle": [
            f"🚴 Cycling {distance_km} km is a great choice! You avoided emitting around {round(distance_km * 0.21, 2)} kg of CO₂ compared to driving. 🚴‍♂️ Keep pedaling for a greener planet!",
            f"🚴‍♂️ Biking this distance instead of using a car saved approximately {round(distance_km * 0.21, 2)} kg of CO₂. Could you incorporate more cycling into your routine?",
        ],
        "Public Transport": [
            f"🚌 Great job choosing public transport! Your trip of {distance_km} km emitted **only about {round(distance_km * 0.06, 2)} kg of CO₂**, far less than a private car.",
            f"🚌 If you'd driven this distance in a car, you'd have emitted **{round(distance_km * 0.21, 2)} kg CO₂**—but by taking the bus/train, you cut that by over 70%! 🌍",
        ],
    }

    # Default message if mode is not recognized
    return random.choice(messages.get(mode, ["No sustainability report available."]))

def generate_diet_plan(age, weight, goal, diet_preference):
    """Generate a concise but goal-oriented AI-powered diet plan."""
    user_query =  (
        f"Create a concise, sustainable daily diet plan for a {age}-year-old weighing {weight} kg, "
        f"whose goal is {goal}, following a {diet_preference} diet. "
        "Prioritize plant-based proteins, seasonal & locally sourced foods, and low-carbon impact meals. "
        "Avoid highly processed foods and suggest eco-friendly meal choices. "
        "Provide 3-4 meal suggestions and include a sustainability impact summary."
    )

    messages = [
        {"role": "system", "content": "You are an expert nutritionist providing compact yet healthy goal-oriented diet plans."},
        {"role": "user", "content": user_query}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=600  # ✅ Keeps response short and effective
    )

    return response.choices[0].message.content.strip()
    
def ask_sustainability_ai(user_question):
    """Get a brief, to-the-point response for carbon footprint advice."""
    user_query = f"Provide a short, clear sustainability tip related to: {user_question}. Keep it under 3 sentences."

    messages = [
        {"role": "system", "content": "You are an expert on sustainability and carbon footprint reduction."},
        {"role": "user", "content": user_query}
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=150  # ✅ Ensures a brief response
    )

    return response.choices[0].message.content.strip()

