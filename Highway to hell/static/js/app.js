
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
        format: 'YYYY-MM-DD HH:mm:ss'
        //defaultDate: '2019-12-01 0:59:50'
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

                }
            });
        },5000);
    });
});