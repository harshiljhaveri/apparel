import os 
import glob
import json
import skimage.draw
import skimage.io
import time 
dataset_dir = '/home/ai/Desktop/fashion/fashion/train'
dataset_img = os.path.join(dataset_dir,'image')
dataset_annos = os.path.join(dataset_dir,'annos')
count = 0 
a = time.time()
for j in glob.glob(dataset_annos + '/*.json'):

    x = []
    y = [] 
    nums_id = []
    filename = j.split('/')[-1][:-5] + '.jpg'
    polygon = {}
    with open(j,"r+") as f:
        data = json.load(f)
    # for i in data.keys():
    #     if i != 'source' and i != 'pair_id':
    #         x.append(data.get(i).get('segmentation')[0][::2])
    #         y.append(data.get(i).get('segmentation')[0][1::2])
    #         nums_id.append(data.get(i).get('category_id'))
    # polygon['x'] = x
    # polygon['y'] = y
        
        image_path = os.path.join(dataset_img, filename)
        image = skimage.io.imread(image_path)
        height, width = image.shape[:2]
        he = {'height' : height , 'width' : width}
        data.update(he)
        f.seek(0)
        json.dump(data, f)
    print(count,filename)
    count +=1

