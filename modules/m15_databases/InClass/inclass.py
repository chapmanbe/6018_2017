all_rad_query = """SELECT * FROM  noteevents WHERE category= 'RADIOLOGY_REPORT'"""

icd9_416_0_query = """SELECT noteevents.*, icd9.code  FROM noteevents INNER JOIN icd9 ON 
                      noteevents.subject_id = icd9.subject_id 
               WHERE icd9.code ='416.0'"""

pah_query = """SELECT noteevents.subject_id, 
                      noteevents.category, 
                      noteevents.text, 
                      icd9.code 
               FROM noteevents INNER JOIN icd9 ON 
                      noteevents.subject_id = icd9.subject_id 
               WHERE icd9.code in ('416.0', '416.8')
               AND noteevents.category = 'RADIOLOGY_REPORT'"""
