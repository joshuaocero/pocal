class Pocal:
    def __init__(self, r1, d1, r2, d2, r3, d3, k):
        self.r1 = r1
        self.d1 = d1
        self.r2 = r2
        self.d2 = d2
        self.r3 = r3
        self.d3 = d3
        self.k = k

    @staticmethod
    def get_daily_rate(cnt, d, r):
        return r if cnt >= d else 0

    def get_days_of_power(self):
        balance, days_of_power, cnt = self.k, 0, 0

        while True:
            cnt += 1
            total_daily_rate = 0

            # Calculate the total daily rate for the 3 loan plans
            total_daily_rate += self.get_daily_rate(cnt, self.d1, self.r1)
            total_daily_rate += self.get_daily_rate(cnt, self.d2, self.r2)
            total_daily_rate += self.get_daily_rate(cnt, self.d3, self.r3)

            if total_daily_rate > balance:
                return days_of_power

            if total_daily_rate > 0:
                balance -= total_daily_rate
                days_of_power += 1
