from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image


class datas(Dataset):
    def __init__(self, array_list,base_path):
        super().__init__()
        self.array_list=array_list
        self.base_path=base_path
    
    def __len__(self):
        return len(self.array_list)
        
    def __getitem__(self,idx):
        anchor_path=self.array_list[idx][0]
        contrast_path=self.array_list[idx][1]
        target=self.array_list[idx][2]
        
        trans=transforms.Compose([transforms.Resize((105,105)),
                                  transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], 
                                                          [0.229, 0.224, 0.225]),
                                 ])
        
        anchor_img=Image.open(os.path.join(self.base_path,anchor_path))
        contrast_img=Image.open(os.path.join(self.base_path,contrast_path))
        anchor_tensor=trans(anchor_img)
        contrast_tensor=trans(contrast_img)
        return anchor_tensor, contrast_tensor,target