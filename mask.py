import numpy as np
import cv2
import os
import pathlib
import json

json_dir =  pathlib.Path(r"C:\Users\Harshil\Desktop\DeepFashion2\train\annos")
json_list = list(json_dir.glob('*'))
json_count = len(json_list)
for w in range(json_count):
    with open(json_list[w], 'r') as f:
        annotations = json.load(f)
    if annotations['item1']['category_name'] == 'sling dress':
        data_dir = pathlib.Path(r"C:\Users\Harshil\Desktop\DeepFashion2\train\image")
        noz = '0'*(6 - len(str(w+1))) + str(w+1) + '.jpg'
        image = cv2.imread(os.path.join(data_dir, noz), -1)

        mask = np.zeros(image.shape, dtype=np.uint8)

        channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,)*channel_count
        a = annotations['item1']['segmentation']
        x = []
        hello = []
        for y in a:
            for i in range(len(y)):
                if i%2==0:
                    x.append(y[i])
                if i%2==1:
                    x.append(y[i])
                    hello.append(x)
                    x = []
            cv2.fillConvexPoly(mask, np.array(hello, 'int32'), ignore_mask_color)
            hello = []

        masked_image = cv2.bitwise_and(image, mask)

        directory = r"C:\Users\Harshil\Desktop\DeepFashion2\train\image"
        folds = 'sling dress'
        filename = str(w+1)+'.jpg'
        cv2.imwrite(os.path.join(directory, folds, filename), masked_image)
    if annotations['item2']['category_name'] == 'sling dress':
        data_dir = pathlib.Path(r"C:\Users\Harshil\Desktop\DeepFashion2\train\sab ka sab")
        noz = '0'*(6 - len(str(w+1))) + str(w+1) + '.jpg'
        image = cv2.imread(os.path.join(data_dir, noz), -1)

        mask = np.zeros(image.shape, dtype=np.uint8)

        channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,)*channel_count
        a = annotations['item2']['segmentation']
        x = []
        hello = []
        for y in a:
            for i in range(len(y)):
                if i%2==0:
                    x.append(y[i])
                if i%2==1:
                    x.append(y[i])
                    hello.append(x)
                    x = []
            cv2.fillConvexPoly(mask, np.array(hello, 'int32'), ignore_mask_color)
            hello = []

        masked_image = cv2.bitwise_and(image, mask)

        directory = r"C:\Users\Harshil\Desktop\DeepFashion2\train\image"
        folds = 'sling dress'
        filename = str(w+1)+'.jpg'
        cv2.imwrite(os.path.join(directory, folds, filename), masked_image)
    if annotations['item3']['category_name'] == 'sling dress':
        data_dir = pathlib.Path(r"C:\Users\Harshil\Desktop\DeepFashion2\train\sab ka sab")
        noz = '0'*(6 - len(str(w+1))) + str(w+1) + '.jpg'
        image = cv2.imread(os.path.join(data_dir, noz), -1)

        mask = np.zeros(image.shape, dtype=np.uint8)

        channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,)*channel_count
        a = annotations['item3']['segmentation']
        x = []
        hello = []
        for y in a:
            for i in range(len(y)):
                if i%2==0:
                    x.append(y[i])
                if i%2==1:
                    x.append(y[i])
                    hello.append(x)
                    x = []
            cv2.fillConvexPoly(mask, np.array(hello, 'int32'), ignore_mask_color)
            hello = []

        masked_image = cv2.bitwise_and(image, mask)

        directory = r"C:\Users\Harshil\Desktop\DeepFashion2\train\image"
        folds = 'sling dress'
        filename = str(w+1)+'.jpg'
        cv2.imwrite(os.path.join(directory, folds, filename), masked_image)
    