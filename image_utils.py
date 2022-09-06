import os
import pickle
import random
import pickle
import torch

def get_single_image_folders(images_directory, images_path):
    subdirs={}
    single_image_folders=[]
    for directory in images_directory:
        subdirs[directory]=os.listdir(os.path.join(images_path,directory))
        if len(subdirs[directory])==1:
            single_image_folders.append(directory)
    return single_image_folders


def get_image_folders(images_directory,images_path):
    single_image_folders=get_single_image_folders(images_directory, images_path)
    multi_image_folders=list(set(images_directory)-set(single_image_folders))
    return single_image_folders, multi_image_folders

def create_positive_dataset(sample_size,multi_image_folders,images_path):
    positives=[]
    while len(positives)<=int(sample_size/2):
        for dir1 in multi_image_folders: #To re-run this, run the preceding cell to reset positives to []
            files=os.listdir(os.path.join(images_path,dir1))
            anchor, positive_img = random.sample(files, 2)
            anchor_path, positive_path=os.path.join(dir1,anchor),os.path.join(dir1,positive_img)
            if [anchor_path, positive_path, torch.ones(1,)] not in positives:
                positives.append([anchor_path, positive_path, torch.ones(1,)])
    return positives

def create_negative_dataset(sample_size,images_path, multi_image_folders,images_directory):
    negatives=[]
    while len(negatives)<=int(sample_size/2):
        for dir1 in multi_image_folders:
            neg_dirs=images_directory[:]
            neg_dirs.remove(dir1)
            neg_dir=random.sample(neg_dirs,1)
            anchor=random.sample(os.listdir(os.path.join(images_path,dir1)),1)
            negative_img=random.sample(os.listdir(os.path.join(images_path,neg_dir[0])),1)
            anchor_path =os.path.join(dir1,anchor[0])
            negative_path=os.path.join(neg_dir[0],negative_img[0])
            if [anchor_path, negative_path, torch.zeros(1,)] not in negatives:
                negatives.append([anchor_path, negative_path, torch.zeros(1,)])
    return negatives

def create_dataset(sample_size,multi_image_folders,images_path, images_directory):
    pos=create_positive_dataset(sample_size,multi_image_folders,images_path)
    neg=create_negative_dataset(sample_size,images_path, multi_image_folders,images_directory)
    final_data=pos+neg
    for _ in range(100):
        random.shuffle(final_data)
    return pos, neg, final_data

def save_data(pos, neg,tot):
    outputFile = 'positive.data'
    fw = open(outputFile, 'wb')
    pickle.dump(pos, fw)
    fw.close()

    outputFile = 'negative.data'
    fw = open(outputFile, 'wb')
    pickle.dump(neg, fw)
    fw.close()

    outputFile = 'total.data'
    fw = open(outputFile, 'wb')
    pickle.dump(tot, fw)
    fw.close()