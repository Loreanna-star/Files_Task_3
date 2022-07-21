import os

def count_lines(file_name): # считает количество строк в файле
    with open(file_name, encoding = 'utf-8') as file_obj:
        counter = 0
        for i in file_obj:
            counter += 1
    return counter

def get_file_list(): # получает список файлов .txt в текущей папке
    directory = os.getcwd()
    files = os.listdir(directory)
    files_txt = list(x for x in files if x.endswith('.txt'))
    return files_txt

def get_file_dict_with_lines_quantity(): # получает словарь на основе ранее полученного списка файлов, где ключ - название файла, значение - количество строк
    dict = {}
    files_in_dir = get_file_list()
    for file in files_in_dir:
        dict[file] = count_lines(file)
    return dict

def create_summary_file(): # создает файл summary.txt в текущей папке с требуемыми в условии данными
    files_dict = get_file_dict_with_lines_quantity()
    sorted_keys = sorted(files_dict, key = files_dict.get) # отсортированный список ключей (отсортированное количество строк в файлах)

    with open ("summary.txt", "a", encoding = "utf-8") as summary_file:   
        for element in sorted_keys:                  
            summary_file.write(f'{element}\n{str(files_dict[element])}\n')  
            with open(element, encoding = "utf-8") as file:
                summary_file.write(f'{file.read()}\n')               
    return

create_summary_file()
        