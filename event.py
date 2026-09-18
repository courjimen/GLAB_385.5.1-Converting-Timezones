#Event Handling Application
import datetime

db = {}
#add event
def add_event():
    # ask for event name
    event_name = input('Enter event name: ')

    # get event date
    date_input = input('Enter date in YYYY-MM-DD Format: ')

    try:
        event_date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
        print(event_date)
    except ValueError as e:
        print('Invalid Date Format. Please use YYYY-MM-DD')
        return
    # create key value pair in db
    # key event name, event date 
    db[event_name] = date_input
    #print success message
    print(f'✅ Your event: {event_name} has been added successfully!')
    #list event

def list_events():
    print('List events')
#quit application

#prompt user for input
def main():
    while True:
        print('\nEvent Management System')
        print('1. Add Event')
        print('2. List Events')
        print('3. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_event()
        elif choice == '2':
            list_events()
        elif choice == '3':
            print('Goodbye 👋🏾')
            break
        else:
            print('Invalid Choice. Choose again.')


if __name__ == '__main__':
    main()