$(document).ready(function() {

    /**variable globale **/
    var executeProgress = true;
    var height = 0;

    //re-dimensionnement de l'image d'entête en fonction de la taille de l'écran
    //puis positionnement du titre
    $(function()    {
        calculerSize();

        $(window).resize(function(){
            calculerSize();
        });
    });

    function calculerSize() {
        height = $(window).innerHeight();
        $('.img-head').css({ height: $(window).innerHeight() });
        $('.titre').css({ 'margin-top': ($(window).innerHeight()/2)-70 });
        //changement de css pour les hobbies
        if($(window).innerWidth() > 768) {
            $('.dropdown-content-bis').addClass('dropdown-content');
            $('.dropdown-content-bis').removeClass('dropdown-content-bis');
        }
        else {
            $('.dropdown-content').addClass('dropdown-content-bis');
            $('.dropdown-content').removeClass('dropdown-content');
        }
    }


    //permet à la bar de navigation de rester sous l'entête si la fenêtre est en haut de la page
    //ou positionne l'entête en haut de l'écran si la page est plus basse
    $(window).scroll(function () {
        if ($(window).scrollTop() > height) {
            $('#nav_bar').addClass('navbar-static-top');
            $('#nav_bar').removeClass('navbar-fixed-top');
            $('#nav_bar').addClass('navbar-fixed');
        }
        if ($(window).scrollTop() < height) {
            $('#nav_bar').removeClass('navbar-static-top');
            $('#nav_bar').addClass('navbar-fixed-top');
            $('#nav_bar').removeClass('navbar-fixed');
        }
    });

    //permet de se déplacer par zone de manière fluide lorsqu'on clique sur un lien de la barre de navigation
    $(function () {
        var navMain = $("#nav_bar");
        $('li[id^="nav"]>a').on('click', function(e) {
            $('.navbar-toggle').click();
            e.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top
            }, 1000, function(){
                window.location.hash = hash;
            });
        });
    });

    //fait une animation de chargement des progress bar lorsque l'écran arrive sur cette partie de la page
    $(function() {
        var oTop = $('#competences').offset().top - window.innerHeight;
        $(window).scroll(function(){

            var pTop = $(document).scrollTop();
            if( pTop > oTop ){
                start_anim();
            }
        });
    });

    //méthode d'animation des progress bar
    function start_anim(){
        if(executeProgress) {
            executeProgress = false;
            setTimeout(function(){
                $('.progress-bar').each(function() {
                    var me = $(this);
                    var perc = me.attr("data-percentage");

                    var current_perc = 0;

                    var progress = setInterval(function() {
                        if (current_perc>=perc) {
                            clearInterval(progress);
                        } else {
                            current_perc +=1;
                            me.css('width', (current_perc)+'%');
                        }

                        me.text((current_perc)+'%');

                    }, 30);

                });
            },100);
        }
    }





});

