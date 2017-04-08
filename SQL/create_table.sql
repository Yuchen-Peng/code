create multiset table UD206.lzq857_my_table_name
as
(select
a.*,
case
    when strategy_segment like '%CIA%' then 'Internet'
    when strategy_segment like '%DM%' then 'Direct_Mail' 
    when strategy_segment like '%Bank%' then 'Bank'
    else 'error'
end as channel
from UD442.ONEM_CCA_MODEL_INPUT_VW a
where strategy_segment in ('Small Business CIA 2x', 'Small Business CIA 1pt5x','Small Business CIA - Access','Small Business CIA - Revolver', 'SB DM 1pt5x CASH ITA', 'SB DM 2x CASH FEE ITA', 'SB Bank', 'SB DM 1x CASH ITA', 'SB DM 2x CASH NO FEE ITA')
and open_dt between '2014-01-01' and '2016-12-31'
and acct_id is not null)
with data
primary index (acct_id)

collect statistics UD206.lzq857_my_table_name index(accd_id);
