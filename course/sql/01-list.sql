-- [房玄龄·2026-11-11] Select fields and order the result.
SELECT currency, observation_date, fx_rate
FROM fx_rates
ORDER BY currency, observation_date;
