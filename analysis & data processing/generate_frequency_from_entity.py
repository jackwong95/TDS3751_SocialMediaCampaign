entity = {}

with open("../output/analysis twitter output/entity.txt", "r", encoding="utf-8") as f:
	for line in f:
	
		word = line.replace('\n','')
		if word not in entity:
			entity[word] = 0
			
		entity[word] = entity[word] + 1

with open("../output/analysis output/entity.txt", "r", encoding="utf-8") as f:
	for line in f:
	
		word = line.replace('\n','')
		if word not in entity:
			entity[word] = 0
			
		entity[word] = entity[word] + 1


entity_freq = open("../output/entity_frequency.csv", "w", encoding="utf-8")
entity_freq.write('entity,frequency\n')

for key in entity:
	entity_freq.write(key+','+str(entity[key])+'\n')

entity_freq.close()
print(entity)