import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, re
from dao.config import BASE_PATH, DATA_WEATHERDATA_PATH

class myFilter(object): 
    def __init__(self, df):
        self.df = df
        self.filter_dict={
            'glt' : lambda x,v: self.df[x]>v, 
            'glte' :lambda x,v: self.df[x]>=v,
            'lt' : lambda x,v: self.df[x]<v, 
            'lte': lambda x,v: self.df[x]<=v, 
            'inlist' : lambda x,lst: self.df[x].isin(lst), 
            'ninlist' : lambda x,lst: ~self.df[x].isin(lst), 
            'isnull' : lambda x,_:self.df[x].isnull(),
            'nnull' : lambda x,_:~self.df[x].isnull()
        } 
        
        self.gen_df=lambda bool_list: self.df[bool_list]
        self.ret_mydf= lambda log_lst: myDFrame(self.df[log_lst])
        self.call_dict = lambda x,v,_dict: self.filter_dict[_dict](x,v)
        self.call_dict_mydf = lambda x,v,_dict: self.ret_mydf( self.call_dict(x,v,_dict) ) 
        
        self.glt=lambda x,v:self.call_dict_mydf(x,v,'glt') 
        self.glte=lambda x,v:self.call_dict_mydf(x,v,'glte') 
        self.lt=lambda x,v:self.call_dict_mydf(x,v,'lt')
        self.lte=lambda x,v:self.call_dict_mydf(x,v,'lte') 
        self.inlist= lambda x,v:self.call_dict_mydf(x,v,'inlist') 
        self.ninlist=lambda x,v:self.call_dict_mydf(x,v,'ninlist') 
        self.isnull = lambda x:self.call_dict_mydf(x,_,'isnull') 
        self.nnull = lambda x:self.call_dict_mydf(x,_,'nnull') 
    
    def select_col(self, *arg): 
        return myDFrame(self.df.loc[:, list(arg)])

    def row_end(self, _x):
        return myDFrame(self.df.loc[ :_x, :])
    
    def row_from(self, _x):
        return myDFrame(self.df.loc[ _x:, :])
    
    def row_btw(self, _x, _y): 
        return myDFrame(self.df.loc[range(_x, _y), :])

    def row_at(self, _x): 
        return myDFrame(self.df.loc[_x, :])

    def irow_end(self, _x):
        return myDFrame(self.df.iloc[ :_x, :])
    
    def irow_from(self, _x):
        return myDFrame(self.df.iloc[ _x:, :])
    
    def irow_at(self, _x):
        return myDFrame(self.df.iloc[ _x, :])
    
    def irow_btw(self, _x, _y): 
        return myDFrame(self.df.iloc[range(_x, _y), :] )

    def select_end(self, *arg):
        return myDFrame(self.df.loc[:arg[0], list(arg[1:])])

    def select_from(self, *arg):
         return myDFrame(self.df.loc[arg[0]:, list(arg[1:])])
    
    def select_btw(self, *arg):
        return myDFrame(self.df.loc[ arg[0]:arg[1], list(arg[2:])])

    def select_at(self, *arg):
        return myDFrame(self.df.loc[ arg[0], list(arg[1:])])
    
    def iselect_end(self, *arg):
        return myDFrame(self.df.iloc[:arg[0], list(arg[1:])])

    def iselect_from(self, *arg):
         return myDFrame(self.df.iloc[arg[0]:, list(arg[1:])])
    
    def iselect_btw(self, *arg):
        return myDFrame(self.df.iloc[ arg[0]:arg[1], list(arg[2:])] )
    
    def iselect_at(self, *arg):
         return myDFrame(self.df.iloc[arg[0], list(arg[1:])])

class myDFrame(myFilter):
    def __init__(self,df):
        self.df=df.copy()
        myFilter.__init__(self, self.df)
    
    def to_datetime(self, col_name, format, target_col=None):
        tmp_col=pd.to_datetime( self.df[col_name] , format=format )
        if target_col == None:
            self.df[col_name]=tmp_col
        else:
            self.df['target_col']=tmp_col 
        
    def get_df(self):
        return self.df
    
    @classmethod
    def read_csv(self,filename, encoding='utf-8'):
        return myDFrame(pd.read_csv(filename, encoding=encoding)) 

def main():
    # This is the test case for runing the myDFrame
    print('Getting the testing data')
    from os import listdir
    a = listdir(DATA_WEATHERDATA_PATH)
    print(a)
    
    print('testing completed')
    
if __name__ == '__main__':
    main()