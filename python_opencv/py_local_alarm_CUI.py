import process_select


PROCNAME = process_select.PROCNAME
win_text = []
for i in process_select.get_processes(PROCNAME):
    try:
        process_select.get_hwnds(process_select.get_hwnds(i.pid)[0])
    except IndexError:
        pass


#hwnd = process_select.get_hwnds(pid)[0]
#client = input("select client : ")
