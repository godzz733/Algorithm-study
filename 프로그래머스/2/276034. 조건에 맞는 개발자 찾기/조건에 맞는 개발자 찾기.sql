SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
WHERE D.SKILL_CODE | (SELECT S.CODE FROM SKILLCODES AS S WHERE
                     S.NAME = 'C#') = D.SKILL_CODE
                     OR D.SKILL_CODE | (SELECT S.CODE FROM SKILLCODES AS S WHERE
                     S.NAME = 'Python') = D.SKILL_CODE
ORDER BY D.ID;
                     