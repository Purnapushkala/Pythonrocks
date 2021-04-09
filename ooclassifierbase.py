# Copyright 2020 Paul Lu
import sys
import copy     # for deepcopy()
from heapq import nlargest
# for OrderedDict{}

Debug = False   # Sometimes, print for debugging
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        # FIXME:  Call superclass, here and for all classes
        self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # FIXME:  Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords Hardcoded (%d): " % ln, end='')
        print(self.get_target_words())
        return

    def print_run_info(self):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)


class TrainingInstance(C274):
    def __init__(self):
        self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        self.prep = []
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]
        
    def lowercase_input(self, text):        
        '''Read from input and convert all the words to lowercase

           Arguments: None

           Return:
               self.text : the words converted to lowercase
        '''
        lines = []
        # to take input from user till an empty line is encountered
        self.text = ' '.join(lines)
        self.text = self.text.lower()
        return


    def rm_punc_symbols(self, text):
        '''Removes all punctutation marks and symbols from the words passed

           Arguments:
               self.text : the string to remove all the punctuation and
                      symbols from.

           Return:
               corrected_self.text: string with no punctuatuion and symbols
        '''
        text = ' '.join(text)
        newtext = []
        '''Going through each character in string to
           check if it is alphanumeric or space and
           appending alphanumeric character to a new list'''
        for i in range(len(text)):
            if text[i].isalnum() or text[i] == " ":
                newtext.append(text[i])
        text = "".join(newtext)
        self.prep = text.split()
        #return self.text
        return self.prep


    def rm_digits(self, text):
        '''Removes all digits from a word but not if the word/token is a number

           Arguments:
               self.text: the string with words containing digits as suffix/prefix

           Return:
               corrected_self.text: the string with words that doesn't contain digits
        '''
        text = ' '.join(text)
        text = list(text.split())
        correct_text = []
        ''' Checking if element in list is number or word,
            then proceeding to remove digits from the words and
            keeping seperate numbers as it is'''
        for char in text:
            if not char.isdigit():
                letters = list(char)
                # Appending all non digits to a new list
                for i in letters:
                    if not i.isdigit():
                        correct_text.append(i)
                correct_text.append(" ")
            else:
                correct_text.append(char + " ")
        text = "".join(correct_text)
        self.prep = text.split()
        return self.prep


    def rm_stopwords(self, text):
        '''Removes all stopwords (given list of words) from a string

           Arguments:
               self.text: the string which contains stopwords

           Return:
               corrected_self.text: the string that does not contain any of the
                               stopwords
        '''
        #correct_text = []
        txt_without_stop = []
        stopwords = [
            "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
            "you", "your", "yours", "yourself", "yourselves",
            "he", "him", "his", "himself", "she", "her",
            "hers", "herself", "it", "its", "itself", "they",
            "them", "their", "theirs", "themselves", "what",
            "which", "who", "whom", "this", "that", "these",
            "those", "am", "is", "are", "was", "were", "be", "been",
            "being", "have", "has", "had", "having", "do", "does",
            "did", "doing", "a", "an", "the", "and", "but", "if",
            "or", "because", "as", "until", "while", "of", "at",
            "by", "for", "with", "about", "against", "between",
            "into", "through", "during", "before", "after", "above",
            "below", "to", "from", "up", "down", "in", "out", "on",
            "off", "over", "under", "again", "further", "then", "once",
            "here", "there", "when", "where", "why", "how", "all",
            "any", "both", "each", "few", "more", "most", "other",
            "some", "such", "no", "nor", "not", "only", "own", "same",
            "so", "than", "too", "very", "s", "t", "can", "will",
            "just", "don", "should", "now"
            ]
        ''' Removing stopwords by appending non-stopwords
            to a new list'''
        for char in text:
            if char not in stopwords:
                txt_without_stop.append(char)
        text = " ".join(txt_without_stop)
        self.prep = text.split()
        return self.prep

    def preprocess_words(self, mode = ' '):
        self.inst['words']
        if mode == "keep-digits":
            processed_words = self.rm_stopwords(self.rm_punc_symbols(self.prep))
        elif mode == "keep-stops":
            processed_words = self.rm_digits(self.rm_punc_symbols(self.prep))
        elif mode == "keep-symbols":
            processed_words = self.rm_stopwords(self.rm_digits(self.prep))
        else:
            processed_words = self.rm_stopwords(self.rm_digits(self.rm_punc_symbols(self.prep)))
        
        self.prep = processed_words
        return self.prep

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=False
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                # FIXME: For testing only.  Compare to previous version.
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)


class TrainingSet(C274):
    def __init__(self):
        self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.preprocessed_inObjList = []
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more
    
    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            # Check for comments
            if line[0] == '%':  # Comments must start with %
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return
    
    def preprocess(self, mode = ' '):
        tr = self.get_instances()
        ti = TrainingInstance()
        for i in range (len(self.get_instances())):
            ti.prep = tr[i].inst["words"]
            ti.preprocess_words()
            tr[i].inst["words"] = ti.prep
        for i in range(len(self.inObjHash)):
            print(self.inObjHash[i].inst["words"])
        return #self.preprocessed_inObjList
    
class ClassifyByTopN(ClassifyByTarget):
    def __init__(self, lw):
        super().__init__(lw)
#       self.new_line = []
        self.count = 0
        self.frequency = 0
        self.sort_words = {}
        
    
    def sort_count_freq_words(self, new_line, num = 5):
        
        
        ''' Adding elements of a list to a dictionary and sorting, counting
            and calculating the frequency of every word

            Arguments:
                new_line: a list containing words to be sorted and counted
                and for whose element frequency is to be calculated

            Return:
                sorted_words: the lexicographically sorted dictionary "words"
                frequency: the frequency of each word#new_line = new_line.split()
        '''
        words = {}
        ''' Adding the elements of new_line to a dictionary "words"
            and using it to count the number of occurence of each word'''
        for char in new_line:
            if char not in words:
                words[char] = 1
            else:
                words[char] += 1

        return words
    
    def target_top_n(self, tset, num=5, label = ' '):
        new = []
        tr = tset.get_instances()
        for i in range(len(tset.get_instances())):            
            if label == tr[i].inst["label"]:
                new.append(tr[i].inst["words"])
        #Since new is a list containing sublists unpacking into a single list

        self.set_target_words(lw)
        return
                
    
               
        
        
def basemain():
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    print(run1)     # Just to show __str__
    lr = [run1]
    print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, '#weather')
    tset.preprocess()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, '#weather')
    return


if __name__ == "__main__":
    basemain()
