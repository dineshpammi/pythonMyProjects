'''
1.ACCEPT FROM THE USER: DAY, MONTH, YEAR.
2.DISPLAY: DAY+SUPERSCRIPT(st,nd,rd,th), MONTHNAME, YEAR
ss=superscript
mn=month names
md=days per month
'''

#define a set of superscripts for each day ... 1=st;2=nd;17=th ... etc...
ss=[0,'st', 'nd', 'rd']+['th']*17+['st', 'nd', 'rd']+['th']*7+['st']

#define the namesofeach month according to the month number...
mn=[0,'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

#define the number of days of each month according to the month number
md=[0,31,28,31,30,31,30,31,31,30,31,30,31]

#define messages
d=m=y=0
invalidDayMsg=invalidMonthMsg=''
#do the process

# run an infinite loop to make the user enter only valid data
while 1:
    d=input('day ?') or '20'      #ask the user for a day
    m=input('Month?') or '7'      #ask the user for a month
    d=int(d)
    m=int(m)
    invalidMonthMsg='invalid Month... enter a Month number between 1 to 12'
    if (m > 0 and m <= 12):         #validate month ... >0 and <=12
        if (d > 0 and d <= md[(m)]):
            break                   #if the day is valid for the entered month then exit the loop
        else:
            invalidDayMsg='invalid day... enter a day > 0 and < {}'.format(md[(m)])
            print(invalidDayMsg)    #otherwise we reloop
    else:
        print(invalidMonthMsg)      #otherwise we reloop

    
y=input('year?') or '2018'       #ask the user for a year
y=int(y)
'''print the entered day plus the superscript for that day,
monthname of the month
and year...'''

print(d,ss[(d)],mn[(m)],y)          

