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
});
