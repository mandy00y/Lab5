


"""
The program is trying to translate a sentence captured as user input.
We first read in the text file Textese.txt
Then from the text file, we create a list of strings from each lines in the text file.
Then, we create a dictionary from the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input
(sentence) into an array of strings ("enjoy the excellent band tonight")
["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we
loop through each words, find the key matching the word and returns back the value tied
to that word in out dictionary.

After each word is translated, we then
Print out the translated sentence to the user. 
"""


"""
main():
    set dictionary = translate()
    translate()

translate(sentence, dictionary):
    words = for each of the word in the sentence
    for each words, trnaslate the word
    print translated sentence to user

create_dictionary():
    read in Textese.txt
    create list = each line from file
    close the file
    create s dict off of the list
    return the dict


main()
"""



def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("Textese.txt")
    translate(sentence, dictionary)


def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word, word), " ", end="")


main()
