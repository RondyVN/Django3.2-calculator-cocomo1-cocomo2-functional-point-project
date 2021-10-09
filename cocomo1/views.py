from django.shortcuts import render
import re

def hello(request):
    return render(request, 'cocomo1/cocomo_start.html')

def basic_cocomo(request):
    basic_data = request.GET.get('basic')

    if not request.GET.get('rows'):
        basic_data = None
    else:
        count_rows = request.GET.get('rows')

    basic_dict = {
        'organic': [2.4, 1.05, 2.5, 0.38],
        'semi_distributed': [3.0, 1.12, 2.5, 0.35],
        'built_in': [3.6, 1.20, 2.5, 0.32],
        None: '',
    }

    if basic_data is not None:
        PM = basic_dict[basic_data][0] * int(count_rows)**basic_dict[basic_data][1]
        TM = basic_dict[basic_data][2] * PM**basic_dict[basic_data][3]
        SS = PM / TM
        P = int(count_rows) / PM
        return render(request, 'cocomo1/basic_cocomo.html', {'PM': PM, 'TM': TM, 'SS': SS, 'P': P})
    else:
        return render(request, 'cocomo1/basic_cocomo.html', {'PM': 'Не повні данні', 'TM': 'Не повні данні', 'SS': 'Не повні данні', 'P': 'Не повні данні'})

def intermediate_cocomo(request):
    basic_data = request.GET.get('basic')

    count_rows = request.GET.get('rows')

    basic_dict = {
        'organic': [3.2, 1.05],
        'semi_distributed': [3.0, 1.12],
        'built_in': [2.8, 1.20],
        None: '',
    }

    dictt = {
        'RELY': ['Дуже низький 0.75', 'Низький 0.88', 'Середній 1.00', 'Високий 1.15', 'Дуже високий 1.40', 'Критичний n/a'],
        'DATA': ['Дуже низький n/a', 'Низький 0.85', 'Середній 1.00', 'Високий 1.08', 'Дуже високий 1.16', 'Критичний n/a'],
        'CPLX': ['Дуже низький 0.70', 'Низький 0.85', 'Середній 1.00', 'Високий 1.15', 'Дуже високий 1.30', 'Критичний 1.65'],
        'TIME': ['Дуже низький n/a', 'Низький n/a', 'Середній 1.00', 'Високий 1.11', 'Дуже високий 1.30', 'Критичний 1.66'],
        'STOR': ['Дуже низький n/a', 'Низький n/a', 'Середній 1.00', 'Високий 1.06', 'Дуже високий 1.21', 'Критичний 1.56'],
        'VIRT': ['Дуже низький n/a', 'Низький 0.87', 'Середній 1.00', 'Високий 1.15', 'Дуже високий 1.30', 'Критичний n/a'],
        'TURN': ['Дуже низький n/a', 'Низький 0.87', 'Середній 1.00', 'Високий 1.07', 'Дуже високий 1.15', 'Критичний n/a'],
        'ACAP': ['Дуже низький 1.46', 'Низький 1.19', 'Середній 1.00', 'Високий 0.86', 'Дуже високий 0.71', 'Критичний n/a'],
        'AEXP': ['Дуже низький 1.29', 'Низький 1.13', 'Середній 1.00', 'Високий 0.91', 'Дуже високий 0.82', 'Критичний n/a'],
        'PCAP': ['Дуже низький 1.42', 'Низький 1.17', 'Середній 1.00', 'Високий 0.86', 'Дуже високий 0.70', 'Критичний n/a'],
        'VEXP': ['Дуже низький 1.21', 'Низький 1.10', 'Середній 1.00', 'Високий 0.90', 'Дуже високий n/a', 'Критичний n/a'],
        'LEXP': ['Дуже низький 1.14', 'Низький 1.07', 'Середній 1.00', 'Високий 0.95', 'Дуже високий n/a', 'Критичний n/a'],
        'MODP': ['Дуже низький 1.24', 'Низький 1.10', 'Середній 1.00', 'Високий 0.91', 'Дуже високий 0.82', 'Критичний n/a'],
        'TOOL': ['Дуже низький 1.24', 'Низький 1.10', 'Середній 1.00', 'Високий 0.91', 'Дуже високий 0.83', 'Критичний n/a'],
        'SCED': ['Дуже низький 1.23', 'Низький 1.08', 'Середній 1.00', 'Високий 1.04', 'Дуже високий 1.10', 'Критичний n/a'],
    }

    name_atributs_dict = {
        'RELY': 'Необхідна надійність ПЗ',
        'DATA': 'Розмір БД додатка',
        'CPLX': 'Складність продукту',
        'TIME': 'Обмеження швидкодії при виконанні програми',
        'STOR': 'Обмеження памяті',
        'VIRT': 'Нестійкість оточення віртуальної машини',
        'TURN': 'Необхідний час відновлення ',
        'ACAP': 'Аналітичні здібності',
        'AEXP': 'Досвід розробки',
        'PCAP': 'Здібності до розробки ПЗ',
        'VEXP': 'Досвід використання віртуальних машин',
        'LEXP': 'Досвід розробки на мовах програмування',
        'MODP': 'Застосування методів розробки ПЗ',
        'TOOL': 'Використання інструментарію розробки',
        'SCED': 'Вимоги дотримання графіка розробки',
    }

    list_data_inter = []

    try:
        for key in dictt:
            a = request.GET.get(key)
            a = re.search(r'(\d+(?:[\.,]\d+)?$)|(n\/a)', a)
            try:
                list_data_inter.append(float(a.group(0)))
            except:
                list_data_inter.append(a.group(0))

        if count_rows:
            EAF = 1
            for a in list_data_inter:
                if type(a) != str:
                    EAF *= a
            PM = EAF * basic_dict[basic_data][0] * int(count_rows)**basic_dict[basic_data][1]
            return render(request, 'cocomo1/intermediate_cocomo.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': PM})
        else:
            return render(request, 'cocomo1/intermediate_cocomo.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': 'Введіть к-ть рядків коду'})
    except:
        return render(request, 'cocomo1/intermediate_cocomo.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': 'Введіть к-ть рядків коду'})


