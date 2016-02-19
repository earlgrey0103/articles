#!usr/bin/env python
# -*- coding: utf-8 -*-

"""Process downloaded documents."""
import PyPDF2
import glob
import time

from collections import Counter
from alchemyapi import AlchemyAPI

alchemyapi = AlchemyAPI()
file_list = glob.glob("pdfs/*.pdf")
entities = {}

for pdf_file in file_list:

    # read in the PDF
    print("[*] Parsing %s" % pdf_file)

    pdf_obj = PyPDF2.PdfFileReader(open(pdf_file, "rb"))

    full_text = ""

    # extract all of the text from each page
    for page in pdf_obj.pages:

        full_text += page.extractText()

    # let the Alchemy API extract entities
    print("[*] Sending %d bytes to the Alchemy API" % len(full_text))

    response = alchemyapi.entities('text', full_text, {'sentiment': 0})

    if response['status'] == 'OK':

        # loop through the list of entities
        for entity in response['entities']:

            # add each entity to our master list
            if entity['text'] in entities:
                entities[entity['text']] += int(entity['count'])
            else:
                entities[entity['text']] = int(entity['count'])

        print("[*] Retrieved %d entities from %s" %
              (len(entities), pdf_file))

    else:
        print("[!] Error receiving Alchemy response: %s" %
              response['statusInfo'])

    time.sleep(1)

# now accumulate our most common terms and print them out
entity_counter = Counter(entities)

top_entities = entity_counter.most_common()

# let's take the top 10 entities UBL mentions
for top_entity in top_entities[0:10]:

    # most_common returns a tuple (entity,count)
    print("%s => %d" % (top_entity[0], top_entity[1]))
