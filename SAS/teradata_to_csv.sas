libname output 'path';
libname udcontainer teradata server="oneview" database="udcontainer" user="***" password="***";


proc sql noerrorstop;
create table output.table as 
select * from UDcontainer.table1;
quit;

proc export data=output.table
     outfile='path/table.csv'
     dbms=csv
     replace;
run; 
