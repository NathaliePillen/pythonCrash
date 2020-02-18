def count_words (filename):
    '''Count the approximate number of words in the file.'''
    try:
        with open(filename, encoding='utf-8')as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist"
        print (msg)
    else:
        words = contents.split()
        num_words = len(words)
        print ("The file " + filename + " has about " + str(num_words) + " words.")

filenames=['text_files/alice.txt', 'text_files/moby_dick.txt', 'text_files/siddhhartha.txt', 'text_files/moby_dick.txt']
for filename in filenames:
    count_words(filename)
