import re

# All VARIABLES
filtered_domain_file = open('filtered_domains.csv', 'w')
# trigram_stat_file = open('trigram_stats.csv', 'w')
database_file = open("alexa.txt", "r+")
domain_probability_file = open('result-alexa.csv', 'w')

domains = []
domain_type = []
filtered_domain_list = []
filter_in_length = int(6)
trigram_total_count_map = {}  # Map to store the total count of tri in filtered domain db
trigram_probability_map = {}  # Map to store the trigram probability of each trigram
total_trigrams = int(0)

### DATABASE FILE PROCESSING STARTS
database_file_line_ptr = database_file.readline()
# Iterates through all the domains and matches for anything before the . and adds that to the array domains
while database_file_line_ptr != "":

    try:
        domain = re.match(r'^(.*?)\.', database_file_line_ptr)
        domains.append(domain.group()[:-1]);

    except:
        default = None

    database_file_line_ptr = database_file.readline()


### DATABASE FILE PROCESSING ENDS


# Function to find out list of trigram of a given domain
def tri_gram(domain):
    trigram_list = []
    index = 2
    while index < len(domain):  # Run the loop till the last index
        trigram_list.append(domain[index - 2] + domain[index - 1] + domain[index])
        index = index + 1
    return trigram_list


def calc_length(x):
    return len(x)


# This function add the domain into filtered_domain_list based on filtering length criteria
def filter_domain_helper(filter_in_length, domain):
    if len(domain) <= filter_in_length:
        filtered_domain_list.append(domain)


def filter_domain_helper_2(filter_in_length):
    filter_in_length_tmp = filter_in_length
    for domain in domains:
        filter_domain_helper(filter_in_length_tmp, domain)


# This will create a list of filtered domain
def filter_domain():
    for domain in domains:
        length = calc_length(domain)
        # filter_domain_helper(filter_in_length,domain)
        filter_domain_helper(length, domain)


# This function is to process the filtered_domain_list to
# get the trigram counts and store in a map trigram_total_count_map
def process_filtered_domain_for_getting_trigram_count():
    for domain in filtered_domain_list:
        domain_tri_list = tri_gram(domain)
        for trigram in domain_tri_list:
            if trigram not in trigram_total_count_map:
                trigram_total_count_map[trigram] = int(1)  # First time this trigram is entering into the map
            else:
                trigram_total_count_map[trigram] = trigram_total_count_map[trigram] + 1


# This function is to get total trigram from trigram_total_count_map
def get_total_trigram_in_filtered_domain():  # This is by using trigram_total_count_map
    total_trigram_tmp = int(0)
    for trigram in trigram_total_count_map:
        # note that, total_trigram is a global variable
        total_trigram_tmp = total_trigram_tmp + trigram_total_count_map[trigram]

    return total_trigram_tmp
    # total_trigrams = total_trigram_tmp
    # print total_trigrams
    # return total_trigrams


def get_trigram_probability():
    for trigram in trigram_total_count_map:
        # print trigram , str(trigram_total_count_map[trigram]), total_trigrams
        trigram_probability = float(trigram_total_count_map[trigram]) / total_trigrams
        trigram_probability_map[trigram] = trigram_probability


def print_trigram_stats():
    for trigram, prob in trigram_probability_map.iteritems():
        out_str = trigram + "," + str(prob)
        trigram_stat_file.write(out_str + '\n')


def print_filtered_domains_and_trigram():
    for domain in filtered_domain_list:
        domain_tri_list = tri_gram(domain)
        out_str = domain
        for trigram in domain_tri_list:
            out_str = out_str + "," + trigram

        filtered_domain_file.write(out_str + '\n')


def print_all_domains_and_trigram():
    for domain in domains:
        domain_tri_list = tri_gram(domain)
        out_str = domain
        for trigram in domain_tri_list:
            out_str = out_str + "," + trigram

        filtered_domain_file.write(out_str + '\n')


def domain_probability():
    for domain in filtered_domain_list:
        domain_tri_list = tri_gram(domain)
        out_str = domain
        prob = float(0.0)

        for trigram in domain_tri_list:
            prob = prob + trigram_probability_map[trigram]

        out_str = out_str + "," + str(prob)
        domain_probability_file.write(out_str + '\n')


# Final Processings

print_all_domains_and_trigram()

for domain in domains:
    # filtered_domain_list.clear()
    del filtered_domain_list[:]
    trigram_probability_map.clear()
    trigram_total_count_map.clear()

    length = calc_length(domain)
    # filter_domain_helper(filter_in_length,domain)
    filter_domain_helper_2(length)
    process_filtered_domain_for_getting_trigram_count()
    total_trigrams = get_total_trigram_in_filtered_domain()
    get_trigram_probability()

    domain_tri_list = tri_gram(domain)
    out_str = domain
    prob = float(0.0)

    for trigram in domain_tri_list:
        prob = prob + trigram_probability_map[trigram]
        out = str(domain) + "_" + str(trigram) + "_" + str(prob)
        # print (out)

    out_str = out_str + "," + str(prob)
    domain_probability_file.write(out_str + '\n')









