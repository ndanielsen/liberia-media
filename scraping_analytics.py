
# coding: utf-8

# In[2]:

import pandas as pd


# In[4]:

df = pd.read_csv("data/url_logger.csv")


# In[10]:

df['unit'] = 1


# In[33]:

success = df[df.url_status_code ==200].unit.count()
success_grouped = df[df.url_status_code ==200].groupby('name').unit.count()

fail = df[df.url_status_code !=200].unit.count()
fail_grouped = df[df.url_status_code !=200].groupby('name').unit.count()


# In[14]:

total_requests = df.url_status_code.sum()


# In[61]:

print "Summary of URL Requests"
print "-" * 50
print "Percentage successful: %r" % (round(float(success)/ (success + fail), 2))
print "Total Succesful:", success
print "Total Unsuccesful:", fail
print "\n"


print 'Quantity of Articles Available'
print "-" * 50

for index, elem in enumerate(success_grouped):
    print success_grouped.index[index].capitalize(),": ", success_grouped[index]


# In[ ]:



