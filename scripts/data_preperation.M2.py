import requests
import os

#https://raw.githubusercontent.com/djph7758-uol/Data/refs/heads/main/quiz_answers_named_a1_to_a25/a1.txt
        
def download_answer_file(cloud_url, path_to_data_folder, respondent_index):

    # Make sure the folder exists (or create it)
    os.makedirs(path_to_data_folder, exist_ok=True)

    # Build URL and output path
    filename = f"a{respondent_index}.txt"
    url = f"{cloud_url}/{filename}"
    out_path = os.path.join(path_to_data_folder, f"answers_respondent_{respondent_index}.txt")

    # Print diagnostics
    print("→ Current working directory:", os.getcwd())
    print("→ Absolute output path:    ", os.path.abspath(out_path))
    print("→ Downloading from URL:     ", url)

    # Download
    resp = requests.get(url)
    resp.raise_for_status()
   
    # Write to disk
    with open(out_path, "w") as fout:
        fout.write(resp.text)

# Call the function
cloud_url = "https://raw.githubusercontent.com/djph7758-uol/Data/refs/heads/main/quiz_answers_named_a1_to_a25"
data_folder = r"C:\Users\shash\Downloads\Data Science Project\ada_lovelace\data"

for i in range(1, 26):
    download_answer_file(cloud_url, data_folder, i)

def collate_answer_files(data_folder_path):
    output_folder_path = r"C:\Users\shash\Downloads\Data Science Project\ada_lovelace\output"
    os.makedirs(output_folder_path, exist_ok=True)

    output_path = os.path.join(output_folder_path, "collated_answers.txt")

    with open(output_path, "w") as outfile:
        for i in range(1, 26):
            file_path = os.path.join(data_folder_path, f"answers_respondent_{i}.txt")

            with open(file_path, "r") as infile:
                    outfile.write(f"Respondent {i}:\n")
                    outfile.write(infile.read())  
                    outfile.write("\n*\n")

collate_answer_files(r"C:\Users\shash\Downloads\Data Science Project\ada_lovelace\data")