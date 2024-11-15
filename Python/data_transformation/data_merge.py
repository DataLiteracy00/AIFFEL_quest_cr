import pandas as pd

df_a = pd.DataFrame({'key': ['a','b','c','d','e'],'num_a': [1,2,3,4,5]})
df_b = pd.DataFrame({'key': ['a','b','d','f','g'],'num_b': [11,15,35,45,55]})
df_c = pd.DataFrame({'key': ['f','g','h','i','g'],'num_a': [6,7,8,9,0]})

# print(pd.concat([df_a, df_b]))
# print(pd.concat([df_a, df_b, df_c]))
# print(pd.concat([df_a, df_b, df_c], axis = 1))
# print(df_a.merge(df_b))
# print(df_a.merge(df_b, how = 'outer'))
# print(df_b.merge(df_a, how = 'outer'))
# print(df_a.merge(df_c, how = 'outer'))

df_d = pd.DataFrame({'key': ['a','b','c','d','e'],'id': ['q','w','e','r','t'],'num_a': [1,2,3,4,5]})
df_e = pd.DataFrame({'key': ['a','b','d','f','g'],'id': ['r','t','z','x','y'],'num_b': [11,15,35,45,55]})

# print(df_d.merge(df_e, on = 'id'))
# print(df_d.merge(df_e, on = 'id', how = 'left'))

df_f = pd.DataFrame({'key': ['a','b','c','d','e'],'num_a': [1,2,3,4,5]})
df_g = pd.DataFrame({'id': ['a','b','d','f','g'],'num_b': [11,15,35,45,55]})
# print(df_f.merge(df_g, left_on = 'key', right_on = 'id', how = 'outer'))

df_h = pd.DataFrame({'key': ['a','b','c','d','e'],'num_a': [1,2,3,4,5]})
df_i = pd.DataFrame({'key': ['a','b','d','f','g'],'num_b': [11,15,35,45,55]})
df_h = df_h.set_index('key')
df_i = df_i.set_index('key')
# print(df_h.join(df_i, lsuffix = '_a', rsuffix = '_b'))
# print(df_h)
# print(df_h.join(df_i, how = 'outer'))
# print(df_h.join(df_i, how = 'inner'))

data = {
    'Country': ['USA', 'Canada', 'Germany', 'USA', 'Germany', 'Canada', 'USA', 'Germany', 'Canada', 'USA'],
    'Purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No'],
    'Age': [22, 25, 30, 28, 35, 40, 45, 28, 25, 38]
}

df = pd.DataFrame(data)

# -----------------------------------------------------------------------------------------