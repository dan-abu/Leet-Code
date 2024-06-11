# Question can be found using this link: https://leetcode.com/problems/combine-two-tables/
# Solution below
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """Left joins two tables on the personId column"""
    combined_table = person.merge(address, how='left', left_on='personId', right_on='personId')
    combined_table = combined_table[['firstName', 'lastName', 'city', 'state']]
    return combined_table