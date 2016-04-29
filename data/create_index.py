import os

f = open('indices.json','w')
f.write('{\n')
line_list = []


filenames = [fn for fn in os.listdir('.') if fn.endswith('.mp4')]
for i, fn in enumerate(sorted(filenames)):
    line_list.append("\"" + str(i) + "\":\"" + fn  + '\",\n')

# remove trailing comma on final item
line_list[-1] = line_list[-1][:-2] + '\n'

f.writelines(line_list)

f.write('}\n')
f.close()
