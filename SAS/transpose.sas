/* transpose table from long_form to wide_form, e.g. acct_ID, stmt_number, CLO -> acct_ID, ACT_CL_1, ..., ACT_CL_99 */

proc transpose data=long_data out=wide_data prefix=ACT_CL_;
    by acct_id ;
    id stmt_number;
    var CLO;
run;

/* transpose table from wide_form to long_form, e.g. acct_ID, ACT_CL_1, ..., ACT_CL_99-> acct_ID, stmt_number, CLO*/

proc transpose data=wide_data out=long_data;
   by acct_id;
run;

/*note that the data need sorted by acct_id first */
/*
PROC SORT DATA=wide_data OUT=wide_data ;
  BY acct_id;
RUN ;
*/

data long_data;
  set long_data (rename=(col1=CREDIT_LIMIT_OPEN));
  stmt_number=input(substr(_name_,8), 2.);
  drop _name_;
run; 
