from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for index, price in enumerate(prices):
            start_index = index + 1
            for price_next_day in prices[start_index:]:
                profit = price_next_day - price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


def example_one(solution):
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    actual = solution.maxProfit(prices)
    assert actual == expected


def example_two(solution):
    prices = [7,6,4,3,1]
    expected = 0
    actual = solution.maxProfit(prices)
    assert actual == expected


def example_three(solution):
    prices = [1, 2]
    expected = 1
    actual = solution.maxProfit(prices)
    assert actual == expected



if __name__ == '__main__':
    solution = Solution()
    example_one(solution)
    example_two(solution)
    example_three(solution)