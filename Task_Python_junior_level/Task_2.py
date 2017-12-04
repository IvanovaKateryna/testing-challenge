# -*- coding: utf-8 -*-
import re
import datetime


in_file = "IN.txt"
out_file = "OUT.txt"
data_file = []


days = {
    '01': 'перше',
    '02': 'друге ',
    '03': 'третє',
    '04': 'четверте',
    '05': 'п\'яте',
    '06': 'шосте',
    '07': 'сьоме',
    '08': 'восьме',
    '09': 'дев\'яте',
    '10': 'десяте',
    '11': 'одинадцяте',
    '12': 'дванадцяте',
    '13': 'тринадцяте',
    '14': 'чотирнадцяте',
    '15': 'п\'ятнадцяте',
    '16': 'шістнадцяте',
    '17': 'сімнадцяте',
    '18': 'вісімнадцяте',
    '19': 'дев\'ятнадцяте',
    '20': 'двадцяте',
    '21': 'двадцять перше',
    '22': 'двадцять друге',
    '23': 'двадцять третє',
    '24': 'двадцять четверте',
    '25': 'двадцять п\'яте',
    '26': 'двадцять шосте',
    '27': 'двадцять сьоме',
    '28': 'двадцять восьме',
    '29': 'двадцять дев\'яте',
    '30': 'тридцяте',
    '31': 'тридцять перше'
}

days_form = {
    '01': 'першого',
    '02': 'другого ',
    '03': 'третього',
    '04': 'четвертого',
    '05': 'п\'ятого',
    '06': 'шостого',
    '07': 'сьомого',
    '08': 'восьмого',
    '09': 'дев\'ятого',
    '10': 'десятого',
    '11': 'одинадцятого',
    '12': 'дванадцятого',
    '13': 'тринадцятого',
    '14': 'чотирнадцятого',
    '15': 'п\'ятнадцятого',
    '16': 'шістнадцятого',
    '17': 'сімнадцятого',
    '18': 'вісімнадцятого',
    '19': 'дев\'ятнадцятого',
    '20': 'двадцятого',
    '21': 'двадцять першого',
    '22': 'двадцять другого',
    '23': 'двадцять третього',
    '24': 'двадцять четвертого',
    '25': 'двадцять п\'ятого',
    '26': 'двадцять шостого',
    '27': 'двадцять сьомого',
    '28': 'двадцять восьмого',
    '29': 'двадцять дев\'ятого',
    '30': 'тридцятого',
    '31': 'тридцять першого'
}

months = {
        '01': 'січня',
        '02': 'лютого',
        '03': 'березня',
        '04': 'квітня',
        '05': 'травня',
        '06': 'червня',
        '07': 'липня',
        '08': 'серпня',
        '09': 'вересня',
        '10': 'жовтня',
        '11': 'листопада',
        '12': 'грудня'
}

years = {
    '2012': 'дві тисячі дванадцятого року',
    '12': 'дві тисячі дванадцятого року',
    '2014': 'дві тисячі чотирнадцятого року',
    '14':'дві тисячі чотирнадцятого року',
    '2016':'дві тисячі шістнадцятого року',
    '16':'дві тисячі шістнадцятого року'
}


date_format = ['%d-%m-%Y', '%d.%m.%Y', '%d %m %Y', '%d.%m.%y', '%d %m %y']


 # Get the list from file
with open(in_file, 'r') as read_file:
    for line in read_file:
        data_file.append(line.strip('\n\r'))


for i in xrange(len(data_file)):
            date_line = re.findall('\d{2}-\d{2}-\d{4}|\d{2}.\d{2}.\d{4}|'
                                   '\d{2}.\d{2}.\d{2}|\d{2} \d{2} \d{2}|'
                                   '\d{2} \d{2} \d{4}', str(data_file))

print(date_line)
result_dates = []
for item in xrange(len(date_line)):
    if '.' in date_line[item]:
        date_line[item] = date_line[item].split('.')
    elif '-' in date_line[item]:
        date_line[item] = date_line[item].split('-')
    else:
        date_line[item] = date_line[item].split(' ')
    day = date_line[item][0]
    month = date_line[item][1]
    year = date_line[item][2]

    for key in days.keys():
        if key == day:
            day = days[key] + " "
        else:
            pass

    for key in months.keys():
        if key == month:
            month = months[key] + " "
        else:
            pass

    for key in years.keys():
        if key == year:
            year = years[key] + " "
        else:
            pass
    date_line[item] = day+month+year
    print(date_line[item])
