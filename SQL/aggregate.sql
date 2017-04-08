select
channel,
count(*) as number_each_channel
from UDcontainer.my_table

group by channel
/* the number of account of each channel is summerized; also can be used to check the frequency of each channel/how many channels are there*/

select
segment,
sum(balance) as total_balance,
count(distinct account_id) as num_account,
avg(zeroifnull(balance)) as avg_balance
from UDcontainer.my_table

group by segment;
/* the total balance of each segment is summed
