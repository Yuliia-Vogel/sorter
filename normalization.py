import os

def normalize(file): # переклад назви файлів на латиницю
    filename = file.rsplit(".", 1) #розділяю назву файлів на 2 частини (справа, лише 1 розділення)
    cyrylic_symbols = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    latin_symbols = ("a", "b", "v", "h", "g", "d", "e", "ye", "j", "z", "y", "i", "yi", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "yu", "ya")
    transl = {}
    for а, a in zip(cyrylic_symbols, latin_symbols):
        transl[ord(а)] = a
        transl[ord(а.upper())] = a.upper()
        transl_name = filename[0].translate(transl)
    upd_name = ""
    for l in transl_name: #заміна різних символів на нижнє підкресленя
        if l.isdigit() != True and l.isalpha() !=True:
            upd_name += "_"
        else:
            upd_name += l
    the_name = upd_name+"."+filename[1] #об'єдную нормалізовану назву з суфіксом (розширення файлу)
    print(the_name)
    return the_name


if __name__ == "__main__":
    normalize(file, path)