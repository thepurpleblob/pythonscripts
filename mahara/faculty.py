from Mahara import Mahara
import sys

# stuffs
endpoint = "https://portfolio.gla.ac.uk/webservice/rest/server.php?alt=json"
wstoken = "c279a0c9bf79bd3fea681a0d02bde710"

institutions = [
    'arts',
    'education',
    'eng',
    'fims',
    'ibls',
    'interdisciplinary',
    'lbss',
    'medicine',
    'moodlenineteen',
    'moodletwo',
    'physci',
    'services',
    'vet'
]


# create webservice 
mahara = Mahara(endpoint, wstoken)

for institution in institutions:
    print("Getting institution users for "+institution)
    users = mahara.mahara_institution_get_members(institution) 
    print("Number of users is " + str(len(users)))

    print("Removing users from institution "+institution)
    data = mahara.mahara_institution_remove_members(institution, users)
    print("done")

