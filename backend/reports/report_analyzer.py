import re

positive_words = [
    "improved", "recovered", "better", "stable", "effective"
]

negative_words = [
    "worsened", "severe", "not improved", "adverse", "deteriorated"
]

def analyze_report(text):
    text = text.lower()

    drug_pattern = r"(paracetamol|ibuprofen|metformin|aspirin)"
    drugs = re.findall(drug_pattern, text)

    side_effects = []
    if "nausea" in text:
        side_effects.append("nausea")
    if "rash" in text:
        side_effects.append("rash")
    if "vomiting" in text:
        side_effects.append("vomiting")

    effect = "No clear effect"

    for w in positive_words:
        if w in text:
            effect = "Improved"

    for w in negative_words:
        if w in text:
            effect = "Worsened"

    return {
        "drugs": list(set(drugs)),
        "side_effects": side_effects,
        "effectiveness": effect
    }
