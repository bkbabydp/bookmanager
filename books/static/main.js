/**
 * Created by bk on 2017/3/13.
 */

$(document).ready(function () {
    // $('.book-rating').each(function () {
    //     $this = $(this);
    //     $this.rating('refresh', {
    //         displayOnly: true,
    //         theme: 'krajee-svg'
    //     });
    // });
    $('.book-rate-star').each(function () {
        $this = $(this);
        $this.raty({
            cancelOff: '//cdn.bootcss.com/raty/2.7.1/images/cancel-off.png',
            cancelOn: '//cdn.bootcss.com/raty/2.7.1/images/cancel-on.png',
            starHalf: '//cdn.bootcss.com/raty/2.7.1/images/star-half.png',
            starOff: '//cdn.bootcss.com/raty/2.7.1/images/star-off.png',
            starOn: '//cdn.bootcss.com/raty/2.7.1/images/star-on.png',
            cancel: true,
            precision: false,
            score: function () {
                return $(this).attr('data-score');
            },
            target: function () {
                return $(this).attr('data-target');
            },
            targetType: 'score',
            targetKeep : true,
        });
    })
});
