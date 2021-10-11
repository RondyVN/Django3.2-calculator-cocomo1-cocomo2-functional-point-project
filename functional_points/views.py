from django.shortcuts import render

def functional_points(request):

    dict_wigthts = {
        'EI': [3, 4, 6],
        'EO': [4, 5, 7],
        'EQ': [3, 4, 6],
        'ILF': [7, 10, 15],
        'EIF': [5, 7, 10],
    }

    dict_inputs = {
        'EI': ['EI', 'EI', 'EI'],
        'EO': ['EO', 'EO', 'EO'],
        'EQ': ['EQ', 'EQ', 'EQ'],
        'ILF': ['ILF', 'ILF', 'ILF'],
        'EIF': ['EIF', 'EIF', 'EIF'],
    }

    dict_name = {
        'EI': 'Зовнішні вводи',
        'EO': 'Зовнішні виводи',
        'EQ': 'Зовнішні запити',
        'ILF': 'Локальні внутрішні логічні файли',
        'EIF': 'Зовнішні інтерфейсні файли',
    }

    list = []

    for key in dict_wigthts:
        num = request.GET.getlist(key)
        multiply = 0

        for inex, v in enumerate(num):
            try:
                multiply += int(v) * dict_wigthts[key][inex]
            except:
                multiply += 0

        list.append(multiply)

    return render(request, 'functional_points/functional_points.html', {'num': list, 'dict_input': dict_inputs, 'name': dict_name})