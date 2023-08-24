from src.logger import logging
from flask import Flask, request, render_template, jsonify
from src.pipeline.predection_pipeline import CustomData, PredictPipeline
from src.pipeline.training_pipeline import TrainingPipeline

application = Flask(__name__, template_folder="templets")
app = application


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
def model_training():
    logging.info("Home page accessed and data training started!!")
    start_training = TrainingPipeline()
    start_training.iniciate_training_pipeline()
    return jsonify("Training Completed")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")

    else:
        data = CustomData(
            carat=float(request.form.get("carat")),
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            cut=request.form.get("cut"),
            color=request.form.get("color"),
            clarity=request.form.get("clarity"),
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0], 2)

        return render_template("results.html", final_result=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
