from django.shortcuts import render,redirect
from django.contrib import messages

from main.forms import ApointmentForm, DeleteForm, FindForm
from main.models import Appointment
from datetime import date, datetime, timedelta
from calendar import mdays



def funt_if(i,arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,next_month2):
    i = i.split(".")
    print((date.today()+timedelta(mdays[date.today().month])).strftime("%m"))
    if i[1] == date.today().strftime("%m"):
        if i[2] == 'Ксюша':
            arr1.append(int(i[0]))

        elif i[2] == 'Настя':
            arr2.append(int(i[0]))

        elif i[2] == 'Надежда':
            arr3.append(int(i[0]))

        elif i[2] == 'Ирина':
            arr4.append(int(i[0]))
    elif i[1] == next_month2.strftime("%m"):
        if i[2] == 'Ксюша':
            arr5.append(int(i[0]))

        elif i[2] == 'Настя':
            arr6.append(int(i[0]))

        elif i[2] == 'Надежда':
            arr7.append(int(i[0]))

        elif i[2] == 'Ирина':
            arr8.append(int(i[0]))

def for_func(brons,arr):
    for i in brons:
        datetime_ = datetime.strptime(str(i.start),"%Y-%m-%d")
        c = int(str(i.end - datetime_.date()).split(" ")[0])
        counter = 0
        while counter < c:
            arr.append(f'{datetime_.strftime("%d.%m")}.{i.person}')
            datetime_+= timedelta(days=1)
            counter+=1

def test_dates(form,c):
    arr= []
    arr_error = []
    brons = Appointment.objects.filter(room = c ).order_by('-id')[:45]
    for i in brons:
        datetime_ = datetime.strptime(str(i.start),"%Y-%m-%d")
        difference = int(str(i.end - datetime_.date()).split(" ")[0])
        counter = 0
        while counter < difference:
            arr.append(f'{datetime_.strftime("%d.%m")}')
            datetime_+= timedelta(days=1)
            counter+=1

    difference_from_form = int(str(form.cleaned_data.get('end') - (datetime.strptime(str(form.cleaned_data.get('start')),"%Y-%m-%d")).date()).split(" ")[0])
    arr_form = []
    datetime_ = datetime.strptime(str(form.cleaned_data.get('start')),"%Y-%m-%d")
    counter_form = 0
    while counter_form < difference_from_form:
        arr_form.append(f'{datetime_.strftime("%d.%m")}')
        datetime_+= timedelta(days=1)
        counter_form+=1

    
    for i in arr_form:
        if i in arr:
            arr_error.append(i)
    
    if not arr_error:
        return 0
    else:
        return arr_error

def maintest(request):
    
    month= {
        "January":30,
        "Feburary":28,
        "March":31,
        "April":30,
        "May":31,
        "June":30,
        "July":31,
        "August":31,
        "September":30,
        "October":31,
        "November":30,
        "December":31,
    }
    month_russia = {
        "January":"Январь",
        "Feburary":"Февраль",
        "March":"Март",
        "April":"Апрель",
        "May":"Май",
        "June":"Июнь",
        "July":"Июль",
        "August":"Август",
        "September":"Сентябрь",
        "October":"Октябрь",
        "November":"Ноябрь",
        "December":"Декабрь"
        }
    # вычисление месяцев
    today = date.today()
    d2 = today.strftime("%B")
    next_month_of_today = today + timedelta(mdays[today.month])
    next_month2 = next_month_of_today.strftime("%B")
    if int(today.strftime("%d")) == int(month[str(next_month2)]):
        next_month_of_today -= timedelta(days=1)
        next_month2 = next_month_of_today.strftime("%B")

        

    # начало отсчета с нужного дня недели
    space_days_1 = today - timedelta(days=int(str(today.strftime("%d")))-1)
    space_days_1 = int(space_days_1.strftime("%w"))
    space_days_2 = next_month_of_today - timedelta(
                        days=int(str(next_month_of_today.strftime("%d")))-1)
    space_days_2 = int(space_days_2.strftime("%w"))



    # создание массива с бронями на голубенькую
    brons_blue = Appointment.objects.filter(room = 2 ).order_by('-id')[:45]
    brons_soffa = Appointment.objects.filter(room = 1 ).order_by('-id')[:45]
    brons_green = Appointment.objects.filter(room = 3 ).order_by('-id')[:45]
    brons_new = Appointment.objects.filter(room = 4 ).order_by('-id')[:45]
    brons_mountain = Appointment.objects.filter(room = 5 ).order_by('-id')[:45]
    brons_voykova = Appointment.objects.filter(room = 6 ).order_by('-id')[:45]
    brons_natash = Appointment.objects.filter(room = 8 ).order_by('-id')[:45]

    arr_blue_1 = []
    arr_blue_2 = []
    arr_blue_3 = []
    arr_blue_4 = []
    arr_blue_5 = []
    arr_blue_6 = []
    arr_blue_7 = []
    uborka = [[],[]]

    # убирать сегодня и завтра
    arr = [brons_blue,brons_soffa,brons_green,
            brons_new,brons_mountain,brons_voykova,brons_natash]
    today = date.today()
    tomorrow = (today + timedelta(days=1))

    # часть с бордерами
    brons_blue_bord = [[],[]]
    brons_soffa_bord = [[],[]]
    brons_green_bord = [[],[]]
    brons_new_bord = [[],[]]
    brons_mountain_bord = [[],[]]
    brons_voykova_bord = [[],[]]
    brons_natash_bord = [[],[]]
    arr2 = [brons_blue_bord,brons_soffa_bord,
            brons_green_bord,brons_new_bord,
            brons_mountain_bord,brons_voykova_bord,
            brons_natash_bord]
    d4 = today.strftime("%m")
    next_month_of_t_2 =next_month_of_today.strftime('%m')
    for i in arr:
        for j in i:
            # часть с уборкой
            if j.end == today:
                uborka[0].append(j.room.name)
            if j.end == tomorrow:
                uborka[1].append(j.room.name)
            # часть с бордерами в начале
            if j.start.strftime("%m") == d4:
                res = arr2[arr.index(i)]
                res[0].append(int(str(j.start.strftime("%d"))))
            elif j.start.strftime("%m") == next_month_of_t_2:
                res = arr2[arr.index(i)]
                res[1].append(int(str(j.start.strftime("%d"))))

            


    # функции заполнения броней по близ месяцам
    for_func(brons_soffa,arr_blue_1)
    for_func(brons_blue,arr_blue_2)
    for_func(brons_green,arr_blue_3)
    for_func(brons_new,arr_blue_4)
    for_func(brons_mountain,arr_blue_5)
    for_func(brons_voykova,arr_blue_6)
    for_func(brons_voykova,arr_blue_6)
    for_func(brons_natash,arr_blue_7)
    # массивы с массивами 
    ksusha = [[],[],[],[],[],[],[]]
    nasty = [[],[],[],[],[],[],[]]
    irina = [[],[],[],[],[],[],[]]
    nadya = [[],[],[],[],[],[],[]]
    ksusha2 = [[],[],[],[],[],[],[]]
    nasty2 = [[],[],[],[],[],[],[]]
    irina2 = [[],[],[],[],[],[],[]]
    nadya2 = [[],[],[],[],[],[],[]]
    
    # заполнение массивов для шаблонов
    for i in arr_blue_1:
        funt_if(i,ksusha[0],nasty[0],nadya[0],irina[0],
        ksusha2[0],nasty2[0],nadya2[0],irina2[0],next_month_of_today)

    for i in arr_blue_2:
        funt_if(i,ksusha[1],nasty[1],nadya[1],irina[1],
        ksusha2[1],nasty2[1],nadya2[1],irina2[1],next_month_of_today)

    for i in arr_blue_3:
        funt_if(i,ksusha[2],nasty[2],nadya[2],irina[2],
        ksusha2[2],nasty2[2],nadya2[2],irina2[2],next_month_of_today)

    for i in arr_blue_4:
        funt_if(i,ksusha[3],nasty[3],nadya[3],irina[3],
        ksusha2[3],nasty2[3],nadya2[3],irina2[3],next_month_of_today)

    for i in arr_blue_5:
        funt_if(i,ksusha[4],nasty[4],nadya[4],irina[4],
        ksusha2[4],nasty2[4],nadya2[4],irina2[4],next_month_of_today)

    for i in arr_blue_6:
        funt_if(i,ksusha[5],nasty[5],nadya[5],irina[5],
        ksusha2[5],nasty2[5],nadya2[5],irina2[5],next_month_of_today)
    
    for i in arr_blue_7:
        funt_if(i,ksusha[6],nasty[6],nadya[6],irina[6],
        ksusha2[6],nasty2[6],nadya2[6],irina2[6],next_month_of_today)

    okonch = ['soffa','blue','green','new','mountain','voykova','natash']
    

  
    context = {
        'month':month_russia[str(d2)],
        'month2':month_russia[str(next_month2)],
        'range': range(1,month[str(d2)]+1),
        'range2': range(1,month[str(next_month2)]+1),
        'uborka':uborka[0],
        'space_days_1':range(1,space_days_1),
        'space_days_2':range(1,space_days_2),
        'uborka_tomorrow':uborka[1],
    }


    for i in range(0,2):
        context[f'brons_blue_bord_{i}'] = brons_blue_bord[i]
        context[f'brons_soffa_bord_{i}'] = brons_soffa_bord[i]
        context[f'brons_green_bord_{i}'] = brons_green_bord[i]
        context[f'brons_new_bord_{i}'] = brons_new_bord[i]
        context[f'brons_mountain_bord_{i}'] = brons_mountain_bord[i]
        context[f'brons_voykova_bord_{i}'] = brons_voykova_bord[i]
        context[f'brons_natash_bord_{i}'] = brons_natash_bord[i]
        

    for i in range(0,7):
        context[f'ksusha_{okonch[i]}'] = ksusha[i]
        context[f'nadya_{okonch[i]}'] = nadya[i]
        context[f'nasty_{okonch[i]}'] = nasty[i]
        context[f'irina_{okonch[i]}'] = irina[i]
        context[f'ksusha2_{okonch[i]}'] = ksusha2[i]
        context[f'nadya2_{okonch[i]}'] = nadya2[i]
        context[f'nasty2_{okonch[i]}'] = nasty2[i]
        context[f'irina2_{okonch[i]}'] = irina2[i]

    return render(request,'main/main.html',context)


def delete(request):
    form = DeleteForm()
    form_bron = ApointmentForm()

    if request.method == "POST":
        form = DeleteForm(request.POST)
        form_bron = ApointmentForm(request.POST)
        
        if form_bron.is_valid():
            if form_bron.cleaned_data['end'] > form_bron.cleaned_data['start']:
                res = test_dates(form_bron,form_bron.cleaned_data['room'])
                if res == 0:
                    form_bron.save()
                    return redirect('main')
                else:
                    messages.add_message(request, messages.INFO, f'Бронь не отправилась эти даты заняты {res}')
                    return redirect('delete')
            else:
                messages.add_message(request, messages.INFO, 'Бронь не отправилась дата окончания меньше даты начала')
                return redirect('delete')

        elif form.is_valid():
            mark_appoint = Appointment.objects.filter(
                room = form.cleaned_data.get('room'),
                person = form.cleaned_data.get('person'),
                start = form.cleaned_data.get('start'))

            mark_appoint.delete()
            return redirect('main')



    context = {
        'form':form,
        'form_bron':form_bron,
    }
    return render(request,'main/delete.html',context)

def find(request):
    form = FindForm()
    ksusha = []
    nasty = []
    irina = []
    nadya = []
    flag = 0
    months = ["January","Feburary","March","April","May",
         "June", "July","August","September","October","November","December"]
    month_russia = {
        "January":"Январь",
        "Feburary":"Февраль",
        "March":"Март",
        "April":"Апрель",
        "May":"Май",
        "June":"Июнь",
        "July":"Июль",
        "August":"Август",
        "September":"Сентябрь",
        "October":"Октябрь",
        "November":"Ноябрь",
        "December":"Декабрь"
    }
    month= {
        "January":30,
        "Feburary":28,
        "March":31,
        "April":30,
        "May":31,
        "June":30,
        "July":31,
        "August":31,
        "September":30,
        "October":31,
        "November":30,
        "December":31,
    }
    space_days = 0
    if request.method == "GET":
        form = FindForm(request.GET)
        arr_find = []

        if form.is_valid():
            app = Appointment.objects.filter(
                                        room = form.cleaned_data.get('room'))

            for_func(app,arr_find)

            flag = form.cleaned_data.get('month')

            if flag<10 and flag!=0:
                    find_month = f'0{flag}'
            else: find_month = flag
            
            for i in arr_find:
                i = i.split(".")
                if str(i[1]) == str(find_month):
                    if i[2] == 'Ксюша':
                        ksusha.append(int(i[0]))

                    elif i[2] == 'Настя':
                        nasty.append(int(i[0]))

                    elif i[2] == 'Надежда':
                        irina.append(int(i[0]))

                    elif i[2] == 'Ирина':
                        nadya.append(int(i[0]))

            today = date.today()
            time_d = today
            for i in range(12):
                time_d += timedelta(days = 31)
                if int(str(time_d.strftime('%-m'))) == int(flag):
                    space_days = time_d - timedelta(
                                        days=int(str(time_d.strftime("%d")))-1)
                    if int(space_days.strftime("%w")) == 0:
                        space_days = 6
                    else:
                        space_days = int(space_days.strftime("%w"))-1
                
    
    context = {
        'form':form,
        'ksusha': ksusha,
        'nasty': nasty,
        'irina': irina,
        'nadya' :nadya,
    }
    context['month'] = month_russia[months[flag-1]]
    context['range'] = range(1,month[months[flag-1]])
    context['space_days'] = range(0,space_days)
    
    return render(request,'main/find.html',context)