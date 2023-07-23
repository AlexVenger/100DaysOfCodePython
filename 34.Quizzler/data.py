import requests


def generate_questions(amount):
    url = "https://opentdb.com/api.php"
    response = requests.get(url, params={"amount": amount, "type": "boolean"})
    response.raise_for_status()
    questions = response.json()["results"]
    return questions


question_data = generate_questions(10)
