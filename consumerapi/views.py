from django.shortcuts import render
from newconsumer.consumerapi.models import Logininfo

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def logout(req):

    del req.session['username']
    return render(req, 'login.html')

def auth_user(req):
    msg = ''
    if req.method == "POST":
        formdata = req.POST
        user = formdata.get('username')
        pwd = formdata.get('password')
        instance = Logininfo.objects.filter(username=user,password=pwd).first()
        if instance:
            req.session['userinfo'] = {"role":instance.role,'username':instance.username}

            print('Session data -->',req.session['userinfo'])
            return render(req,'home.html',{'user':req.session['userinfo'],'flag':None,"val" : {"a":10}})  #
        msg = "Invalid Login Credentionls"
    return render(req, 'login.html', {'resp': msg})


def register_user(req):
    msg = ''
    if req.method =="POST":
        formdata = req.POST

        login = Logininfo(name=formdata.get('name'),
                  username=formdata.get('username'),
                  password=formdata.get('password'),
                  email=formdata.get('email'))
        login.save()
        msg ="User Registered Successfully....!"

    return render(req,'register.html',{'resp':msg})



from newconsumer.consumerapi.iteminfo import Item
from newconsumer.consumerapi.productconsumer import *

def add_product(req):
    msg = ''
    if req.method=='POST':
        formdata = req.POST
        pid = formdata.get('itid')
        pnm = formdata.get('itnm')
        prc = formdata.get('itpri')
        pqty = formdata.get('itqty')
        item = Item(pid,pnm,prc,pqty)
        msg = add_new_product(item)
    return render(req,'home.html',{"flag" : "AD",'resp':msg,'user':req.session['userinfo']})

def get_product(req):
    return render(req,'home.html',{"flag" : "SE",'user':req.session['userinfo']})

def show_all_products(req):
    prodlist = get_all_products()
    return render(req,'home.html',{"flag" : "AL",'user':req.session['userinfo'],
                                   'products' : prodlist})
def deleteproduct(req):
    itid = req.POST['delid']
    return delete_product(req,int(itid))

def delete_product(req,itid):
    msg = ''
    if itid>=0:
            msg = delete_product_api(itid)
    return render(req,'home.html',{"flag" : "DE",'user':req.session['userinfo'],'resp':msg})


def update_product(req):
    return render(req,'home.html',{"flag" : "UP",'user':req.session['userinfo']})
