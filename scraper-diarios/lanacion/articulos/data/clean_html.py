
import sys
import re
import json
import os
import unicodedata
import string

filename = sys.argv[1] # nombre del archivo a procesar

def remove_accents(data):
    return unicodedata.normalize('NFD', data).encode('ASCII', 'ignore')

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def cleantitle(title):
	return re.split('-',title)[0]

with open(filename, 'r+') as input_file:
	with open('v2-'+filename, 'w') as output_file:
    
		data = json.load(input_file)
		new_data = []

		for row in data:
			new_row = {"titulo": "", "texto": "", "categoria": ""}
			for title in row["titulo"]:
				new_row["titulo"] += remove_accents(cleantitle(cleanhtml(title)))
			for text in row["texto"]:
				new_row["texto"] += remove_accents(cleanhtml(text))
			
			new_row["categoria"] = row["categoria"]
			new_row["dia"] = row["dia"]

			new_data.append(new_row)

		json.dump(new_data, output_file)