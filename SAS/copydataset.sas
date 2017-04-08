/* create new dataset out of old one, choose the columns to keep/drop */

libname lib1 'path';
data lib1.output1;
set lib1.input(keep= id revenue rate channel);
REV_VAR3 = revenue;
if rate = 1.5 then rate = 1.45;
if channel = 'Online' then channel_A = 'INTERNET';
else if channel = 'DM' then channel_A = 'Mail';
else channel_A = 'BRANCH';
run;

Data lib1.output2;
set lib1.input(keep= id Balance_1-Balance_99);
run;

data lib1.output1
set lib1.output1(drop=channel);
run;

