
/* Portfolio */
$(window).load(function() {
    var $cont = $('.portfolio-group');
    
    $cont.isotope({
        itemSelector: '.portfolio-group .portfolio-item',
        masonry: {columnWidth: $('.isotope-item:first').width(), gutterWidth: -20, isFitWidth: true},
        filter: '*',
    });

    $('.portfolio-filter-container a').click(function() {
        $cont.isotope({
            filter: this.getAttribute('data-filter')
        });

        return false;
    });

    var lastClickFilter = null;
    $('.portfolio-filter a').click(function() {

        //first clicked we don't know which element is selected last time
        if (lastClickFilter === null) {
            $('.portfolio-filter a').removeClass('portfolio-selected');
        }
        else {
            $(lastClickFilter).removeClass('portfolio-selected');
        }

        lastClickFilter = this;
        $(this).addClass('portfolio-selected');
    });

});

/* Image Hover  - Add hover class on hover */
$(document).ready(function(){
    if (Modernizr.touch) {
        // show the close overlay button
        $(".close-overlay").removeClass("hidden");
        // handle the adding of hover class when clicked
        $(".image-hover figure").click(function(e){
            if (!$(this).hasClass("hover")) {
                $(this).addClass("hover");
            }
        });
        // handle the closing of the overlay
        $(".close-overlay").click(function(e){
            e.preventDefault();
            e.stopPropagation();
            if ($(this).closest(".image-hover figure").hasClass("hover")) {
                $(this).closest(".image-hover figure").removeClass("hover");
            }
        });
    } else {
        // handle the mouseenter functionality
        $(".image-hover figure").mouseenter(function(){
            $(this).addClass("hover");
        })
        // handle the mouseleave functionality
        .mouseleave(function(){
            $(this).removeClass("hover");
        });
    }
});

// thumbs animations
$(function () {
    
    $(".thumbs-gallery i").animate({
             opacity: 0
    
          }, {
             duration: 300,
             queue: false
          });

   $(".thumbs-gallery").parent().hover(
       function () {},
       function () {
          $(".thumbs-gallery i").animate({
             opacity: 0
          }, {
             duration: 300,
             queue: false
          });
   });
 
   $(".thumbs-gallery i").hover(
      function () {
          $(this).animate({
             opacity: 0
    
          }, {
             duration: 300,
             queue: false
          });

          $(".thumbs-gallery i").not( $(this) ).animate({
             opacity: 0.4         }, {
             duration: 300,
             queue: false
          });
      }, function () {
      }
   );
});

// Mobile Menu
$(function(){
    $('#hornavmenu').slicknav();
    $( "div.slicknav_menu" ).addClass( "hidden-lg" );
});

// Sticky Div
$(window).load(function(){
    $("#hornav").sticky({ topSpacing: 0 });
});

$(document).ready(function() {
    $('#demo').click(function() {
        $.blockUI({ 
            message: $(
                '<div class="lds-ellipsis">' +
                '<div><div></div></div>' +
                '<div><div></div></div>' +
                '<div><div></div></div>' +
                '<div><div></div></div>' +
                '<div><div></div></div>' +
                '</div>'
            ),

            css: { borderWidth: '0px', backgroundColor: 'transparent' },

            //css: {
            //    border: 'none',
            //    padding: '15px',
            //    backgroundColor: '#000',
            //    color: '#fff',
            //    '-webkit-border-radius': '10px',
            //    '-moz-border-radius': '10px',
            //    opacity: .5,
            //    top:  ($(window).height() - 200) /2 + 'px', 
            //    left: ($(window).width() - 400) /2 + 'px', 
            //    width: '400px' 
            //},
        });

        setTimeout($.unblockUI, 2000);
    });
});
