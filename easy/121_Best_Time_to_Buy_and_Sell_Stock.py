from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # минимальная цена, встреченная до текущего дня
        max_profit = 0             # лучшая прибыль

        for price in prices:
            if price < min_price:
                min_price = price                  # нашли цену дешевле — обновляем
            elif price - min_price > max_profit:
                max_profit = price - min_price     # продаём сегодня, если выгодно

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