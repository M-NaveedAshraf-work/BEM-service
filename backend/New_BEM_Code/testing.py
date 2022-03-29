from app import UQData

print(UQData['UQParams'][0]['param'])

param_info = []
i=0
state = 'true'

while state != 'end':
    if UQData['UQParams'] == None:
        break
    else:
        # TODO: param "names" not ouputing to read at line 467
        param_info.append(UQData['UQParams'][i]['param'])
        i += 1
        if i >= len(UQData['UQParams']):
            state = 'end'

print(param_info)