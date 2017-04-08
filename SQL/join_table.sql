create multiset table join_table as 
(
select a.*,
b.*
from table1 as a
join table2 as b
on a.ID = b.ID
)
with data
primary index (ID)
