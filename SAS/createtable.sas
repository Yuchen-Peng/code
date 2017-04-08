/*create dataset from Teradata table*/

libname official 'path1';
libname ud_container teradata server="oneview" database="ud_container" user="***" password="***";
libname output 'path2';

proc sql;

create table output.result as (
select a.*, b.* from official.table1 as a
left join ud_container.table2  as b
on a.id = b.id
)
;
quit;
