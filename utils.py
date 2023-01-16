import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def extract(rules, filter= "All", min_element=1):
    # rules: a list containing the association rules.
    # filter: default value is 'all'; however, you can filter out any RHS item
    # min_element: default value is 1, it defines the minimum number of elements in each rule
    """
    extract function accepts a list of association rules and the above parameters, and shows the extracted rules 
    and returns the related metrics and the extracted rules.
    """
    LHS_list = []
    RHS_list = []
    support = []
    confidence = []
    lift = []
    for relation_record in rules:
        num_of_rules = len(relation_record[2])
        for itemset in range(num_of_rules):
            LHS_list.append(list(relation_record[2][itemset][0]))
            RHS_list.append(list(relation_record[2][itemset][1]))
            support.append(relation_record[1])
            confidence.append(relation_record[2][itemset][2])
            lift.append(relation_record[2][itemset][3])
    associationRules = []
    for rule in range(len(LHS_list)):
        if len(LHS_list[rule]) + len(RHS_list[rule]) < min_element:
            continue
        if (filter == 'All') | (filter in RHS_list[rule]):
            associationRules.append([LHS_list[rule], RHS_list[rule], support[rule], confidence[rule], lift[rule]])
    return associationRules
    

def data_prepare(dataset, filter='All'):
    # dataset is a dataframe where each columns 
    # is an item, and each value is either yes or no to show whether an item exists in a transaction.
    # filter: default value is 'All'; however, it is possible to filter out transactions containing a specific item.
    """
    data_prepare accepts a dataframe and a given filter and returns a list of lists containig
    item sets in all transactions.
    """
    transactions = []
    columns = dataset.columns.tolist()
    for row in dataset.iterrows():
        tr = []
        for col in columns:
            if row[1][col] == 'Yes':
                tr.append(col)
        if (filter== 'All') | (filter in tr):
            transactions.append(tr)
    return transactions
    
def plot(supp, conf, lif):
    # supp: a list of calculated supports of the extracted rules.
    # conf: a list of calculated confidence of the extracted rules.
    # lif: a list of calculated lifts of the extracted rules.
    
    x = np.array(supp)
    y = np.array(conf)
    plt.xlabel('Support')
    plt.ylabel('Confidence')
    colors = np.array(lif)
    plt.scatter(x, y, c=colors, cmap='CMRmap')
    plt.colorbar()
    plt.show()

def inspect(rules):
    print("The number of associated rules:",len(rules))
    if len(rules) == 0:
        return
    for rule in rules:
        print("LHS: "+ str(rule[0])+" -->"+" RHS:"+ str(rule[1])+ ", support: "+ "{:.2f}".format(rule[2]) +", confidence: " + "{:.2f}".format(rule[3]) +", lift: "+ "{:.2f}".format(rule[4]))
        print(20*"----")