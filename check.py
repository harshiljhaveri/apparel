import glob 
import json
import os 
import psutil
niceValue = os.nice(-20) 
print(niceValue)
dataset_dir = '/home/ai/Desktop/fashion/fashion/train'
dataset_img = os.path.join(dataset_dir,'image')
dataset_annos = os.path.join(dataset_dir,'annos')

k  =  glob.glob(dataset_annos + '/*.json')
count = 1
for j in k:
    print(count)
    x = []
    y = [] 
    nums_id = []
    filename = j.split('/')[-1][:-5] + '.jpg'
    polygon = {}
    with open(j,"r+") as f:
        data = json.load(f)
        print(data.get('height'), data.get('width'))
    count +=1