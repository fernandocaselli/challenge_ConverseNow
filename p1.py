import pandas as pd
import pymongo

try:
	#df = pd.read_csv('es.tar.gz', compression='gzip', header=0, sep=' ', quotechar='"', error_bad_lines=False)
	#df=pd.read_csv('train.tsv',sep='	',low_memory=False)
	#df_train=pd.read_csv('train.tsv',sep='	',low_memory=False)
	#df_test=pd.read_csv('test.tsv',sep='	',low_memory=False)
	df_validated=pd.read_csv('validated.tsv',sep='	',low_memory=False)
	#df = pd.concat([df_train,df_test,df_validated])
	#dfdd = df.drop_duplicates()

	#limpio posibles duplicado
	df_validated=df_validated.drop_duplicates()

	#print(df_validated)
	#print(df_validated.index)

	#conecto con base mongodb
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["conversenow"]
	mycol = mydb["tabla1"]

	#escribo el dataframe
	x = mycol.insert_many(df_validated.to_dict('records'))
	#print(x.inserted_ids)
except Exception as inst:
	print(inst)
