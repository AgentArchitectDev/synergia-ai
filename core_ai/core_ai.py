import re

def detect_category(prompt: str):
    prompt = prompt.lower()

    if "gastronom" in prompt or "restaurante" in prompt:
        return "05_gastronomia_experiencial"

    if "arquitectura" in prompt or "casa" in prompt:
        return "04_arquitectura_interiorismo"

    return "11_Ejemplo1"


def build_json(prompt: str):
    return {
        "tagline": prompt,
        "item_1_name": "Item generado IA",
        "item_1_img": "https://images.unsplash.com/photo-1544025162-d76694265947",
        "item_1_price": "$10.000"
    }


def build_from_prompt(prompt: str):
    template = detect_category(prompt)
    data = build_json(prompt)

    return {
        "status": "ok",
        "template": template,
        "data": data
    }
