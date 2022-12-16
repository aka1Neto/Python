import string;
import random;

key_string = "METHINKS IT IS LIKE A WEASEL"
copies = 100;
probability = 5;
string_len = len(key_string);
chars = string.ascii_uppercase + ' ';

def generator():
    new_str = "";
    for _ in range(string_len):
        new_str += random.choice(chars);
    return new_str;

def get_score(new_str):
    score = 0;
    for i in range(string_len):
        if new_str[i] == key_string[i]:
            score +=1;
    return score;

def modify_char(new_str):
    aux_str = new_str;
    for i in range(string_len):
        new_probability = random.randint(1, 100)
        if new_probability <= probability:
            aux_str = aux_str[:i] + random.choice(chars) + aux_str[i+1:];
    return aux_str;

def weasel_program():
    rand_str = generator();
    generation_number = 0;
    bests_strings = []
    while(True):
        generations = {};
        for _ in range(copies):
            new_str = modify_char(rand_str);
            score = get_score(new_str);
            generations[new_str] = score;
        sorted_generations = sorted(generations.items(), key=lambda x:x[1], reverse=True);
        bests_strings.append(sorted_generations[0]);
        best_score = bests_strings[generation_number][1];
        if best_score == string_len:
            break;
        rand_str = bests_strings[generation_number][0];
        generation_number +=1;
    for i in range(len(bests_strings)):
        print(f'{i}: {bests_strings[i][0]} -- score: {bests_strings[i][1]}');

weasel_program();