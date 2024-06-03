#!/usr/bin/python3
"""for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

todo_url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
   if len(sys.argv) > 1:
      if re.fullmatch(r'\d+', sys.argv[1]):
         employee = request.get('name')
         emp_id = int(sys.argv[1])
         req = requests.get('{}/users/{}'.format(todo_url, emp_id)).json()
         task_req = requests.get('{}/todos'.format(todo_url)).json()
         tasks = list(filter(lambda x: x.get('emp_id') == emp_id, task_request))
         task_done = list(filter(lambda x: x.get('completed'), tasks))

         print(
              'Employee {} is done with tasks({}/{}):'.format(
				employee,len(task_done),len(tasks))
	)
      if len(task_done) > 0:
         for task in task_done:
             print('\t {}'.format(task.get('title')))
