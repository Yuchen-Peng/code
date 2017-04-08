libname output '/prod/app/npv/analysis/cca/Personal/lzq857/dataset';
libname ud206 teradata server="oneview" database="ud206" user="lzq857" password="PWD";


proc sql noerrorstop;
create table output.ic_build2_2 as 
select * from UD206.ic_build2_2;
quit;

proc export data=output.ic_build2_2 
     outfile='/prod/app/npv/analysis/cca/Personal/lzq857/dataset/ic_build2_2.csv'
     dbms=csv
     replace;
run; 
