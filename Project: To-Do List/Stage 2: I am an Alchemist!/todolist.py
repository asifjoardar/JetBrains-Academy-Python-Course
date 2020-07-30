from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker


#create db file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

#model classes should inherit from the DeclarativeMeta
Base = declarative_base()

#model class that describes the table in the database
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field

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
    # To create a row in our table,
    # we need to create an object
    # of the model class and pass it
    # to the add() method
    new_row = Table(task = new_task, deadline = datetime.today())
    session.add(new_row)
    session.commit()
    print('The task has been added!')

def get_all_rows():
    # To get all rows from the table,
    # we can pass the model class to the
    # query() method that selects all rows
    # from the table represented by a model class
    rows = session.query(Table).all()
    tsk = list()
    for i in rows:
        tsk.append(i.task)
    print('Today:')
    for indx in range(len(tsk)):
        print('{}. {}'.format(indx+1, tsk[indx]))
    if len(tsk) == 0:
        print('Nothing to do!')

while True:
    print("1) Today's tasks")
    print("2) Add task")
    print("0) Exit")
    choice = int(input())
    if choice == 1:
        get_all_rows()
    elif choice == 2:
        add_row()
    else:
        print("Bye!")
        exit()
