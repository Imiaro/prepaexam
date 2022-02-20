import datetime
import time


class Task:
    def __init__(self, name, is_hard_real_time, is_interruptible, execution_time, period, priority):
        self.name = name
        self.is_hard_real_time = is_hard_real_time
        self.is_interruptible = is_interruptible
        self.execution_time = execution_time
        self.period = period
        self.priority = priority
        self.deadline = datetime.datetime.now() + datetime.timedelta(seconds=self.period)
        self.run_at = datetime.datetime.now()
        self.finished = 0

    def need_to_run(self):
        if datetime.datetime.now() >= self.run_at:
            return True
        return False

    def run(self):
        if self.is_interruptible == False:
            print("Task : " + self.name + " done")
            self.run_at = self.run_at + datetime.timedelta(seconds=self.period)
            self.deadline = self.run_at + datetime.timedelta(seconds=self.period)
            time.sleep(self.execution_time)

        else:
            print("Processing for task : " + self.name)
            self.finished += 1
            time.sleep(1)
            if datetime.datetime.now() > self.deadline:
                print("Task : " + self.name + " failed")
                self.run_at = self.run_at + datetime.timedelta(seconds=self.period)
                self.deadline = self.run_at + datetime.timedelta(seconds=self.period)
                self.finished = 0

            if self.finished == self.execution_time:
                print("Task : " + self.name + " done")
                self.run_at = self.run_at + datetime.timedelta(seconds=self.period)
                self.deadline = self.run_at + datetime.timedelta(seconds=self.period)
                self.finished = 0

if __name__ == "__main__":

    #Les tâches et ses instantiations
    task_list = [
        Task('Motor', is_hard_real_time=True, is_interruptible=False, execution_time=1, period=10, priority=4),
        Task('Sensor', is_hard_real_time=True, is_interruptible=False, execution_time=1, period=10, priority=3),
        Task('Transmission', is_hard_real_time=False, is_interruptible=True, execution_time=20, period=60, priority=2),
        Task('Camera', is_hard_real_time=False, is_interruptible=True, execution_time=20, period=30, priority=1)
    ]

    while(True):
        task_to_run = None
        priority = 0
        for current_task in task_list:
            if current_task.need_to_run():
                if current_task.priority > priority:
                    task_to_run = current_task
                    priority = current_task.priority

        task_to_run.run()