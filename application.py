############## Seyhan Van Khan
############## Sort & Search
############## Execute & present the complexity of different sorting & searching algorithms
############## January 2018

################################### CONSTANTS ##################################


# Allowed file types
# Key: file extension
# Definition: what seperates values in file to form a list
ALLOWED_EXTENSIONS = {'txt':'\n', 'csv':','}
DATA_INPUT_FILENAME = 'dataFile'


################################### LIBRARIES ##################################


from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from data import *
from search import *
from sort import *


##################################### INIT #####################################


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()


############################### INPUT NUMBER DATA ##############################


# Checks if given file is valid & in ALLOWED_EXTENSIONS
# Returns its extension if valid, else returns NONE
def valid_file_extension(filename):
    if ('.' in filename
            and filename[filename.index('.') + 1:].lower() in ALLOWED_EXTENSIONS.keys()
        ):
        return filename[filename.index('.') + 1:]

    else:
        return None

# Gets input from form to create a list of numbers / strings
# Returns the list of values
# If successful
### Returns True & the list of values
# Else
### Returns False & HTML template for failure
def InputData(request):
    # Randomly generated list
    if request.form['getNumberMethod'] == 'random':
        try:
            num_numbers = int(request.form.get("num_numbers"))
            minimum = int(request.form.get("minimum"))
            maximum = int(request.form.get("maximum"))
        except:
            return False, render_template("failure.html",
                apology="All 3 fields of random list generator must be filled with integers")
        if maximum <= minimum:
            return False, render_template("failure.html",
                apology="Maximum must be bigger than minimum.")

        numbers = RandomList(num_numbers, minimum, maximum)

    # Use given file to create list
    else:
        try:
            file = request.files[DATA_INPUT_FILENAME]
        except:
            return False, render_template("failure.html",
                apology="No file found")

        if not file.filename:
            return False, render_template("failure.html",
                apology="No selected file")

        data_fileExtension = valid_file_extension(file.filename)
        if not data_fileExtension:
            return False, render_template("failure.html",
                apology="File is in invalid format")

        # Sanitise file input
        data_filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
        # Save file in local directory
        file.save(filepath)
        # Open file in read mode
        data_file = open(filepath).read()
        # Split file by certain seperators into values
        numbers = data_file.split(ALLOWED_EXTENSIONS[data_fileExtension])
        # Remove any empty values in list
        numbers = [n for n in numbers if n]


    return True, numbers


################################## HOME PAGE ###################################


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        # If user clicks Search button on navbar
        if request.form['action'] == 'search':
            return render_template("search.html")
        # If user clicks Sort button on navbar
        elif request.form['action'] == 'sort':
            return render_template("sort.html")
    # If user gets homepage or clicks Sort N Search button on navbar
    return render_template("index.html")


################################### SEARCH PAGE ##################################


@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "POST":
        successful, numbers = InputData(request)
        if not successful:
            return numbers

        searchType = request.form["search method"]

        if not searchType:
            return render_template("failure.html",
                apology="Input search method")

        # Binary sort requires list to already be in ascending order
        if searchType == "Binary":
            numbers = sorted(numbers)


        wanted = request.form.get("wanted")
        if request.form['getNumberMethod'] == 'random':
            try:
                wanted = int(wanted)
            except:
                return render_template("failure.html",
                    apology="Enter integer to be searched")

        elif not wanted:
            return render_template("failure.html",
                apology="Enter a string to be searched")

        # Find function from key searchType in searchMethods to perform search algorithm
        found, steps, time = searchMethods[searchType](numbers, wanted)

        return render_template("searched.html",
                                searchMethod=searchType,
                                wanted=wanted,
                                found="Yes" if found else "No",
                                listLength=FormatNum(len(numbers), int),
                                best_steps=bigOmega[searchType]["function"](len(numbers)),
                                steps=FormatNum(steps, int),
                                worst_steps=bigO[searchType]["function"](len(numbers)),
                                time=time,
                                best=bigOmega[searchType]["text"],
                                worst=bigO[searchType]["text"],
                                entireList=numbers)

    else:
        return render_template("search.html")


################################### SORT PAGE ##################################


@app.route("/sort", methods=["GET","POST"])
def sort():
    if request.method == "POST":
        successful, numbers = InputData(request)
        if not successful:
            return numbers

        sortType = request.form["sort method"]
        if not sortType:
            return render_template("failure.html",
                apology="Input sort method")

        # Determine order. If unspecified, set to default: ASCENDING
        order = request.form["order"]
        if not order:
            order = "ASC"

        # Find function from key sortType in sortMethods to perform sort algorithm
        numbers, steps, time = sortMethods[sortType](numbers, order)

        return render_template("sorted.html",
                                sortMethod=sortType,
                                order="Ascending" if order == "ASC" else "Descending",
                                listLength=FormatNum(len(numbers), int),
                                best_steps=bigOmega[sortType]["function"](len(numbers)),
                                steps=FormatNum(steps, int),
                                worst_steps=bigO[sortType]["function"](len(numbers)),
                                time=time,
                                best=bigOmega[sortType]["text"],
                                worst=bigO[sortType]["text"],
                                entireList=numbers)


    else:
        return render_template("sort.html")
    
if __name__ == "__main__":
    app.run(debug=True)
