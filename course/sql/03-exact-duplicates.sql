-- [房玄龄·2026-11-11] Collapse rows with three identical field values.
SELECT DISTINCT currency, observation_date, fx_rate
FROM fx_rates
ORDER BY currency, observation_date;
