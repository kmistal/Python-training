import json

journal_entries = []


def start():
    print_header()
    fetch_entries()
    start_event_loop()


def print_header():
    print('---------------------')
    print('     JOURNAL APP     ')
    print('---------------------')


def start_event_loop():
    while True:
        selected_option = str.strip(
            input('What do you want to do? [l]ist, [a]dd, e[x]it ')
        )

        if selected_option.lower() == 'l':
            print_all_entries()
        elif selected_option.lower() == 'a':
            add_entry()
        elif selected_option.lower() == 'x':
            save_entries()
            break


def fetch_entries():
    print('... Loading from journal.json ...')

    global journal_entries
    journal_file = open('files/journal.json', 'r')
    file_content = journal_file.read()

    if len(file_content) != 0:
        journal_entries = json.loads(file_content)

    print('... Loaded {} entries ...'.format(len(journal_entries)))
    journal_file.close()


def add_entry():
    global journal_entries
    entry = input('Enter your journal entry: ')

    if len(entry) != 0:
        journal_entries.append(entry)
    else:
        print('Entry empty, not added')


def save_entries():
    print('... Saving to journal.json ...')
    global journal_entries

    journal_file = open('journal.json', 'w')
    json.dump(journal_entries, journal_file)

    journal_file.close()
    print('... Save complete ...')


def print_all_entries():
    global journal_entries
    index = 1

    for entry in journal_entries:
        print('{}. {}'.format(index, entry))
        index += 1


if __name__ == "__main__":
    start()
