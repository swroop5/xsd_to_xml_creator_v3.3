

def splitIntoDataTypes(lines):
    resultLst = []
    ind = 0
    if ind < len(lines)-1:
        while lines[ind] and ind < len(lines)-1:
            finished = False
            if 'start#' in lines[ind]:
                datatypeLst = []
                while 'finish#' not in lines[ind]:
                    datatypeLst.append(lines[ind])
                    if ind < len(lines)-1:
                        ind = ind +1
                else:
                    if ind < len(lines)-1:
                        ind = ind + 1
                    finished = True
            else:
                if ind < len(lines)-1:
                    ind = ind + 1
            if finished:
                resultLst.append(datatypeLst[1:])
                finished = False
    return resultLst

def printData(datatypes):
    for datatype in datatypes:
        for elem in datatype:
            print(elem)

def printAllDatatypes(datatypes):
    for datatype in datatypes:
        for elem in datatype:
            if 'complexType' in elem:
                print(elem[12:])

def printAllCodeTypes(datatypes):
    for datatype in datatypes:
        for elem in datatype:
            if elem.startswith('Codelisten Code.'):
                print(elem[16:])

def printXMLTags(datatype, datatypes, fw, tabs):
    xmlTagsLst = []
    tabsCopy = tabs + ''
    for elem in datatype:
        if 'complexType' in elem:
            continue
        if '(extension of tns:' in elem:
            elem = elem.strip(')\n')
            elem = elem[18:]
            tabsCopy = processTypGDSComplexTypes(elem, datatype, datatypes, tabsCopy, tabs)
        if '0..1' in elem or '1..1' in elem or '.*' in elem or '..' in elem or '(' in elem or ')' in elem:
            continue
        #if 'type tns:Type.' in elem:
        if elem.startswith('type'):
            if 'type tns:Type.' in elem:
                if 'type tns:Type.GDS.Akte\n' == elem or 'type tns:Type.GDS.Teilakte\n' == elem or 'type tns:Type.GDS.Dokument\n' == elem:
                    continue
                else:
                    tabsCopy = processTypGDSComplexTypes(elem[9:], datatype, datatypes, tabsCopy, tabs)
                    continue
            else:
                fw.write(tabs + elem)
                continue
        #print(elem)
        fw.write(tabs + elem)

def processTypGDSComplexTypes(elem, datatype, datatypes, tabsCopy, tabs):
    if elem not in datatype[0]:
        for data in datatypes:
            if 'complexType ' + elem in data[0]:
                if not 'Type.GDS.Xdomea.stringUUIDType' in data[0] and \
                            not 'Type.GDS.Datumsangabe' in data[0] and \
                                not 'Type.GDS.Zeitangabe' in data[0]:
                    tabsCopy = tabsCopy + '\t'
                printXMLTags(data, datatypes, fw, tabsCopy)
                if not 'Type.GDS.Xdomea.stringUUIDType' in data[0] and \
                            not 'Type.GDS.Datumsangabe' in data[0] and \
                                not 'Type.GDS.Zeitangabe' in data[0]:
                    tabsCopy = tabs + ''
                break
        else:
            print(elem + '    ' + data[0])
    return tabsCopy
        
def printXMLTags_with_Codelisten(datatype, datatypes, fw):
    xmlTagsLst = []
    for elem in datatype:
        if 'complexType' in elem:
            continue
        if '(extension of tns:' in elem:
            elem = elem.strip(')\n')
            elem = elem[18:]
            for data in datatypes:
                if 'complexType ' + elem in data[0]:
                    if not 'Type.GDS.Xdomea.stringUUIDType' in data[0]:
                        tabsCopy = tabsCopy + '\t'
                    printXMLTags(data, datatypes, fw, tabsCopy)
                    if not 'Type.GDS.Xdomea.stringUUIDType' in data[0]:
                        tabsCopy = tabs + ''
                    break
            else:
                print(elem + '    ' + data[0])
        if '0..1' in elem or '1..1' in elem or '.*' in elem or '..' in elem or '(' in elem or ')' in elem:
            continue
        #if 'type tns:Type.' in elem:
        if elem.startswith('type'):
            if 'type tns:Code' in elem:
                fw.write(elem)
            if 'type tns:Type.' in elem:
                if 'Type.GDS.Akte' in elem or 'Type.GDS.Teilakte' in elem or 'Type.GDS.Dokument' in elem:
                    continue
                else:
                    if elem[9:] not in datatype[0]:
                        for data in datatypes:
                            if 'complexType ' + elem[9:] in data[0]:
                                printXMLTags_with_Codelisten(data, datatypes, fw)
                                break
                        continue
            else:
                continue
        #print(elem)
        fw.write(elem)
            

nachricht_type = 'nachricht.straf.owi.verfahrensmitteilung.externAnJustiz.0500010'
indNach = 0
with open("all_xjustiz_types.txt", "r+") as f:
    lines = f.readlines()
    datatypes = splitIntoDataTypes(lines)
    for index, type in enumerate(datatypes):
        if nachricht_type in type[0]:
            indNach = index
            break
    #printData(datatypes)
    #printAllDatatypes(datatypes)
    with open("output_nachricht.straf.owi.verfahrensmitteilung.externAnJustiz.0500010.txt", "w+") as fw:
        printXMLTags(datatypes[indNach], datatypes, fw, '')

nachricht_type = 'nachricht.straf.aktenzeichenmitteilung.0500002'
indNach = 0
with open("all_xjustiz_types.txt", "r+") as f:
    lines = f.readlines()
    datatypes = splitIntoDataTypes(lines)
    for index, type in enumerate(datatypes):
        if nachricht_type in type[0]:
            indNach = index
            break
    #printData(datatypes)
    #printAllDatatypes(datatypes)
    with open("nachricht.straf.aktenzeichenmitteilung.0500002.txt", "w+") as fw:
        printXMLTags(datatypes[indNach], datatypes, fw, '')

nachricht_type = 'nachricht.straf.strafverfahren.0500013'
indNach = 0
with open("all_xjustiz_types.txt", "r+") as f:
    lines = f.readlines()
    datatypes = splitIntoDataTypes(lines)
    for index, type in enumerate(datatypes):
        if nachricht_type in type[0]:
            indNach = index
            break
    with open("nachricht.straf.strafverfahren.0500013.txt", "w+") as fw:
        printXMLTags(datatypes[indNach], datatypes, fw, '')

nachricht_type = 'nachricht.straf.aktenzeichenmitteilung.0500002'
indNach = 0
with open("all_xjustiz_types.txt", "r+") as f:
    lines = f.readlines()
    datatypes = splitIntoDataTypes(lines)
    for index, type in enumerate(datatypes):
        if nachricht_type in type[0]:
            indNach = index
            break
    with open("nachricht.straf.aktenzeichenmitteilung.0500002_331.txt", "w+") as fw:
        printXMLTags(datatypes[indNach], datatypes, fw, '')
        
nachricht_type = 'nachricht.straf.verfahrensausgangsmitteilung.justizZuExtern.0500006'
indNach = 0
with open("all_xjustiz_types.txt", "r+") as f:
    lines = f.readlines()
    datatypes = splitIntoDataTypes(lines)
    for index, type in enumerate(datatypes):
        if nachricht_type in type[0]:
            indNach = index
            break
    with open("nachricht.straf.verfahrensausgangsmitteilung.justizZuExtern.0500006_331.txt", "w+") as fw:
        printXMLTags(datatypes[indNach], datatypes, fw, '')