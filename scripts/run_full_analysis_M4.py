import data_preperation_M2 as m2
import data_extraction_M1 as m1

cloud_url = "https://raw.githubusercontent.com/djph7758-uol/Data/refs/heads/main/quiz_answers_named_a1_to_a25"
data_folder = r"C:\Users\richa_6\Data Science Leeds\MATH1604\Summative Group Project\ada_lovelace\data"
output_folder = r"C:\Users\richa_6\Data Science Leeds\MATH1604\Summative Group Project\ada_lovelace\output"

for i in range(1, 26):
    m2.download_answer_file(cloud_url=cloud_url, path_to_data_folder=data_folder, respondent_index=i)
m2.collate_answer_files(data_folder_path=data_folder, output_folder_path=output_folder)