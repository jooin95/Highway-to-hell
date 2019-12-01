
let selectedVariables = [];
let selectedLine = {};
let selectedMachine = {};
let selectedProcess = {};
let selectedProduct = {};
let lastUslLsls = {};
let count = 30;
let time = 1;
let frequency = 5; //sec
let intervals = {};
let countOptions = [
    {
        value: 30,
        text: "30 개"
    },
    {
        value: 50,
        text: "50 개"
    },
    {
        value: 100,
        text: "100 개"
    },
    {
        value: 200,
        text: "200 개"
    },
    {
        value: 500,
        text: "500 개"
    }
];
let timeOptions = [
    {
        value: 1,
        text: "1 시간"
    },
    {
        value: 2,
        text: "2 시간"
    },
    {
        value: 3,
        text: "3 시간"
    },
    {
        value: 4,
        text: "4 시간"
    }
];
$(function() {
//'use strict';
  $(document).ready(function() {
    if ($('#formTest').length) {
      var waitingAjax = false;
      var $graphArea = $('#graphArea');
      var $test = $('.test');
      var $alert = $graphArea.find('.alert-danger');
      var $charts = $graphArea.find('.charts');
      var $alert2 = $('#formTest').find('.alert-warning');
      var $alertMessage = $alert2.find('.message');

      $('#formTest').on('submit', function(e) {
        e.preventDefault();
        const form = $(this);
        const url = form.attr('action');

        const drStart = form.find('#drStart').val();
        const drEnd = form.find('#drEnd').val();

        if (!waitingAjax) {
          $.ajax({
            url: url,
            method: 'POST',
            dataType: 'html',
            data: form.serialize(),
            success: function(data) {
              $charts.append(data);
            },
            error: function(err) {
              $alert.text(err.responseText);
              $alert.show();
            },
            complete: function() {
              $graphArea.show();
              setTimeout(function() {
                waitingAjax = false;
              }, 2000);
            }
          });
        }
      });
    }
  });
  function update() {
        $('#current_time').html(moment().format('YYYY년 MM월 DD일 HH시 mm분 ss초'));

  }
  setInterval(update, 1000);
  $('#startDate').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        defaultDate: '2019-11-01 23:59:50'
  });
  $('#process').click(function(e) {

            playAlert = setInterval(function () {
                var StartDate=$("#txtStartDate").val();
                var start_point=$("#start_point").val();
                var finish_point=$("#finish_point").val();
                $.ajax({
                    url: '/vis/test_send/',
                    method: 'POST',
                    dataType: 'json',
                    data: {"StartDate":StartDate, "start_point":start_point, "finish_point":finish_point},
                    beforeSend: function () {
                    },
                    success: function (data) {

                        var sel_Data = data['Sel_list'];
                        console.log(data['Sel_list'].startDate);

                    }
                });
            },5000);
        });
});
async function initGraph(_data, id, Sel_data, title) {

    let lastWorkpiece = null;
    let data = [];
    let data1 = [];
    var al_max = 1000;
    var al_min =0
    var col_rag = 100;
    _data.forEach(function (d) {
        let date = moment(d["GetTime"], "YYYY-MM-DD HH:mm:ss").toDate();
        data.push({

                date:  date.getTime(),
                readData: d[title] // My data
         });
        data1.push(d[title]);

     });
    if(title != "Ampere" && title != "CastSpeed")
       col_rag = 10;
    else if(title == "CastSpeed")
        col_rag = 3;
    else
        col_rag = 100;
    console.log(Math.max.apply(null, data1));
    al_max = Math.max.apply(null, data1) + col_rag;
    if(Math.min.apply(null, data1) > col_rag)
        al_min = Math.min.apply(null, data1) - col_rag;
    else
        al_min = 0;

//    for(var i = 0; i < data.length; i++){
//        let date = moment(d["GetTime"], "YYYY-MM-DDTHH:mm:ss").toDate();
//        console.log(data[i]);
//        console.log(data[i].getTime)
//        data.push({
//
//                date:  date[i].getTime(),
//                readData: date[i].Ampere // My data
//         });
//     }
//    _data.forEach(function (d) {
//
//        data.push({
//            date:  d["GetTime"],
//            readData: d["ElePower"] // My data
//        });
//
//        console.log("data = ",data);
//        lastWorkpiece = d;//Don't need
//    });



    // Set the dimensions of the canvas / graph
    let margin = {top: 40, right: 20, bottom: 40, left: 60},
        width = $('#testing').width() - margin.left - margin.right,
        height = $('#testing').height() - margin.top - margin.bottom;


    // Set the ranges
    var x = d3.time.scale().range([0, width]);
    var y = d3.scale.linear().range([height, 0]);

    // Define the axes
    var xAxis = d3.svg.axis().scale(x)
        .orient("bottom").ticks(5);

    var yAxis = d3.svg.axis().scale(y)
        .orient("left").ticks(5);

    // Define the line
   var valueline = d3.svg.line()
        .x(function (d) {
            return x(d.date);
        })
        .y(function (d) {
            return y(d.readData);
        });


    let isSLAvailable = true;

    // Adds the svg canvas
    var svg = d3.select('#testing')
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Scale the range of the data
//    x.domain([d3.min(data, function (d) {
//        return d.date;
//    }), new Date().getTime()]);
        x.domain(d3.extent(data.map(function(d) { return d.date; })));


//     if (isSLAvailable){
         y.domain([Math.min(al_min, d3.min(data, function (d) {
            return d.readData;
        })), Math.max(al_max, d3.max(data, function (d) {
            return d.readData;
        }))]);
//        y.domain([0, 300]);
//     } else {
//         y.domain(d3.extent(data, function (d) {
//             return d.readData;
//         }));
//     }


    // Add the valueline path.

    svg.append("path")
        .attr("class", "line")
        .attr("stroke-width", 10)
        .attr("d", valueline(data));

    // draw the scatterplot
    svg.selectAll("dot")
        .data(data)
        .enter().append("circle")
        .attr("r", 3)
        .attr("cx", function (d) {
            return x(d.date);
        })
        .attr("cy", function (d) {
            return y(d.readData);
        })
        .style("fill", function (d) {
            if (isSLAvailable){
                if (d.readData > 0 || d.readData < 200000){
                    return "#ff0000";
                } else {
                    return "#00ff00";
                }
            } else {
                if (d.state === "NG")
                    return "#ff0000";
                if (d.state === "OK")
                    return "#00ff00";
            }
            return "#000000";
        })
        // Tooltip stuff after this
        .on("mouseover", function (d) {
            d3.select("#tooltip").transition()
                .duration(500)
                .style("opacity", 0);
            d3.select("#tooltip").transition()
                .duration(200)
                .style("opacity", .9);
            d3.select("#tooltip").html(
                moment(d.date).format("YYYY MMM DD hh:mm a") +
                "<br/>" +
                "Read data: " + d.readData
               )
                .style("left", (d3.event.pageX - $(".content").position().left - 180) + "px")
                .style("top", (d3.event.pageY - $(".content").position().top - 28) + "px");
        })
        .on("mouseleave", function (d) {
            d3.select("#tooltip").transition()
                .style("opacity", 0);
        });

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("y", -15)
        .attr("dy", ".71em")
        .text(title);

    //if (isSLAvailable) {
//         svg.append('line')
//            .attr('x1', 0)
//            .attr('y1', y(data.readData))
//            .attr('stroke', 'red');
//        svg.append('line')
//            .attr('x1', 0)
//            .attr('y1', y(data.readData))
//            .attr('x2', width)
//            .attr('y2', y(data.readData))
//            .attr('stroke', 'red');
    //}

}
