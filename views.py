from flask import render_template,request
from flask import redirect, url_for
import os
from util import predict
from util import get_pred_label
import numpy
import pickle 


load_dict=pickle.load(open('labels_dict', 'rb'))
Uploaded_folder='static/uploads'
def base():
    if request.method=='POST':
        f=request.files["image"]
        filename=f.filename
        Path=os.path.join(Uploaded_folder,filename)
        f.save(Path)
        pred_idx=predict(Path)
        index=pred_idx.numpy()[0]
        plant_name, disease_name=get_pred_label(load_dict,index)
        a='Predicted plant name: {} '.format(plant_name) 
        b='Predicted disease: {} '.format(disease_name)
        return render_template('base.html',fileupload=True,img_name=filename,a=a,b=b)
    return render_template('base.html',fileupload=False,img_name="leafdoctor.png")



