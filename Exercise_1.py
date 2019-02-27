#I guess that my solusion is not the best for this task
#But I didn't manage to do it better :(

def song_text(string_num=3, la_num=3, last_symbol=1):
    """
    The method generates strings which consist of 1 same word with separator "-".
    Takes 3 params:
    :param string_num: - number of lines
    :param la_num: - number of words
    :param last_symbol: - the last symbol for the last line. 1 == !, 0 == .
    :var word: - contains word you want to use while generate your strings
    :return: string
    """
    word = "la"
    song_string = [word for i in range(la_num)]
    counter = 0
    for i in range(string_num):
        counter += 1
        if counter == string_num and last_symbol==1:
            print("-".join(song_string)+"!")
        elif counter == string_num and last_symbol==0:
            print("-".join(song_string) + ".")
        else:
            print("-".join(song_string))

song_text()
