// from data.js
var tableData = data;


var filter_button=d3.select("#filter-btn")

var tbody=d3.select("tbody",".table table-striped")



filter_button.on("click",function(){
    var user_data_date = d3.select("#datetime");
    var user_date =user_data_date.property("value");
    user_date=user_date.trim();
    console.log(user_date);

    var user_data_city = d3.select("#city");
    var user_city =user_data_city.property("value");
    user_city=user_city.toLowerCase();
    user_city=user_city.trim();
    console.log(user_city);

    var user_data_state = d3.select("#state");
    var user_state =user_data_state.property("value");
    user_state=user_state.toLowerCase();
    user_state=user_state.trim();
    console.log(user_state);

    var user_data_country = d3.select("#country");
    var user_country =user_data_country.property("value");
    console.log(user_country);
    user_country=user_country.toLowerCase();
    user_country=user_country.trim();
    console.log(user_country);


    var user_data_shape = d3.select("#shape");
    var user_shape =user_data_shape.property("value");
    user_shape=user_shape.toLowerCase();
    user_shape=user_shape.trim();
    console.log(user_shape);

    var filter_data = tableData.filter(ufo => ufo.datetime === user_date || ufo.city === user_city || ufo.state === user_state  || ufo.country === user_country || ufo.shape === user_shape);
    
    tbody.html("");
    
    filter_data.forEach((ufo) => {
        var row =tbody.append("tr");
        Object.entries(ufo).forEach(([key, value]) =>{
            var cell = row.append("td");
            cell.text(value);
        });
    });    
});