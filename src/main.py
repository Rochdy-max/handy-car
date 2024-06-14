import sys
from MainApp import MainApp

if __name__ == "__main__":
    app = MainApp()
    sys.exit(app.main(sys.argv))