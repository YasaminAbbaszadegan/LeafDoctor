import torch
import torch.nn as nn
from torchvision import models,transforms

from PIL import Image
import os
import mlflow.pytorch
import mlflow
import pickle 


mlflow_pytorch_path=os.getcwd()+'/model'
model = mlflow.pytorch.load_model(mlflow_pytorch_path)


def predict(Path):
    """
    img : is an image conforms to PIL image format
    It returns the label index predicted by model
    """
    img=Image.open(Path)
    transform = transforms.Compose([            
    transforms.Resize(256),                    
    transforms.CenterCrop(224),                
    transforms.ToTensor(),                     
    transforms.Normalize(                      
    mean=[0.485, 0.456, 0.406],                
    std=[0.229, 0.224, 0.225]                  
    )])

    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)  
    out = model(batch_t)
    _, index = torch.max(out, 1)
    # percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100 
    # conf = percentage[index[0]].item()
    
    return index

def get_pred_label(labels_dict, idx=-1):
    """
    Return class label (plant_name, disease_name) having a valid index
    """
    if (idx>=0 and idx<=37):
        label = labels_dict[idx].split("___") 
    else:
        label = ['','']
    return label[0],label[1]
