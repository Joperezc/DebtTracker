import os
import firstUse
import CreateDB
def main():
    if(os.path.exists("test.db")):
        firstUse.main()
    else:
        CreateDB.main()
        firstUse.main()
    
main()