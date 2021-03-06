import os
import sys
import pickle
sys.path.append("layout_solver")
sys.path.append("theme_classifier")
from layout_solver import analyze_layout, generate_words
from clue_maker import generate_clues
from gui import run_intro_gui, run_exit_gui

test_mat = run_intro_gui()
word_dict = analyze_layout.analyze_layout(test_mat)
if word_dict == -1:
    print("CROSSWORD LAYOUT BAD \n")
    exit(0)
print(test_mat)
with open(os.path.join("theme_classifier", "pkl_storage", "theme_dictionary.pkl"), "rb") as f:
    themed_words = pickle.load(f)
new_layout, theme_name = generate_words.create_crossword(word_dict, len(test_mat[0]), len(test_mat), \
                                                        themed_words, 1, 0, 0)
generate_clues(word_dict)
print(word_dict)
print(new_layout)
print("\n")
run_exit_gui(test_mat, word_dict, theme_name)