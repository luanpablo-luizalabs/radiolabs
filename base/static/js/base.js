$(function () {
    $('.btn-add').click(function () {
        $('.error-add-msg').text('');
        var that = $(this);

        var $strong = that.find('strong');
        var $div = $('<div>').addClass('loading');
        $div.append($strong);
        that.html($div);
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
        jqxhr.fail(function () {
            $('.error-add-msg').text('Oops... :(');
        });
        jqxhr.always(function () {
            $('input[name="url"]').val('');
            that.html($strong);
        });
    });
});
