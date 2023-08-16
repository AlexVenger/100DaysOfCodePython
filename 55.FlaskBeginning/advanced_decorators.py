from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"
    return bold


def make_emphasis(function):
    def emphasise():
        return f"<em>{function()}</em>"
    return emphasise


def make_underlined(function):
    def underline():
        return f"<u>{function()}</u>"
    return underline


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
