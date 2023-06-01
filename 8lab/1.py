import string
import re


class StringProcessor:
    def __init__(self):
        pass

    def __split_with_punctuation(self, text):
        words_and_punctuation = re.findall(r"\d+\.\d+|\w+|[^\w\s]", text)
        return [word.strip() for word in words_and_punctuation]

    def __split_and_format_numbers(self, text):
        arr = text
        arr_len = len(arr)
        for index in range(arr_len):
            if not self.__is_number(arr[index]):
                continue
            arr[index] = self.__format_number(arr[index])
        return arr

    def __is_number(self, text):
        try:
            number = float(text)
            return True
        except ValueError:
            return False

    def __format_number(self, text):
        try:
            number = float(text)
            return f"{number:.2f}"
        except ValueError:
            return text

    def __remove_extra_punctuation(self, words_and_punctuation):
        first_punct = True
        new_words_and_punct = []
        for word in words_and_punctuation:
            if re.match(r"\W", word):
                if first_punct:
                    new_words_and_punct.append(word)
                    first_punct = False
                else:
                    continue
            else:
                new_words_and_punct.append(word)
                first_punct = True
        return new_words_and_punct

    def __add_spaces(self, words):
        punctuation_marks = [".", ",", "!", "?", ";", ":"]
        result = []
        for i in range(len(words)):
            if i == 0:
                result.append(words[i])
            elif words[i] in punctuation_marks:
                result.append(words[i])
            else:
                result.append(" " + words[i])
        return "".join(result)

    def format_text(self, text):
        text = self.__split_with_punctuation(text)
        text = self.__split_and_format_numbers(text)
        text = self.__remove_extra_punctuation(text)
        text = self.__add_spaces(text)
        return text

    def remove_extra_spaces(self, text):
        text = self.__split_with_punctuation(text)
        text = self.__add_spaces(text)
        return text

    def remove_extra_punctuation(self, text):
        punctuations = string.punctuation
        output = ''
        in_punctuation_sequence = False
        for char in text:
            if char in punctuations:
                if not in_punctuation_sequence:
                    output += char
                    in_punctuation_sequence = True
            else:
                if in_punctuation_sequence:
                    in_punctuation_sequence = False
                output += char
        return output

    def format_numbers(self, text):
        output = ''
        in_number_sequence = False
        current_number = ''
        for char in text:
            if char.isdigit() or char == '.':
                current_number += char
                in_number_sequence = True
            else:
                if in_number_sequence:
                    formatted_number = '{:.2f}'.format(float(current_number))
                    output += formatted_number
                    current_number = ''
                    in_number_sequence = False
                output += char
        if in_number_sequence:
            formatted_number = '{:.2f}'.format(float(current_number))
            output += formatted_number

        return output

    def add_missing_spaces(self, text):
        pattern = r'([' + re.escape(string.punctuation) + r'])(?!\s)'
        matches = re.findall(pattern, text)
        for match in matches:
            text = text.replace(match, match + ' ')

        return text


lol = StringProcessor()
print(lol.add_missing_spaces("drer erferfre,wefwef,wefwe.wfewe"))


class StringArrayList:
    def __init__(self):
        self.array_list = []

    def add_string(self, string):
        self.array_list.append(string)

    def add_string_at_index(self, index, string):
        self.array_list.insert(index, string)

    def add_strings_to_beginning(self, strings):
        self.array_list = strings + self.array_list

    def change_array_list_size(self, new_size):
        current_size = len(self.array_list)
        if new_size > current_size:
            self.array_list.extend([''] * (new_size - current_size))
        elif new_size < current_size:
            self.array_list = self.array_list[:new_size]

    def view_all_elements(self):
        for i in range(len(self.array_list)):
            print(f'Элемент {i}: {self.array_list[i]}')

    def get_elements_count(self):
        count = 0
        for elem in self.array_list:
            if elem == "":
                continue
            count += 1
        return count

    def get_list_capacity(self):
        return len(self.array_list)


# my_list = StringArrayList()

# my_list.add_string("1111111")
# my_list.add_string("hello world")
# my_list.add_string("!")
# my_list.add_string("222")
# my_list.add_string("ArrayList")

# my_list.add_strings_to_beginning(
#     ["inheritance", "encapsulation", "polymorphism"])

# my_list.add_string_at_index(3, "python")

# my_list.change_array_list_size(13)

# my_list.view_all_elements()

# print("количество элементов:", my_list.get_elements_count())

# print("емкость списка:", my_list.get_list_capacity())

# string_processor = StringProcessor()

# my_list.add_string(string_processor.format_text(
#     "iuhiuhu    ihhui r 444545,..., ,.,.,  ,,.!! rfe"))

# my_list.add_string(string_processor.format_text(
#     "rife  er887 334.. 35.,. 45665 2322. 57776.223433435"))

# my_list.add_string(string_processor.format_text(
#     "riieh 838488      53 4 ..,.,4  4 4,.3,3 33,.,!!! 4r 3  4 ff..,.43 34.,,3.3 "))

# my_list.view_all_elements()
