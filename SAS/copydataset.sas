/* create new dataset out of old one, choose the columns to keep/drop */

libname lib1 '/prod/app/npv/analysis/cca/Personal/lzq857/dataset';
data lib1.output1;
set lib1.input(keep= acct_id a_ss_s1086_r ICL SB_revenue rwds_expect_earn_rt);
SB_REV_VAR3 = SB_revenue;
if rwds_expect_earn_rt = 1.5 then rwds_expect_earn_rt = 1.45;
if sentinel_channel = 'CIA' then SBV_channel = 'INTERNET';
else if sentinel_channel = 'DM_ITA' then SBV_channel = 'DM';
else SBV_channel = 'BRANCH';
run;

Data lib1.output2;
set lib1.input(keep= acct_id ACT_CL_1-ACT_CL_99);
run;

data lib1.output1
set lib1.output1(drop=sentinel_channel);
run;

