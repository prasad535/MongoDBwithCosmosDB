
from db_connection import MongoDBClient
from constants import DATABASE_NAME

mongo_db_client = MongoDBClient(database_name=DATABASE_NAME)
collection = mongo_db_client.database['test-collection-v1']

sample_data = [{'case_id': 'EZYV01',
  'continent': 'Asia',
  'education_of_employee': 'High School',
  'has_job_experience': 'N',
  'requires_job_training': 'N',
  'no_of_employees': 14513,
  'yr_of_estab': 2007,
  'region_of_employment': 'West',
  'prevailing_wage': 592.2029,
  'unit_of_wage': 'Hour',
  'full_time_position': 'Y',
  'case_status': 'Denied'},
 {'case_id': 'EZYV02',
  'continent': 'Asia',
  'education_of_employee': "Master's",
  'has_job_experience': 'Y',
  'requires_job_training': 'N',
  'no_of_employees': 2412,
  'yr_of_estab': 2002,
  'region_of_employment': 'Northeast',
  'prevailing_wage': 83425.65,
  'unit_of_wage': 'Year',
  'full_time_position': 'Y',
  'case_status': 'Certified'},
 {'case_id': 'EZYV03',
  'continent': 'Asia',
  'education_of_employee': "Bachelor's",
  'has_job_experience': 'N',
  'requires_job_training': 'Y',
  'no_of_employees': 44444,
  'yr_of_estab': 2008,
  'region_of_employment': 'West',
  'prevailing_wage': 122996.86,
  'unit_of_wage': 'Year',
  'full_time_position': 'Y',
  'case_status': 'Denied'}
]

rec = collection.insert_many(sample_data)
print(len(collection.find()))