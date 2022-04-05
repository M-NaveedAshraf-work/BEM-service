from app import calData

keys = calData['capxParameterValues']['DHWGenerationSystem'].keys()

names = []
for name in keys:
    names.append(name)

print(calData['capxParameterValues']['DHWGenerationSystem'][names[0]]["cost"])