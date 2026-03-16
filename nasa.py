import requests
from flask import Flask, request, render_template

app = Flask(__name__)

API_key = #enter your own API key ---> Get it at https://api.nasa.gov/
base_url = "https://api.nasa.gov/neo/rest/v1/feed"

@app.route("/asteroids", methods=["GET", "POST"])
def asteroids():
    try:
        result = []
        
        if request.method == "POST":
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]

            params = {
                "start_date": start_date,
                "end_date": end_date,
                "api_key": API_key
            }

            response = requests.get(base_url, params=params)
            data = response.json()
        
            for date, asteroid_list in data["near_earth_objects"].items():
                for asteroid in asteroid_list:
                    result.append({
                        "name": asteroid["name"],
                        "date": date,
                        "nevaren": asteroid["is_potentially_hazardous_asteroid"]
                    })

        return render_template("asteroids.html", asteroids=result)
    
    except Exception as e:
        print(e)
        return render_template("asteroids.html", asteroids=[])

if __name__ == "__main__":
    app.run(host="192.168.64.150", port=8080, debug=True)