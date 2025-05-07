# ------------------------------------------------------------
# Function: extract_answers_sequence
#   read one respondent txt file → list of 100 ints
# ------------------------------------------------------------

def extract_answers_sequence(file_path):
    # answers will store final 100 numbers
    answers = []
    # idx counts which option (1‑4) inside current question
    idx = 0
    # mark saves the option number that has an 'x'
    mark = None

    # open file and read line by line
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()  # remove tail spaces/newline

            # not an option line → skip
            if not line.startswith('['):
                continue

            idx += 1  # we saw one more option

            # option chosen?
            if 'x' in line.lower():
                mark = idx

            # after 4 options the question is done
            if idx == 4:
                answers.append(mark or 0)  # 0 if no option chosen
                idx, mark = 0, None        # reset for next question

    # sanity check
    if len(answers) != 100:
        raise ValueError('need 100 answers')

    return answers


# ------------------------------------------------------------
# Function: write_answers_sequence
#   save list to answers_list_respondent_<n>.txt
# ------------------------------------------------------------
def write_answers_sequence(answers, n):
    if len(answers) != 100:
        raise ValueError('len not 100')

    file_name = f'answers_list_respondent_{n}.txt'

    # write numbers line by line
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(map(str, answers)))
