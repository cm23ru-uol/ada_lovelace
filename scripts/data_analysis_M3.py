import data_extraction_M1 as M1
import matplotlib.pyplot as plt
import os
def split_collated_file(collated_path):
    f = open(collated_path,'r')
    text = f.read()
    f.close()
    return text.strip().split('\n*\n')
#split the content into individual respondent blocks using '*'

def parse_all_sequence(collated_path) :
    blocks =split_collated_file(collated_path)
    sequences = []
    for i,block in enumerate(blocks,start=1):
        filename = f"temp_{i}.txt"
        with open(filename,'w') as f :
            f.write(block)
        try:
            sequences.append(M1.extract_answers_sequence(filename))
        except Exception as e:
            print("error")
        os.remove(filename)
    return sequences
#

def generate_means_sequence(collated_answers):
    data = parse_all_sequence(collated_answers)
    means = []
    for i in range(100):
        total = 0
        count = 0
        for respondent in data:
            answer =respondent[i]
            if answer != 0:
                total += answer
                count += 1
        means.append(total / count if count > 0 else 0)
    return means
#

def visualize_data (collated_answers,n):
    data =  parse_all_sequence(collated_answers)
    if n ==1:
        means = generate_means_sequence(collated_answers)
        plt.scatter(range(1,101),means)
        plt.title('mean answer per question')
        plt.xlabel("number of question")
        plt.ylabel("mean value")
        plt.show
    elif n ==2:
        for seq in data:
            plt.title("individual answers")
            plt.xlabel("number of question")
            plt.ylabel("answer")
            plt.show
    else:
        print("invalid value for n")
