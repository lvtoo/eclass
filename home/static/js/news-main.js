$(function(){//Wait for page to be ready
  $('#hamburger').click(function(){
    $('.nav').css('margin-left', '0');
    $('.navoverlay').css('opacity', '1');
    $('.navoverlay').css('z-index', '60');
    $('.navoverlay').click(function(){
      $('.navoverlay').css('opacity', '0');
      $('.navoverlay').css('z-index', '-1');
      $('.nav').css('margin-left', '-100%');
    })
  })
});
// $(function(){//Wait for page to be ready
//       var filtersOpen = false;
//   $('#option').click(function(){
//     $('.nav').css('margin-left', '0');
//     $('.navoverlay').css('opacity', '0');
//     $('.navoverlay').css('z-index', '60');
//     $('.navoverlay').click(function(){
//       if(filtersOpen){
//       //Move Filter Window Off screen
//       $('.filters').css('right','-100%');
//       filtersOpen = false;//set the boolean to false
//     }else{
//       $('.filters').css('right', '0px');
//       filtersOpen = true; //set the boolean to true
//     }
//
//       $('.navoverlay').css('opacity', '0');
//       $('.navoverlay').css('z-index', '-1');
//       $('.nav').css('margin-left', '-100%');
//     })
//   })
// })



$(function(){//Wait for page to be ready
  var filtersOpen = false;
  $('#option').click(function(){
    $('.competition-post').css('display', 'block');
  });
  $('#settings').click(function(){
    if(filtersOpen){
      //Move Filter Window Off screen
      $('.filters').css('right','-100%');
      filtersOpen = false;//set the boolean to false
    }else{
      $('.filters').css('right', '0px');
      filtersOpen = true; //set the boolean to true
    }
  })
});

var competitionOpen = false;
$('#competition-filter').click(function(){
  if(!competitionOpen){
    $('.competition').css('height', '0');
    $('.competition').css('margin-bottom', '0');
    $('#competition-filter').css('color', '#DEDEDE');
    competitionOpen = true;
  }else{
    $('.competition').css('height', '120px');
    $('.competition').css('margin-bottom', '1px');
    $('#competition-filter').css('color', '#222');
    competitionOpen = false;
  }
});


var portfolioOpen = false;
$('#portfolio-filter').click(function(){
  if(!portfolioOpen){
    $('.portfolio').css('height', '0');
    $('.portfolio').css('margin-bottom', '0px');
    $('#portfolio-filter').css('color', '#DEDEDE');
    portfolioOpen = true;
  }else{
    $('.portfolio').css('height', '120px');
    $('.portfolio').css('margin-bottom', '1px');
    $('#portfolio-filter').css('color', '#222');
    portfolioOpen = false;
  }
});





