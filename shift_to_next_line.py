
def shift_to_next_line_ends_with(start_tags, lines, filename):
    result = []
    
    for line in lines:
        line = line.strip('\r\n')
        found = False
        for start_tag in start_tags:
            if start_tag in line:
                if line.endswith(start_tag):
                    new_lines = line.split(start_tag)
                    for new_line in new_lines:
                        if(new_line):
                            result.append(new_line)
                    result.append(start_tag)
                    found = True
                    break
        if not found:
            result.append(line)
    return result

def shift_to_next_line_begins_with(start_tags, lines, filename):
    result = []
    
    for line in lines:
        line = line.strip('\r\n')
        found = False
        for start_tag in start_tags:
            if start_tag in line:
                if line.startswith(start_tag) and not line.startswith(start_tag + ' '):
                    new_lines = line.split(start_tag)
                    result.append(start_tag)
                    for new_line in new_lines:
                        if(new_line):
                            result.append(new_line)
                    found = True
                    break
        if not found:
            result.append(line)
    return result

lines=[]
with open('xjustiz_3_3_1.txt', '+r') as f:
    lines = f.readlines()

filename = 'xjustiz_3_3_1_mod.txt'

start_tags_ends_with = ['0..11..* 0..1', '0..1 1..* 0..1', '1..*0..*', '0..*0..1', '1..* 0..1', '0..10..1', '0..*1..*', '1..* 0..*', '1..* 0..1', '0..10..*', '0..*0..1*', '1..*', '0..1', '0..*', '1..1']
start_tags_begins_with = ['type']

result = shift_to_next_line_ends_with(start_tags_ends_with, lines, filename)
result = shift_to_next_line_begins_with(start_tags_begins_with, result, filename)

with open(filename, '+w') as f:
    for line in result:
        f.write(line + '\n')