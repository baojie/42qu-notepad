function _focus(sel, start, end) {
    if (sel.setSelectionRange) {
    sel.focus();
    sel.setSelectionRange(start,end);
    }
    else if (sel.createTextRange) {
        var range = sel.createTextRange();
        range.collapse(true);
        range.moveEnd('character', end);
        range.moveStart('character', start);
        range.select();
    }
}
function focus(sel) {
    length=sel.value.length;
    _focus(sel, length, length);
}
_gaq = [['_setAccount', 'UA-35931591-1'], ['_trackPageview'], ['_trackPageLoadTime'],['_setDomainName', location.host.split(".").slice("-2").join(".")]];
$(function(){
   $('.back').click(function(){
        $(window).scrollTop(0)
    })
    (function() {

        var ga = document.createElement('script');
        var s = document.getElementsByTagName('script')[0];
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl': 'http://www') + '.google-analytics.com/ga.js';
        s.parentNode.insertBefore(ga, s);

    })();
})


