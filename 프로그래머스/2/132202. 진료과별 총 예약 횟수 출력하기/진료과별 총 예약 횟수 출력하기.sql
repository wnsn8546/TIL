-- 코드를 입력하세요
# SELECT MCDP_CD AS 진료과코드, COUNT(*) AS 5월예약건수
# FROM APPOINTMENT 
# WHERE APNT_YMD LIKE '2022-05%'
# GROUP BY MCDP_CD 
# ORDER BY COUNT(*) AND 진료과코드;
select MCDP_CD as '진료과코드', count(*) as '5월예약건수' from APPOINTMENT

where month(APNT_YMD) = '05' and year(APNT_YMD) = '2022'
group by MCDP_CD
order by count(MCDP_CD), MCDP_CD;

