from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/oranges')
def lemons():
    title = "My Ice Cream Form"
    options = ["vanilla", "strawberry", "chocolate", "mint chip", "cherry", "fudge"]
    title_var = "A cool ice cream flavor app"
    # Add code -- what type should options hold?
    return render_template('seeform.html',title=title_var, lst_stuff=options)

@app.route('/apples', method = ['GET'])
def plants():
    ## Add code here
    if request.method == 'GET'
        name = request.args.get('name', 'not found') #.args is essentially the dictionary response from the form request.
        name_len = len(name)
        flavor_options = []
        for x in request.args:
            if x != 'name':
                flavor_options.append(request.args.get(x))

    return render_template('results.html',flavors=flavor_options, name_len=name_len, name=name)


if __name__ == "__main__":
    app.run(debug=True)
