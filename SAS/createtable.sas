/*create dataset from SQL table*/

proc sql;

create table output.result as (
select a.*, b.* from table1 as a
left join table2  as b
on a.id = b.id
)
;
quit;
