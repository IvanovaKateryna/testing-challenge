# -*- coding: utf-8 -*-
#   By Python 2.7

import re
import datetime


in_file = "IN.txt"
out_file = "OUT.txt"
date_file = []
result_dates = []
date_form = []

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
    '2011': 'дві тисячі одинадцятого року',
    '11': 'дві тисячі одинадцятого року',
    '2012': 'дві тисячі дванадцятого року',
    '12': 'дві тисячі дванадцятого року',
    '2013': 'дві тисячі тринадцятого року',
    '13': 'дві тисячі тринадцятого року',
    '2014': 'дві тисячі чотирнадцятого року',
    '14': 'дві тисячі чотирнадцятого року',
    '2015': 'дві тисячі п\'ятнадцятого року',
    '15': 'дві тисячі п\'ятнадцятого року',
    '2016': 'дві тисячі шістнадцятого року',
    '16': 'дві тисячі шістнадцятого року',
    '2017': 'дві тисячі сімнадцятого року',
    '17': 'дві тисячі сімнадцятого року',
    '2018': 'дві тисячі вісімнадцятого року',
    '18': 'дві тисячі вісімнадцятого року'
}


#  Get the list from file
#  date_file - lines with dates, not in sentence of text
#  date_form - lines with dates in sentences.
with open(in_file, 'r') as read_file:
    for line in read_file:
        if len(re.findall('\d{2,4} \D', line)) == 0 \
                and len(re.findall('\D \d{2,4}', line)) == 0:
                date_file.append(line.strip('\n\r'))
        else:
            date_form.append(line.strip('\n\r'))


def findall_date(f_date):
    """
    The function find all dates
    :param f_date: the list of lines from file
    :return: find_date - the list of dates with format %d-%m-%Y, %d.%m.%Y, %d %m %Y, %d.%m.%y, %d %m %y
    """
    for i in xrange(len(f_date)):
        find_date = re.findall('\d{2}-\d{2}-\d{4}|\d{2}.\d{2}.\d{4}|'
                               '\d{2}.\d{2}.\d{2}|\d{2} \d{2} \d{2}|'
                               '\d{2} \d{2} \d{4}', str(f_date))
    return find_date


def split_date(dmy):
    """
    The function split dates for 3 elements(dmy - day, month, year)
    :param dmy: list of dates(find_date)
    :return: the list of dmy in list of dates
    """
    for i in xrange(len(dmy)):
        if '.' in dmy[i]:
            dmy[i] = dmy[i].split('.')
        elif '-' in dmy[i]:
            dmy[i] = dmy[i].split('-')
        else:
            dmy[i] = dmy[i].split(' ')
    return dmy


def get_day(dmy):
    """
    The function get the day from number to ukrainian word(Nominative case)
    :param dmy: the list of dmy
    :return: day in dmy(ua) - 0 element
    """
    for i in xrange(len(dmy)):
        day = dmy[i][0]
        for key in days.keys():
            if key == day:
                day = days[key] + " "
            else:
                pass
        dmy[i][0] = day
    return dmy


def get_day_form(dmy):
    """
    The function get the day from number to ukrainian word(Genitive)
    :param dmy: the list of dmy
    :return: day in dmy(ua)
    """
    for i in xrange(len(dmy)):
        day = dmy[i][0]
        for key in days.keys():
            if key == day:
                day = days_form[key] + " "
            else:
                pass
        dmy[i][0] = day
    return dmy


def get_month(dmy):
    """
    The function get the month from number to ukrainian word(Genitive)
    :param dmy: the list of dmy
    :return: month in dmy(ua) - 1 element
    """
    for i in xrange(len(dmy)):
        month = dmy[i][1]
        for key in months.keys():
            if key == month:
                month = months[key] + " "
            else:
                pass
        dmy[i][1] = month
    return dmy


def get_year(dmy):
    """
    The function get the year from number to ukrainian word(Genitive)
    :param dmy: the list of dmy
    :return: year in dmy(ua) - 2 element
    """
    for i in xrange(len(dmy)):
        year = dmy[i][2]
        for key in years.keys():
            if key == year:
                year = years[key] + " "
            else:
                pass
            dmy[i][2] = year
    return dmy


def get_result_date(list_date):
    """
    The function get the string = result of ua-dmy (day month year)
    :param list_date: the list of dmy
    :return: result string of dmy
    """
    result = ""
    for item in xrange(len(list_date)):
            result += ' '.join(list_date[item]) + "; "
    return result


date_line = findall_date(date_file)
date_line = split_date(date_line)
date_line = get_day(date_line)
date_line = get_month(date_line)
date_line = get_year(date_line)
result_date = get_result_date(date_line)

date_line_form = findall_date(date_form)
date_line_form = split_date(date_line_form)
date_line_form = get_day_form(date_line_form)
date_line_form = get_month(date_line_form)
date_line_form = get_year(date_line_form)
result_form_date = get_result_date(date_line_form)

# Write to file out_file the full result of dates
with open(out_file, 'w') as save_file:
    line = save_file.writelines(result_date + result_form_date)
