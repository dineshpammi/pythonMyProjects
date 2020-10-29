'''
1.ACCEPT FROM THE USER & VALIDATE : DAY, MONTH, YEAR. USE CURRENT DEFAULTS.
2.DISPLAY: DAY+SUPERSCRIPT(st,nd,rd,th), MONTHNAME, YEAR
3.ACCEPT FROM THE USER: DAY OF THE WEEK
4.ACCEPT FROM THE USER: DAYS IN FUTURE
5.DISPLAY: FUTURE DAY+SUPERSCRIPT(st,nd,rd,th), MONTHNAME, YEAR, DAY OF THE WEEK
'''
# nodif=numberofdaysinfuture
# nodicm=numberofdaysincurrentmonth
# nodbcm=numberofdaysbeyondcurrentmonth

ss=[0,'st', 'nd', 'rd']+['th']*17+['st', 'nd', 'rd']+['th']*7+['st']
mn=[0,'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
md=[0,31,28,31,30,31,30,31,31,30,31,30,31]
#----------------------------------------------------------
y=input('year?') or '2018'          #default to 2018
y=int(y)
while 1:
    m=input('Month?') or '3'        #default to 3                      
    m=int(m)
    if (m >= 1 and m <= 12):
        if y%4 and m==2:
            md[m]-=1
        d=input('day ?') or '12'    #default to 12            
        d=int(d)
        if (d > 0 and d <= md[m]):
            break
    else: print('invalid Date !.. re-enter..')

print(d,ss[d],mn[m],y)
#----------------------------------------------------------
#wricw=weekdays remaninig in current week
dow=['0','M','TU','W','TH','FR','SA','SU']

w=int(input('enter correct DOW... monday=1 etc'))

wricw=7-w

#-----------------------------------------------------------
nodif=input('How many days after ?') or '60'    #default to 60
nodif=int(nodif)
fw=((nodif-wricw)%7)    #weekday calculation                
nodicm=md[m]-d          #<31-12=19>

if nodif <= nodicm:                 # ?? 60<=19    
    nodif=d+nodif
else :
    while 1:        
        nodbcm=nodif-nodicm if nodif > nodicm else 0          
                                    #<60-19=41>  <41-30=11>  <0>        

        if not nodbcm: break        #?? nodbcm==0.   ->zero days beyond current month
        m=(m+1 if m<12 else 1)      #<m=4>    <5>    ->month increases upto dec..then becomes 1
        y=(y+1 if m==1 else y)      #<y=2018> <2018> ->year increases from jan

        nodicm=md[m]                #<30>     <31>
        nodif=nodbcm                #<41>     <11>
        
        #print(nodif,' days in the future beyond %s / %d' %(mn[m-1],y))
        #input('continue...')
        
fd=nodif                            #11   ->final number of days in future
fm=m                                #5    ->final value of month
fy=y                                #2018 ->final value of year

print(fd,' / ',fm,' / ',fy)
print(fd,ss[fd],mn[fm],fy, ' on a ', dow[fw] )

#---------------------



