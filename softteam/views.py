from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import detail_of_worker,User,attendence,attends
from datetime import date, datetime

import sys
def welcome(request):
    return render(request, 'welcome2.html')

def index(request):
    return render(request, 'index2.html')


def first(request):
    return render(request, 'first.html')


def second(request):
    return render(request, 'second.html')


a='anshul'
b='akotiya'


def user_idfirst(request):
    Auserid = (request.POST.get('userid1', 'invalid'))
    Apassword1 = (request.POST.get('password1', 'invalid'))
    if(Auserid == a):
        if(Apassword1==b):
            return render(request, 'firstlogin.html')
        else:
            messages.error(request, 'Invalid login id or password')
            return redirect(first)
    else:
        messages.error(request, 'Invalid login id or password')
        return redirect(first)



def user_idsecond(request):
    Buserid1 = (request.POST.get('userid2', 'invalid'))
    Bpassword1 = (request.POST.get('password2', 'invalid'))
    if(Buserid1 == a):
        if(Bpassword1==b):
            return render(request, 'secondlogin.html')
        else:
            messages.error(request, 'Invalid login id or password')
            return redirect(second)
    else:
        messages.error(request, 'Invalid login id or password')
        return redirect(second)



def applied_job(request):
        return render(request, 'applied.html')

def add_sups(request):
    return render(request, 'addsup.html')


def add_supervisor(request):
    name = (request.POST.get('name_supervisor', 'default'))
    gender = (request.POST.get('address', 'invalid'))
    addhar_no = (request.POST.get('addhar', '0'))
    mobile_no = (request.POST.get('mobile_no', '0'))
    password = 'hello'
    add_sup = User(name=name, gender=gender, addhar_no=addhar_no, mobile_no=mobile_no,password=password)
    add_sup.save()
    return HttpResponse("form submited")


def detail(request):
    all_data = detail_of_worker.objects.all()
    return render(request, 'detail.html', {'data':all_data})


def add_worker(request):
    name_worker = (request.POST.get('name', 'default'))
    headname_worker = (request.POST.get('hname', 'default'))
    address_worker = (request.POST.get('personal_address', 'default'))
    mobile_worker = (request.POST.get('mobile_no', '0'))
    addhar_worker = (request.POST.get('addhar', '0'))
    gender_worker = (request.POST.get('gender', 'default'))
    dob_worker = (request.POST.get('dob', '0'))
    age_worker = (request.POST.get('age', '0'))
    image_worker = (request.POST.get('image'))
    state_worker = (request.POST.get('state', 'default'))
    distric_worker = (request.POST.get('distric', 'default'))
    block_worker = (request.POST.get('block', 'default'))
    panchayat_worker = (request.POST.get('panchayat', 'default'))
    account_worker = (request.POST.get('ac_no', '0'))
    ifsc_worker = (request.POST.get('code', 'default'))
    bank_worker =(request.POST.get('bank'))
    reaccount =(request.POST.get('reac_no'))
    ans = detail_of_worker.objects.latest('ap_no_worker')
    ap_no_worker = ans.ap_no_worker + 1
    # checkstro
    if len(mobile_worker) == 10:
        if len(addhar_worker) == 12:
            if age_worker >= str(18):
                if reaccount ==account_worker:
                        detail = detail_of_worker(name_worker=name_worker, headname_worker=headname_worker,
                        address_worker=address_worker, mobile_worker=mobile_worker, addhar_worker=addhar_worker,
                        gender_worker=gender_worker, dob_worker=dob_worker, age_worker=age_worker,
                        image_worker=image_worker, state_worker=state_worker, distric_worker=distric_worker,
                        block_worker=block_worker, panchayat_worker=panchayat_worker, account_worker=account_worker,
                        ifsc_worker=ifsc_worker, bank_worker=bank_worker, ap_no_worker=ap_no_worker)
                        detail.save()
                        messages.success(request, 'your application is saved successfully')
                        return redirect('applied')
                else:
                    messages.error(request,'account number not matched')
                    return redirect('applied')
            else:
                messages.error(request, 'age should be greater than or equal to 18')
                return redirect('applied')
        else:
            messages.error(request, 'addhar number should be of 12 digits')
            return redirect('applied')
    else:
        messages.error(request, 'mobile number should be of 10 digits')
        return redirect('applied')


def bank_detail(request):
      all_detail = detail_of_worker.objects.all()
      return render(request, 'bank.html', {'data': all_detail})


def hello2(request):
    return render(request, 'hello.html')

def verify(request):
    app_no = (request.POST.get('application'))
    global c
    c = app_no
    all_data = detail_of_worker.objects.get(ap_no_worker=app_no)
    if str(all_data.card_status) == str('not issued'):
            all_data = detail_of_worker.objects.get(ap_no_worker=app_no)
            return render(request, 'verify.html', {'data': all_data})
    else:
        messages.error(request, 'please write the correct application number')
        return redirect('/softteam/not_verify')

def verifing(request):
    verify_name = request.POST.get('name', 'off')
    verify_addhar =request.POST.get('addhar', 'off')
    verify_gender =request.POST.get('gender', 'off')
    verify_image =request.POST.get('image', 'off')
    verify_address =request.POST.get('address', 'off')
    verify_account = request.POST.get('account', 'off')
    verify_bank = request.POST.get('bank', 'off')
    verify_ifsc = request.POST.get('ifsc', 'off')
    app_no = c
    all_data = detail_of_worker.objects.get(ap_no_worker=app_no)
    if verify_name == 'on':
        all_data.verify_name = 'Verified'

    if verify_addhar == 'on':
        all_data.verify_addhar = 'Verified'

    if verify_gender == 'on':
        all_data.verify_gender = 'Verified'

    if verify_image == 'on':
        all_data.verify_image = 'Verified'

    if verify_address == 'on':
        all_data.verify_address = 'Verified'

    if verify_account == 'on':
        all_data.verify_account = 'Verified'

    if verify_bank == 'on':
        all_data.verify_bank = 'Verified'

    if verify_ifsc == 'on':
        all_data.verify_ifsc = 'Verified'
    all_data.save()
    if all_data.verify_name == 'Verified':
        if all_data.verify_addhar == 'Verified':
            if all_data.verify_gender == 'Verified':
                if all_data.verify_image == 'Verified':
                    if all_data.verify_address == 'Verified':
                        if all_data.verify_account == 'Verified':
                            if all_data.verify_bank == 'Verified':
                                if all_data.verify_ifsc == 'Verified':
                                    all_data.card_status = 'Issued'
                                    messages.success(request, "job card is issued")
    all_data.save()
    messages.success(request, "successfully save the verification")
    return redirect(not_verified)

def app_status(request):
    return render(request, 'application_status.html')


def result(request):
    appli = request.POST.get('application')
    detail = detail_of_worker.objects.all()
    for i in detail:
        if str(appli) == str(i.ap_no_worker):
            res = detail_of_worker.objects.get(ap_no_worker=appli)
            return render(request, 'result.html', {'data': res})
    else:
        messages.error(request, 'Please enter valid application number')
        return redirect('/softteam/status')

def not_verified(request):
    all_detail = detail_of_worker.objects.all()
    return render(request, 'verification_table.html', {'data': all_detail})

def add_officer(request):
    return render(request, 'add.html')


def Attendence(request):
    all_data =attends.objects.all()
    todays = datetime.now()
    return render(request, 'daily_att.html', {'data': all_data, 'today':todays})

def date_att(request):
    return render(request, 'date_attendence.html')

def table_att(request):
    f_date = request.POST.get('fromdate')
    t_date = request.POST.get('todate')
    all_data = attendence.objects.all()
    todays = date.today()
    return render(request, 'date_atte.html',{'data':all_data, 'today':todays,'from_date':f_date,'to_date':t_date})

def muster(request):
    return render(request, 'musteroll.html')

def attby_app(request):
    return render(request, 'attby_app.html')


def att_search(request):
    appli = request.POST.get('appli')
    appl  =str(appli)
    all_data = attendence.objects.all()
    return render(request, 'attby_application.html', {'data': all_data, 'app': appl})

def work(request):
    return render(request, 'work.html')

def bank_by_app(request):
    app = request.POST.get('application')
    all_data = detail_of_worker.objects.get(ap_no_worker=app)
    return render(request,'bank_detailby_app.html',{'data':all_data})

def password2(request):
    return HttpResponse('password changed')

def logout2(request):
    return HttpResponse('YOU ARE SUCCESSFULLY LOGGED OUT')

def hello(request):
    return render(request, 'hello.html')