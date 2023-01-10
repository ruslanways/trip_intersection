def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    calendar =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_calendar = [0]
    for i in calendar[1:-1]:
        days_calendar.append(days_calendar[-1]+i)
    def to_days(coord):
        return days_calendar[int(coord[:2])-1]+int(coord[3:])
    arriveA = to_days(arriveAlice)
    leaveA = to_days(leaveAlice)
    arriveB = to_days(arriveBob)
    leaveB = to_days(leaveBob)
    if arriveB > leaveA or arriveA > leaveB:
        return 0
    else:
        return (365-max(arriveA,arriveB)+1)-(365-min(leaveA, leaveB))
