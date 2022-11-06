                                            #Stop words
stop_words_english = ['able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj',
                      'after', 'afterwards',
                      'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along',
                      'alongside',
                      'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and',
                      'another', 'any',
                      'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear',
                      'appreciate',
                      'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking', 'associated',
                      'at', 'available',
                      'away', 'awfully', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become',
                      'becomes', 'becoming',
                      'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside',
                      'besides', 'best',
                      'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant',
                      "can't", 'caption',
                      'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', "c'mon", 'co', 'co.', 'com',
                      'come', 'comes',
                      'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains',
                      'corresponding',
                      'could', "couldn't", 'course', "c's", 'currently', 'dare', "daren't", 'definitely', 'described',
                      'despite', 'did',
                      "didn't", 'different', 'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down',
                      'downwards',
                      'during', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending',
                      'enough',
                      'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody',
                      'everyone', 'everything',
                      'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far', 'farther', 'few', 'fewer',
                      'fifth', 'first',
                      'five', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth',
                      'forward', 'found',
                      'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go',
                      'goes', 'going',
                      'gone', 'got', 'gotten', 'greetings', 'had', "hadn't", 'half', 'happens', 'hardly', 'has',
                      "hasn't", 'have',
                      "haven't", 'having', 'he', "he'd", "he'll", 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
                      'hereby',
                      'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him', 'himself', 'his',
                      'hither', 'hopefully',
                      'how', 'howbeit', 'however', 'hundred', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm", 'immediate',
                      'in', 'inasmuch',
                      'inc', 'inc.', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar',
                      'instead', 'into',
                      'inward', 'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'just', 'k',
                      'keep', 'keeps',
                      'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
                      'less', 'lest', 'let',
                      "let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low',
                      'lower', 'ltd',
                      'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime',
                      'meanwhile',
                      'merely', 'might', "mightn't", 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly',
                      'mr', 'mrs', 'much',
                      'must', "mustn't", 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need',
                      "needn't",
                      'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
                      'ninety', 'no',
                      'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor', 'normally', 'not', 'nothing',
                      'notwithstanding',
                      'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on',
                      'once', 'one',
                      'ones', "one's", 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
                      "oughtn't", 'our',
                      'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly',
                      'past', 'per',
                      'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provided',
                      'provides', 'que',
                      'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
                      'regardless',
                      'regards', 'relatively', 'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying',
                      'says',
                      'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self',
                      'selves', 'sensible',
                      'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't", 'she', "she'd", "she'll",
                      "she's", 'should',
                      "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone',
                      'something', 'sometime',
                      'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
                      'still', 'sub',
                      'such', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank',
                      'thanks', 'thanx',
                      'that', "that'll", 'thats', "that's", "that've", 'the', 'their', 'theirs', 'them', 'themselves',
                      'then', 'thence',
                      'there', 'thereafter', 'thereby', "there'd", 'therefore', 'therein', "there'll", "there're",
                      'theres', "there's",
                      'thereupon', "there've", 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing',
                      'things', 'think',
                      'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through',
                      'throughout', 'thru',
                      'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly',
                      'try', 'trying',
                      "t's", 'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless',
                      'unlike', 'unlikely',
                      'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
                      'usually', 'v', 'value',
                      'various', 'versus', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we',
                      "we'd", 'welcome',
                      'well', "we'll", 'went', 'were', "we're", "weren't", "we've", 'what', 'whatever', "what'll",
                      "what's", "what've",
                      'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's",
                      'whereupon',
                      'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd",
                      'whoever', 'whole',
                      "who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will', 'willing', 'wish', 'with',
                      'within', 'without',
                      'wonder', "won't", 'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're",
                      'yours',
                      'yourself', 'yourselves', "you've", 'zero', 'a', "how's", 'i', "when's", "why's", 'b', 'c', 'd',
                      'e', 'f', 'g',
                      'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'I',
                      'www', 'amount',
                      'bill', 'bottom', 'call', 'computer', 'con', 'couldnt', 'cry', 'de', 'describe', 'detail', 'due',
                      'eleven',
                      'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give', 'hasnt',
                      'herse', 'himse',
                      'interest', 'itse', 'mill', 'move', 'myse', 'part', 'put', 'show', 'side', 'sincere', 'sixty',
                      'system', 'ten',
                      'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted',
                      'affected',
                      'affecting', 'affects', 'ah', 'announce', 'anymore', 'apparently', 'approximately', 'aren',
                      'arent', 'arise',
                      'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date', 'ed', 'effect',
                      'et-al', 'ff', 'fix',
                      'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately', 'importance',
                      'important', 'index',
                      'information', 'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line', "'ll", 'means',
                      'mg', 'million',
                      'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord',
                      'owing', 'page',
                      'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously',
                      'primarily',
                      'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref', 'refs', 'related', 'research',
                      'resulted', 'resulting',
                      'results', 'run', 'sec', 'section', 'shed', 'shes', 'showed', 'shown', 'showns', 'shows',
                      'significant',
                      'significantly', 'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state',
                      'states', 'stop',
                      'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof',
                      'therere', 'thereto',
                      'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til', 'tip', 'ts', 'ups', 'usefully',
                      'usefulness',
                      "'ve", 'vol', 'vols', 'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
                      'world', 'youd', 'youre']


def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):#first function which works on one book
    try:#checks if Word_Order parameter is an integer
        Word_Order += 1#if it can be added with one it is an integer
        Word_Order -= 1# substrac 1 to keep it as the first value
        try:#checks if file exists
            if Word_Order != 1 and Word_Order != 2:#if Word_Order's value is something different than 1 and 2, prints an error message
                print("The Word_Order parameter can only take the value 1 and 2.")#error message
            else:#if Word_Order parameter is compatible
                is_book_a_string = isinstance(Book, str)#checks if the Book parameter is a string
                if is_book_a_string == True:#if all parameters are compatible, works the program

                    with open(Book, encoding="latin1") as input_file:#opens the Book file
                        inside = input_file.read()#reads the content
                        encoded_string = inside.encode("ascii", "ignore")#encodes the content
                        inside = encoded_string.decode()#decodes the content
                        punc = '''!()-[]{};:"\,<>./?@#$%^&*_~1234567890'''#punctation marks which will be removed
                        for element in inside:#iterates inside the content
                            if element in punc:#iterates inside the punc list
                                inside = inside.replace(element, " ")#if element is in punc replaces it with a single blank
                        inside = inside.lower()#lowers the words in content
                        inside = inside.replace("\n", " ")#removes the enters at the and of the rows
                        book = inside.split(" ")#splits the content with blank
                        for i in range(len(book)):
                            for j in range(len(stop_words_english)):
                                if book[i] == stop_words_english[j]:#if word equals to a stop word replaces it with nothing
                                    book[i] = ""
                        book_words = []#final book words
                        for string in book:#this for loop adds the words to the final book word and lefts out the empty elements
                            if string != "":
                                book_words.append(string)
                        word_counts = {}#dictionary which storages the word counts
                        if Word_Order == 1:#checks for single words
                            for i in range(len(book_words)):
                                if book_words[i] in word_counts:#if the word already exists in the word count dictinionary adds 1
                                    word_counts[book_words[i]] = word_counts[book_words[i]] + 1
                                if book_words[i] not in word_counts and book_words[i] != "":#if word does not exist in the dictionary adds it to the dictionary and makes its count 1
                                    word_counts[book_words[i]] = 1
                            sorted_word_counts = {k: v for k, v in#sorts the dictionary by value and reverses it and makes it from highest to lowest
                                                  sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}
                            with open(File_Output, "w") as output_file:#opens the output file to write
                                written_word = 0#to write exactly 100 words to output file this variable is the count
                                output_file.write("|Frequency\t")#frequency coloumn
                                output_file.write("|Word\n")#word coloumn
                                for key in sorted_word_counts.keys():#writes words and counts orginized
                                    if sorted_word_counts[key] > 99:
                                        output_file.write("|" + str(sorted_word_counts[key]) + "\t\t")
                                        output_file.write("|" + key + "\t\n")
                                    else:
                                        output_file.write("|" + str(sorted_word_counts[key]) + "\t\t\t")
                                        output_file.write("|" + key + "\t\n")
                                    written_word += 1#implements the count one by one
                                    if written_word == 100:#if 100 words had written, stops the process
                                        break
                        elif Word_Order == 2:#checks for binary words
                            for i in range(len(book_words) - 1):#iterates inside the words
                                book_words[i] = book_words[i] + " " + book_words[i + 1]#adds the next word
                            for i in range(len(book_words)):
                                if book_words[i] in word_counts:#if binary word exists in the dictionary adds 1 to the value
                                    word_counts[book_words[i]] = word_counts[book_words[i]] + 1
                                if book_words[i] not in word_counts:#if binary word does not exist in the dictionary adds it and gives the value 1
                                    word_counts[book_words[i]] = 1
                            sorted_word_counts = {k: v for k, v in#sorts the word count by value and reverses it so it is from highest to lowest
                                                  sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}
                            with open(File_Output, "w") as output_file:#opens output file to write inside
                                written_words = 0#holds the written word count
                                output_file.write("|Frequency\t")#frequency coloumn
                                output_file.write("|Word\n")#word coloumn
                                for key in sorted_word_counts.keys():#prints the keys and values of the dictionary
                                    if sorted_word_counts[key] > 99:
                                        output_file.write("|" + str(sorted_word_counts[key]) + "\t\t")
                                    else:
                                        output_file.write("|" + str(sorted_word_counts[key]) + "\t\t\t")
                                    output_file.write("|" + key + "\t\n")

                                    written_words += 1
                                    if written_words == 100:#stops when 100 words had written
                                        break
                else:#if Book parameter is not a string, prints an error message
                    print("Book parameter must be a string.")
        except FileNotFoundError: #if user wants to open a non-existing file
            print("Please try to open an existing file.")
    except TypeError:#if Word_Order parameter is not an integer
        print("Word_Order parameter must be an integer.")


def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):#function for two books
    try:#checks if Word_Order parameter is an integer
        Word_Order += 1#if it can be added with one it is an integer
        Word_Order -= 1# substrac 1 to keep it as the first value
        try:#checks if file exists
            is_book_1_string = isinstance(Book_1, str)#if book 1 is an integer returns true
            is_book_2_string = isinstance(Book_2, str)#if book 2 is an integer returns true
            if is_book_1_string == True and is_book_2_string == True:#if both inputs are string continues processing
                if Word_Order != 2 and Word_Order != 1:#if Word_Order parameter is not equals to 1 or 2, prints an error message
                    print("The Word_Order parameter can only take the value 1 and 2.")
                else:#if Word_Order parameter is equals to 1 or 2 continues processing
                    with open(Book_1, encoding="latin1") as input_file_1:#opens the first book
                        inside_1 = input_file_1.read()#reads the content
                        encoded_string1 = inside_1.encode("ascii", "ignore")#encodes the content
                        inside_1 = encoded_string1.decode()#decodes the content
                        punc = '''!()-[]{};:"\,<>./?@#$%^&*_~1234567890'''#punctation marks which will be removed
                        for element in inside_1:#iterates inside the content
                            if element in punc:#iterates inside the punc list
                                inside_1 = inside_1.replace(element, " ")#if element is in punc replaces it with a single blank
                        inside_1 = inside_1.lower()#lowers the words in content
                        inside_1 = inside_1.replace("\n", " ")#removes the enters at the and of the rows
                        book_1 = inside_1.split(" ")#splits the content with blank
                        for i in range(len(book_1)):
                            for j in range(len(stop_words_english)):
                                if book_1[i] == stop_words_english[j]:#if word equals to a stop word replaces it with nothing
                                    book_1[i] = ""
                        book_1_words = []#final book words
                        for string in book_1:#this for loop adds the words to the final book word and lefts out the empty elements
                            if string != "":
                                book_1_words.append(string)
                    with open(Book_2, encoding="latin1") as input_file_2:#opens the second book
                        inside_2 = input_file_2.read()#reads the content
                        encoded_string2 = inside_2.encode("ascii", "ignore")#encodes the content
                        inside_2 = encoded_string2.decode()#decodes the content
                        punc = '''!()-[]{};:"\,<>./?@#$%^&*_~1234567890'''#punctation marks which will be removed
                        for element in inside_2:#iterates inside the content
                            if element in punc:#iterates inside the punc list
                                inside_2 = inside_2.replace(element, " ")#if element is in punc replaces it with a single blank
                        inside_2 = inside_2.lower()#lowers the words in content
                        inside_2 = inside_2.replace("\n", " ")#removes the enters at the and of the rows
                        book_2 = inside_2.split(" ")#splits the content with blank

                        for i in range(len(book_2)):
                            for j in range(len(stop_words_english)):
                                if book_2[i] == stop_words_english[j]:#if word equals to a stop word replaces it with nothing
                                    book_2[i] = ""
                        book_2_words = []#final book words
                        for string in book_2:#this for loop adds the words to the final book word and lefts out the empty elements
                            if string != "":
                                book_2_words.append(string)
                        all_book = book_1_words + book_2_words#adds books end to end to count how many times it repeted
                        if Word_Order == 1:#checks for single words
                            word_counts_1 = {}#dictionary which storages the word counts
                            for i in range(len(all_book)):
                                if all_book[i] in word_counts_1:#if the word already exists in the word count dictinionary adds 1
                                    word_counts_1[all_book[i]] = word_counts_1[all_book[i]] + 1
                                if all_book[i] not in word_counts_1 and all_book[i] != "":#if word does not exist in the dictionary adds it to the dictionary and makes its count 1
                                    word_counts_1[all_book[i]] = 1
                            sorted_word_counts_1 = {k: v for k, v in#sorts the dictionary by value and reverses it and makes it from highest to lowest
                                                    sorted(word_counts_1.items(), key=lambda item: item[1], reverse=True)}
                            written_words = 0#to write exactly 100 words to output file this variable is the count
                            with open(File_Output, "w") as output_file_1:#opens the output file to write
                                output_file_1.write("Book 1\t")
                                output_file_1.write("|Book 2\t")
                                output_file_1.write("|Total\t")
                                output_file_1.write("|Word\n")
                                for key in sorted_word_counts_1.keys():#writes words and counts orginized
                                    count_first = 0
                                    count_second = 0
                                    for i in range(len(book_1_words)):#counts in first book
                                        if book_1_words[i] == key:
                                            count_first += 1
                                    for i in range(len(book_2_words)):#counts in second book
                                        if book_2_words[i] == key:
                                            count_second += 1
                                    if count_first > 999:
                                        output_file_1.write(str(count_first) + "\t" + "|")
                                    else:
                                        output_file_1.write(str(count_first) + "\t\t" + "|")
                                    if count_second > 99:
                                        output_file_1.write(str(count_second) + "\t" + "|")
                                    else:
                                        output_file_1.write(str(count_second) + "\t\t" + "|")
                                    if sorted_word_counts_1[key] > 99:
                                        output_file_1.write(str(sorted_word_counts_1[key]) + "\t" + "|")
                                    else:
                                        output_file_1.write(str(sorted_word_counts_1[key]) + "\t\t" + "|")
                                    output_file_1.write(key + "\n")
                                    written_words += 1
                                    if written_words == 100:#if 100 words had written, stops the process
                                        break
                        elif Word_Order == 2:#checks for binary words
                            for i in range(len(book_1_words) - 1):#iterates the words for the first book
                                book_1_words[i] = book_1_words[i] + " " + book_1_words[i + 1]#adds the next word for the first book
                            for i in range(len(book_2_words) - 1):#iterates the words for the second book
                                book_2_words[i] = book_2_words[i] + " " + book_2_words[i + 1]#adds the next word for the second book
                            double_words = book_1_words + book_2_words #adds binary words end to end
                            binary_word_counts_1 = {}#holds the binary word counts
                            for i in range(len(double_words)):
                                if double_words[i] in binary_word_counts_1:#if binary word exists in the dictionary adds 1 to the value
                                    binary_word_counts_1[double_words[i]] = binary_word_counts_1[double_words[i]] + 1
                                if double_words[i] not in binary_word_counts_1 and double_words[i] != "":#if binary word does not exist in the dictionary adds it and gives the value 1
                                    binary_word_counts_1[double_words[i]] = 1
                            sorted_binary_word_counts = {k: v for k, v in#sorts the word count by value and reverses it so it is from highest to lowest
                                                         sorted(binary_word_counts_1.items(), key=lambda item: item[1],
                                                                reverse=True)}
                            written_words = 0#holds the written word count
                            with open(File_Output, "w") as output_file_2:#opens output file to write inside
                                output_file_2.write("| Book 1")
                                output_file_2.write("|Book 2\t")
                                output_file_2.write("|Total\t")
                                output_file_2.write("|Word\n")
                                for key in sorted_binary_word_counts.keys():
                                    count_first2 = 0
                                    count_second2 = 0
                                    for i in range(len(book_1_words)):
                                        if book_1_words[i] == key:
                                            count_first2 += 1
                                    for i in range(len(book_2_words)):
                                        if book_2_words[i] == key:
                                            count_second2 += 1
                                    if count_first2 > 999:
                                        output_file_2.write("|" + str(count_first2) + "\t" + "|")
                                    elif count_first2 > 99:
                                        output_file_2.write("|" + str(count_first2) + "\t" + "|")
                                    else:
                                        output_file_2.write("|" + str(count_first2) + "\t\t" + "|")
                                    if count_second2 > 99:
                                        output_file_2.write(str(count_second2) + "\t" + "|")
                                    else:
                                        output_file_2.write(str(count_second2) + "\t\t" + "|")
                                    if sorted_binary_word_counts[key] > 99:
                                        output_file_2.write(str(sorted_binary_word_counts[key]) + "\t" + "|")
                                    else:
                                        output_file_2.write(str(sorted_binary_word_counts[key]) + "\t\t" + "|")
                                    output_file_2.write(key + "\n")
                                    written_words += 1
                                    if written_words == 100:#stops when 100 words had written
                                        break
            else:#if Book parameter is not a string, prints an error message
                print("Book_1 and Book_2 parameter must be a string.")
        except FileNotFoundError:#if user wants to open a non-existing file
            print("Please try to open an existing file.")
    except TypeError:#if Word_Order parameter is not an integer
        print("Word_Order parameter must be an integer.")



