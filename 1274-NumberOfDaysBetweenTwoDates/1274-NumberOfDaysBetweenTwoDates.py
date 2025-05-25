# Last updated: 5/25/2025, 9:29:34 PM
class Solution(object):
    def is_leap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        # case 1: both within a month day1 - day2
        # case 2: diff months 
        # case 3: diff years: case 2 + 365 * year diff
        mydict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                  7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        if date1[5:7] == date2[5:7] and date1[0:4] == date2[0:4]:
            return abs(int(date1[8:10]) - int(date2[8:10]))

        elif date1[5:7] != date2[5:7] and date1[0:4] == date2[0:4]:
            sum = 0
            for i in range(int(date1[5:7]), int(date2[5:7])):
                sum += mydict[i]
            return abs(int(date1[8:10]) - int(date2[8:10])) + sum

        else:
            sum = 0
            sumyear = 0

            if date1 > date2:
                date1, date2 = date2, date1

            y1, m1, d1 = int(date1[0:4]), int(date1[5:7]), int(date1[8:10])
            y2, m2, d2 = int(date2[0:4]), int(date2[5:7]), int(date2[8:10])

            # Remaining days in date1's month
            sum += mydict[m1] - d1
            if m1 == 2 and self.is_leap(y1):
                sum += 1

            # From next month to December in year y1
            for i in range(m1 + 1, 13):
                sum += mydict[i]
                if i == 2 and self.is_leap(y1):
                    sum += 1

            # Full years in between
            for j in range(y1 + 1, y2):
                sumyear += 366 if self.is_leap(j) else 365

            # From January to month before date2 in y2
            for i in range(1, m2):
                sum += mydict[i]
                if i == 2 and self.is_leap(y2):
                    sum += 1

            # Days in final month
            sum += d2

            return sum + sumyear
            
