/*create dataset from Teradata table*/

libname official '/prod/app/npv/models/cca/lava/Official/InputData/InputData_V19';
libname ud442 teradata server="oneview" database="ud442" user="lzq857" password="***";
libname output '/prod/app/npv/analysis/cca/Personal/lzq857/dataset';

proc sql;

create table output.sb_dm_jun2015 as (
select a.*, b.credit_policy_seg from official.sb_dm_jun2015 as a
left join ud442.ONEM_CCA_MODEL_INPUT_VW as b
on a.application_id = b.application_id
)
;
quit;
