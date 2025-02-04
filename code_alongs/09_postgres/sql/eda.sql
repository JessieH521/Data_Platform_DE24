-- SELECT
--     utbildningsnamn,
--     utbildningsområde,
--     "yh-poäng",
--     beslut,
--     "utbildningsanordnare administrativ enhet",
--     kommun 
-- INTO 
--     it_educations          -- 建了一个新表：it_educations 
-- FROM
--     myh_2024
-- WHERE
--     beslut = 'Beviljad'
--     AND utbildningsområde = 'Data/IT';

SELECT
    utbildningsnamn,
    utbildningsområde,
    "yh-poäng",
    beslut,
    "utbildningsanordnare administrativ enhet",
    kommun
FROM
    myh_2024
WHERE
    beslut = 'Beviljad'
    AND utbildningsområde = 'Data/IT';

SELECT
    COUNT(*) AS total_applied
FROM
    it_educations;

WITH
    approved AS (
        SELECT
            COUNT(*) AS count
        FROM
            it_educations
        WHERE
            beslut = 'Beviljad'
    ),
    total AS (
        SELECT
            COUNT(*) AS count
        FROM
            it_educations
    )
SELECT
    approved.count,
    total.count,
    CAST(approved.count AS NUMERIC) / total.count  as proportion_approved 
FROM
    approved,
    total














