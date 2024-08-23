class Person:
  def __init__(company, name, project):
    company.name = name
    company.project = 10
  def name(company):
      print("Harish")

  def get_work_done(company):
        print(f"You done a projects in {company.name} {company.project}")

p1 = Person("Harish", 10)

print(p1.name)
print(p1.project)

p1.get_work_done()

your_projects = Person('Zoho', 'Software Developer')
your_projects.get_work_done()