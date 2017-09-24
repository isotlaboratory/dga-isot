import re
import math

f = open("alexa.txt", "r+")
next = f.readline()

domains = []
domain_type = []

# This iterates through all domains and matches for anything before the . and adds that to the array domains
# trigrams

while next != "":

    try:

        domain = re.match(r'^(.*?)\.', next)
        domains.append(domain.group()[:-1]);
        # domain = next.split('.')[0]
        # com = next.split('.')[1]
        # domains.append(domain)
        # domain_type.append(com)
    except:
        default = None

    next = f.readline()


def tri_gram(domain):
    s = []
    count = 2
    while count < len(domain):
        s.append(domain[count - 2] + domain[count - 1] + domain[count])
        count = count + 1
    return s


dataset = {}
sum_of_frequency = 0.0
# load trigrams_google into dataset

with open("trigram_google.txt") as f:
    for line in f:
        (key, val) = line.split()
        dataset[key] = float(val)
        sum_of_frequency += dataset[key]


# print sum
def calc_freq(trigrams):
    frequency = sum([dataset.get(trigram, 0) for trigram in trigrams]) / sum_of_frequency
    return frequency


# calculate entropy
def calc_entropy(n):
    ent = 0.0
    if n > 0:
        ent += n * math.log(n, 2)
        ent = -ent
    return ent


# print length of all domains

def calc_length(x):
    leng = len(x)
    return leng


# calculate vowels
def calc_vowels(y):
    num_vowel = 0
    vowels = list('aeiou')
    for char in y:
        if char in vowels:
            num_vowel += 1

    return num_vowel


def calc_digits(z):
    num_digit = 0
    digits = list('0123456789')
    for char in z:
        if char in digits:
            num_digit += 1

    return num_digit


def consecutive_consonant(word):
    # how many consecutive consonant
    consonant = set(
        ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    digit_map = [int(i in consonant) for i in word]
    consecutive = [(k, len(list(g))) for k, g in groupby(digit_map)]
    count_consecutive = sum(j for i, j in consecutive if j > 1 and i == 1)
    return count_consecutive


ent = []
length = []
vowels = []
digits = []
consonants = []

f1 = open("file-result-alexa.txt", 'w')

for domain in domains:
    Tri = tri_gram(domain)
    Length = calc_length(domain)
    Vowels = calc_vowels(domain)
    Digits = calc_digits(domain)
    Consonants = consecutive_consonant(domain)
    Freq = calc_freq(Tri)
    Entropy = calc_entropy(Freq)

    ent.append(Entropy)
    length.append(Length)
    vowels.append(Vowels)
    digits.append(Digits)
    consonants.append(Consonants)

    f1.write(','.join([domain, str(Entropy), str(Length), str(Vowels), str(Digits), str(Consonants), 'alexa' + '\n']))

f1.close()

