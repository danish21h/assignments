#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df_maths = pd.read_excel(r'Python_Assignment.xlsx',sheet_name = 'Maths')
df_physics = pd.read_excel(r'Python_Assignment.xlsx',sheet_name = 'Physics')
df_hindi = pd.read_excel(r'Python_Assignment.xlsx',sheet_name = 'Hindi')
df_economics = pd.read_excel(r'Python_Assignment.xlsx',sheet_name = 'Economics')
df_music = pd.read_excel(r'Python_Assignment.xlsx',sheet_name = 'Music')


# In[4]:


df_maths['% Marks Maths'] = 100.0 * (df_maths['Theory Marks'] + df_maths['Numerical Marks'] + df_maths['Practical Marks'])/300
df_physics['% Marks Physics'] = 100.0 * (df_physics['Theory Marks'] + df_physics['Numerical Marks'] + df_physics['Practical Marks'])/300
df_hindi['% Marks Hindi'] = 100.0 * (df_hindi['Marks'])/100
df_economics['% Marks Economics'] = 100.0 * (df_economics['Theory Marks'] + df_economics['Numerical Marks'])/200
df_music['% Marks Music'] = 100.0 * (df_music['Theory Marks'] + df_music['Practical Marks'])/200


# In[5]:


df_maths.drop(['Theory Marks','Numerical Marks','Practical Marks'], inplace = True , axis = 1)
df_physics.drop(['Theory Marks','Numerical Marks','Practical Marks'], inplace = True , axis = 1)
df_hindi.drop(['Marks'], inplace = True , axis = 1)
df_economics.drop(['Theory Marks','Numerical Marks'], inplace = True , axis = 1)
df_music.drop(['Theory Marks','Practical Marks'], inplace = True , axis = 1)


# In[6]:


df_final = pd.merge(df_maths,df_physics,how = 'outer', on = ['Roll No','Class'])
df_final = pd.merge(df_final,df_hindi,how = 'outer', on = ['Roll No','Class'])
df_final = pd.merge(df_final,df_economics,how = 'outer', on = ['Roll No','Class'])
df_final = pd.merge(df_final,df_music,how = 'outer', on = ['Roll No','Class'])


# In[8]:


# 1.0 Table asked in part 1
df_final.to_csv('part_1.csv',index = False)


# In[9]:


# 2.1 How many students are enrolled with the tution provider:
answer_2a = len(df_final) # Since table is at student level (Roll No and Class), length of it would be unique students enrolled


# In[10]:


print(answer_2a)


# In[11]:


#2.2 How many students have taken all the five subjects?
df_final['All Subjects Flag'] = (df_final['% Marks Maths'].notnull()) & (df_final['% Marks Physics'].notnull()) & (df_final['% Marks Hindi'].notnull()) & (df_final['% Marks Economics'].notnull()) & (df_final['% Marks Music'].notnull()) 
answer_2b = sum(df_final['All Subjects Flag'])
print(answer_2b)


# In[12]:


#2.3 Which class has the most number of students?
answer_2c = df_final.groupby("Class").size().reset_index(name = 'counts')
answer_2c = answer_2c[answer_2c['counts'] == answer_2c['counts'].max()]
print(answer_2c) # There is a tie for class 6,7,8,8,10


# In[13]:


#2.4 Which class has the highest average percentage of marks across all subjects?
# Average % at student level (Average of %)
df_final["Overall % Marks"] = df_final[['% Marks Maths','% Marks Physics','% Marks Hindi','% Marks Economics','% Marks Music']].mean(axis=1)
answer_2d = df_final.groupby("Class")['Overall % Marks'].mean().reset_index(name = 'Average % Marks')
answer_2d = answer_2d[answer_2d['Average % Marks'] == answer_2d['Average % Marks'].max()]


# In[14]:


#answer for questoin 2d (Class 5 has best average % Marks)
print(answer_2d)


# In[15]:


#2.5 Which subject has the highest average percentage of marks across all classes?
answer_2e = df_final[['% Marks Maths','% Marks Physics','% Marks Hindi','% Marks Economics','% Marks Music']].mean(axis = 0).reset_index()
answer_2e.columns  = ['Type','% Marks']
answer_2e = answer_2e[answer_2e['% Marks'] == answer_2e['% Marks'].max()]


# In[16]:


# Answer for question 2e (Hindi has best average % Marks)
print(answer_2e)


# In[20]:


data = {'question': 
        ['How many students in total are enrolled with the tuition provider?',
         'How many students have taken all the five subjects?',
         'Which class has the most number of students?',
         'Which class has the highest average percentage of marks across all subjects?',
        'Which subject has the highest average percentage of marks across all classes?'],
        'answer': [answer_2a, answer_2b, 'there is a tie for class 6,7,8,9,10', 'Class 5','Hindi']}
pd.DataFrame.from_dict(data).to_csv('part_2.csv',index=False)


# In[ ]:




