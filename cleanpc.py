import os
import shutil
import winshell
import sys

def cleanup(dst):
    user = os.getlogin()
    # Cleans the Recycle Bin

    if dst == 'Recycle Bin':
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        except:
            print('\nAlready empty')

    
    # Cleans the Downloads folder

    elif dst == 'Downloads':
        os.chdir(f"C:\\Users\\{user}\Downloads")
        list_of_files = os.listdir(f"C:\\Users\\{user}\\Downloads")
        for file in list_of_files:
            try:
                os.remove(file)
            except PermissionError:
                shutil.rmtree(file)
        print('\nAll done')
    
    # Cleans Both

    elif dst == 'Both':

        # Cleans the Recycle Bin

        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        except:
            print('\nRecycle bin is already empty')
        
        # Cleans the Downloads folder

        os.chdir(f"C:\\Users\\{user}\\Downloads")
        list_of_download_files = os.listdir(f"C:\\Users\\{user}\\Downloads")
        for file in list_of_download_files:
            try:
                os.remove(file)
            except PermissionError:
                shutil.rmtree(file)
        print('\nAll done')




def main():

    # Asks the user their option to clear which folder 

    print('What would you like to clean today?\n')
    print('Downloads, Recycle Bin, or Both')
    print()
    choice = input().title()

    # Asks they want to continue
    
    print()
    print(f'Are you sure you want to clean {choice}?\n\nYes or No')
    print()
    final_answer = input().title()
    print()

    # Lets user input their choice if they fail to input a valid option 

    while choice != 'Recycle Bin' and choice != 'Downloads' and choice != 'Both':
        choice = input('Please choose valid option: ').title()
    
    # Lets user input their choice if they fail to put "Yes" or "No"
    if final_answer == 'No':
        print('Program Terminated')
        sys.exit()

    while final_answer != 'No' and final_answer != 'Yes':
        final_answer = input('Please choose valid option: ').title()

    cleanup(choice)

main()








