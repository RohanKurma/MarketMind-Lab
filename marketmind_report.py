"""Create a repeatable CSV summary from a simulated market run.

No API keys required. Uses the stock and trade spreadsheets produced by main.py.
"""
from __future__ import annotations
import argparse
import csv
from pathlib import Path


def compute_summary(stocks, trades):
    """Summarize prices and trade volume from DataFrame-compatible rows."""
    if not stocks:
        raise ValueError("No stock price records found")
    a_prices = [float(r["阶段结束后股票A价格"]) for r in stocks]
    b_prices = [float(r["阶段结束后股票B价格"]) for r in stocks]
    def change(values):
        return round((values[-1] / values[0] - 1) * 100, 2) if values[0] else None
    return [
        {"metric": "price_A_first", "value": a_prices[0]},
        {"metric": "price_A_last", "value": a_prices[-1]},
        {"metric": "price_A_change_pct", "value": change(a_prices)},
        {"metric": "price_B_first", "value": b_prices[0]},
        {"metric": "price_B_last", "value": b_prices[-1]},
        {"metric": "price_B_change_pct", "value": change(b_prices)},
        {"metric": "executed_trade_count", "value": len(trades)},
        {"metric": "executed_trade_quantity", "value": sum(float(r["交易数量"]) for r in trades)},
    ]


def main():
    parser = argparse.ArgumentParser(description="Summarize a MarketMind Lab run")
    parser.add_argument("--results", type=Path, default=Path("res"))
    parser.add_argument("--output", type=Path, default=Path("res/summary.csv"))
    args = parser.parse_args()
    import pandas as pd
    stock_path = args.results / "stocks.xlsx"
    if not stock_path.exists():
        parser.error(f"Missing {stock_path}. Run main.py first.")
    trade_path = args.results / "trades.xlsx"
    stocks = pd.read_excel(stock_path).to_dict("records")
    trades = pd.read_excel(trade_path).to_dict("records") if trade_path.exists() else []
    rows = compute_summary(stocks, trades)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["metric", "value"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {args.output}")
    for row in rows:
        print(f"{row['metric']}: {row['value']}")


if __name__ == "__main__":
    main()
