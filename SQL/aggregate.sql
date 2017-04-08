
select
state,
count(*) as people_each_state
from my_table

group by state;
/* the number of people of each state is summerized; also can be used to check the frequency of each state/how many sts are there*/

select
county,
sum(house_price) as total_value,
count(distinct agent_id) as num_agent,
avg(zeroifnull(house_price)) as avg_price
from my_table

group by county;
