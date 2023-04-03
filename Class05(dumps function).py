# Dumps() function.

# Parameters for dumps() are:
# skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, spearators,sort_keys.

# 1. skipkeys - if skipkeys is True by default it is False, then dict keys that are not basic type i.e, str, int, float, bool and None will be skipped instead of raising an error. 
# 2. indent - if indent parameter is a integer(non-negative ) or string, then JSON object members will be printed in a more readable manner.
# 3. sort_keys - if sort_keys is True by default it is False, then the output of dict will be sorted according to keys.






# Using the three parameters:


#(i) Using Skipkeys and indent:
import json

my_dict1 = {
           'c' :'Mango',
           'd' : 'Grapes',
           'e' : 'Oranges',
           'a' : 'Pears',
           'b' : 'Watermelon',
           (5,6,7) : 'Coconut'
           }

into_json_string = json.dumps(my_dict1,
                              skipkeys = True,                # here skipkeys parameter will skip the tuple (5,6,7) and its value 'Coconut' when converting the dict into a json string.
                              indent=4 ,
                              )
                              
print("With parameters- \"skipkeys\" and \"indent\" :", into_json_string)





#(ii) Using Skipkeys, indent and sort_keys:

my_dict2 = {
           'c' :'Mango',
           'd' : 'Grapes',
           'e' : 'Oranges',
           'a' : 'Pears',
           'b' : 'Watermelon',
           }


into_json_string = json.dumps(my_dict2,
                              skipkeys = True,
                              indent=4 ,
                              sort_keys = True               # Sort_keys cannot work with tuple as dict keys.
                              )

print("With parameters- \"skipkeys\" , \"indent\" and \"sort_keys\" :", into_json_string)