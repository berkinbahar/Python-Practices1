# Python-Practices1

## TASK 1

You have been asked to find the job titles of the highest-paid employees.

Your output should include the highest-paid title or multiple titles with the same salary.

DataFrames: worker, title

### worker

worker_id:int64

first_name:object

last_name:object

salary:int64

joining_date:datetime64

department:object


### title

worker_ref_id:int64

worker_title:object

affected_from:datetime64


### Expected Output Type: 

pandas.DataFrame

### Expected Output:


best_paid_title

Asst. Manager

Manager


