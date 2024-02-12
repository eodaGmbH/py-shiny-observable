function _1(md){return(
md`# Playground`
)}

function _chartist(require){return(
require("chartist@1.3.0")
)}

function _h3(require){return(
require("h3-js@4.1.0")
)}

function _data(){return(
[{letter: "A", frequency:0.6}, {letter: "B", frequency:0.3}, {letter: "C", frequency:0.8}]
)}

function _5(h3){return(
h3.latLngToCell(20, 123, 2)
)}

function _echarts(require){return(
require("echarts@5.4.3")
)}

function* _echart(htl,echarts,chartData,lineColor)
{
  const container = htl.html`<div style="height:450px;">`;
  yield container;
  
  const ec = echarts.init(container, "dark");
  const option = {
    title: {text: "Awesome chart", "x": "right"},
    legend: {},
    tooltip: {trigger: "axis"},
    xAxis: {
      data: chartData.x
    },
    yAxis: {},
    series: [
          {
            name: 'sales',
            type: 'bar',
            data: chartData.y
          },
          {
            name: 'sales line',
            type: 'line',
            data: chartData.y,
            color: lineColor
          }
        ]
  };
  ec.setOption(option);
}


function _chartData()
{
  return {
    x: ['Shirts', 'Cardigans', 'Chiffons', 'Pants', 'Heels', 'Socks'],
    y: [5, 20, 36, 10, 10, 20]
  }
}


function _lineColor(){return(
"yellow"
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  main.variable(observer()).define(["md"], _1);
  main.variable(observer("chartist")).define("chartist", ["require"], _chartist);
  main.variable(observer("h3")).define("h3", ["require"], _h3);
  main.variable(observer("data")).define("data", _data);
  main.variable(observer()).define(["h3"], _5);
  main.variable(observer("echarts")).define("echarts", ["require"], _echarts);
  main.variable(observer("viewof echart")).define("viewof echart", ["htl","echarts","chartData","lineColor"], _echart);
  main.variable(observer("echart")).define("echart", ["Generators", "viewof echart"], (G, _) => G.input(_));
  main.variable(observer("chartData")).define("chartData", _chartData);
  main.variable(observer("lineColor")).define("lineColor", _lineColor);
  return main;
}
