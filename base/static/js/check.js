function update_video_list() {
    var jqxhr = $.ajax({
        url: VIDEO_LIST_URL,
    });
    jqxhr.done(function (data) {
        var ids = [];
        $('.card').each(function (i) {ids.push(parseInt($(this).attr('rel')));});

        parsed_data = JSON.parse(data);
        ids.forEach(function (id) {
            // delete
            if (parsed_data.indexOf(id) < 0) {
                $('.card[rel="' + id + '"]').remove();
            }
        });

        // add TODO
        if (parsed_data.length > ids.length) {
            location.reload();
        }

    });
}

function vote($el, vote) {
    var video_id = $el.parents('.card').attr('rel');
    var jqxhr = $.ajax({
        url: VOTE_ADD_URL,
        method: 'POST',
        data: {
            vote: vote,
            video_id: video_id,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        }
    });

    jqxhr.done(function (data) {
        $el.find('.qt').text(data);
    });

}

$(function () {
    setInterval(update_video_list, 5000);

    $('.likes').click(function () {
        vote($(this), 1);
    });
    $('.dislikes').click(function () {
        vote($(this), -1);
    });

});
