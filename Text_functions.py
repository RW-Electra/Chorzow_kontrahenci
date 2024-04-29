def text_finding(Text_to_Search, Template_to_find, list_form=False):
    found = None
    if list_form:
        found = []
    iter = 0
    for m in range(len(Text_to_Search) - len(Template_to_find) + 1):
        idx = 0
        iter += 1
        while Text_to_Search[m + idx] == Template_to_find[idx] and idx < len(Template_to_find) - 1:
            # print(Text_to_Search[m+idx],' ',Template_to_find[idx],' ', idx)
            idx += 1
            iter += 1
        if idx == len(Template_to_find) - 1 and Text_to_Search[m + idx] == Template_to_find[idx]:
            if list_form:
                found.append(m)
            if not list_form:
                found = m
            iter += 1
    return found, iter


def Find_buyerID_switch_command():
    f = open(f"Additional_files/temporary_data.ams", encoding='ANSI')
    text = f.readlines()
    Search = ''.join(text).lower()
    Template = "switch(  [buyerid] )"
    found1, iter1 = text_finding(Search, Template)
    Template = "case else"
    found2, iter2 = text_finding(Search[found1:], Template, list_form=True)
    reduced_text = Search[found1:][:found2[0]].split('\n\t\t')[1:]
    reduced_text = [i.strip().replace(" ", '').replace('\"', '') for i in reduced_text]
    return reduced_text


def Case_reduction_to_int(segment):
    number = segment[4:]
    final_string = ''
    left_zero = True
    for letter in range(len(number)):
        if number[letter] != '0' and number[letter] != "\"":
            left_zero = False
            final_string = final_string + number[letter]
        else:
            if not left_zero and number[letter] != "\"":
                final_string += number[letter]
    return int(final_string)


def kkk_string_to_int(segment):
    equal_sign_right_side = False
    final_string = ''
    for letter in range(len(segment)):
        if equal_sign_right_side:
            final_string += segment[letter]

        if segment[letter] == "=":
            equal_sign_right_side = True
    return int(final_string)


def Switch_command_to_pairs(reduced_text):
    case_elems = {}
    case_indexes_list = []
    target = None
    for segment in reduced_text:
        if len(segment) > 0:
            if segment[0] == "c":
                case_indexes_list.append(Case_reduction_to_int(segment))
            if segment[0] == "@":
                target = kkk_string_to_int(segment)
            if segment[0] == "b":
                case_elems[target] = case_indexes_list
                case_indexes_list = []
    return case_elems


