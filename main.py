from flask import Flask, request, render_template
import os
from fit_model import train_model

app = Flask(__name__)
model = train_model()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       popularity = float(request.form.get("popularity"))
       duration_ms = float(request.form.get("duration_ms"))
       acoustic = float(request.form.get("acoustic"))
       energy = float(request.form.get("energy"))
       instrumentalness = float(request.form.get("instrumentalness"))
       liveness = float(request.form.get("liveness"))
       loudness = float(request.form.get("loudness"))
       speechiness = float(request.form.get("speechiness"))
       tempo = float(request.form.get("tempo"))
       audio_valence = float(request.form.get("audio_valence"))

       pred_list = [popularity, duration_ms, acoustic, energy, instrumentalness, liveness, loudness, speechiness, tempo, audio_valence]
       print("PREDICTION LIST:")
       print(pred_list)
       danceability = model.predict([pred_list])[0] * 100

       return "Your danceability score is: " + str(danceability) + "/100"
    return render_template("ml.html")

# action_page.php?popularity=0.256&duration_ms=0.5&acoustic=0.2&energy=0.5&instrumentalness=0.5&liveness=0.5&loudness=0.7&speechiness=0.5&tempo=0.5&audio_valence=0.5



host = 'localhost' # '0.0.0.0' #"127.0.0.1" # I tried all of these ip's

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8080)) # I also tried port was 5000
    app.run(host='0.0.0.0', port=8080, debug=True)