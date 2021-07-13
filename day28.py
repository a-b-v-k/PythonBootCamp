import threading
from datetime import datetime, date, timedelta


class sub_thread(threading.Thread):
    def run(self):
        super().run()


def print_date():
    dt = date.today() - timedelta(5)
    print('Current Date :',date.today())


st = sub_thread(target=print_date, name='sub thread')

st.start()

st.join()


