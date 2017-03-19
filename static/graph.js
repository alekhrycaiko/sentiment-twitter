/*
    Primary graph.
    Should read in two streams of data, and produce an interactable graph based on the hot pick of the day.
 */
/*
 historic   tweets
 sentament for tweets
 stock price for each tweets
 correlation for each tweets
 confidence interval for tweets.
  */


// Correlation.
// Stock price?

$(document).ready(function () {
var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  type: 'scatter'
};

var trace2 = {
  x: [1, 2, 3, 4],
  y: [16, 5, 11, 9],
  type: 'scatter'
};

var data = [trace1, trace2];

Plotly.newPlot('evil-plot-div', data);
});