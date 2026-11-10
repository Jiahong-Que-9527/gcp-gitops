-- [房玄龄·2026-11-10] Replace YOUR_PROJECT in an ignored local copy.
-- Fixture dates are intentional; update the bounded interval for new data.
SELECT DATE(event_time) AS event_date, airport,
       COUNT(*) AS event_count, AVG(delay_minutes) AS mean_delay_minutes
FROM `YOUR_PROJECT.gcp_gitops_dev.events`
WHERE event_time >= TIMESTAMP('2026-11-10T00:00:00Z')
  AND event_time < TIMESTAMP('2026-11-11T00:00:00Z')
  AND synthetic = TRUE
GROUP BY event_date, airport;
