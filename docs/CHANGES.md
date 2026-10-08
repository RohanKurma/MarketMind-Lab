# Adaptation notes

This repository contains a derivative of StockAgent with the following changes:

- Rebranded as MarketMind Lab; replaced user-facing README with installation, limitations, and attribution guidance.
- Added independently testable trade and price analytics (`marketmind_report.py`).
- Added report tests and CLI options for agent count, day count and seed.
- Replaced the empty embedded API key in `secretary.py` with environment-based credentials and added Gemini support there.
- Added clean-checkout output directory creation and non-sensitive log paths.
- Added missing explicitly imported runtime dependencies and Git hygiene files.

Original simulation algorithms, agent prompts and diagrams remain based on the upstream code.
