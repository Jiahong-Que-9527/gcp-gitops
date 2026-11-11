-- [房玄龄·2026-11-11] Count input rows, including duplicates.
SELECT currency, COUNT(*) AS row_count
FROM fx_rates
GROUP BY currency
ORDER BY currency;
