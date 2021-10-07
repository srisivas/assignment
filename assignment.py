import datetime
from datetime import date
def solution(D):
 res={'Mon':0,
      'Tue':0,
      'Wed':0,
      'Thu':0,
      'Fri':0,
      'Sat':0,
      'Sun':0,
 }
 for date in D:
     year,month,day = date.split('-')
     day_name = datetime.date(int(year), int(month),int(day))
     day=day_name.strftime("%A")[:3]
     res[day]+=D[date]
     return(res)
D={'2020-01-01':4, '2020-01-02':4, '2020-01-03':6, '2020-01-04':8, '2020-01-05':2,
'2020-01-05':-6,'2020-01-06':2,'2020-01-07':-2}

print(solution(D))
