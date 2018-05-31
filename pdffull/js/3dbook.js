var urlfinale=$("#urlpdf").html();
$('#container').FlipBook({
         pdf: urlfinale,
         pages: 5,
         template: {
           html: '/media/pdffull/templates/default-book-view.html',
           styles: [
             '/media/pdffull/css/white-book-view.css'
           ],
           links: [
             {
               rel: 'stylesheet',
               href: '/media/pdffull/css/font-awesome.min.css'
             }
           ],
           script: '/media/pdffull/js/default-book-view.js'
         }
       });
