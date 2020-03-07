// from data.js
var tableData = data;

//filter button
var filter_button=d3.select("#filter-btn")


// YOUR CODE HERE!


var tbody=d3.select("tbody",".table table-striped")


data.forEach((ufo) => {
    var row =tbody.append("tr");
    Object.entries(ufo).forEach(([key, value]) =>{
        var cell = row.append("td");
        cell.text(value);
    });
});

filter_button.on("click",function(){
var user_data = d3.select("#datetime");

var user_date =user_data.property("value");
console.log(user_date);
var filter_data = tableData.filter(ufo => ufo.datetime === user_date);

tbody.html("");

filter_data.forEach((ufo) => {
    var row =tbody.append("tr");
    Object.entries(ufo).forEach(([key, value]) =>{
        var cell = row.append("td");
        cell.text(value);
    });
});

});