import json
import glob 
new_dict = {}
names  = glob.glob('/home/ai/Desktop/fashion/fashion/train/annos' + '/*.json')
names = sorted(names)
for j in names:

    filename = j.split('/')[-1][:-5] + '.jpg'
    with open(j,"r+") as f:
        data = json.load(f)
        new_dict[filename] = data
        print(filename)
print(len(new_dict.keys()))     
import json

with open('train.json', 'w') as fp:
    json.dump(new_dict, fp)