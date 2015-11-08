#!/usr/local/bin/python

from pandas import DataFrame, read_csv
import pandas as pd

def ReadTables():
	inputs=pd.read_csv("inputs.csv")
	outputs= pd.read_csv("outputs.csv")
	tx=pd.read_csv("transactions.csv")
	return (inputs,outputs,tx)



def doubleSpend(Inputs,Outputs):
	print "Looking for double spend transactions"
	print "*"*20
	df=Inputs.groupby(["output_id"]).size().sort_values()
	DoubleSpends = df.loc[df.values>=2]
	Dobule_ids=[]
	for i in DoubleSpends.index:
		if i== -1 :
			continue
		#Else we found a double spend TX
		Dobule_ids.append(i)

	for i in Dobule_ids:
		print Inputs.loc[Inputs["output_id"] == i]

	#Remove TX number 216580
	Inputs=Inputs[ Inputs["tx_id"] != 216580 ]
	Outputs=Outputs[ Outputs["tx_id"] != 216580 ]
	print "#"*20
	return (Inputs,Outputs)


def MinerValid(Inputs,Outputs):
	coinBase=Inputs[ Inputs["address_id"] == 0 ]
	L=[]
	for i in coinBase["tx_id"]:
		tx_value= Outputs[ Outputs["tx_id"]==i ]["value"]
		if int(tx_value.values) > 5000000100 :
			L.append (int(tx_value.values))

	L.sort()
	print L

	return (Inputs,Outputs)




def IllegalTX():
	(inputs,outputs,tx)=ReadTables()
	(inputs,outputs) = doubleSpend(inputs,outputs)
	(inputs,outputs) = MinerValid(inputs,outputs)

	return

IllegalTX()