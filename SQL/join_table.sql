create multiset table UD206.lzq857_my_join_table as 
(
select a.*,
b.*
from table1 as a
join table2 as b
on a.acct_id = b.acct_id
)
with data
primary index (acct_id)
