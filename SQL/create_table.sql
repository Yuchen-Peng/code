create multiset table my_table
as
(select
a.*,
case
    when country like '%America%' then 'US'
    when country like '%China%' then 'CN' 
    else 'OTHER'
end as country
from table_1 a
where continent in ('Asia','America','Europe')
and national_day between '1700-01-01' and '2000-12-31'
and country_name is not null)
with data
primary index (country_name)

collect statistics my_table index(country_name);
