import requests
import operator
import datetime

data = requests.get("https://sheetdb.io/api/v1/ebkxvvw0cdyp4").json()

today = [datetime.datetime.now().strftime("%x")]
today.append(int(input("How many minutes do you have to do homework today? ")))

tomorrow = [(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%x")]
tomorrow.append(int(input("How many minutes do you have to do homework tomorrow? ")))

dayafter = [(datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%x")]
dayafter.append(int(input("How many minutes do you have to do homework the day after? ")))

# ASSIGNMENT STARTS HERE

# FIRST WRITE A COMMENT DESCRIBING YOUR ALGORITHM
# HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A FEW ASSIGNMENTS.  
'''
- My heuristic will be to do whatever has the nearest due date first. 
    - sort assignments into a dictionary based on due date
        -sort each list in the dictionary by priority
        - order the dictionary by the key (due date)
        - create a list of the dictionary values, which are in the order of due date and then priority

Part 1:
    - If there are assignments due tomorrow:
        - Immediately add to today homework list, regardless of time needed.
        - If there is extra time, do whatever other assignments I can
        - Remainding time will be added to tomorrow's homework time

    - If there are assignments due dayafter:
        - Loop through all the assignments
            - If there is time to do some of it day today (after adding all the homework due tomorrow if applicable)
                - add to today's homework list

            - All the other assignments due the day after will be tomorrow's homework

Part 2 (will run regardless of the due date of assignments. If part 1 is applicable, it will run after part 1):
    - Loop through all the assignments
        - If I have enough time for the assignment
            - do it

        - If not, leave it in the to-do list

    - Add remainding homework time to the next day
    - repeat for tomorrow and day after
'''

# NEXT WRITE YOUR ALGORITHM OUT IN PSEUDOCODE

#FINALLY - IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT
class Day():
    def __init__(self, date, homework_time):
        self.date = datetime.datetime.strptime(str(date), '%x').strftime('%-m/%-d/%Y')
        self.homework_time = float(homework_time)


class Assignments():
    def __init__(self, assignment_data, today, tomorrow, dayafter):
        self.data = assignment_data
        self.today = Day(today[0], today[1])
        self.tomorrow = Day(tomorrow[0], tomorrow[1])
        self.dayafter = Day(dayafter[0], dayafter[1])

    def sort_data_by_due_date(self):
        sorted_data = {}

        for assignment in self.data:
            if assignment["DUE DATE"] not in list(sorted_data.keys()):
                sorted_data[assignment["DUE DATE"]] = [assignment]

            else:
                sorted_data[assignment["DUE DATE"]].append(assignment)

        return sorted_data

    def sort_list_by_priority(self, input_list):
        for assignment in input_list:
            priority_value = float(assignment["PRIORITY"])
            assignment["PRIORITY"] == priority_value

        sorted_list = sorted(input_list, key=lambda d: d['PRIORITY'], reverse=True) 
        return sorted_list

    def sort_assignments(self):
        data_dict = self.sort_data_by_due_date()

        for due_data in data_dict:
            data_dict[due_data] = self.sort_list_by_priority(self.sort_list_by_priority(data_dict[due_data]))

        return data_dict

    def set_assignments_to_date(self, assignments, day):
        do_homework = True
        day_work = []

        for assignment in assignments:
            if day.homework_time - float(assignment["TIME NEEDED (MIN)"]) >= 0:
                day_work.append(assignment)
                day.homework_time -= float(assignment["TIME NEEDED (MIN)"])

            else:
                do_homework = False

        return [day.homework_time, day_work]

    def needed_homework_time(self, assignments):
        time_needed = 0

        for assignment in assignments:
            time_needed += float(assignment["TIME NEEDED (MIN)"])

        return time_needed

    def run(self):
        dates = list(self.sort_assignments().keys())
        dates.sort(key = lambda date: datetime.datetime.strptime(date, '%m/%d/%Y'))

        sorted_by_date_data = {}

        for date in dates:
            sorted_by_date_data[date] = self.sort_assignments()[date]

        all_assignments = []
        
        for assignments in list(sorted_by_date_data.values()):
            for assignment in assignments:
                all_assignments.append(assignment)

        do_what_when = {self.today.date: [], self.tomorrow.date: [], self.dayafter.date: []}

        if self.tomorrow.date in list(sorted_by_date_data.keys()):
            for assignment in sorted_by_date_data[self.tomorrow.date]:
                do_what_when[self.today.date].append(str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]))
                self.today.homework_time -= float(assignment["TIME NEEDED (MIN)"])
                all_assignments.remove(assignment)
        
        if self.dayafter.date in list(sorted_by_date_data.keys()):
            for assignment in sorted_by_date_data[self.dayafter.date]:
                if self.today.homework_time - float(assignment["TIME NEEDED (MIN)"]) >= 0:
                    do_what_when[self.today.date].append(str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]))
                    self.today.homework_time -= float(assignment["TIME NEEDED (MIN)"])
                    all_assignments.remove(assignment)

                else:
                    do_what_when[self.tomorrow.date].append(str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]))
                    self.tomorrow.homework_time -= float(assignment["TIME NEEDED (MIN)"])
                    all_assignments.remove(assignment)

        today_hw_data = self.set_assignments_to_date(all_assignments, self.today)
        self.tomorrow.homework_time += today_hw_data[0]

        for assignment in today_hw_data[1]:
            do_what_when[self.today.date].append(str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]))
            all_assignments.remove(assignment)

        tomorrow_hwk_data = self.set_assignments_to_date(all_assignments, self.tomorrow)
        self.dayafter.homework_time += tomorrow_hwk_data[0]

        for assignment in tomorrow_hwk_data[1]:
            do_what_when[self.tomorrow.date].append(str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]))
            all_assignments.remove(assignment)

        dayafter_hwk_data = self.set_assignments_to_date(all_assignments, self.dayafter)

        for assignment in dayafter_hwk_data[1]:
            do_what_when[self.dayafter.date].append(str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]))
            all_assignments.remove(assignment)  


        return do_what_when, [str(assignment["CLASS"]) + " " + str(assignment["ASSIGNMENT"]) for assignment in all_assignments]

    def print_results(self, do_what_when, remaining_assignments):
        for key in do_what_when:
            if len(do_what_when[key]) != 0:
                info = f"On {key}, you have to do "

                for assignment in do_what_when[key]:
                    if assignment == do_what_when[key][-1]:
                        if len(do_what_when[key]) == 1:
                            info += assignment + "."

                        else:
                            info += "and " + assignment + "."

                    else:
                        info += assignment + ", "

                print(info)

        if len(remaining_assignments) != 0:
            info = "Be sure to do "

            for assignment in remaining_assignments:
                if assignment == remaining_assignments[-1]:
                    if len(remaining_assignments) == 1:
                        info += assignment + " in 3 days or so, or at the very most over the weekend."

                    else:
                        info += "and " + assignment + " in 3 days or so, or at the very most over the weekend."
                
                else:
                    info += assignment + ", "

            print(info)



assignments = Assignments(data, today, tomorrow, dayafter)
do_what_when, remaining_assignments = assignments.run()
assignments.print_results(do_what_when, remaining_assignments)