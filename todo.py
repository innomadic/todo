import argparse
from models import session, Todo
from init import initialize_db

#ref https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

def add(args):
    
    # create todo object
    new_todo = Todo(text=args.text)
    # add to database
    session.add(new_todo)
    session.commit()
    print(f"Saved! '{args.text}' to database.")
    return args.text

def print_all_todos():
    todos = session.query(Todo).all()
    for todo in todos:
        print(f'#{todo.id}: {todo.text}')    

def list(args):
    print_all_todos()

def init(args):
    initialize_db()

def edit(args):    

    try:
        id = int(args.id)
    except Exception as error:
        print(f'You submitted "{args.id}" as the identifier, but this is not an integer.')
        return
     

    todo = session.query(Todo).filter(Todo.id==args.id).first()
    
    if todo is None:
        print(f'Unable to find todo #{args.id}')
        print(f'Here are the current todos:')
        print_all_todos()
    else:
        todo.text = args.new_text
        session.commit()
        print(f"Todo #{args.id} has been updated to '{todo.text}'")

def delete(args):

    try:
        id = int(args.id)
    except Exception as error:
        print(f'You submitted "{args.id}" as the identifier, but this is not an integer.')
        return
            
    todo = session.query(Todo).filter(Todo.id==args.id).first()
    if todo is None:
        print(f'Unable to find todo #{args.id}')
        print(f'Here are the current todos:')
        print_all_todos()
    else:
        session.delete(todo)
        session.commit()
        print(f'Deleted #{todo.id}')


parser = argparse.ArgumentParser()
parser.set_defaults(func=lambda args: parser.print_help())
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add')
add_parser.add_argument('text') 
add_parser.set_defaults(func=add)  # set the default function to hello

list_parser = subparsers.add_parser('list')
list_parser.set_defaults(func=list)

init_parser = subparsers.add_parser('init')
init_parser.set_defaults(func=init)

edit_parser = subparsers.add_parser('edit')
edit_parser.add_argument('id')
edit_parser.add_argument('new_text')  
edit_parser.set_defaults(func=edit)

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id')
delete_parser.set_defaults(func=delete)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function

