# generate 40 random numbers from 1-199 without repetition
import random

question_num_list = random.sample(range(1, 199), 40)
print(question_num_list)

# get question from json file
import json


def read_json():
    with open("/itil_foundation/questions_and_answers.json") as f:
        pop_data = json.load(f)
        return pop_data


# get the json data
questions_dict = read_json()


# print(questions_dict)


# generate 40 random questions
def generate_questions(question_num_list, questions_dict):
    generated_questions = {}
    generated_answers = {}

    # get the questions
    for i in range(1, 41):
        question_num = question_num_list[i - 1]
        single_question = questions_dict[str(question_num)]
        print(single_question)
        generated_questions[i] = single_question

    # get the answers
    for i in question_num_list:
        single_answer = questions_dict[str(i)]["answer"]
        generated_answers[i] = single_answer

    return generated_questions, generated_answers


question_num_list, questions_dict = generate_questions(question_num_list, questions_dict)
print(question_num_list, "\n", questions_dict)
