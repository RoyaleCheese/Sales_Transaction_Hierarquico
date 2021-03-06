import csv
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from scipy.spatial import distance
from matplotlib import pyplot as plt

def get_data():
    newfile = open ("noheadertable.txt", "r+")
    aux_list = []
    with open('Sales_Transactions_Dataset_Weekly.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        #print spamreader.shape
        next(spamreader, None)
        for row in spamreader:
            vector =[]
            for j in range (1, 53):
                vector.append(float(row[j]))
            aux_list.append(vector)
    for i in range (len(aux_list)):    
        newfile.write(str(aux_list[i]))
    newfile.close()
    return aux_list

def main():
    #chamada da funcao que retorna lista da base de dados de cada produto pelas 52 semanas
    data = get_data()
    data = np.array(data)
    
    #normalizacao dos dados
    for i in range(len(data)):
        s = 0 #soma total dos valores
        j = 0
        for j in range(len(data[i])):
            s += data[i][j]
        j = 0
        for j in range(len(data[i])):
            data[i][j] = data[i][j]/s

#separando o produto 1 em 13 meses

    #final= []
    end = 0
    for i in range (len (data)):
        tab_month = [] #tabela de tabelas de meses por relacao de venda de cada produto no mes
        for j in range (len(data[i])):
            if ((j%4)== 0):
                start = j
            if ((j % 4 )== 3):
                end = j
                tab_month.append(data[:, start:end+1])

    for i in range (len(tab_month)):
        aux = tab_month[i]
        X = pdist(aux, 'euclidean')
        #print len(X)
        Z = sch.linkage(X, 'average')
        #print Z
        #print len(Z[0])

        fig = plt.figure(figsize=(25, 10))
        dn = sch.dendrogram(Z)
        plt.show()

if __name__ =='__main__':
    main()