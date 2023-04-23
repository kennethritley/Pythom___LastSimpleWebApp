# Project Title

This is a more sophisticated Flask application. It demonstrates how you can
send data to a browser, get data back from a browser, and use style sheets.
For each of these actions you need a "route." If you want to do more sophisticated
things like use stored JavaScript, you can see how CSS is handled with a "route"
and create a similar "route" for any JS code.

## Table of Contents

- [Installation](#installation)
- [Authors](#authors)
- [License](#license)
- [CHANGELOG.md](CHANGELOG.md)


## Changelog

For a detailed list of changes and version history, please refer to the [CHANGELOG.md](CHANGELOG.md) file.

## Installation

No installation necessary. When the app runs it starts the Flask server that
listens to localhost:5000.  It should accept:

- http://127.0.0.1:5000 - Hello World
- http://127.0.0.1:5000/cat - Display the cat's name
- http://127.0.0.1:5000/cat_page - HTML page for changing cat's name and CSS
- curl -X POST -F "name=Whiskers" http://127.0.0.1:5000/cat - To change the cat's name


## Authors

Your friendly, neighborhood Dr. Ken

## License

Never operate a motor vehicle without the proper license.