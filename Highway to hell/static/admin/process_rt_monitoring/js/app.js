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
$(function() {
//'use strict';
    $(document).ready(function() {
    var startDate;
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
    function analysis(data1, data2, data3, total, rate){
        $.ajax({
            url: '/test/test_analysis/',
            method: 'POST',
            dataType: 'json',
            data: {"data1": data1, "data2" : data2, "data3" : data3, "startDate" : startDate},
            beforeSend: function () {

            },
            success: function (data) {
                /*성공시 작업 data는 return값*/
                var Data = JSON.stringify(data);
//                Data = Data.replace(/\[/gi, "");
//                Data = Data.replace(/\]/gi, "");
                Data = Data.replace(/\ /gi, "");
                Data = JSON.parse(Data);
                let section1 = Data['select'][0]['TfD'];
                var name1 = Data['select'][0]['name'];
                let section2 = Data['select'][1]['TfD'];
                var name2 = Data['select'][1]['name'];
                let section3 = Data['select'][2]['TfD'];
                var name3 = Data['select'][2]['name'];
                $('.n1')
                .append(name1);
                $('.n2')
                .append(name2);
                $('.n3')
                .append(name3);
                console.log(total);
                console.log(rate);
                console.log(JSON.stringify(startDate));
                var tDate = new Date(startDate);
                tDate.setMinutes(tDate.getMinutes() + total/6000);
                var s_D = new Date(startDate);
                $('.an_ta')
                .append("<tr>")
                .append("<td>"+s_D+"</td>")
                .append("<td>"+tDate+"</td>")
                .append("<td>"+rate/6000+"</td>")
                .append("</tr>");
                console.log(section1);
                var chart1 = c3.generate({
                    bindto: ".charts1",
                    size: {
                       height: 300
                    },
                    data: {
                        json: section1,
                        keys: {
                            x: 'index', // it's possible to specify 'x' when category axis
                            value: ['정방향', '역방향']
                        },
                        names:{
                            정방향:"정방향",
                            역방향:"역방향"
                        },
                    },
                    axis: {
                        x: {
                            type: 'category',
                            categories: ['Time']
                        },
                        y: {
                            label: { // ADD
                            text: '방향',
                            position: 'outer-middle'
                            }
                        }
                    }
                });
                var chart2 = c3.generate({
                    bindto: ".charts2",
                    size: {
                       height: 300
                    },
                    data: {
                        json: section2,
                        keys: {
                            x: 'index', // it's possible to specify 'x' when category axis
                            value: ['정방향', '역방향']
                        },
                        names:{
                            정방향:"정방향",
                            역방향:"역방향"
                        },
                    },
                    axis: {
                        x: {
                            type: 'category',
                            categories: ['Time']
                        },
                        y: {
                            label: { // ADD
                            text: '방향',
                            position: 'outer-middle'
                            }
                        }
                    }
                });
                var chart3 = c3.generate({
                    bindto: ".charts3",
                    size: {
                       height: 300
                    },
                    data: {
                        json: section3,
                        keys: {
                            x: 'index', // it's possible to specify 'x' when category axis
                            value: ['정방향', '역방향']
                        },
                        names:{
                            정방향:"정방향",
                            역방향:"역방향"
                        },
                    },
                    axis: {
                        x: {
                            type: 'category',
                            categories: ['Time']
                        },
                        y: {
                            label: { // ADD
                            text: '방향',
                            position: 'outer-middle'
                            }
                        }
                    }
                });
            }
        });
    }
    function realize(P1x, P2x, P3x, P4x){
            $.ajax({
                url: '/test/test_visualize/',
                method: 'POST',
                dataType: 'json',
                data: {"place1X":P1x, "place1Y":P2x, "place2X":P3x, "place2Y":P4x},
                beforeSend: function () {
                },
                success: function (data) {
                    var Data = JSON.parse(data['data']);
                    let section = Data['route']['trafast'][0]['section'];
                    let guide = Data['route']['trafast'][0]['guide'];
                    var distance_time = 0;
                    check_point = new Array;
                    var check_count = 0 ;
                    var count = 0;
                    var total_time = 0;
                    for(i=0; i < guide.length; i++)
                    {
                        total_time = total_time + guide[i]['duration'];
                        if(guide[i]['type'] == 47 || guide[i]['type'] == 50 || guide[i]['type'] == 51
                           || guide[i]['type'] == 57 || guide[i]['type'] == 58 || guide[i]['type'] == 66 ||
                            guide[i]['type'] == 67 || guide[i]['type'] == 121 || guide[i]['type'] == 122 ||
                            guide[i]['type'] == 123){
                            check_point.push(1);
                            count++;
                        }else{
                            check_point.push(0);
                        }
                    }
                    total_time = total_time;
                    var start_max = 0;
                    var end_max = 0;
                    for(i=0; i< guide.length; i++){
                        if (check_point[i] == 1){
                            check_count += 1;
                            if (check_count == 1){
                                distance_time += start_max;
                            }
                        }else{
                            if(check_count != count){
                                start_max += guide[i]["duration"];
                            }
                            else{
                                end_max += guide[i]["duration"];
                            }
                        }
                    }
                    distance_time += end_max;
                    analysis(section[0]['name'], section[1]['name'], section[2]['name'], total_time, distance_time);
                }
            });
    }
    setInterval(update, 1000);
    $('#startDate').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',
        defaultDate: moment()
    });
    $('#process').click(function(e) {
        var StartDate=$("#txtStartDate").val();
        var start_point=$("#start_point").val();
        var finish_point=$("#finish_point").val();
        $.ajax({
            url: '/test/test_send/',
            method: 'POST',
            dataType: 'json',
            data: {"StartDate":StartDate, "start_point":start_point, "finish_point":finish_point},
            beforeSend: function () {
            },
            success: function (data) {
                var Data1 = JSON.parse(data['data1']);
                var Data2 = JSON.parse(data['data2']);
                var place1X = Data1['places'][0]['x'];
                var place1Y = Data1['places'][0]['y'];
                var AllPlace = Data1['places']
                var place2X = Data2['places'][0]['x'];
                var place2Y = Data2['places'][0]['y'];
                startDate = data['startDate'];
                realize(place1X, place1Y, place2X, place2Y);
            }
        });
    });
});