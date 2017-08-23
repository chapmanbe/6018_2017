import os
from nose.tools import assert_equal
import stat
import shutil

def reset_mkdir():
    try:
        shutil.rmtree(os.path.join(os.path.expanduser("~"),"work","OutbreakDetection"))
    except FileNotFoundError:
        print("OutbreakDetection not created")

    try:
        shutil.rmtree(os.path.join(os.path.expanduser("~"),"OutbreakDetectionBackup"))
    except FileNotFoundError:
        print("OutbreakDetectionBackup not created")
    try:
        os.remove("home_directory.txt")
    except FileNotFoundError:
        print("home_directory.txt not created")

def ls_quiz(number_of_files, largest_file, most_recent_file):
    answers = {}
    os.chdir("/home/jovyan/DATA/Misc")
    files = os.listdir()
    answers["number_of_files"] = len(files)
    files.sort(key=os.path.getsize)
    answers["largest_file"] = files[-1]
    files.sort(key=os.path.getmtime)
    answers["most_recent_file"] = files[-1]

    try:
        assert_equal(number_of_files, answers["number_of_files"])
        print("your number of files answer is correct")
    except:
        print("your number of files answer is incorrect")
        
    try:
        assert_equal(largest_file, answers["largest_file"])
        print("your largest file answer is correct")
    except:
        print("your largest file answer is incorrect")

    try:
        assert_equal(most_recent_file, answers["most_recent_file"])
        print("your most recent answer is correct")
    except:
        print("your most recent answer is incorrect")

def mkdir_quiz():
    correct = 0

    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"),"work","OutbreakDetection")), True)
        print('OutbreakDetection created correctly')
        correct += 1
    except:
        print('OutbreakDetection NOT created correctly')
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "work", "OutbreakDetection", 
                                                "SocialMedia")), True)
        print('SocialMedia created correctly')
        correct += 1
    except:
        print('SocialMedia NOT created correctly')
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "work", "OutbreakDetection", 
                                                "SocialMedia", "Twitter")), True)
        print('Twitter created correctly')
        correct += 1
    except:
        print('Twitter NOT created correctly')
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "work", "OutbreakDetection", 
                                                "ChiefComplaints")), True)
        print('ChiefComplaints created correctly')
        correct += 1
    except:
        print('ChiefComplaints NOT created correctly')
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "work", "OutbreakDetection", 
                                                "Sales")), True)
        print('Sales created correctly')
        correct += 1
    except:
        print('Sales NOT created correctly')
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "work", "OutbreakDetection", 
                                                "Obituaries")), True)
        print('Obituaries created correctly')
        correct += 1
    except:
        print('Obituaries NOT created correctly') 
        
    print("You created %d out of 6 directories correctly"%correct)

def file_creator_quiz():
    ref_txt = """# Outbreak Detector\nThis directory contains data for developing an outbreak detector.\n"""

    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), 
                                                 "work", 
                                                 "OutbreakDetection", 
                                                 "README.md")), True)
        print("README.md created correctly")
    except:
        print("README.md NOT created correctly")
    try:
        with open(os.path.join(os.path.expanduser("~"), 
                                                 "work", 
                                                 "OutbreakDetection", 
                                                 "README.md"), 'r') as f0:
            txt = f0.read()
        assert_equal(txt, ref_txt)
        print("README.md content created correctly")
    except:
        print("README.md content NOT created correctly")
        #print("\n".join(list(difflib.ndiff(txt,ref_txt))))

def mv_quiz():
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "work", "OutbreakDetection", 
                                                "DrugSales")), True)
        print('Sales moved correctly')
    except:
        print('Sales NOT moved correctly')

def cp_quiz():
    try:
        assert_equal(os.path.exists(os.path.join(os.path.expanduser("~"), "OutbreakDetectionBackup")), True)
        print('OutbreakDetection copied correctly')
    except:
        print('OutbreakDetection NOT copied correctly')


def permissions_quiz():
    test_file = os.path.join(os.path.expanduser("~"), 
                             "work",
                             "OutbreakDetection",
                             "Obituaries",
                             "obits.txt")
    try:
        assert_equal( os.path.exists(test_file), True)
        print('obits.txt copied correctly.')
    except:
        print('obits.txt NOT copied correctly')
    try:
        mode = oct(stat.S_IMODE(os.stat(test_file).st_mode))
        assert_equal(mode, oct(0o444))
        print("obits.txt mode set correctly")
    except:
        print("obits.txt mode NOT set correctly. The mode was set to %s"%mode)


