import requests

import os
import json

USER = os.getenv('AZURE_USER')
PAT = os.getenv('AZURE_PAT')
BASE = 'https://dev.azure.com'
ORGANIZATION = os.getenv('AZURE_ORG')
PROJECT = os.getenv('AZURE_PROJECT')

URL = f'{BASE}/{ORGANIZATION}/{PROJECT}/_apis'



def request():
    # 1. Pega a query e as colunas
    query_id = 'cd30e09b-be52-43e9-b83c-c664e7612205'
    query = requests.get(f'{URL}/wit/queries/{query_id}?$expand=wiql&api-version=5.0',
                       headers={
                           'Content-Type':'application/json',
                           'Accept': 'application/json' },
                       auth=(USER, PAT))
    query_json = query.json()
    
    fields = [c.get('referenceName') for c in query_json.get('columns')]
    columns = [c.get('name') for c in query_json.get('columns')]
    
    # 2. Pega os ids dos work itens da query
    work_items = requests.post(f'{URL}/wit/wiql/{query_id}?api-version=5.0',
                       headers={
                           'Content-Type':'application/json',
                           'Accept': 'application/json' },
                       data=json.dumps({ 'query': query_json.get('wiql') }),
                       auth=(USER, PAT))
    work_items_json = work_items.json()
    work_items_ids = [wi.get('id') for wi in work_items_json.get('workItems')]
    
    # 3. Busca todos os detalhes dos workitens acima
    data =  requests.post(f'{URL}/wit/workitemsbatch?api-version=5.0',
                    headers={
                        'Content-Type':'application/json',
                        'Accept': 'application/json' },
                    data=json.dumps({ 'ids': work_items_ids,
                                      'fields': fields
                                     }),
                    auth=(USER, PAT))
    
    return fields, data.json()

