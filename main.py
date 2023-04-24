from db import DBClass
import cmds


def main():
    db = DBClass()
    db.firstTimeSetup()
    print('DB is ready')

    cmds.letsBegin(db)
    


if __name__ == "__main__":
    main()