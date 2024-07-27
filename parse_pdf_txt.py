from bs4 import BeautifulSoup
import re

def parse_text_old(text, start_tag, end_tag_1, end_tag_2):
    pattern = re.escape(start_tag) + r'(.*?)' + re.escape(end_tag_1) + '|' + re.escape(start_tag) + r'(.*?)' + re.escape(end_tag_2)
    match = re.search(pattern, text, re.DOTALL)
    filtered_text = start_tag + (match.group(1) if match else '')
    return filtered_text

def parse_text(textLst, start_tag, end_tag_1, end_tag_2):
    result = []
    shrinkedLst = []
    index = 0
    while index < len(textLst):
        line = textLst[index]
        if line.startswith(start_tag):
            while(not end_tag_1 in line and not end_tag_2 in line):
                result.append(line)
                index = index + 1
                line = textLst[index]
                line = line.strip('\r\n')
            break
        else:
            index = index + 1
    while index < len(textLst):
        line = textLst[index]
        shrinkedLst.append(line)
        index = index + 1
    return result, shrinkedLst

def parse_text_end_tag_lst(textLst, start_tag, end_tags_lst):
    result = []
    shrinkedLst = []
    index = 0
    while index < len(textLst):
        line = textLst[index]
        if line.startswith(start_tag):
            not_the_end = True
            while(not_the_end):
                result.append(line)
                index = index + 1
                line = textLst[index]
                line = line.strip('\r\n')
                not_the_end = not_the_end_check(line, end_tags_lst)
            break
        else:
            index = index + 1
    while index < len(textLst):
        line = textLst[index]
        shrinkedLst.append(line)
        index = index + 1
    return result, shrinkedLst

def not_the_end_check(line, end_tags_lst):
    ret = True
    for tag in end_tags_lst:
        if tag in line:
            ret = False
            break
    return ret

def recursive_parse(filtered_text, end_tag_1, end_tag_2):
    for line in filtered_text:
        start_tag = ''
        if 'complexType' in line:
            continue
        if type_gds in line:
            start_tag = line.split('type tns:')[1]
        filtered_t = parse_text(document, start_tag, end_tag_1, end_tag_2)
        recursive_parse(filtered_t, end_tag_1, end_tag_2)


lines = ''
with open('xjustiz_3_3_1_mod.txt', '+r') as f:
    lines = f.readlines()

document = []
for line in lines:
    document.append(line)
    
# start_tag = 'complexType '
# end_tag_1 = 'Der Grunddatensatz (GDS)'
# end_tag_2 = 'Kindelement'
# type_gds = 'Type.GDS.'
# filename = 'all_xjustix_complex_types.txt'

# result = ['dummy']
# documentTmp = document.copy()

# while(not len(result) == 0):
#     result, document = parse_text(document, start_tag, end_tag_1, end_tag_2)

#     with open(filename, '+a') as f:
#         f.write('start#\n') 
#         for line in result:
#             f.write(line + '\n')
#         f.write('finish#\n\n')

# start_tag = 'element nachricht'
# end_tag_1 = 'Der Grunddatensatz (GDS)'
# end_tag_2 = 'Kindelement'
# type_gds = 'Type.GDS.'
# filename = 'all_xjustix_element_nachricht_types.txt'

# result = ['dummy']
# document = documentTmp

# while(not len(result) == 0):
#     result, document = parse_text(document, start_tag, end_tag_1, end_tag_2)

#     with open(filename, '+a') as f:
#         f.write('start#\n') 
#         for line in result:
#             f.write(line + '\n')
#         f.write('finish#\n\n')

start_tag = 'complexType '
end_tags_lst = ['Dieser Typ ist eine Erweiterung', 'Diese Nachricht ist eine Erweiterung', 'Der Grunddatensatz (GDS)', 'Kindelement']
type_gds = 'Type.GDS.'
filename = 'all_xjustix_complex_types.txt'

result = ['dummy']
documentTmp = document.copy()

while(not len(result) == 0):
    result, document = parse_text_end_tag_lst(document, start_tag, end_tags_lst)

    with open(filename, '+a') as f:
        f.write('start#\n') 
        for line in result:
            f.write(line + '\n')
        f.write('finish#\n\n')

start_tag = 'element nachricht'
end_tags_lst = ['Dieser Typ ist eine Erweiterung', 'Diese Nachricht ist eine Erweiterung', 'Der Grunddatensatz (GDS)', 'Kindelement']
type_gds = 'Type.GDS.'
filename = 'all_xjustix_element_nachricht_types.txt'

result = ['dummy']
document = documentTmp

while(not len(result) == 0):
    result, document = parse_text_end_tag_lst(document, start_tag, end_tags_lst)

    with open(filename, '+a') as f:
        f.write('start#\n') 
        for line in result:
            f.write(line + '\n')
        f.write('finish#\n\n')