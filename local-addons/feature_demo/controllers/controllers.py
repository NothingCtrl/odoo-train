# -*- coding: utf-8 -*-
# from odoo import http


# class FeatureDemo(http.Controller):
#     @http.route('/feature_demo/feature_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_demo/feature_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_demo.listing', {
#             'root': '/feature_demo/feature_demo',
#             'objects': http.request.env['feature_demo.feature_demo'].search([]),
#         })

#     @http.route('/feature_demo/feature_demo/objects/<model("feature_demo.feature_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_demo.object', {
#             'object': obj
#         })
