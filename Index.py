import pandas as pd
#Convert the tables into data frames. First table is Document and Rev, second table is Rev and Sequence
d={'Doc':['DOC 1','DOC 1','DOC 1','DOC 1','DOC 2','DOC 2','DOC 2','DOC 2','DOC 2','DOC 2','DOC 3','DOC 3','DOC 3','DOC 3'],
   'Rev':[0,'B','A','C','A','B','C','D',0,1,'A','B',0,1]}
df=pd.DataFrame(data=d)
rev_dict={'Rev':['A','B','C','D','E',0,1],'Value':[1,2,3,4,5,6,7] }
df2=pd.DataFrame(data=rev_dict)
#Merge 2 data frames
df3=pd.merge(df,df2,left_on='Rev', right_on='Rev', how='left', sort=False)

doc_list=[]
for i in range(len(df.iloc[:,0])):
    if df.iloc[:,0][i] in doc_list:
        continue
    else:
        doc_list.append(df.iloc[:,0][i])

grouped_df_by_doc_no=df3.groupby('Doc')
index_store_array = []

def store_indexes(my_val):
    # This function stores the final output
    index_store_array.append(my_val)
    # return index_store_array
    return index_store_array

def ret_group(my_data_frame,doc_no):
    #This group retrives each group which is like a container represented by Document Number
    extracted=my_data_frame.get_group(doc_no)
    return extracted
for selected_doc in doc_list:
    yy=ret_group(grouped_df_by_doc_no,selected_doc)
    temp_array = yy['Value'].tolist()
    temp_array.sort()
    for item_val in yy['Value']:
        sorted_index=temp_array.index(item_val)
        #item_val=sorted_index
        store_indexes(sorted_index)
df3['Submission Seq']=index_store_array
print(df3)
