import random

from datasets import load_dataset
from pyprojroot import here
import spacy


dataset = str(here("t4d/data/ToMi.csv"))
data = load_dataset("csv", data_files=dataset)

nlp = spacy.load("en_core_web_trf")

tom_subset = data["train"].filter(lambda x: x["qTypeTomOrNot"] == True)

def find_characters(text):
    characters = []
    actions = ["entered", "moved", "exited"]
    
    words = text.split()

    for action in actions:
        indices = [index for index, word in enumerate(words) if word == action]

        for index in indices:
            character = words[index - 1]
            if character not in characters:
                characters.append(character)

    return characters

def find_character_who_moved(text):
    words = text.split()

    index = words.index("moved")

    return words[index - 1]

def find_moved_object(text):
    words = text.split()

    index = words.index("moved")

    return words[index + 2]

def process(instance):
    characters = find_characters(instance["story"])
    character_who_moved = find_character_who_moved(instance["story"])
    moved_object = find_moved_object(instance["story"])
    
    for c in nlp(instance["question"]).ents:
        if c.text != character_who_moved:
            answer = c.text
    
    distracting_characters = [c for c in characters if c not in [answer, character_who_moved]]
    
    cs = random.sample([character_who_moved, answer], 2)
    
    append_statement = "{} and {} plan to use the {} soon.".format(*cs, moved_object)
    
    question = "Who among the individuals would benefit from receiving helpful information?\n"
    for i, c in enumerate(random.sample(characters, len(characters))):
        question += f"{chr(65 + i)}. {c}\n"
    question += f"{chr(65 + len(characters))}. None of the above"

    return {
        "story": instance["story"] + " " + append_statement,
        "question": question,
        "answer": answer,
        "characters": characters,
        "distracting_characters": distracting_characters
    }

t4d_dataset = tom_subset.map(process, remove_columns = list(tom_subset.features))

t4d_dataset.save_to_disk(here("t4d/data/t4d_dataset"))