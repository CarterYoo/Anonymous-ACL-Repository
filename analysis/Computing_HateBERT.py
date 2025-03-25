import json
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from itertools import combinations

# Load HateBERT tokenizer and model
model_name = "GroNLP/hateBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Load puzzle data from Real_Data_Ans.json
with open('Real_Data_Ans.json', 'r', encoding='utf-8') as file:
    puzzles = json.load(file)

def get_embedding(word):
    inputs = tokenizer(word, return_tensors='pt')
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.detach().numpy().flatten()


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

results = {}

for puzzle in puzzles:
    puzzle_id = puzzle['id']
    puzzle_results = {}
    categories = {ans['group']: ans['members'] for ans in puzzle['answers']}

    for category_name, words in categories.items():
        embeddings = [get_embedding(word) for word in words]

        # Semantic Cohesion Calculation
        pairwise_scores = [cosine_similarity(emb1, emb2) for emb1, emb2 in combinations(embeddings, 2)]
        cohesion_score = np.mean(pairwise_scores)

        # Ambiguity Index Calculation (simple threshold method)
        ambiguity_count = 0
        for word, emb in zip(words, embeddings):
            ambiguous = False
            for other_category, other_words in categories.items():
                if other_category == category_name:
                    continue
                other_embs = [get_embedding(w) for w in other_words]
                sim_scores = [cosine_similarity(emb, o_emb) for o_emb in other_embs]
                if max(sim_scores) > 0.8:  # Ambiguity threshold
                    ambiguous = True
                    break
            ambiguity_count += ambiguous
        ambiguity_index = ambiguity_count / len(words)

        puzzle_results[category_name] = {
            "Cohesion_Score": round(float(cohesion_score), 3),
            "Ambiguity_Index": round(float(ambiguity_index), 3)
        }

    results[f"Puzzle {puzzle_id}"] = puzzle_results

# Compute Puzzle-level average difficulty
average_cohesion = []
average_ambiguity = []
for puzzle in results.values():
    for cat in puzzle.values():
        average_cohesion.append(cat["Cohesion_Score"])
        average_ambiguity.append(cat["Ambiguity_Index"])

final_cohesion_avg = np.mean(average_cohesion)
final_ambiguity_avg = np.mean(average_ambiguity)

print(f"Overall Average Cohesion: {final_cohesion_avg:.3f}")
print(f"Overall Average Ambiguity: {final_ambiguity_avg:.3f}")
