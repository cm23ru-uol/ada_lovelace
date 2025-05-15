import data_preperation_M2 as m2
import data_extraction_M1 as m1
import data_analysis_M3 as m3
import os 

cloud_url = "https://raw.githubusercontent.com/djph7758-uol/Data/refs/heads/main/quiz_answers_named_a1_to_a25"
data_folder = r"C:\Users\richa_6\Data Science Leeds\MATH1604\Summative Group Project\ada_lovelace\data"
output_folder = r"C:\Users\richa_6\Data Science Leeds\MATH1604\Summative Group Project\ada_lovelace\output"

num_of_respondents = 25
for i in range(1, num_of_respondents+1):
    m2.download_answer_file(cloud_url=cloud_url, path_to_data_folder=data_folder, respondent_index=i)
m2.collate_answer_files(data_folder_path=data_folder, output_folder_path=output_folder)

#Directory containing the collated respondents
collated = r"C:\Users\richa_6\Data Science Leeds\MATH1604\Summative Group Project\ada_lovelace\output\collated_answers.txt"

respondent_files = os.listdir(data_folder)

respondent_response_data = []
for i in respondent_files:
    respondent_response_data.append(m1.extract_answers_sequence(f"{data_folder}\\{i}"))
    
# print(respondent_response_data[0])
# print(len(respondent_response_data[0]))

gms = m3.generate_means_sequence(collated)
m3.visualize_data(collated, 1)
# print(gms)
