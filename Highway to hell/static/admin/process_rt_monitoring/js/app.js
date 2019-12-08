
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
    function analysis(Data, startDate){
        $.ajax({
            url: '/test/test_analysis/',
            method: 'POST',
            dataType: 'json',
            data: {"data": Data, "startDate0" : startDate},
            beforeSend: function () {

            },
            success: function (data) {
                /*성공시 작업 data는 return값*/




            }
        });
    }
    function realize(P1x, P2x, P3x, P4x){
//        playAlert = setInterval(function () {
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


                    console.log(section);
                    console.log(guide);
                    analysis(Data, startDate);
                    console.log(Data['route']['trafast'][0]['path']);


                }
            });
//        },5000);
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
                realize(place1X, place1Y, place2X, place2Y)

            }
        });
    });
});
