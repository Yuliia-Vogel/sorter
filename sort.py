import os
import sys 
import shutil
from pathlib import Path

import normalization
import del_empty_dirs

def main():
    lenargv = len(sys.argv) # sys.argv - через нього отримуємо шлях до папки, яку треба опрацювати
    if lenargv != 2: # перевіряємо довжину аргумента: [0]назва файлу sort.py і [1]шлях до папки
        print("Incorrect number of arguments! exit1")
        exit(1)
    elif lenargv == 2:
        print('Agrv is Ok')
        path = sys.argv[1] 
        if os.path.isfile(path): # перевірка, чи шлях є папкою, якщо не папка - то екзіт
            print("this is file, cannot wirk with it, exit")
            exit(1)
        elif os.path.isdir(path): 
            print("this is folder, I go to work with it")
            folder_processing(path) #тут виклик функції обробки папки, бо все з посиланням на папку Ок
        else:
            print("file type is different, cannot work with it, exit")
            

def folder_processing(path): # функція обробки папки
    print("I started folder_processing now")

    images = [] # створюю пусті лісти, куди я складатиму назви файлів відповідних типів
    documents = []
    audio = []
    video = []
    archives = []
    others = []
    all_file_types = set() #сюди складаємо суфікси (розширення) відомих розширень
    other_types = set() #сюди складаємо суфікси (розширення) невідомих розширень
    ignore_list = set(['images', 'documents', 'audio', 'video', 'archives', 'others'])

    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if d not in ignore_list]
        for file in files:
            file_path = os.path.join(root, file) # отримую повну назву файлів із шляхом
            filename = file.rsplit(".", 1) #розділяю коротку назву файлів на 2 частини (справа, лише 1 розділення)

            if filename[1]=='jpeg' or filename[1]=='png' or filename[1]=='jpg' or filename[1]=='svg':
                try:
                    im_dir_path = os.path.join(path, 'images') # створення шляху папки
                    os.mkdir(im_dir_path) # створення папки
                    print("dir 'images' created")
                except FileExistsError: # якщо папка вже існує 
                    print("folder images exists")
                    pass
                norm_name = normalization.normalize(file)
                new_file_path = os.path.join(im_dir_path, norm_name)
                dup = 0
                while os.path.isfile(new_file_path): # перевіряю, чи такий файл уже існує
                    print(f'file already exists!') # ок, така назва файлу вже існує
                    splitted_n_name = norm_name.rsplit(".", 1) # знов ділимо назву для апдейту назви
                    dup += 1
                    n = f"{splitted_n_name[0]}_{dup}" 
                    print(n)
                    with_end = f'{n}.{splitted_n_name[1]}'
                    new_file_path = (os.path.join(im_dir_path, with_end))
                shutil.move(file_path, new_file_path)
                images.append(norm_name)
                all_file_types.add(filename[1])

            elif filename[1]=='doc' or filename[1]=='docx' or filename[1]=='txt' or filename[1]=='pdf' or filename[1]=='xlsx' or filename[1]=='pptx':
                try:
                    doc_dir_path = os.path.join(path, 'documents') # створення шляху папки
                    os.mkdir(doc_dir_path) # створення папки
                    print("dir 'documents' created")
                except FileExistsError: # якщо папка вже існує 
                    print("folder documents exists")
                    pass
                norm_name = normalization.normalize(file)
                new_file_path = os.path.join(doc_dir_path, norm_name)
                dup = 0
                while os.path.isfile(new_file_path): # перевіряю, чи такий файл уже існує
                    print(f'file already exists!') # ок, така назва файлу вже існує
                    splitted_n_name = norm_name.rsplit(".", 1) # знов ділимо назву для апдейту назви
                    dup += 1
                    n = f"{splitted_n_name[0]}_{dup}" 
                    print(n)
                    with_end = f'{n}.{splitted_n_name[1]}'
                    new_file_path = (os.path.join(im_dir_path, with_end))
                shutil.move(file_path, new_file_path)
                documents.append(norm_name)
                all_file_types.add(filename[1])
            
            elif filename[1]=='mp3' or filename[1]=='ogg' or filename[1]=='wav' or filename[1]=='amr':
                try:
                    aud_dir_path = os.path.join(path, 'audio') # створення шляху папки
                    os.mkdir(aud_dir_path) # створення папки
                    print("dir 'audio' created")
                except FileExistsError: # якщо папка вже існує 
                    print("folder audio exists")
                    pass
                norm_name = normalization.normalize(file)
                new_file_path = os.path.join(aud_dir_path, norm_name)
                dup = 0
                while os.path.isfile(new_file_path): # перевіряю, чи такий файл уже існує
                    print(f'file already exists!') # ок, така назва файлу вже існує
                    splitted_n_name = norm_name.rsplit(".", 1) # знов ділимо назву для апдейту назви
                    dup += 1
                    n = f"{splitted_n_name[0]}_{dup}" 
                    print(n)
                    with_end = f'{n}.{splitted_n_name[1]}'
                    new_file_path = (os.path.join(im_dir_path, with_end))
                shutil.move(file_path, new_file_path)
                audio.append(norm_name)
                all_file_types.add(filename[1])

            elif filename[1]=='avi' or filename[1]=='mp4' or filename[1]=='mov' or filename[1]=='mkv':
                try:
                    vid_dir_path = os.path.join(path, 'video') # створення шляху папки
                    os.mkdir(vid_dir_path) # створення папки
                    print("dir 'video' created")
                except FileExistsError: # якщо папка вже існує 
                    print("folder video exists")
                    pass
                norm_name = normalization.normalize(file)
                new_file_path = os.path.join(vid_dir_path, norm_name)
                dup = 0
                while os.path.isfile(new_file_path): # перевіряю, чи такий файл уже існує
                    print(f'file already exists!') # ок, така назва файлу вже існує
                    splitted_n_name = norm_name.rsplit(".", 1) # знов ділимо назву для апдейту назви
                    dup += 1
                    n = f"{splitted_n_name[0]}_{dup}" 
                    print(n)
                    with_end = f'{n}.{splitted_n_name[1]}'
                    new_file_path = (os.path.join(im_dir_path, with_end))
                shutil.move(file_path, new_file_path)
                video.append(norm_name)
                all_file_types.add(filename[1])

            elif filename[1]=='zip' or filename[1]=='gz' or filename[1]=='tar':
                try:
                    arch_dir_path = os.path.join(path, 'archives') # створення шляху папки
                    os.mkdir(arch_dir_path) # створення папки
                    print("dir 'archives' created")
                except FileExistsError: # якщо папка вже існує 
                    print("folder archives exists")
                    pass 
                norm_name = normalization.normalize(file)
                new_file_path = os.path.join(arch_dir_path, norm_name)
                dup = 0
                while os.path.isfile(new_file_path): # перевіряю, чи такий файл уже існує
                    print(f'file already exists!') # ок, така назва файлу вже існує
                    splitted_n_name = norm_name.rsplit(".", 1) # знов ділимо назву для апдейту назви
                    dup += 1
                    n = f"{splitted_n_name[0]}_{dup}" 
                    print(n)
                    with_end = f'{n}.{splitted_n_name[1]}'
                    new_file_path = (os.path.join(im_dir_path, with_end))
                shutil.unpack_archive(file_path, new_file_path)
                archives.append(norm_name)
                all_file_types.add(filename[1])
                os.remove(file_path)
            
            else:
                try:
                    unk_dir_path = os.path.join(path, 'others') # створення шляху папки
                    os.mkdir(unk_dir_path) # створення папки
                    print("dir 'others' created")
                except FileExistsError: # якщо папка вже існує 
                    print("folder others exists")
                    pass 
                norm_name = normalization.normalize(file)
                new_file_path = os.path.join(unk_dir_path, norm_name)
                dup = 0
                while os.path.isfile(new_file_path): # перевіряю, чи такий файл уже існує
                    print(f'file already exists!') # ок, така назва файлу вже існує
                    splitted_n_name = norm_name.rsplit(".", 1) # знов ділимо назву для апдейту назви
                    dup += 1
                    n = f"{splitted_n_name[0]}_{dup}" 
                    print(n)
                    with_end = f'{n}.{splitted_n_name[1]}'
                    new_file_path = (os.path.join(im_dir_path, with_end))
                shutil.move(file_path, new_file_path)
                others.append(norm_name)
                other_types.add(filename[1])


    del_empty_dirs.removeEmptyFolders(path)

    print(images)
    print(documents)
    print(audio)
    print(video)
    print(archives)
    print(others)
    print(all_file_types)
    print(other_types)


if __name__ == "__main__":
    # sys.argv[1] - другий переданий через консоль аргумент - це папку, яку треба опрацювати
    main() 