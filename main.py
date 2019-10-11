def get_daily_rate(cnt, d, r):
    return r if cnt >= d else 0


def get_days_of_power(r1, d1, r2, d2, r3, d3, k):
    balance, days_of_power, cnt = k, 0, 0

    while True:
        cnt += 1
        total_daily_rate = 0

        # Calculate the total daily rate for the 3 loan plans
        total_daily_rate += get_daily_rate(cnt, d1, r1)
        total_daily_rate += get_daily_rate(cnt, d2, r2)
        total_daily_rate += get_daily_rate(cnt, d3, r3)

        if total_daily_rate > balance:
            return days_of_power

        if total_daily_rate > 0:
            balance -= total_daily_rate
            days_of_power += 1


print(get_days_of_power(r1=1000, d1=3, r2=500, d2=10, r3=1500, d3=7, k=21000))
