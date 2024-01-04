import html
from flask import Flask, render_template, request, escape

app = Flask(__name__)

def search4vowels4(phrase:str, letters:str='aeiou') -> set:
    """ return a set of the 'letters' found in the 'phrase'  """
    return set(letters).intersection(set(phrase))

def log_request(req: str, res: str) -> None:
    with open('vsearch.log', 'a') as log :
        print(req, res, file=log)

def log_request(req: str, res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
        contents = log.readlines()
    return escape(''.join(contents))      

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4String', methods=['POST'])
def do_search() -> str:
    return str(search4vowels4('life, the universe, and everything', 'eiru,!'))

@app.route('/search4HTMLString', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4vowels4(phrase, letters))

    """ add the request and results to the log  """
    log_request(request, results)

    return render_template('results.html',
    the_title=title,
    the_phrase=phrase,
    the_letters=letters,
    the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':
   return render_template('request.html', the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


# app.run()

if __name__ == '__main__':
    app.run(debug=True)


