import re


def remove_tags_and_comments(text):
    text = re.sub(r'<summary>.*?</summary>', '', text, flags=re.DOTALL)
    text = re.sub(r'#.*', '', text)
    text = re.sub(r'(?s)<!--.*?-->', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)  # Добавленная строка
    text = "\n".join([line for line in text.split("\n") if line.strip() != ""])
    return text


original_text = '''
    <summary>
    This is a class in Python that does something useful.
    </summary>
    # woijei erghieruh epoiijgeri
    <!-- This is a comment. -->
    class MyClass:
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    	/*
        jjih iuhiuh iuihiuh  iohpiuhip piuhpiuhipuhiuph
        [oijipohoii
        oijoihiuhp
        
        iooih9[ohj ihpiuhipuhipuhu]]
        */
# '''

original_text_1 = '''
    <summary>
    This function takes two integers as input and returns their product.
    </summary>

    

    def multiply(a, b):
        # This is a comment.
        # This is a comment.
        return a * b
'''

original_text_2 = '''
    <summary>
    This is a class that represents a car.
    </summary>

    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

        def get_description(self):
            return f"{self.year} {self.make} {self.model}"
'''

original_text_3 = '''
    <summary>
    This script reads a file and prints its contents to the console.
    </summary>

    # This is a comment.
    with open('myfile.txt', 'r') as f:
        print(f.read())
'''

original_text_4 = '''
    <summary>
    This class represents a student and stores their name and ID number.
    </summary>

    class Student:
        def __init__(self, name, id_number):
            self.name = name
            self.id_number = id_number
        #new comment
        def __str__(self):
            return f"Student: {self.name} ({self.id_number})"
'''

cleaned_text = remove_tags_and_comments(original_text)
print(cleaned_text)
