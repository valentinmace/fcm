# Valentin Macé
# valentin.mace@kedgebs.com
# Developed for my internship at the LIS lab during my 4th year in the Computer Science Engineer program at Polytech Marseille

# Feel free to use this code as you wish as long as you quote me as author

#  ----------------------------
# |          PURPOSE           |
#  ----------------------------

# Pupose of this script is to run the FCM on various embeddings (contained in the 'word_emb' folder)
# and to get results in a file ('macro_f1' folder) including macro f1, micro f1 and weigthed f1 scores (plus precision and recall)
# Early stopping is not implemented yet (it might be necessary to modify the FCM directly)

#  ----------------------------
# |            USAGE           |
#  ----------------------------

# Using python 3 (I have not tested with version 2)

# Open a terminal, go to 'fcm_global.py' folder and use :
# python fcm_global.py <training_file> <testing_file> <number of epochs> <learning rate> [word embeddings]
# If you do NOT fill the argument for word embeddings, it will run on all the files availables in the folder
# Example : python fcm_global.py semeval2018_train semeval2018_test 30 0.005

# Note test_file and train_file have to be in data/corpus/formated folder, word embeddings has to be in data/corpus/word_emb folder

# Setup
import sys
import subprocess
import numpy as np
import os
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

# Function for running the FCM once
# Returns a string containing results
# Takes as parameters:
# train_file and test_file which must be in data/corpus/formated folder
# epochs and learning_rate
# word_emb the name of the file of embeddings which must be in data/word_emb
def fcm_and_results(train_file=None, test_file=None, epochs=None, learning_rate=None, word_emb=None):
	# Command to run the FCM, check its README if you need to modify
	command = ['RE_FCT', '../data/corpus/formated/'+train_file,
				'../data/corpus/formated/'+test_file, '../results/predict',
				'../data/word_emb/'+word_emb, epochs, learning_rate]
	print("Loading word embedding... (can take a while)")
	process = subprocess.run(command, cwd="fcm", shell=True, stderr=subprocess.PIPE)	# starting FCM and waiting for it

	file = open("results/predict", "r")		# reading results of FCM
	lines = file.readlines()
	file.close()

	# Getting predicted labels
	predicted = []					# will contain all predictions
	for i in range(len(lines)):
	    line_split = lines[i].split()
	    predicted.append(line_split[1])

	# Getting real labels
	file = open("results/macro_f1/keys/"+test_file+"_keys", "r")
	lines = file.readlines()
	file.close()
	keys = []						# will contain all keys
	for i in range(len(lines)):
	    line_split = lines[i].split()
	    keys.append(line_split[0])
	set_keys = set(keys)

	# Preparing string with results
	results = '\n\n -----------------------------------------------------\n'
	results += '|       Results for FCM on the '+test_file[:-5]+' corpus       |\n'
	results += ' -----------------------------------------------------\n'
	results += '| Word Embedding:   '+word_emb+'\n'
	results += '| Learning Rate:    '+learning_rate+'\n'
	results += '| Number of Epochs: '+epochs+'\n\n'
	results += classification_report(keys, predicted, target_names=set_keys, digits=4)				# Tab showing results
	results += '\n| Macro F1:    ' + "{0:.4f}".format(f1_score(keys, predicted, average='macro'))	# Various F1 scores...
	results += '\n| Micro F1:    ' + "{0:.4f}".format(f1_score(keys, predicted, average='micro'))
	results += '\n| Weighted F1: ' + "{0:.4f}".format(f1_score(keys, predicted, average='weighted'))
	results += '\n-------------------------------------------------------\n'
	print(results)
	return results 		# returning string


#--------------------------------------------------------------------------------------------------------
# The script starts here

# Arguments for the script
if(len(sys.argv) == 5):
	train_file = 	str(sys.argv[1])
	test_file = 	str(sys.argv[2])
	epochs = 		str(sys.argv[3])
	learning_rate = str(sys.argv[4])
	word_emb_arg = 	None
elif(len(sys.argv) == 6):
	train_file = 	str(sys.argv[1])
	test_file = 	str(sys.argv[2])
	epochs = 		str(sys.argv[3])
	learning_rate = str(sys.argv[4])
	word_emb_arg = 	str(sys.argv[5])
else:
	sys.exit('\nArguments number invalid')

# Reading embeddings available (in folder data/corpus/word_emb)
embeddings = os.listdir("data/word_emb")

# Creating file containing keys (true labels for the data) using the corpus file
file = open("data/corpus/raw/"+test_file, "r")
lines = file.readlines()
file.close()
for i in range(0, len(lines), 3):				# deleting useless lines
    lines[i] = ''

for i in range(2, len(lines), 3):				# deleting useless lines
    lines[i] = ''    
# Creating the key file
file = open("results/macro_f1/keys/"+test_file+"_keys", "w")
for line in lines:
    file.write(line)
file.close()

# Results will contain the string of FCM results
results = ''
# Case where word embedding argument is empty, run the FCM on all embeddings in word_emb folder
if(word_emb_arg == None):
	for word_emb in embeddings:
		results += fcm_and_results(train_file=train_file, test_file=test_file, epochs=epochs, learning_rate=learning_rate, word_emb=word_emb)
# Case where word embedding arg is provided, run the FCM with only this embedding
else:
	results = fcm_and_results(train_file=train_file, test_file=test_file, epochs=epochs, learning_rate=learning_rate, word_emb=word_emb_arg)

# Writing results in a text file
file = open("results/macro_f1/"+test_file+'_results.txt', "w")
file.write(results)
file.close()
print("End, see the results in 'macro_f1' folder")