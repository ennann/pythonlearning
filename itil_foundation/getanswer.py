## get answer from file
def read_txt(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        # lines = [line+"" for line in lines if "答案：" in line]
        return lines


txt_data = read_txt('/Users/Elton/Code-stuff/pythonlearning/itil_foundation/raw.txt')

list = []

for line in txt_data:
    if ("答案" in line):
        # print(line, "\n")
        answer = line.split("答案：")[1][0]

        list.append(answer)


# for index, item in enumerate(list):
#     print(index+1, item)


# get question from file
def read_txt_lines(filename):
    lines = read_txt(filename)
    long_str = []
    for line in lines:
        long_str.append(line)

    return str.join('', long_str)


questions_text = read_txt_lines('/Users/Elton/Code-stuff/pythonlearning/itil_foundation/raw.txt')
print(questions_text)

print("打印题目+答案")
# get questions from questions_text
questions_and_answers = {}

for i in range(199):

    if (i == 0):
        single_question, answer = questions_text.split("（共 199 题）")[1].split("答案：")[0], "A"
        question = single_question.split("A.")[0].strip()
    else:
        single_question, answer = questions_text.split("答案：")[i], questions_text.split("答案：")[i + 1][0]
        question = single_question.split("A.")[0].strip()[1:]

    choice_a = single_question.split("A.")[1].split("B.")[0].strip()
    choice_b = single_question.split("B.")[1].split("C.")[0].strip()
    choice_c = single_question.split("C.")[1].split("D.")[0].strip()
    choice_d = single_question.split("D.")[1].split("答案：")[0].strip()

    single_question_dict = {}
    single_question_dict[question] = {"choice_a": choice_a, "choice_b": choice_b, "choice_c": choice_c,
                                      "choice_d": choice_d}
    single_question_dict["answer"] = answer

    questions_and_answers[i + 1] = single_question_dict

    print(question, '\n', 'A.', choice_a, '\n', 'B.', choice_b, '\n', 'C.', choice_c, '\n', 'D.', choice_d, '\n', )

    # write to txt file
    with open('/Users/Elton/Code-stuff/pythonlearning/itil_foundation/questions.txt', 'a') as f:
        f.write(f"{question} \n A. {choice_a} \n B. {choice_b} \n C. {choice_c} \n D. {choice_d} \n")
        f.write('\n')

print(questions_and_answers)

print("\n\n\n\n")
# print 10 elements each line
for i in range(0, len(list), 10):
    # print(list[i:i+5]," ", list[i+5:i+10])
    print(f"{i + 1} - {i + 10}", str.join("", list[i:i + 5]), str.join("", list[i + 5:i + 10]))
