from datetime import datetime

def days_diff(date1, date2):
    spec_YMD = "{:0>4}-{:0>2}-{:0>2}"
    d1 = spec_YMD.format(date1[0], date1[1], date1[2])
    d2 = spec_YMD.format(date2[0], date2[1], date2[2])

    dt1 = datetime.strptime(d1, "%Y-%m-%d")
    dt2 = datetime.strptime(d2, "%Y-%m-%d")
    
    return abs((dt1 - dt2).days)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

