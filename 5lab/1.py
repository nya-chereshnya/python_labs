from enum import Enum
import tkinter as tk
from tkinter import messagebox


class Properties(Enum):
    prop0 = 'Are you ready to work full time?'
    prop1 = 'Are you ready to work remotely?'
    prop2 = 'do you have a driving license?'
    prop3 = 'Are you ready to work on a fixed schedule?'
    # prop4 = 'education'
    # prop5 = 'work experience'


class Prop:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Candidate:
    def __init__(self, name, props):
        self.name = name
        self.props = props

    def get_props(self):
        return self.props


class Firm:
    def __init__(self, name, props):
        self.name = name
        self.props = props

    def get_rank(self, candidate):
        rank = 0
        for i in range(len(Properties)):
            if candidate.get_props()[i].value == self.props[i].value:
                rank += 1
        return rank

    def get_props(self):
        return [prop for prop in self.props]


class Firms:
    def __init__(self, firms, candidates):
        self.firms = firms
        self.candidates = candidates

    def get_candidate_ranks(self, candidate):
        ranks_dict = {}
        for firm in self.firms:
            ranks_dict[firm.name] = firm.get_rank(candidate)
        return ranks_dict

    def get_top_ranks(self):
        top_ranks = dict()
        for firm in self.firms:
            firmName = firm.name
            top_ranks[firmName] = []
            for candidate in self.candidates:
                top_ranks[firmName].append(
                    {candidate.name: firm.get_rank(candidate)})
        return (top_ranks)


candidate1_props = [
    Prop(Properties.prop0, 60000),
    Prop(Properties.prop1, False),
    Prop(Properties.prop2, True),
    Prop(Properties.prop2, True)
]

candidate1 = Candidate('Vasya', candidate1_props)

candidate2_props = [
    Prop(Properties.prop0, 50000),
    Prop(Properties.prop1, False),
    Prop(Properties.prop2, False),
    Prop(Properties.prop2, True)
]

candidate2 = Candidate('Oleg', candidate2_props)

firm1_props = [
    Prop(Properties.prop0, 80000),
    Prop(Properties.prop1, True),
    Prop(Properties.prop2, False),
    Prop(Properties.prop2, True),
]

firm2_props = [
    Prop(Properties.prop0, 30000),
    Prop(Properties.prop1, False),
    Prop(Properties.prop2, True),
    Prop(Properties.prop2, False),
]

firms = [
    Firm('firmName1', firm1_props),
    Firm('firmName2', firm2_props)
]

candidates = [Candidate('Dima', candidate1_props),
              Candidate('Sasha', candidate2_props)]

firms_obj = Firms(firms, candidates)
# ranks = firms_obj.get_top_ranks()


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.firms = []
        self.candidates = []

        self.candidate_button = tk.Button(
            master, text="Candidate: Get tested", command=self.open_candidate_form)
        self.candidate_button.pack(pady=10, padx=5)

        self.firm_button = tk.Button(
            master, text="Firm: Create form", command=self.open_firm_form)
        self.firm_button.pack(pady=10)
        self.candidate_search = tk.Entry(self.master)
        self.label_input_candidate_name = tk.Label(
            master, text="enter the name of \nthe candidate\n to show his results")
        self.label_input_candidate_name.pack()
        self.candidate_search.pack(pady=10)
        self.show_results = tk.Button(
            master, text="Show results", command=self.show_ranks)
        self.show_results.pack(pady=10)

    def show_ranks(self):
        found = False
        for candidate in self.candidates:
            if candidate.name == self.candidate_search.get():
                found = candidate
                break
        if found == False:
            self.show_error()
            return
        self.ranks = tk.Toplevel(self.master)

        candidate_top_firms_dict = Firms(
            self.firms, self.candidates).get_candidate_ranks(candidate)
        candidate_top_firms_text = ""

        for key, value in candidate_top_firms_dict.items():
            candidate_top_firms_text += (key + ": " + str(value)) + "\n"

        self.candidate_top_firms = tk.Label(
            self.ranks, text=candidate_top_firms_text)
        self.candidate_top_firms.pack()
        data = Firms(
            self.firms, self.candidates).get_top_ranks()

        for firm, candidates in data.items():
            firm_label = tk.Label(self.ranks, text=f"{firm}:\n")
            firm_label.pack()
            for candidate in candidates:
                candidate_label = tk.Label(
                    self.ranks, text=f" - {list(candidate.keys())[0]}: {list(candidate.values())[0]}")
                candidate_label.pack()

        self.candidate_top_firms.pack()

    def show_error(self):
        messagebox.showerror("Error", "error")

    def open_candidate_form(self):
        self.form_candidate_window = tk.Toplevel(self.master)
        self.candidate_name_entry = tk.Entry(self.form_candidate_window)
        self.candidate_name_entry.grid(row=0, column=0)

        self.candidate_props = []
        for i, prop in enumerate(Properties):
            prop_name = prop.value
            prop_var = tk.IntVar()

            prop_label = tk.Label(self.form_candidate_window, text=prop_name)
            prop_label.grid(row=i+1, column=0, sticky='w')

            prop_checkbox = tk.Checkbutton(
                self.form_candidate_window, variable=prop_var)
            prop_checkbox.grid(row=i+1, column=1, sticky='e')

            self.candidate_props.append(Prop(prop_name, prop_var))

        self.candidate_submit_button = tk.Button(
            self.form_candidate_window, text='Submit', command=self.submit_candidate_form)
        self.candidate_submit_button.grid(row=len(Properties)+1, column=0)

    def submit_candidate_form(self):
        self.candidate_props = self.__export_props_values(self.candidate_props)
        self.candidates.append(
            Candidate(self.candidate_name_entry.get(), self.candidate_props))
        print([i.name for i in self.candidates])
        self.form_candidate_window.destroy()

    def open_firm_form(self):
        self.form_redactor_window = tk.Toplevel(self.master)
        self.firm_name_entry = tk.Entry(self.form_redactor_window)
        self.firm_name_entry.grid(row=0, column=0)

        self.firm_props = []
        for i, prop in enumerate(Properties):
            prop_name = prop.value
            prop_var = tk.IntVar()

            prop_label = tk.Label(self.form_redactor_window, text=prop_name)
            prop_label.grid(row=i+1, column=0, sticky='w')

            prop_checkbox = tk.Checkbutton(
                self.form_redactor_window, variable=prop_var)
            prop_checkbox.grid(row=i+1, column=1, sticky='e')

            self.firm_props.append(Prop(prop_name, prop_var))

        self.firm_submit_button = tk.Button(
            self.form_redactor_window, text='Submit', command=self.submit_firm_form)
        self.firm_submit_button.grid(row=len(Properties)+1, column=0)

    def submit_firm_form(self):
        self.firm_props = self.__export_props_values(self.firm_props)
        self.firms.append(Firm(self.firm_name_entry.get(), self.firm_props))
        self.form_redactor_window.destroy()

    def __export_props_values(self, data):
        for i in range(len(data)):
            data[i].value = data[i].value.get()
        return data


root = tk.Tk()
gui = MainWindow(root)
root.mainloop()
