odoo.define('modulo_conversaciones.tree_view_button', function (require){
    "use strict";

    var ajax = require('web.ajax');
    var ListController = require('web.ListController');

    ListController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            var self = this;
            if (this.$buttons) {
                $(this.$buttons).find('.oe_new_custom_button').on('click', function() {
                    console.log('Hola buenas')
                });
            }
        },
    });
});