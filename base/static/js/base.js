$(function () {
    $('.btn-add').click(function () {
        var jqxhr = $.ajax({
            url: VIDEO_ADD_URL,
            method: 'POST',
            data: {
              url: $('input[name="url"]').val(),
              csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            }
        });
        jqxhr.done(function () {
            $('input[name="url"]').val('');
        });
    });
});
