import tkinter as tk
from tkinter import simpledialog, messagebox
from collections import deque
from prettytable import PrettyTable

def round_robin_dialog():
    time_quantum = simpledialog.askinteger("Round Robin", "Enter Time Quantum:")
    
    if time_quantum is not None:
        num_processes = simpledialog.askinteger("Round Robin", "Enter Number of Processes:")
        
        if num_processes is not None:
            pq = deque()
            arrival = []
            burst = []
            rt = []
            
            q = time_quantum
            n = num_processes
            p = [0] * n
            for i in range(n):
                p[i] = i

            for i in range(1, num_processes + 1):
                arrival_time = simpledialog.askinteger("Round Robin", f"Enter Arrival Time for Process {i}:")
                burst_time = simpledialog.askinteger("Round Robin", f"Enter Burst Time for Process {i}:")
                
                arrival.append(arrival_time)
                burst.append(burst_time)
                rt.append(burst_time)

            c = n  
            t = 0
            ct = 0
            ct1 = [0] * n
            start_times = []
            end_times = []

            while c != 0:
                for i in range(n):
                    if t == arrival[i] and rt[i] != 0:
                        pq.appendleft(p[i])
                temp = t
                if pq:
                    sp = pq.pop()        
                else:
                    t = t + 1
                if rt[sp] <= q and rt[sp] > 0:
                    start_times.append(t)
                    t = t + rt[sp]
                    end_times.append(t)
                    rt[sp] = 0
                    ct1[sp] = t
                    c = c - 1
                elif rt[sp] > 0:
                    start_times.append(t)
                    t = t + q
                    end_times.append(t)
                    rt[sp] = rt[sp] - q
                    for i in range(n):
                        if t == arrival[i]:
                            pq.appendleft(p[i])
                    for i in range(n):
                        if arrival[i] > temp and arrival[i] < t:
                            pq.appendleft(p[i])
                    if rt[sp] > 0:
                        pq.appendleft(sp)

            
            table = PrettyTable(["Process No", "Arrival time", "Burst time", "Completion time", "Turnaround time", "Waiting time", "Turnaround to Service Time Ratio"])
            for i in range(n):
                table.add_row([i + 1, arrival[i], burst[i], ct1[i], ct1[i] - arrival[i], ct1[i] - arrival[i] - burst[i], ((ct1[i] - arrival[i]) / burst[i])])

            
            avg_turnaround_time = sum(ct1[i] - arrival[i] for i in range(n)) / n
            avg_waiting_time = sum(ct1[i] - arrival[i] - burst[i] for i in range(n)) / n

            
            result_window = tk.Toplevel(root)
            result_window.title("Round Robin Results")

            
            text_widget = tk.Text(result_window, height=20, width=140)
            text_widget.insert(tk.END, str(table) + "\n\n")
            text_widget.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")
            text_widget.insert(tk.END, f"Average Waiting Time: {avg_waiting_time:.2f}\n")
            text_widget.pack()

def fcfs_dialog():
    num_processes = simpledialog.askinteger("FCFS", "Enter Number of Processes:")

    if num_processes is not None:
        arrival = []
        burst = []
        ct1 = [0] * num_processes
        start_times = []
        end_times = []

        for i in range(1, num_processes + 1):
            arrival_time = simpledialog.askinteger("FCFS", f"Enter Arrival Time for Process {i}:")
            burst_time = simpledialog.askinteger("FCFS", f"Enter Burst Time for Process {i}:")

            arrival.append(arrival_time)
            burst.append(burst_time)

        processes = list(range(1, num_processes + 1))
        processes.sort(key=lambda x: arrival[x - 1])  # Sort processes based on arrival time

        t = 0

        for process in processes:
            start_times.append(t)
            t = max(t, arrival[process - 1])  
            t += burst[process - 1]
            end_times.append(t)
            ct1[process - 1] = t

        table = PrettyTable(["Process No", "Arrival time", "Burst time", "Completion time", "Turnaround time", "Waiting time", "Turnaround to Service Time Ratio"])
        for i in range(num_processes):
            table.add_row([i + 1, arrival[i], burst[i], ct1[i], ct1[i] - arrival[i], ct1[i] - arrival[i] - burst[i], ((ct1[i] - arrival[i]) / burst[i])])

        
        avg_turnaround_time = sum(ct1[i] - arrival[i] for i in range(num_processes)) / num_processes
        avg_waiting_time = sum(ct1[i] - arrival[i] - burst[i] for i in range(num_processes)) / num_processes

       
        result_window = tk.Toplevel(root)
        result_window.title("FCFS Results")

        
        text_widget = tk.Text(result_window, height=25, width=160)
        text_widget.insert(tk.END, str(table) + "\n\n")
        text_widget.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")
        text_widget.insert(tk.END, f"Average Waiting Time: {avg_waiting_time:.2f}\n")
        text_widget.pack()

        

    num_processes = simpledialog.askinteger("FCFS", "Enter Number of Processes:")

    if num_processes is not None:
        arrival = []
        burst = []
        ct1 = [0] * num_processes
        start_times = []
        end_times = []

        for i in range(1, num_processes + 1):
            arrival_time = simpledialog.askinteger("FCFS", f"Enter Arrival Time for Process {i}:")
            burst_time = simpledialog.askinteger("FCFS", f"Enter Burst Time for Process {i}:")

            arrival.append(arrival_time)
            burst.append(burst_time)

        t = 0
        processes = list(range(1, num_processes + 1))

        for process in processes:
            start_times.append(t)
            t += burst[process - 1]
            end_times.append(t)
            ct1[process - 1] = t

        
        table = PrettyTable(["Process No", "Arrival time", "Burst time", "Completion time", "Turnaround time", "Waiting time", "Turnaround to Service Time Ratio"])
        for i in range(num_processes):
            table.add_row([i + 1, arrival[i], burst[i], ct1[i], ct1[i] - arrival[i], ct1[i] - arrival[i] - burst[i], ((ct1[i] - arrival[i]) / burst[i])])

        
        avg_turnaround_time = sum(ct1[i] - arrival[i] for i in range(num_processes)) / num_processes
        avg_waiting_time = sum(ct1[i] - arrival[i] - burst[i] for i in range(num_processes)) / num_processes

        
        result_window = tk.Toplevel(root)
        result_window.title("FCFS Results")

      
        text_widget = tk.Text(result_window, height=25, width=160)
        text_widget.insert(tk.END, str(table) + "\n\n")
        text_widget.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")
        text_widget.insert(tk.END, f"Average Waiting Time: {avg_waiting_time:.2f}\n")
        text_widget.pack()

def shortest_process_next_dialog():
    num_processes = simpledialog.askinteger("Shortest Process Next", "Enter Number of Processes:")

    if num_processes is not None:
        arrival = []
        burst = []
        ct1 = [0] * num_processes
        start_times = []
        end_times = []

        for i in range(1, num_processes + 1):
            arrival_time = simpledialog.askinteger("Shortest Process Next", f"Enter Arrival Time for Process {i}:")
            burst_time = simpledialog.askinteger("Shortest Process Next", f"Enter Burst Time for Process {i}:")

            arrival.append(arrival_time)
            burst.append(burst_time)

        t = 0
        processes = list(range(1, num_processes + 1))

        while processes:
            eligible_processes = [p for p in processes if arrival[p-1] <= t]
            if not eligible_processes:
                t += 1
                continue

            shortest_process = min(eligible_processes, key=lambda x: burst[x-1])

            start_times.append(t)
            t += burst[shortest_process-1]
            end_times.append(t)
            ct1[shortest_process-1] = t
            processes.remove(shortest_process)

       
        table = PrettyTable(["Process No", "Arrival time", "Burst time", "Completion time", "Turnaround time", "Waiting time", "Turnaround to Service Time Ratio"])
        for i in range(num_processes):
            table.add_row([i + 1, arrival[i], burst[i], ct1[i], ct1[i] - arrival[i], ct1[i] - arrival[i] - burst[i], ((ct1[i] - arrival[i]) / burst[i])])

     
        avg_turnaround_time = sum(ct1[i] - arrival[i] for i in range(num_processes)) / num_processes
        avg_waiting_time = sum(ct1[i] - arrival[i] - burst[i] for i in range(num_processes)) / num_processes

        
        result_window = tk.Toplevel(root)
        result_window.title("Shortest Process Next Results")

        
        text_widget = tk.Text(result_window, height=25, width=160)
        text_widget.insert(tk.END, str(table) + "\n\n")
        text_widget.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")
        text_widget.insert(tk.END, f"Average Waiting Time: {avg_waiting_time:.2f}\n")
        text_widget.pack()
      

def shortest_remaining_time_dialog():
    num_processes = simpledialog.askinteger("Shortest Remaining Time First", "Enter Number of Processes:")

    if num_processes is not None:
        arrival = []
        burst = []
        ct1 = [0] * num_processes
        start_times = []
        end_times = []

        for i in range(1, num_processes + 1):
            arrival_time = simpledialog.askinteger("Shortest Remaining Time First", f"Enter Arrival Time for Process {i}:")
            burst_time = simpledialog.askinteger("Shortest Remaining Time First", f"Enter Burst Time for Process {i}:")

            arrival.append(arrival_time)
            burst.append(burst_time)

        t = 0
        processes = list(range(1, num_processes + 1))
        remaining_burst = burst.copy()

        while processes:
            eligible_processes = [p for p in processes if arrival[p - 1] <= t]
            if not eligible_processes:
                t += 1
                continue

            shortest_process = min(eligible_processes, key=lambda x: remaining_burst[x - 1])

            start_times.append(t)
            t = max(t, arrival[shortest_process - 1])  

            
            t += remaining_burst[shortest_process - 1]
            end_times.append(t)
            remaining_burst[shortest_process - 1] = 0
            ct1[shortest_process - 1] = t
            processes.remove(shortest_process)

    
        table = PrettyTable(["Process No", "Arrival time", "Burst time", "Completion time", "Turnaround time", "Waiting time", "Turnaround to Service Time Ratio"])
        for i in range(num_processes):
            turnaround_time = ct1[i] - arrival[i]
            waiting_time = turnaround_time - burst[i]
            ratio = turnaround_time / burst[i] if burst[i] != 0 else 0  # Avoid division by zero
            table.add_row([i + 1, arrival[i], burst[i], ct1[i], turnaround_time, waiting_time, ratio])


        avg_turnaround_time = sum(ct1[i] - arrival[i] for i in range(num_processes)) / num_processes
        avg_waiting_time = sum(ct1[i] - arrival[i] - burst[i] for i in range(num_processes)) / num_processes

        result_window = tk.Toplevel(root)
        result_window.title("Shortest Remaining Time First Results")


        text_widget = tk.Text(result_window, height=25, width=160)
        text_widget.insert(tk.END, str(table) + "\n\n")
        text_widget.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")
        text_widget.insert(tk.END, f"Average Waiting Time: {avg_waiting_time:.2f}\n")
        text_widget.pack()
      
        
def run_algorithm():
    selected_algorithm = algorithm_var.get()
    
    if selected_algorithm == "":
        messagebox.showwarning("Error", "Please select a processing algorithm.")
    elif selected_algorithm == "Round Robin":
        round_robin_dialog()
    elif selected_algorithm == "FCFS":
        fcfs_dialog()
    elif selected_algorithm == "Shortest Process Next":
        shortest_process_next_dialog()
    elif selected_algorithm == "Shortest Remaining Time First":
        shortest_remaining_time_dialog()


root = tk.Tk()
root.title("Processing Scheduling Application")


label = tk.Label(root, text="Select Processing Algorithm:")
label.pack()


algorithms = ["Round Robin", "FCFS", "Shortest Process Next", "Shortest Remaining Time First"]
algorithm_var = tk.StringVar(root)
algorithm_var.set("")  

algorithm_menu = tk.OptionMenu(root, algorithm_var, *algorithms)
algorithm_menu.pack()


run_button = tk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.pack()


root.mainloop()
