

$(function() {

    // hide navigation links
    $('div.related ul li a:contains("index")').parent().css('display', 'none');
    $('div.related ul li a:contains("next")').parent().css('display', 'none');
    $('div.related ul li a:contains("previous")').parent().css('display', 'none');

    // ga code
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'UA-149959808-1');

 });

