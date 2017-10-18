from flask import Flask, request, render_template, redirect

from formulas import carga_electrica

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Practice U2')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    i = float(request.form['I'])
    t = float(request.form['T'])
    title = 'El resultado de la funcion son:'
    result = float(carga_electrica(i, t))
    return render_template('result.html',
                           the_title=title,
                           the_i=i,
                           the_t=t,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)