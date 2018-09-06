from flask_assets import Bundle

def create_assets(assets):
    js = Bundle(
         #'vendor/jquery/jquery.min.js',
         'vendor/jquery-easing/jquery.easing.min.js',
         #'vendor/bootstrap/js/bootstrap.bundle.min.js',
         'js/grayscale.min.js',
         output='js/libs.js'
    )
    assets.register('JS_FRAMEWORS', js)

    css = Bundle(
        'vendor/bootstrap/css/bootstrap.css',
        'vendor/fontawesome-free/css/all.min.css',
        'css/grayscale.css',
        'css/sticky-footer.css',
        #'vendor/bootstrap/css/bootstrap-grid.css',
        #'vendor/bootstrap/css/bootstrap-reboot.css',
        #'vendor/bootstrap/css/bootstrap-grid.css',
        output='css/min.css'
    )
    assets.register('CSS_FRAMEWORKS', css)