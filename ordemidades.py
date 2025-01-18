from datetime import date
from random import randint
I1 = randint(0, 10)
I2 = randint(0, 10)
I3 = randint(0, 10)
I4 = randint(0, 10)
I5 = randint(0, 10)
if I1 == 0:
    I1 = 2017
elif I1 == 1:
    I1 = 2016
elif I1 == 2:
    I1 = 2015
elif I1 == 3:
    I1 = 2014
elif I1 == 4:
    I1 = 2013
elif I1 == 5:
    I1 = 2012
elif I1 == 6:
    I1 = 2011
elif I1 == 7:
    I1 = 2010
elif I1 == 8:
    I1 = 2009
elif I1 == 9:
    I1 = 2008
elif I1 == 10:
    I1 = 2007

if I2 == 0:
    I2 = 2017
elif I2 == 1:
    I2 = 2016
elif I2 == 2:
    I2 = 2015
elif I2 == 3:
    I2 = 2014
elif I2 == 4:
    I2 = 2013
elif I2 == 5:
    I2 = 2012
elif I2 == 6:
    I2 = 2011
elif I2 == 7:
    I2 = 2010
elif I2 == 8:
    I2 = 2009
elif I2 == 9:
    I2 = 2008
elif I2 == 10:
    I2 = 2007

if I3 == 0:
    I3 = 2017
elif I3 == 1:
    I3 = 2016
elif I3 == 2:
    I3 = 2015
elif I3 == 3:
    I3 = 2014
elif I3 == 4:
    I3 = 2013
elif I3 == 5:
    I3 = 2012
elif I3 == 6:
    I3 = 2011
elif I3 == 7:
    I3 = 2010
elif I3 == 8:
    I3 = 2009
elif I3 == 9:
    I3 = 2008
elif I3 == 10:
    I3 = 2007
if I4 == 0:
    I4 = 2017
elif I4 == 1:
    I4 = 2016
elif I4 == 2:
    I4 = 2015
elif I4 == 3:
    I4 = 2014
elif I4 == 4:
    I4 = 2013
elif I4 == 5:
    I4 = 2012
elif I4 == 6:
    I4 = 2011
elif I4 == 7:
    I4 = 2010
elif I4 == 8:
    I4 = 2009
elif I4 == 9:
    I4 = 2008
elif I4 == 10:
    I4 = 2007
if I5 == 0:
    I5 = 2017
elif I5 == 1:
    I5 = 2016
elif I5 == 2:
    I5 = 2015
elif I5 == 3:
    I5 = 2014
elif I5 == 4:
    I5 = 2013
elif I5 == 5:
    I5 = 2012
elif I5 == 6:
    I5 = 2011
elif I5 == 7:
    I5 = 2010
elif I5 == 8:
    I5 = 2009
elif I5 == 9:
    I5 = 2008
elif I5 == 10:
    I5 = 2007
print(f'Claudio nasceu em {I1}')
print(f'Miguel nasceu em {I2}')
print(f'José nasceu em {I3}')
print(f'Mario nasceu em {I4}')
print(f'Luigi nasceu em {I5}')


I1a = date.today().year - I1
if I1a <= 9:
    print("Claudio é Benjamin!")
elif I1a <= 14:
    print("Claudio é Infantil")
elif I1a <= 19:
    print("Claudio é Junior")
elif I1a <= 25:
    print("Claudio é Sénior")
else:
    print("Claudio é Master")
