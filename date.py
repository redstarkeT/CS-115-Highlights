'''
Created on April 29, 2020
@author:   Timothy Stephens
Pledge:    I pledge my honor that I have abided by the Stevens Honors System. 

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
         '''Returns a new object with the same month, day, year
         as the calling object (self).'''
         dnew = Date(self.month, self.day, self.year)
         return dnew
    def equals(self, d2):
         '''Decides if self and d2 represent the same calendar date,
         whether or not they are the in the same place in memory.'''
         return self.year == d2.year and self.month == d2.month and \
             self.day == d2.day
    def tomorrow(self):
        '''Changes the current date to the next day.'''
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            DAYS_IN_MONTH[2] = 29
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.month == 12:
                self.month = 1
                self.day = 1
                self.year += 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1
    def yesterday(self):
        '''Changes the current date to the previous day.'''
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            DAYS_IN_MONTH[2] = 29
        if self.day == 1:
            if self.month == 1:
                self.month = 12
                self.day = 31
                self.year -= 1
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
    def addNDays(self,num):
        '''Adds a certain amount of days to the current date.'''
        for x in range(num):
            self.tomorrow()
            print(self)
    def subNDays(self,num):
        '''Subtracts a certain amount of days to the current date.'''
        for x in range(num):
            self.yesterday()
            print(self)
            
    def isBefore(self, d2):
        '''Checks if date is before d2 or not.'''
        if self == d2:
            return False
        if self.year > d2.year:
            return False
        if self.year < d2.year:
            return True
        else:
            if self.month > d2.month:
                return False
            if self.month < d2.month:
                return True
            else:
                if self.day > d2.day:
                    return False
                if self.day < d2.day:
                    return True
                else:
                    return False
                
    def isAfter(self, d2):
        '''Checks if date is after d2 or not.'''
        if self == d2:
            return False
        if self.year > d2.year:
            return True
        if self.year < d2.year:
            return False
        else:
            if self.month > d2.month:
                return True
            if self.month < d2.month:
                return False
            else:
                if self.day > d2.day:
                    return True
                if self.day < d2.day:
                    return False
                else:
                    return False
            
    def diff(self,d2):
        """Returns difference between self and d2 in days"""
        Goku = 0
        selfC = self.copy()
        if selfC == d2:
            return Goku
        if selfC.isBefore(d2):
            while selfC.isBefore(d2):
                selfC.tomorrow()
                Goku -= 1
        else:
            while selfC.isAfter(d2):
                selfC.yesterday()
                Goku += 1
        return Goku
        
    




    
    def dow(self):
        """ Returns the day of the week of the date given """
        Trunks = Date(4, 2, 2020)
        Vegeta = self.diff(Trunks)
        if Vegeta % 7 == 0:
            return "Thursday"
        if Vegeta % 7 == 1:
            return "Friday"
        if Vegeta % 7 == 2:
            return "Saturday"
        if Vegeta % 7 == 3:
            return "Sunday"
        if Vegeta % 7 == 4:
            return "Monday"
        if Vegeta % 7 == 5:
            return "Teusday"
        if Vegeta % 7 == 6:
            return "Wednesday"

            
        
