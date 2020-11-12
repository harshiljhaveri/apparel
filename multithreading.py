from multiprocessing.dummy import Pool as ThreadPool


from concurrent.futures import ProcessPoolExecutor
import os 
import glob
import json
import skimage.draw
import skimage.io
import time 
dataset_dir = '/home/ai/Desktop/fashion/fashion/train-og'
dataset_img = os.path.join(dataset_dir,'image')
dataset_annos = os.path.join(dataset_dir,'annos')
count = 0 
a = time.time()
#niceValue = os.nice(-20) 

def write(j):
    x = []
    y = [] 
    nums_id = []
    filename = j.split('/')[-1][:-5] + '.jpg'
    polygon = {}
    with open(j,"r+") as f:
        data = json.load(f)
        image_path = os.path.join(dataset_img, filename)
        image = skimage.io.imread(image_path)
        height, width = image.shape[:2]
        he = {'height' : height , 'width' : width}
        data.update(he)
        f.seek(0)
        json.dump(data, f)
    print(filename)
    #count +=1

def write_now(k):
    for j in k:
        x = []
        y = [] 
        nums_id = []
        filename = j.split('/')[-1][:-5] + '.jpg'
        polygon = {}
        with open(j,"r+") as f:
            data = json.load(f)
            image_path = os.path.join(dataset_img, filename)
            image = skimage.io.imread(image_path)
            height, width = image.shape[:2]
            he = {'height' : height , 'width' : width}
            data.update(he)
            f.seek(0)
            json.dump(data, f)
        print(filename)


j =  glob.glob(dataset_annos + '/*.json')
j = sorted(j)
print(len(j))
pool = ThreadPool()

import concurrent.futures
executor = concurrent.futures.ProcessPoolExecutor(12)
futures = [executor.submit(write, item) for item in j]
concurrent.futures.wait(futures)

# from more_itertools import grouper    
# executor = concurrent.futures.PoolExecutor(12)
# futures = [executor.submit(write_now, group) 
#            for group in grouper(5, j[50000:100000])]
# concurrent.futures.wait(futures)
print(time.time() - a)
