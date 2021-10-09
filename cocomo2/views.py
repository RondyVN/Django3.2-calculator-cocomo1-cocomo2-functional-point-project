from django.shortcuts import render
import re

def cocomo2_start(request):
    return render(request, 'cocomo2/start.html')

def preliminary_assessment(request):

    count_rows = request.GET.get('rows')

    dictt = {
        'PREC': ['Very Low 6.20', 'Low 4.96', 'Nominal 3.72', 'Hight 2.48', 'Very High 1.24', 'Extra High 0.00'],
        'FLEX': ['Very Low 5.07', 'Low 4.05', 'Nominal 3.04', 'Hight 2.03', 'Very High 1.01', 'Extra High 0.00'],
        'RESL': ['Very Low 7.07', 'Low 5.56', 'Nominal 4.24', 'Hight 2.83', 'Very High 1.41', 'Extra High 0.00'],
        'TEAM': ['Very Low 5.48', 'Low 4.38', 'Nominal 3.29', 'Hight 2.19', 'Very High 1.10', 'Extra High 0.00'],
        'PMAT': ['Very Low 7.80', 'Low 6.24', 'Nominal 4.68', 'Hight 3.12', 'Very High 1.56', 'Extra High 0.00'],
        'PERS': ['Extra low 2.12', 'Very Low 1.62', 'Low 1.26', 'Nominal 1.00', 'Hight 0.83', 'Very High 0.63', 'Extra High 0.50'],
        'PREX': ['Extra low 1.59', 'Very Low 1.33', 'Low 1.22', 'Nominal 1.00', 'Hight 0.87', 'Very High 0.74', 'Extra High 0.62'],
        'RCPX': ['Extra low 0.49', 'Very Low 0.60', 'Low 0.83', 'Nominal 1.00', 'Hight 1.33', 'Very High 1.91', 'Extra High 2.72'],
        'RUSE': ['Extra low n/a', 'Very Low n/a', 'Low 0.95', 'Nominal 1.00', 'Hight 1.07', 'Very High 1.15', 'Extra High 1.24'],
        'PDIF': ['Extra low n/a', 'Very Low n/a', 'Low 0.87', 'Nominal 1.00', 'Hight 1.29', 'Very High 1.81', 'Extra High 2.61'],
        'FCIL': ['Extra low 1.43', 'Very Low 1.30', 'Low 1.10', 'Nominal 1.00', 'Hight 0.87', 'Very High 0.73', 'Extra High 0.62'],
        'SCED': ['Extra low n/a', 'Very Low 1.43', 'Low 1.14', 'Nominal 1.00', 'Hight 1.00', 'Very High n/a', 'Extra High n/a'],

    }

    name_atributs_dict = {
        'PREC': 'Прецедентність, наявність досвіду аналогічних розробок',
        'FLEX': 'Гнучкість процесу розробки',
        'RESL': 'Архітектура і дозвіл ризиків',
        'TEAM': 'Спрацьованість команди',
        'PMAT': 'Зрілість процесів',
        'PERS': 'Кваліфікація персоналу',
        'PREX': 'Досвід персоналу',
        'RCPX': 'Складність і надійність продукту',
        'RUSE': 'Розробка для повторного використання',
        'PDIF': 'Складність платформи розробки',
        'FCIL': 'Обладнання',
        'SCED': 'Необхідний для виконання графік робіт',
    }

    list_data_inter = []
    lenght = len(dictt['PERS'])
    try:
        for key in dictt:
            a = request.GET.get(key)
            a = re.search(r'(\d+(?:[\.,]\d+)?$)|(n\/a)', a)
            try:
                list_data_inter.append(float(a.group(0)))
            except:
                list_data_inter.append(a.group(0))

        if count_rows:
            count_iter_list_data = 0
            SF = 0
            EAF = 1
            for a in list_data_inter:
                if count_iter_list_data <= 4:
                    if type(a) != str:
                        SF += a
                else:
                    if type(a) != str:
                        EAF = EAF * a
                count_iter_list_data += 1
            E = 0.91 + 0.01 * SF
            PM = EAF * 2.94 * int(count_rows)**E
            return render(request, 'cocomo2/preliminary_assessment.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': PM, 'len': lenght})
        else:
            return render(request, 'cocomo2/preliminary_assessment.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': 'Введіть к-ть рядків коду'})
    except:
        return render(request, 'cocomo2/preliminary_assessment.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': 'Введіть к-ть рядків коду'})

def detailed_assessment(request):

    count_rows = request.GET.get('rows')

    dictt = {
        'PREC': ['Very Low 6.20', 'Low 4.96', 'Nominal 3.72', 'Hight 2.48', 'Very High 1.24', 'Extra High 0.00'],
        'FLEX': ['Very Low 5.07', 'Low 4.05', 'Nominal 3.04', 'Hight 2.03', 'Very High 1.01', 'Extra High 0.00'],
        'RESL': ['Very Low 7.07', 'Low 5.56', 'Nominal 4.24', 'Hight 2.83', 'Very High 1.41', 'Extra High 0.00'],
        'TEAM': ['Very Low 5.48', 'Low 4.38', 'Nominal 3.29', 'Hight 2.19', 'Very High 1.10', 'Extra High 0.00'],
        'PMAT': ['Very Low 7.80', 'Low 6.24', 'Nominal 4.68', 'Hight 3.12', 'Very High 1.56', 'Extra High 0.00'],

        'ACAP': ['Very Low 1.42', 'Low 1.29', 'Nominal 1.00', 'Hight 0.85', 'Very High 0.71', 'Extra High n/a'],
        'AEXP': ['Very Low 1.22', 'Low 1.10', 'Nominal 1.00', 'Hight 0.88', 'Very High 0.81', 'Extra High n/a'],
        'PCAP': ['Very Low 1.34', 'Low 1.15', 'Nominal 1.00', 'Hight 0.88', 'Very High 0.76', 'Extra High n/a'],
        'PCON': ['Very Low 1.29', 'Low 1.12', 'Nominal 1.00', 'Hight 0.90', 'Very High 0.81', 'Extra High n/a'],
        'PEXP': ['Very Low 1.19', 'Low 1.09', 'Nominal 1.00', 'Hight 0.91', 'Very High 0.85', 'Extra High n/a'],
        'LTEX': ['Very Low 1.20', 'Low 1.09', 'Nominal 1.00', 'Hight 0.91', 'Very High 0.84', 'Extra High n/a'],
        'RELY': ['Very Low 0.84', 'Low 0.92', 'Nominal 1.00', 'Hight 1.10', 'Very High 1.26', 'Extra High n/a'],
        'DATA': ['Very Low n/a', 'Low 0.23', 'Nominal 1.00', 'Hight 1.14', 'Very High 1.28', 'Extra High n/a'],
        'CPLX': ['Very Low 0.73', 'Low 0.87', 'Nominal 1.00', 'Hight 1.17', 'Very High 1.34', 'Extra High 1.74'],
        'RUSE': ['Very Low n/a', 'Low 0.95', 'Nominal 1.00', 'Hight 1.07', 'Very High 1.15', 'Extra High 1.24'],
        'DOCU': ['Very Low 0.81', 'Low 0.91', 'Nominal 1.00', 'Hight 1.11', 'Very High 1.23', 'Extra High n/a'],
        'TIME': ['Very Low n/a', 'Low n/a', 'Nominal 1.00', 'Hight 1.11', 'Very High 1.29', 'Extra High 1.63'],
        'STOR': ['Very Low n/a', 'Low n/a', 'Nominal 1.00', 'Hight 1.05', 'Very High 1.17', 'Extra High 1.46'],
        'PVOL': ['Very Low n/a', 'Low 0.87', 'Nominal 1.00', 'Hight 1.15', 'Very High 1.30', 'Extra High n/a'],
        'TOOL': ['Very Low 1.17', 'Low 1.09', 'Nominal 1.00', 'Hight 0.90', 'Very High 0.78', 'Extra High n/a'],
        'SITE': ['Very Low 1.22', 'Low 1.09', 'Nominal 1.00', 'Hight 0.93', 'Very High 0.86', 'Extra High 0.80'],
        'SCED': ['Very Low 1.43', 'Low 1.14', 'Nominal 1.00', 'Hight 1.00', 'Very High 1.00', 'Extra High n/a'],




    }

    name_atributs_dict = {
        'PREC': 'Прецедентність, наявність досвіду аналогічних розробок',
        'FLEX': 'Гнучкість процесу розробки',
        'RESL': 'Архітектура і дозвіл ризиків',
        'TEAM': 'Спрацьованість команди',
        'PMAT': 'Зрілість процесів',

        'ACAP': 'Можливості аналітика',
        'AEXP': 'Досвід розробки додатків',
        'PCAP': 'Можливості програміста',
        'PCON': 'Тривалість роботи персоналу',
        'PEXP': 'Досвід роботи з платформою',
        'LTEX': 'Досвід використання мови програмування і інструментальних засобів',
        'RELY': 'Необхідна надійність програми',
        'DATA': 'Розмір бази даних',
        'CPLX': 'Складність програми',
        'RUSE': 'Необхідна можливість багаторазового використання',
        'DOCU': 'Відповідність документації потребам життєвого циклу',
        'TIME': 'Обмеження часу виконання',
        'STOR': 'Обмеження памяті',
        'PVOL': 'Змінність платформи',
        'TOOL': 'Використання інструментальних програмних засобів',
        'SITE': 'Багатоабонентська (віддалена) розробка',
        'SCED': 'Необхідний виконання графіка робіт',
    }

    list_data_inter = []
    lenght = len(dictt['ACAP'])
    try:
        for key in dictt:
            a = request.GET.get(key)
            a = re.search(r'(\d+(?:[\.,]\d+)?$)|(n\/a)', a)
            try:
                list_data_inter.append(float(a.group(0)))
            except:
                list_data_inter.append(a.group(0))

        if count_rows:
            count_iter_list_data = 0
            SF = 0
            EAF = 1
            for a in list_data_inter:
                if count_iter_list_data <= 4:
                    if type(a) != str:
                        SF += a
                else:
                    if type(a) != str:
                        EAF = EAF * a
                count_iter_list_data += 1
            E = 0.91 + 0.01 * SF
            PM = EAF * 2.45 * int(count_rows)**E
            return render(request, 'cocomo2/preliminary_assessment.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': PM, 'len': lenght})
        else:
            return render(request, 'cocomo2/preliminary_assessment.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': 'Введіть к-ть рядків коду'})
    except:
        return render(request, 'cocomo2/preliminary_assessment.html', {'dict': dictt, 'arr': list_data_inter, 'name_atribut': name_atributs_dict, 'PM': 'Введіть к-ть рядків коду'})




