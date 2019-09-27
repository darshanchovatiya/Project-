from django import forms
from .models import *
from django.forms.widgets import *


class productu(forms.ModelForm):
        class Meta:
            model = item
            fields = ['p_name','price','stock','desc','image']
            labels  = {
                'p_name':'Product Name', 
                'price':'Price of Product', 
                'stock':'Stock Of Product', 
                'desc':'Product Discription', 
                'image':'Image Of Product'
            }
class editprofile(forms.ModelForm):
    class Meta:
        model=Uregiser
        fields=['u_name','city','area','contect','pincode','password']
        labels  = {
                'u_name':'User Name', 
                'city':'City', 
                'area':'Address', 
                'contect':'Contect', 
                'pincode':'Pincode',
                'password':'Password',
            }

class engprofile(forms.ModelForm):
    class Meta:
        model=eregiser
        fields=['e_name','contect','e_type','city','password']
        labels  = {
                'e_name':'Engineer Name', 
                'contect':'Contect', 
                'e_type':'Engineer Type', 
                'city':'City', 
                'password':'password'
            }
class headprofile(forms.ModelForm):
    class Meta:
        model=head
        fields=['a_name','email','contect','password']
        labels  = {
                'a_name':'Admin Name', 
                'email':'Admin email',
                'contect':'Contect Number',  
                'password':'Password'
            }
class VideoForm(forms.ModelForm):
    class Meta:
        model= video
        fields= ["v_name", "video","image","discr"]
        labels  = {
                'v_name':'Video Name', 
                'video':'Upload Video', 
                'image':'Upload Image', 
                'desc':'Video Discription', 
        }

class comp(forms.ModelForm):
        class Meta:
            model = complain
            fields = ['c_type','c_desc','image']
            labels  = { 
                'c_type':'Complain Type', 
                'c_desc':'Complain discription', 
                'image':'Image Of Complaint'
            }

class compc(forms.ModelForm):
        class Meta:
            model = complain
            fields = ['creq']
            labels  = { 
                'creq':'Your Rquirement(In Peace) ',                 
            }

class compbill(forms.ModelForm):
        class Meta:
            model = transection
            fields = ['c_desc','total']
            labels  = {               
                'c_desc':'Discription', 
                'total':'Total Price'
            }
class csobill(forms.ModelForm):
        class Meta:
            model = transection
            fields = ['total']
            labels  = {            
                'total':'Total Price'
            }
class product(forms.ModelForm):
        class Meta:
            model = cart
            fields = []
            
class ord(forms.ModelForm):
        class Meta:
            model = order
            fields = ['address','pincode','landmark']
           
class ser(forms.ModelForm):
        class Meta:
            model = server
            fields = ['company','switch','contact']
            labels  = {               
                'company':'Company Of Server', 
                'switch':'Switch Board For Server'
            }
            widgets = {'company':forms.RadioSelect}

class came(forms.ModelForm):
        class Meta:
            model = camera
            fields = ['company','cprice','vision','Megapixel']
            labels  = {               
                'company':'Company Of Camara', 
                'cprice':'Camera Price',
                'vision':'Camera Vision'
            }
            widgets = {'vision':forms.RadioSelect}    
         