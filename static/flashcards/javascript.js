

document.addEventListener('DOMContentLoaded', function() {


    var grid = document.querySelector('.grid-container');

    var masonry = new Masonry(grid, {

        itemSelector: '.grid-item',

        columnWidth: '.grid-item',

        gutter: 10

    });

});


function detectZoom() {

var ratio = 0,

    screen = window.screen,

    ua = navigator.userAgent.toLowerCase();



if (window.devicePixelRatio !== undefined) {

    ratio = window.devicePixelRatio;

} else if (~ua.indexOf('msie')) {

    if (screen.deviceXDPI && screen.logicalXDPI) {

        ratio = screen.deviceXDPI / screen.logicalXDPI;

    }

} else if (window.outerWidth !== undefined && window.innerWidth !== undefined) {

    ratio = window.outerWidth / window.innerWidth;

}



return ratio;

}



function checkZoomLevel() {

var zoomLevel = detectZoom();




if (zoomLevel > 1.24) {


    document.querySelectorAll('.grid-item').forEach(function(item) {

        item.style.width = '98%';

    });

} else {



    document.querySelectorAll('.grid-item').forEach(function(item) {

        item.style.width = '22%';

    });

}

}


window.addEventListener('load', checkZoomLevel);

window.addEventListener('resize', checkZoomLevel);
