// Filter JS
$(document).ready(function(){
    $('.filter-item').click(function(){
        const value = $(this).attr('data-filter');
        if (value === 'all') {
            $('.post-box').show('100');
        }
        else{
            $('.post-box').not('.' + value).hide('100');
            $('.post-box').filter('.' + value).show('100');
        }
    });
    // Add active to btn
    $('.filter-item').click(function(){
        $(this).addClass('active-filter').siblings().removeClass('active-filter');

    });
});

// Header BackGround Change On Scroll
let header = document.querySelector('header');

window.addEventListener('scroll', () => {
    header.classList.toggle('shadow', window.scrollY > 0);
});