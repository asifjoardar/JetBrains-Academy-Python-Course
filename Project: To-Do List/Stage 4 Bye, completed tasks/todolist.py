
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


# create db file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# model classes should inherit from the DeclarativeMeta
Base = declarative_base()

# model class that describes the table in the database
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return f"{self.id}. {self.task}"

# This method creates a table in our database-
# by generating SQL queries according to the-
# models we described.
Base.metadata.create_all(engine)

# To access the database, we need to create a session.
# The session object is the only thing we need to-
# manage the database.
Session = sessionmaker(bind=engine)
session = Session()

def add_row():
    print('Enter task')
    new_task = str(input())
    print('Enter deadline')
    dead_line = datetime.strptime(input(), r'%Y-%m-%d')
    # To create a row in our table,
    # we need to create an object
    # of the model class and pass it
    # to the add() method
    new_row = Table(task = new_task, deadline = dead_line)
    session.add(new_row)
    session.commit()
    print('The task has been added!')

def get_all_rows(what = False):
    # To get all rows from the table,
    # we can pass the model class to the
    # query() method that selects all rows
    # from the table represented by a model class
    tasks = session.query(Table).order_by(Table.deadline).all()
    if not tasks:
        if not what:
            print('Nothing to do!')
        else:
            print('Nothing to delete')
    else:
        if not what:
            print("All tasks:")
        else:
            print('Choose the number of the task you want to delete:')
        for task in tasks:
            month = task.deadline.strftime('%b')
            day = task.deadline.day
            print(f"{task.id}. {task.task}. {day} {month}")

def todays_tasks():
    date_today = datetime.today()
    month = date_today.strftime('%b')
    day = date_today.day

    tasks = session.query(Table).filter(Table.deadline == date_today.date()).all()
    print(f"Today {day} {month}:")
    for task in tasks:
        print(task)
    if not tasks:
        print("Nothing to do!")
def weeks_tasks():
    for date in (datetime.today() + timedelta(n) for n in range(7)):
        day = date.day
        day_name = date.strftime("%A")
        month = date.strftime('%b')
        tasks = session.query(Table).filter(Table.deadline == date.date()).all()
        print(f"{day_name} {day} {month}:")
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.task}")
        else:
            print("Nothing to do!")
        print()

def missed_task():
    print("Missed tasks:")
    rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    if rows:
        for task in rows:
            month = task.deadline.strftime('%b')
            day = task.deadline.day
            print(f"{task.id}. {task.task}. {day} {month}")
    else:
        print("Nothing is missed!")
    print()

def delete_task():
    get_all_rows(True)
    num = int(input())
    raw = session.query(Table).order_by(Table.deadline).all()
    session.delete(raw[num - 1])
    session.commit()
    print('The task has been deleted!')


while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    choice = int(input())
    if choice == 1:
        todays_tasks()
    elif choice == 2:
        weeks_tasks()
    elif choice == 3:
        get_all_rows()
    elif choice == 4:
        missed_task()
    elif choice == 5:
        add_row()
    elif choice == 6:
        delete_task()
    else:
        print("Bye!")
        exit()
