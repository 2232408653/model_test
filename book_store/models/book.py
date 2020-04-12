# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'book_store.book'

    name = fields.Char("名称", help='书名')
    author = fields.Char('作者', help='作者')
    date = fields.Datetime("出版日期", help="日期")
    price = fields.Float("定价", help='定价')
