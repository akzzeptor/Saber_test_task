--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.3 в Ср фев 1 19:37:13 2023
--
-- Использованная кодировка текста: System
--
-- Результаты запроса:
-- WITH subq1 AS (
--   select 
--     issue_key, 
--     CASE when issue_key LIKE 'A%' THEN 'A' 
--         when issue_key LIKE 'B%' THEN 'B' 
--         when issue_key LIKE 'C%' THEN 'C' 
--         when issue_key LIKE 'D%' THEN 'D' 
--         else 'E' END as class, 
--     SUM(minutes_in_status) AS sum_minutes_in_status 
--   from 
--     history 
--   WHERE 
--     status = 'Open' 
--   GROUP BY 
--     issue_key
-- ) 
-- select 
--   class, 
--   round(
--     avg(sum_minutes_in_status / 60.00), 
--     2
--   ) AS avg_hour_in_status 
-- FROM 
--   subq1 
-- GROUP BY 
--   class
--
BEGIN TRANSACTION;
INSERT INTO history (class, avg_hour_in_status) VALUES ('A', 247.9);
INSERT INTO history (class, avg_hour_in_status) VALUES ('B', 281.51);
INSERT INTO history (class, avg_hour_in_status) VALUES ('C', 595.62);
INSERT INTO history (class, avg_hour_in_status) VALUES ('D', 842.02);
INSERT INTO history (class, avg_hour_in_status) VALUES ('E', 817.94);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
