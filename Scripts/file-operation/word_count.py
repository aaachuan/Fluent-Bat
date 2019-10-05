import sys
import re
def word_count(path):
    count = {}
    with open(path) as f:
        str = f.read()
        str = str.lower()
        str = re.sub(r'\W', ' ', str)

        for word in str.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        return count

def main(argv):
    print(word_count(argv))

if __name__ == '__main__':
    main(sys.argv[1])