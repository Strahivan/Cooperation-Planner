# Cooperation Planner
This application reads in a large list of domains/urls and lets you filter them

## Header und File Structure

For the CSV file to be accepted by the program, the CSV file must look like this in the header: reach, url, statuscode, globalrank
You can also add more elements, but the application doesn't take these values into account, it only takes the upper 4 and generates TLDs.
CSV must have the header in the first line with the corresponding data fields.

## How to create a PyInstaller Package:

### Unix/Mac (note the four leading slashes)
sqlite:////absolute/path/to/foo.db
#Windows (note 3 leading forward slashes and backslash escapes)
sqlite:///C:\\absolute\\path\\to\\foo.db

### Windows:
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" main.py

### Linux:
pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" --add-data "tld/res:tld/res" --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py
