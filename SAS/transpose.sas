/* transpose table from long_form to wide_form, e.g. ID, day, price -> ID, price_1, ..., price_99 */

proc transpose data=long_data out=wide_data prefix=price;
    by ID ;
    id day;
    var price;
run;

/* transpose table from wide_form to long_form, e.g. ID, price_1, ..., price_99 -> ID, day, price */

proc transpose data=wide_data out=long_data;
   by ID;
run;

/*note that the data need sorted by ID first */
/*
PROC SORT DATA=wide_data OUT=wide_data ;
  BY ID;
RUN ;
*/

/* check column name format and drop no need names */

data long_data;
  set long_data (rename=(col1=Price_per_product));
  stmt_number=input(substr(_name_,8), 2.); /* adjust these numbers */
  drop _name_;
run; 
