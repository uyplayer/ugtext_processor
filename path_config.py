import os

project_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(project_dir, 'tests')
os.makedirs(test_dir, exist_ok=True)

data_dir = os.path.join(project_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

print(test_dir)
