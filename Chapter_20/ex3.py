#THIS PROGRAM CAN BE CONSIDERED AS THE 'alice_words.py' FILE OF THE EXERCISE 3
import urllib.request
import wordtools

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta

#get text from a internet site
the_text = retrieve_page("http://www.gutenberg.org/cache/epub/28885/pg28885.txt")

output_file = open("alice_words.txt", "w")
#prepare the output file
output_file.writelines(["Word              Count\n", "=======================\n"])

#count every word
db_word = {}
for word in wordtools.extract_words(the_text):
    db_word[word] = db_word.get(word, 0) + 1

for word in sorted(db_word):
    output_file.write("{0:<18}{1}\n".format(word, db_word[word]))

output_file.close()