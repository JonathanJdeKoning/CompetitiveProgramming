class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = defaultdict(int)
        for log in logs:
            for year in range(log[0],log[1]):
                years[year] += 1
        mx = max(years.values())


        for year in sorted(years.keys()):
            if years[year] == mx:
                return year
