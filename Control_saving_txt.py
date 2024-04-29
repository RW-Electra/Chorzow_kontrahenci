import sql_database_functions as sql
import File_copy_and_deleting as Fc
import Text_functions as Txt

error_bool = False
errors = [False, False]
proccess_done = False


def get_error():
    return error_bool, errors, copy_correct


def ready_to_update():
    return proccess_done


def reset_proccess():
    global proccess_done
    proccess_done = False


def File_to_database(path, filename, library, tablename):
    global errors
    global error_bool
    global start_time
    global copy_correct
    global proccess_done
    copy_correct = Fc.copy_file(filename, path)
    if copy_correct:
        buyer_segment = Txt.Find_buyerID_switch_command()
        Buyer_connections = Txt.Switch_command_to_pairs(buyer_segment)
        error_bool = sql.Update_data_in_database(Buyer_connections, library, tablename)
        errors = sql.get_errors()
    proccess_done = True
    return
