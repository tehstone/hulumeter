// Load the stuff we need
google.load('visualization', '1.0', {'packages':['corechart']});
google.load("jquery", "1.7.1");

// Set a callback to run when the Google Visualization API is loaded.
google.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.

function getHappinessIndex() {
    response = $.ajax({
                    url: "scores",
                    dataType: "json",
                    async: false
                }).responseText
    return $.parseJSON(response)
}

function drawChart() {

  // Create the data table.
  var index = getHappinessIndex();
  var data = new google.visualization.DataTable();
  
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Happy', index.happy],
    ['Sad', index.sad],
  ]);

  // Set chart options
  var options = {'title':'How are people feeling about hulu right now?',
                 'width':'100%',
                 'height': 500};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}