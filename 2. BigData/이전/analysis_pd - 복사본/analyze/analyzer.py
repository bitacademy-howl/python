import json

import math
import pandas as pd
import scipy.stats as ss
# import numpy as np
import matplotlib.pyplot as plt

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
        # print(json_data)

######################################################################################################################
    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    print(tourspotvisitor_table)

    # 일자별 그룹핑 하여 방문객의 총합을 구한다
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())
#######################################################################################################################

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['date', 'country_name', 'visit_count'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')

        merge_table = pd.merge(temp_tourspotvisitor_table, foreignvisitor_table, left_index=True, right_index=True)
        print(merge_table)

        # 데이터 전처리 - 시각화를 위한
        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        # r = ss.correlation_coefficient(x, y)
        r = ss.pearsonr(x, y)
        # 넘파이 코릴레이션을 제공하지만 자세한 사용법은 알아보고 할 것
        # r = np.corrcoef(x, y)[0]

        data = {'x': x, 'y' : y, 'country_name': country_name, 'r' : r}
        results.append(data)

        merge_table['visit_count'].plot(kind='bar')
        plt.show()

    return results



def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    # 테이블에 상수로 초기화된 열을 삽입하기 위한 변수
    lenOfTourspotvisitor_table = len(json_data)

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    print(tourspotvisitor_table)

    # 관광지별 그룹핑 하여 방문객의 총합을 구한다
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('tourist_spot')['count_foreigner'].sum())
    print('temp table : ', temp_tourspotvisitor_table)

    results = []
    results.append(addcol(resultfiles))
    print(results)

    for i in range(0, lenOfTourspotvisitor_table+1):


    return

def addcol(resultfiles):
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
        country = filename['country_name']

        sumation = 0
        for i in json_data:
            sumation += i['visit_count']

        yield sumation


def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError as e:
        r = 0.0

    return r
