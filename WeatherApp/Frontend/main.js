function getWeather(){
    var data = document.getElementById("data").value
    eel.find_city_weather("This is eel")(function(ret){console.log(ret)})
}