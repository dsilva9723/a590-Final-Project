WITH 
  r1 AS (select country, 
                dense_rank() over (order by count(c.comment_id) desc) AS 2020_rank
          from users u left join comments c 
            on extract(year from c.posted_at)=2020 and c.user_id=u.user_id
          group by country),
  r2 AS (select country, 
                dense_rank() over (order by count(c.comment_id) desc) AS 2021_rank
          from users u left join comments c 
            on extract(year from c.posted_at)=2021 and c.user_id=u.user_id
          group by country)     
SELECT  r1.country, 2020_rank, 2021_rank,
        (2020_rank - 2021_rank) AS rise
FROM    r1 JOIN r2 ON r1.country = r2.country
WHERE   2021_rank < 2020_rank
;  

select   a.faa, a.name,
         100*count(f.id)/(select count(*) from flights where duration>180) AS share_flight_gt180
from     airports a LEFT JOIN flights f 
          ON f.duration > 180 and a.faa = f.origin
group by a.faa
order by share_flight_gt180 desc
;
