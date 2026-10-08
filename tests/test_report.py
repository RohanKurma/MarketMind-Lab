import unittest
from marketmind_report import compute_summary


class TestMarketMindReport(unittest.TestCase):
    def test_price_change_and_trade_count(self):
        prices = [
            {"阶段结束后股票A价格": 100, "阶段结束后股票B价格": 80},
            {"阶段结束后股票A价格": 110, "阶段结束后股票B价格": 60},
        ]
        trades = [{"交易数量": 3}, {"交易数量": 4}]
        result = {row["metric"]: row["value"] for row in compute_summary(prices, trades)}
        self.assertEqual(result["price_A_change_pct"], 10.0)
        self.assertEqual(result["price_B_change_pct"], -25.0)
        self.assertEqual(result["executed_trade_count"], 2)
        self.assertEqual(result["executed_trade_quantity"], 7)

    def test_rejects_empty_prices(self):
        with self.assertRaises(ValueError):
            compute_summary([], [])


if __name__ == "__main__":
    unittest.main()
