import re
from zipfile import ZipFile
import datetime

class TextAnalyzer:
    def __init__(self, filename, text=""):
        self.filename = filename
        self.text = text
    
    def get_text(self):
        """Get text from file"""
        with open(self.filename, "r") as fh:
            self.text = " ".join(fh.readlines())

    def find_amount_of_sentences(self):
        """Calculate amount of sentence"""
        res = re.findall(r'.+\.\D', self.text)
        res2 = re.findall(r'.+\!', self.text)
        res3 = re.findall(r'.+\?', self.text)
        return (len(res), len(res2), len(res3))
    

    def avarage_sentence(self):
        """Calculate average params"""
        amount_of_words = 0
        amount_of_letters = 0
        res = re.findall(r'[^.!?]+[.!?]', self.text)
        amount_of_sentence = len(res)
        for el in res:
            res2 = re.findall(r'\S+', self.text)
            amount_of_words += len(res2)
            for el in res2:
                amount_of_letters += len(el)
        av_sentence = amount_of_letters / amount_of_sentence
        av_word = amount_of_letters / amount_of_words
        return (av_sentence, av_word)

    def amount_of_smiles(self):
        res = re.findall(r'[;:]-*[()\[\]]+', self.text)
        if res:
            return len(res)
        return False
    
    def save_results(self, filename):
        with open(filename, "w") as fh:
            self.get_text()
            amount = self.find_amount_of_sentences()
            av = self.avarage_sentence()
            smiles = self.amount_of_smiles()
            alphes_dig = self.find_alphes_digits_words()
            ips = self.is_ip_adress()
            amount_6 = self.find_length()
            min_w = self.find_shortest()
            sorted_words = self.sort_for_length()
            self.print_results((amount, av, smiles, alphes_dig, ips, amount_6, min_w, sorted_words))
            all_sentence = int(amount[0]) + int(amount[1]) + int(amount[2])
            fh.write(f"Общее количество предложений в тексте: {all_sentence}\n")
            fh.write(f"Повествовательных: {amount[0]}\n")
            fh.write(f"Побудительных: {amount[1]}\n")
            fh.write(f"Вопросиьельных: {amount[2]}\n")
            fh.write(f"Средняя длина предложений: {av[0]}\n")
            fh.write(f"Средняя длина слов: {av[1]}\n")
            fh.write(f"Среднее количество смайликов в тексте: {smiles}\n")

            fh.write(f"Слова только из букв в нижнем рег и цифр: {alphes_dig}\n")
            fh.write(f"Ip адреса: {ips}\n")
            fh.write(f"Число слов, доина которых меньще 6 символов: {amount_6}\n")
            fh.write(f"Самое короткое слово заканчивающееся на w: {min_w}\n")
            fh.write(f"Отсортированные слова в порядке роста их длин: {sorted_words}\n")


        with ZipFile("data.zip", "w") as zip:
            zip.write(filename)

            info = zip.getinfo(filename)
            print("Информация о файле в архиве")
            print(f"Имя файла: {info.filename}")
            print(f"Дата создания в архиве: {datetime.datetime(*info.date_time)}")


    def print_results(self, results):
        print("Общее количество предложений в тексте: ", results[0][0] + results[0][1] + results[0][2])
        print("Повествовательных: ", results[0][0])
        print("Побудительных: ",     results[0][1])
        print("Вопросиьельных: ",    results[0][2])
        print("Средняя длина предложений: ", results[1][0])
        print("Средняя длина слов: ", results[1][1])
        print("Среднее количество смайликов в тексте: ", results[2])
        print("Слова только из букв в нижнем рег и цифр: ", results[3])
        print("Ip адреса: ", results[4])
        print("Число слов, доина которых меньще 6 символов: ", results[5])
        print("Самое короткое слово заканчивающееся на w: ", results[6])
        print("Отсортированные слова в порядке роста их длин: ", results[7])

    def get_zip_info(self):
        with ZipFile("data.zip", "r") as zip:
            info = zip.infolist()
            print(f"File Name: {info[0].filename} Date: {info[0].date_time} Size: {info[0].file_size}.")

    def find_alphes_digits_words(self):
        res = re.findall(r'\b[a-z0-9]+\b', self.text)
        return res
    
    def is_ip_adress(self):
        str = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d', self.text)
        return str
    
    def find_length(self):
        amount = 0
        res = re.findall(r'\w+', self.text)
        for el in res:
            if len(el) < 6:
                amount += 1
        return amount
    
    def find_shortest(self):
        res = re.findall(r'\w+w\s', self.text)
        min = res[0]
        for el in res:
            if len(el) < len(min):
                min = el
        return min
    
    def sort_for_length(self):
        res = re.findall(r'\w+', self.text)
        res.sort(key=lambda el: len(el))
        return res