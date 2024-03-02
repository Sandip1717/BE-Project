import os
from twilio.rest import Client
account_sid = "AC77be3f2b24198f1a9f45947ce55a78e9"
auth_token = "60245d60398cfffabbdecd2b352faed8"
client = Client(account_sid, auth_token)

from datetime import datetime, timedelta
today = datetime.now()

from django.http import HttpResponse
from django.shortcuts import render,redirect

from childdata.models import  Imagef
from childdata.form import ImagefForm


from childdata.models import  Doctor
from childdata.models import  Parent
from childdata.models import  Blog
from childdata.models import  Vaccine
from childdata.models import  Vaccinereport


#home page

def index(request):
   request.session['fsrole']='Parent'
   form=ImagefForm()
   hn=Doctor.objects.only('hname')
   d={'form':form,
      'hname':hn
     }
   return render(request,"index.html",d)

def rdoctor(request):
      form=ImagefForm(files=request.FILES)
      if form.is_valid():
          form.save()
      a=request.FILES['image'].name
      fname=request.POST.get('fname')
      sname=request.POST.get('sname')
      photo=a
      uname=request.POST.get('uname')
      epass=request.POST.get('epass')
      cpass=request.POST.get('cpass')
      hname=request.POST.get('hname')
      haddress=request.POST.get('haddress')
      mobile=request.POST.get('mobile')
      nname=request.POST.get('nname')
      nphoto=a
      nuname=request.POST.get('nuname')
      nepass=request.POST.get('nepass')
      cepass=request.POST.get('cepass')
      z=Doctor(fname=fname,sname=sname,photo=photo,uname=uname,epass=epass,hname=hname,haddress=haddress,mobile=mobile,nname=nname,nphoto=nphoto,nuname=nuname,nepass=nepass)
      z.save()
      return redirect("index")

def fillvr(hid,cid):
    v=Vaccine.objects.all()
    hd=Doctor.objects.get(id=hid)
    did=hd.id
    dname=hd.sname
    hname=hd.hname
    cd=Parent.objects.get(id=cid)
    cname=cd.cname
    cphoto=cd.photo
    pname=cd.fname
    cdob=cd.cdob
    presentday= datetime.strptime(cdob, '%Y-%m-%d')
    for i in v:
       vid=i.id
       age=i.age
       vaccine=i.vaccine
       due=int(i.due)
       max=int(i.max)
       dued=(presentday+timedelta(due)).strftime('%Y-%m-%d')
       maxd=(presentday+timedelta(max)).strftime('%Y-%m-%d')
       given="0"
       dose=i.Dose
       route=i.route
       disease=i.disease
       symptoms=i.symptoms
       precautions=i.precautions
       height="0"
       weight="0"
       action="pending"
       vr=Vaccinereport(vid=vid,age=age,vaccine=vaccine,due=dued,max=maxd,given=given,dose=dose,route=route,disease=disease,symptoms=symptoms,precautions=precautions,cid=cid,cname=cname,cphoto=cphoto,pname=pname,did=did,dname=dname,hname=hname,height=height,weight=weight,action=action)
       vr.save()
    return 1


def rparent(request):
      form=ImagefForm(files=request.FILES)
      if form.is_valid():
          form.save()
      a=request.FILES['image'].name
      hid=request.POST.get('hid')
      s=Doctor.objects.get(id=hid)
      hname=s.hname
      fname=request.POST.get('fname')
      photo=a
      address=request.POST.get('address')
      mobile=request.POST.get('mobile')
      cname=request.POST.get('cname')
      cdob=request.POST.get('cdob')
      uname=request.POST.get('uname')
      epass=request.POST.get('epass')
      cpass=request.POST.get('cpass')
      sms="welcome parent on child immunization system Dear parent "+fname+" your child "+cname+" register succefully. Your username is "+uname+" and password is "+epass
      message = client.messages.create(body=sms,from_="+12706067452",to="+919373809473")
      z=Parent(fname=fname,photo=photo,address=address,mobile=mobile,cname=cname,cdob=cdob,uname=uname,hid=hid,hname=hname,epass=epass)
      z.save()
      s=Parent.objects.get(uname=uname)
      cid=s.id
      d=fillvr(hid,cid)
      return redirect("index")

def login(request):
     role=request.POST.get('role')
     email=request.POST.get('email')
     epass=request.POST.get('epass')
     if(role=='Admin'):
          fu=Parent.objects.filter(fname='admin',uname=email,epass=epass)
          if fu:
               s=Parent.objects.get(uname=email)
               request.session['auid']=s.id
               request.session['role']='Admin'
               return redirect("admin")
          else:
               return redirect("index")
     elif(role=='Doctor'):
          fu=Doctor.objects.filter(uname=email,epass=epass)
          if fu:
               s=Doctor.objects.get(uname=email)
               request.session['duid']=s.id
               request.session['drole']='Doctor'
               return redirect("doctor")
          else:
               return redirect("index")
     elif(role=='Parent'):
          fu=Parent.objects.filter(uname=email,epass=epass)
          if fu:
               s=Parent.objects.get(uname=email)
               request.session['puid']=s.id
               request.session['role']='Parent'
               return redirect("parent")
          else:
               return redirect("index")
     else:
        fu=Doctor.objects.filter(nuname=email,nepass=epass)
        if fu:
            s=Doctor.objects.get(nuname=email)
            request.session['nuid']=s.id
            request.session['role']='Nurse'
            return redirect("nurse")
        else:
            return redirect("index")

def fpassword(request):
     role=request.POST.get('role')
     email=request.POST.get('email')
     epass=request.POST.get('epass')
     cpass=request.POST.get('cpass')
     if(role=='Admin'):
        try:
            fu=Parent.objects.get(uname=email)
            fu.epass=cpass
            fu.save()
            return redirect("index")
        except:
            return HttpResponse("not changed user notfound")
     elif(role=='Doctor'):
        try:
            fu=Doctor.objects.get(uname=email)
            fu.epass=cpass
            fu.save()
            return redirect("index")
        except:
            return HttpResponse("not changed user notfound")
     elif(role=='Parent'):
        try:
            fu=Parent.objects.get(uname=email)
            fu.epass=cpass
            fu.save()
            return redirect("index")
        except:
            return HttpResponse("not changed user notfound")
     else:
        try:
            fu=Doctor.objects.get(nuname=email)
            fu.nepass=cpass
            fu.save()
            return redirect("index")
        except:
            return HttpResponse("not changed user notfound")
def logout(request):
    return redirect("index")

#admin page 

def getAdata(uid):
    fu=Parent.objects.get(id=uid)
    fname=fu.cname
    photo=fu.photo
    address=fu.address
    mobile=fu.mobile
    email=fu.uname
    form=ImagefForm()
    bd=Blog.objects.all().order_by('-id').values()
    data={'name':fname,'img':photo,'address':address,'mobile':mobile,'email':email,'form':form,'blist':bd}
    return data

def adminh(request):
    uid=request.session['auid']
    data=getAdata(uid)
    td=Doctor.objects.all()
    data['td']=td
    tp=Parent.objects.all()
    data['tp']=tp
    tv=Vaccinereport.objects.all()
    data['tv']=tv
    dv=Vaccinereport.objects.filter(action=0).values()
    data['dv']=tp
    return render(request,"admin.html",data)

def aprofile(request):
    uid=request.session['auid']
    fu=Parent.objects.get(id=uid)
    if request.method=="POST":
        try:
            form1=ImagefForm(files=request.FILES)
            if form1.is_valid():
                form1.save()
            a=request.FILES['image'].name
            fname=request.POST.get('fname')
            address=request.POST.get('address')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            epass=request.POST.get('epass')
            if fu.epass==epass:
                fu.cname=fname
                fu.address=address
                fu.mobile=mobile
                fu.uname=email
                fu.photo=a
                fu.save()
                return redirect("aprofile")
            else:
                return HttpResponse("password doesnot match")
        except:
            return HttpResponse("not update profile")
    else:
        data=getAdata(uid)
        return render(request,"aprofile.html",data)

def amanageuser(request):
    uid=request.session['auid']
    data=getAdata(uid)
    fsrole=request.session['fsrole']
    if fsrole=='Parent':
        udata=Parent.objects.all()
        data['udata']=udata
        data['role']=1
    else:
        udata=Doctor.objects.all()
        data['udata']=udata
        data['role']=2
    return render(request,"amanageuser.html",data)

def srole(request):
    fsr=request.POST.get('role')
    request.session['fsrole']=fsr
    return redirect("amanageuser")

def deleteu(request):
    role=request.POST.get('role')
    id=request.POST.get('id')
    if role=='1':
        fu=Parent.objects.get(id=id)
        fu.delete()
    else:
        fu=Doctor.objects.get(id=id)
        fu.delete()
    return redirect("amanageuser")

def aviewblog(request):
    uid=request.session['auid']
    data=getAdata(uid)
    return render(request,"aviewblog.html",data)

def addblog(request):
    form=ImagefForm(files=request.FILES)
    if form.is_valid():
        form.save()
    a=request.FILES['image'].name
    btitle=request.POST.get('btitle')
    bphoto=a
    bdata=request.POST.get('bdata')
    bauthor=request.POST.get('bauthor')
    bdate=today.strftime("%Y-%m-%d")
    z=Blog(btitle=btitle,bphoto=bphoto,bdata=bdata,bauthor=bauthor,bdate=bdate)
    z.save()
    return redirect("aviewblog")

def vblog(request):
    uid=request.session['auid']
    data=getAdata(uid)
    bid=int(request.POST.get('bid'))
    data['bdata']=Blog.objects.get(id=bid)
    return render(request,"ademo.html",data)


#parent page
def getPdata(uid):
    fu=Parent.objects.get(id=uid)
    cid=str(fu.id)
    fname=fu.fname
    photo=fu.photo
    address=fu.address
    mobile=fu.mobile
    cname=fu.cname
    hname=fu.hname
    email=fu.uname
    form=ImagefForm()
    bd=Blog.objects.all().order_by('-id').values()
    data={'cid':cid,'name':fname,'img':photo,'address':address,'mobile':mobile,'cname':cname,'hname':hname,'email':email,'form':form,'blist':bd}
    return data

def parenth(request):
    uid=request.session['puid']
    data=getPdata(uid)
    tv=Vaccinereport.objects.filter(cid=uid).values()
    data['tv']=tv
    dv=Vaccinereport.objects.filter(action=0,cid=uid).values()
    data['dv']=dv
    pv=Vaccinereport.objects.filter(action='pending',cid=uid).values()
    data['pv']=pv
    mv=Vaccinereport.objects.filter(action=3,cid=uid).values()
    data['mv']=mv

    b=Vaccinereport.objects.filter(cid=uid).order_by('-given')[0]
    weight=float(b.weight)
    height=int(b.height)
    vid=b.vid
    fu=Vaccine.objects.get(id=vid)
    day=fu.days
    month=int(day)//12
    #ml model
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    dataf= pd.read_csv(r'./media/childgrowth.csv')    #Loading the dataset
    x=dataf.drop('Result', axis=1)
    y=dataf['Result']
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.30) #Train test split
    model = LogisticRegression() #Training
    model.fit(x_train, y_train)  #Predicting
    pred = model.predict([[month,weight,height]])
    if pred==1:
        data['growth']='1'
    else:
        data['growth']='0'
    return render(request,"parent.html",data)

def pprofile(request):
    uid=request.session['puid']
    fu=Parent.objects.get(id=uid)
    if request.method=="POST":
        try:
            form1=ImagefForm(files=request.FILES)
            if form1.is_valid():
                form1.save()
            a=request.FILES['image'].name
            fname=request.POST.get('fname')
            address=request.POST.get('address')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            epass=request.POST.get('epass')
            if fu.epass==epass:
                fu.fname=fname
                fu.address=address
                fu.mobile=mobile
                fu.uname=email
                fu.photo=a
                fu.save()
                return redirect("pprofile")
            else:
                return HttpResponse("password doesnot match")
        except:
            return HttpResponse("not update profile")
    else:
        data=getPdata(uid) 
        return render(request,"pprofile.html",data)

def pcheckreport(request):
    uid=request.session['puid']
    data=getPdata(uid)
    data['vrdata']=Vaccinereport.objects.all()
    return render(request,"pcheckreport.html",data)

def pappointment(request):
    uid=request.session['puid']
    data=getPdata(uid)
    data['vrdata']=Vaccinereport.objects.all()
    return render(request,"pappointment.html",data)

def paappointment(request):
    vid=request.POST.get('vid')
    fu=Vaccinereport.objects.get(id=vid)
    fu.action=2
    fu.save()
    return redirect("pappointment")

def pvdetails(request,vid):
    uid=request.session['puid']
    data=getPdata(uid)
    vd=Vaccinereport.objects.get(id=vid)
    data['vdata']=vd
    return render(request,"pvdetails.html",data)

def pviewblog(request):
    uid=request.session['puid']
    data=getPdata(uid)
    return render(request,"pviewblog.html",data)

def pvblog(request):
    uid=request.session['puid']
    data=getPdata(uid)
    bid=int(request.POST.get('bid'))
    data['bdata']=Blog.objects.get(id=bid)
    return render(request,"pdemo.html",data)

#doctor page
def getDdata(uid):
    fu=Doctor.objects.get(id=uid)
    did=str(fu.id)
    fname=fu.fname
    photo=fu.photo
    address=fu.haddress
    hname=fu.hname
    dname=fu.sname
    mobile=fu.mobile
    email=fu.uname
    form=ImagefForm()
    bd=Blog.objects.all().order_by('-id').values()
    data={'did':did,'name':fname,'img':photo,'address':address,'mobile':mobile,'hname':hname,'dname':dname,'email':email,'form':form,'blist':bd}
    return data


def doctorh(request):
    uid=request.session['duid']
    data=getDdata(uid)
    tp=Parent.objects.all()
    data['tp']=tp
    tdate=today.strftime("%Y-%m-%d")
    tdv=Vaccinereport.objects.filter(given=tdate,did=uid).values()
    data['tdv']=tdv
    tv=Vaccinereport.objects.filter(did=uid).values()
    data['tv']=tv
    dv=Vaccinereport.objects.filter(action=0,did=uid).values()
    data['dv']=dv
    return render(request,"doctor.html",data)

def dprofile(request):
    uid=request.session['duid']
    fu=Doctor.objects.get(id=uid)
    if request.method=="POST":
        try:
            form1=ImagefForm(files=request.FILES)
            if form1.is_valid():
                form1.save()
            a=request.FILES['image'].name
            fname=request.POST.get('fname')
            address=request.POST.get('address')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            epass=request.POST.get('epass')
            if fu.epass==epass:
                fu.fname=fname
                fu.haddress=address
                fu.mobile=mobile
                fu.uname=email
                fu.photo=a
                fu.save()
                return redirect("dprofile")
            else:
                return HttpResponse("password doesnot match")
        except:
            return HttpResponse("not update profile")
    else:
        data=getDdata(uid)
        return render(request,"dprofile.html",data)

def dappointment(request):
    uid=request.session['duid']
    data=getDdata(uid)
    data['vrdata']=Vaccinereport.objects.all()
    tdate=today.strftime("%Y-%m-%d")
    data['today']=tdate
    return render(request,"dappointment.html",data)

def vdone(request):
    vid=request.POST.get('vid')
    ch=request.POST.get('ch')
    cw=request.POST.get('cw')
    fu=Vaccinereport.objects.get(id=vid)
    fu.height=ch
    fu.weight=cw
    fu.given=today.strftime("%Y-%m-%d")
    fu.action=0
    fu.save()
    sms="welcome parent on child immunization system Dear parent "+fu.pname+" your child "+fu.cname+" "+fu.vaccine+" vaccination done succefull."
    message = client.messages.create(body=sms,from_="+12706067452",to="+919373809473")
    return redirect("dappointment")

def dvdetails(request,vid):
    uid=request.session['duid']
    data=getDdata(uid)
    vd=Vaccinereport.objects.get(id=vid)
    data['vdata']=vd
    return render(request,"dvdetails.html",data)


def dviewblog(request):
    uid=request.session['duid']
    data=getDdata(uid)
    return render(request,"dviewblog.html",data)

def daddblog(request):
    form=ImagefForm(files=request.FILES)
    if form.is_valid():
        form.save()
    a=request.FILES['image'].name
    btitle=request.POST.get('btitle')
    bphoto=a
    bdata=request.POST.get('bdata')
    bauthor=request.POST.get('bauthor')
    bdate=today.strftime("%Y-%m-%d")
    z=Blog(btitle=btitle,bphoto=bphoto,bdata=bdata,bauthor=bauthor,bdate=bdate)
    z.save()
    return redirect("dviewblog")

def dvblog(request):
    uid=request.session['duid']
    data=getNdata(uid)
    bid=int(request.POST.get('bid'))
    data['bdata']=Blog.objects.get(id=bid)
    return render(request,"ddemo.html",data)


def getNdata(uid):
    fu=Doctor.objects.get(id=uid)
    did=str(fu.id)
    fname=fu.nname
    photo=fu.nphoto
    address=fu.haddress
    mobile=fu.mobile
    email=fu.nuname
    hname=fu.hname
    dname=fu.sname
    form=ImagefForm()
    bd=Blog.objects.all().order_by('-id').values()
    data={'did':did,'name':fname,'img':photo,'address':address,'mobile':mobile,'email':email,'hname':hname,'dname':dname,'form':form,'blist':bd}
    return data

def nurseh(request):
    uid=request.session['nuid']
    data=getNdata(uid)
    tp=Parent.objects.all()
    data['tp']=tp
    tdate=today.strftime("%Y-%m-%d")
    tdv=Vaccinereport.objects.filter(given=tdate,did=uid).values()
    data['tdv']=tdv
    tv=Vaccinereport.objects.filter(did=uid).values()
    data['tv']=tv
    dv=Vaccinereport.objects.filter(action=0,did=uid).values()
    data['dv']=dv
    return render(request,"nurse.html",data)

def nprofile(request):
    uid=request.session['nuid']
    fu=Doctor.objects.get(id=uid)
    if request.method=="POST":
        try:
            form1=ImagefForm(files=request.FILES)
            if form1.is_valid():
                form1.save()
            a=request.FILES['image'].name
            fname=request.POST.get('fname')
            address=request.POST.get('address')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            epass=request.POST.get('epass')
            if fu.nepass==epass:
                fu.nname=fname
                fu.haddress=address
                fu.mobile=mobile
                fu.nuname=email
                fu.nphoto=a
                fu.save()
                return redirect("nprofile")
            else:
                return HttpResponse("password doesnot match")
        except:
            return HttpResponse("not update profile")
    else:
        data=getNdata(uid)
        return render(request,"nprofile.html",data)

def nviewchild(request):
    uid=request.session['nuid']
    data=getNdata(uid)
    data['cdata']=Parent.objects.all()
    hn=Doctor.objects.only('hname')
    data['hname']=hn
    return render(request,"nviewchild.html",data)

def nrparent(request):
      form=ImagefForm(files=request.FILES)
      if form.is_valid():
          form.save()
      a=request.FILES['image'].name
      hid=request.POST.get('hid')
      s=Doctor.objects.get(id=hid)
      hname=s.hname
      fname=request.POST.get('fname')
      photo=a
      address=request.POST.get('address')
      mobile=request.POST.get('mobile')
      cname=request.POST.get('cname')
      cdob=request.POST.get('cdob')
      uname=request.POST.get('uname')
      epass=request.POST.get('epass')
      cpass=request.POST.get('cpass')
      sms="welcome parent on child immunization system Dear parent "+fname+" your child "+cname+" register succefully. Your username is "+uname+" and password is "+epass
      message = client.messages.create(
      body=sms,
      from_="+12706067452",
      to="+919373809473"
      )
      z=Parent(fname=fname,photo=photo,address=address,mobile=mobile,cname=cname,cdob=cdob,uname=uname,hid=hid,hname=hname,epass=epass)
      z.save()
      s=Parent.objects.get(uname=uname)
      cid=s.id
      d=fillvr(hid,cid)
      return redirect("nviewchild")

def nappointment(request):
    uid=request.session['nuid']
    data=getNdata(uid)
    data['vrdata']=Vaccinereport.objects.all().order_by('due').values()
    return render(request,"nappointment.html",data)

def nvdetails(request,vid):
    uid=request.session['nuid']
    data=getNdata(uid)
    vd=Vaccinereport.objects.get(id=vid)
    data['vdata']=vd
    return render(request,"nvdetails.html",data)

def naappointment(request):
    vid=request.POST.get('vid')
    gdate=request.POST.get('gdate')
    fu=Vaccinereport.objects.get(id=vid)
    fu.given=gdate
    fu.action=1
    fu.save()
    sms="welcome parent on child immunization system Dear parent "+fu.pname+" your child "+fu.cname+" "+fu.vaccine+" vaccine schedule on "+gdate+" at "+fu.hname+" so don't missed it."
    message = client.messages.create(body=sms,from_="+12706067452",to="+919373809473")
    return redirect("nappointment")
    
def nviewblog(request):
    uid=request.session['nuid']
    data=getNdata(uid)
    return render(request,"nviewblog.html",data)

def naddblog(request):
    form=ImagefForm(files=request.FILES)
    if form.is_valid():
        form.save()
    a=request.FILES['image'].name
    btitle=request.POST.get('btitle')
    bphoto=a
    bdata=request.POST.get('bdata')
    bauthor=request.POST.get('bauthor')
    bdate=today.strftime("%Y-%m-%d")
    z=Blog(btitle=btitle,bphoto=bphoto,bdata=bdata,bauthor=bauthor,bdate=bdate)
    z.save()
    return redirect("nviewblog")

def nvblog(request):
    uid=request.session['nuid']
    data=getNdata(uid)
    bid=int(request.POST.get('bid'))
    data['bdata']=Blog.objects.get(id=bid)
    return render(request,"ndemo.html",data)



    